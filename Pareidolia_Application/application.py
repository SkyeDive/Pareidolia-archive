import sys
import time
import logging
import threading
import multiprocessing
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtq
from PySide6.QtWidgets import QFileDialog, QApplication

import steganography
import packing
import encryption
import json

from data_entry import DataEntry
from password_entry import PasswordEntry
from pathlib import Path
import backend
from typing import TypedDict, Optional, Callable, Any, cast

from Pareidolia_Application.ui.Pareidolia import Ui_MainWindow
from Pareidolia_Application.ui.PasswordModal import Ui_modal_PasswordEntry
from Pareidolia_Application.ui.DataModal import Ui_modal_DataEntry


class Worker(qtc.QObject):
    finished = qtc.Signal()

    def set_task(self, task: Callable):
        self.task = task

    def run(self):
        self.task()
        self.finished.emit()


class CurrentVault(TypedDict):
    vault_type: Optional[backend.VaultType]
    path: str
    entries: list[PasswordEntry] | list[DataEntry]


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    # vault_type: backend.VaultType | None,
    # path: str (absolute path to vault file, empty string when closed),
    # entries: list[PasswordEntry | DataEntry]
    current_vault: CurrentVault = {"vault_type": None, "path": "", "entries": []}
    current_password: str = ''
    unsaved_changes = False
    is_locking = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.refresh_entry_list()

        # Initialize Inactivity Timer
        self.inactivity_timer = qtc.QTimer()
        self.settings_ComboBoxTimeOut.setCurrentIndex(1)
        self.inactivity_timer.setInterval(self.settings_SpinBoxMinutesForTimeOut.value() * 60 * 100)
        self.timer_connection = self.inactivity_timer.timeout.connect(self.on_inactivity)

        # Settings Stuff
        self.settings_SpinBoxMinutesForTimeOut.valueChanged.connect(self.on_spinboxvaluechanged)
        self.settings_ComboBoxTimeOut.currentTextChanged.connect(self.on_comboboxtextchanged)

        # Menu Buttons (Along top of window)
        self.toolButton_Home.clicked.connect(self.switch_to_home)  # Home Button
        self.toolButton_Settings.clicked.connect(self.switch_to_settings)  # Settings Button
        self.toolButton_Save.clicked.connect(self.save_vault)
        self.toolButton_Lock.clicked.connect(self.lock_vault)

        # Home Navigation Buttons
        self.home_ButtonCreateVault.clicked.connect(self.switch_to_createvault)
        self.home_ButtonOpenVault.clicked.connect(self.switch_to_entermasterpass)
        self.home_ButtonEditVault.clicked.connect(self.switch_to_vaultentries)
        self.home_ButtonEditVault.setVisible(False)

        # Create Vault Buttons
        self.createVault_ButtonBrowseForVaultDir.clicked.connect(self.create_vault_browse)
        self.createVault_confirmVaultDetails.setEnabled(False)
        self.createVault_confirmVaultDetails.clicked.connect(self.create_vault_confirm)

        self.createVault_ComboBoxchooseVaultType.currentIndexChanged.connect(self.create_vault_update_validity)
        self.createVault_LineEditEnterMasterPassword.textEdited.connect(self.create_vault_update_validity)
        self.createVault_cancel.clicked.connect(self.switch_to_home)
        self.createVault_cancel.clicked.connect(self.create_vault_clear)

        def toggle_create_password_mode():
            if self.createVault_showPasswordCheckbox.isChecked():
                self.createVault_LineEditEnterMasterPassword.setEchoMode(qtw.QLineEdit.EchoMode.Normal)
            else:
                self.createVault_LineEditEnterMasterPassword.setEchoMode(qtw.QLineEdit.EchoMode.Password)

        self.createVault_showPasswordCheckbox.checkStateChanged.connect(toggle_create_password_mode)
        self.createVault_LineEditEnterMasterPassword.setEchoMode(qtw.QLineEdit.EchoMode.Password)

        # Open Vault Buttons
        self.openVault_ButtonbrowseForVaultDir.clicked.connect(self.open_vault_browse)
        self.openVault_VaultList.itemClicked.connect(self.open_vault_list_select)
        self.openVault_ComboBoxVaultType.currentTextChanged.connect(self.open_vault_type)
        self.openVault_ButtonConfirmPassword.clicked.connect(self.open_vault_decrypt)
        self.openVault_PasswordEntryField.setEchoMode(qtw.QLineEdit.EchoMode.Password)
        self.openVault_VaultList.setSortingEnabled(True)
        self.openVault_VaultList.clear()

        def toggle_open_password_mode():
            if self.openVault_showPasswordCheckbox.isChecked():
                self.openVault_PasswordEntryField.setEchoMode(qtw.QLineEdit.EchoMode.Normal)
            else:
                self.openVault_PasswordEntryField.setEchoMode(qtw.QLineEdit.EchoMode.Password)
        self.openVault_showPasswordCheckbox.checkStateChanged.connect(toggle_open_password_mode)

        # trying to add a scene to graphicsview here caps its size before it updates to the "maximum" size policy
        self.openVault_LabelFilePath.setText("(Choose an image)")
        self.openVault_LabelEnterPass.setText("")
        self.openVault_LabelEnterPass.setPalette(qtq.QPalette(qtq.QColorConstants.DarkRed))
        self.openVault_ButtonConfirmPassword.setEnabled(False)

        # Browse Entries Buttons
        self.browsEntries_AddEntryButton.clicked.connect(self.add_entry)
        self.browseEntries_Table.setSortingEnabled(True)

        self.entryerrorbutton = qtw.QPushButton()
        self.entryerrorbutton.clicked.connect(self.openerror)

    def lock_vault(self):
        if self.current_vault['vault_type'] is None or self.is_locking is True:
            return

        # Fixes bug that corrupts png if you rapidly click lock icon / vault locks from timeout right when you click the icon, by indicating program is in process of locking.
        self.is_locking = True

        loading_dialog = qtw.QProgressDialog(
            labelText='Locking vault...',
            minimum=0,
            maximum=0
        )
        loading_dialog.setWindowTitle('Locking Vault')
        loading_dialog.setModal(True)
        loading_dialog.setWindowFlag(qtc.Qt.WindowContextHelpButtonHint, False)
        loading_dialog.setCancelButton(None)
        loading_dialog.setRange(0, 00)
        loading_dialog.show()

        def save():
            backend.save_vault_entries(self.current_vault["entries"], self.current_vault["path"], self.current_password)

        def done():
            loading_dialog.close()
            self.current_vault = {"vault_type": None, "path": "", "entries": []}
            self.switch_to_home()
            self.current_password = ''
            self.toolButton_Save.setPalette(self.palette())
            self.unsaved_changes = False
            self.home_ButtonEditVault.setVisible(False)
            self.is_locking = False

        self.async_do(save, done)

    # =======================
    # Inactivity Timer Events
    # =======================

    def eventFilter(self, watched, event):
        if event.type() in {qtc.QEvent.MouseMove, qtc.QEvent.KeyPress, qtc.QEvent.MouseButtonPress}:  # on user activity
            if self.current_vault['vault_type'] is not None:  # if there is a vault loaded
                self.inactivity_timer.start()  # restart the timer
            else:  # otherwise
                self.inactivity_timer.stop()  # stop timer incase one is running
        return super().eventFilter(watched, event)

    def on_inactivity(self):
        self.lock_vault()  # lock the vault when inactivity timer runs out
        self.inactivity_timer.stop()  # Ensure another timer doesnt start

    def on_spinboxvaluechanged(self, value):
        self.inactivity_timer.setInterval(value * 1000 * 60)

    def on_comboboxtextchanged(self, text):
        if text == "Timeout (Minutes)":
            if not self.timer_connection:
                self.timer_connection = self.inactivity_timer.timeout.connect(self.on_inactivity)
        else:
            if self.timer_connection:
                self.inactivity_timer.timeout.disconnect(self.on_inactivity)
                self.timer_connection = None
            self.inactivity_timer.stop()

    # ==========================
    # miscellaneous ui functions
    # ==========================

    def async_do(self, task: Callable, after: Optional[Callable] = None):
        """
        Do the provided task in a separate thread and then run the 'after' function if provided.
        """

        # Note: this implementation might not be 100% right, but it seems to work

        self.worker = Worker()
        self.worker.set_task(task)

        self.thread = qtc.QThread()  # type: ignore
        self.worker.moveToThread(self.thread)  # type: ignore
        self.thread.started.connect(self.worker.run)  # type: ignore
        self.worker.finished.connect(self.thread.quit)  # type: ignore
        self.worker.finished.connect(self.worker.deleteLater)  # type: ignore
        self.thread.finished.connect(self.thread.deleteLater)  # type: ignore

        self.worker.finished.connect(after)
        self.thread.start()  # type: ignore

    # Attempt to save the vault in-place, prompting for (new) password
    def save_vault(self):
        if self.current_vault["path"] and self.unsaved_changes:
            try:
                # password input modal
                saving_password = qtw.QInputDialog.getText(
                    self,
                    "Save vault",
                    "Please enter a master password to save with",
                    qtw.QLineEdit.EchoMode.Password,
                    self.current_password
                )[0]
                # clicked cancel or empty box
                if not saving_password:
                    raise Exception("A password is required to save")

                # file does not exist
                if not Path(self.current_vault["path"]).is_file():
                    raise Exception(f"Vault file could not be found at:\n{self.current_vault['path']}")

                # file cant be saved to
                if not steganography.check_image_path(self.current_vault["path"], False, True):  # saving vault, require png
                    raise Exception(f"Vault file could not be saved to!\nTry replacing the file ({Path(self.current_vault['path']).stem}) with a large PNG image.")

                # attempt to encrypt and save
                loading_dialog = qtw.QProgressDialog(
                    labelText='Saving vault...',
                    minimum=0,
                    maximum=0
                )
                loading_dialog.setWindowTitle('Saving Vault')
                loading_dialog.setModal(True)
                loading_dialog.setWindowFlag(qtc.Qt.WindowContextHelpButtonHint, False)
                loading_dialog.setCancelButton(None)
                loading_dialog.setRange(0, 00)
                loading_dialog.show()

                def save():
                    backend.save_vault_entries(self.current_vault["entries"], self.current_vault["path"], saving_password)

                self.async_do(save, lambda: loading_dialog.close())

                # mark changes as saved, reset save button to default bg color
                self.unsaved_changes = False
                self.toolButton_Save.setPalette(self.palette())
            except Exception as err:
                error_modal = qtw.QMessageBox(
                    qtw.QMessageBox.Icon.Warning,
                    "Save vault",
                    f"Vault failed to save:\n{err}",
                    qtw.QMessageBox.StandardButton.Ok,
                    self
                )
                error_modal.exec()

    # prompt user if they want to discard changes to current vault, returns true on discard
    def prompt_to_discard(self) -> bool:
        discard_modal = qtw.QMessageBox(
            qtw.QMessageBox.Icon.Warning,
            "Discard changes?",
            "The currently loaded vault has unsaved changes. Proceed and discard these changes?",
            qtw.QMessageBox.StandardButton.Cancel | qtw.QMessageBox.StandardButton.Discard,
            self
        )
        discard_modal.setDefaultButton(qtw.QMessageBox.StandardButton.Cancel)
        button_clicked = discard_modal.exec()
        return True if (button_clicked == qtw.QMessageBox.StandardButton.Discard) else False

    # Switches stacked widget to home
    def switch_to_home(self):
        index_of_home = self.stackedWidget.indexOf(self.page_home)
        self.stackedWidget.setCurrentIndex(index_of_home)

    # Switches stacked widget to settings
    def switch_to_settings(self):
        index_of_settings = self.stackedWidget.indexOf(self.page_settings)
        self.stackedWidget.setCurrentIndex(index_of_settings)

    # Switches stacked widget to the enter password page
    def switch_to_entermasterpass(self):
        index_of_openvault = self.stackedWidget.indexOf(self.page_openVault)
        self.stackedWidget.setCurrentIndex(index_of_openvault)
        # Clear password when re-entering
        self.openVault_PasswordEntryField.clear()

    # Switches stacked widget to the vault creation page
    def switch_to_createvault(self):
        index_of_createvault = self.stackedWidget.indexOf(self.page_createVault)
        self.stackedWidget.setCurrentIndex(index_of_createvault)

    def switch_to_vaultentries(self):
        index_of_vaultentries = self.stackedWidget.indexOf(self.page_browseEntries)
        self.stackedWidget.setCurrentIndex(index_of_vaultentries)

        # update list of vault entries
        self.refresh_entry_list()

    # Refresh the list of entries in the entry viewing page
    def refresh_entry_list(self):
        self.browseEntries_Table.setSortingEnabled(False)
        entries = self.current_vault['entries']
        self.browseEntries_Table.setRowCount(len(entries))

        for i in range(len(entries)):
            self.browseEntries_Table.setRowHeight(i, 40)

        VAULT_TYPE: backend.VaultType = self.current_vault['vault_type']
        if VAULT_TYPE not in [backend.VaultType.DATA, backend.VaultType.PASSWORD]:
            return

        if VAULT_TYPE == backend.VaultType.DATA:
            self.browseEntries_Table.setHorizontalHeaderLabels(['Title', 'Filename', ''])
        else:
            self.browseEntries_Table.setHorizontalHeaderLabels(['Title', 'Username', ''])

        for i, entry in enumerate(entries):
            entry: PasswordEntry | DataEntry  # type hint

            title = qtw.QTableWidgetItem(entry.title)
            title.setFlags(title.flags() & ~qtc.Qt.ItemFlag.ItemIsEditable)
            self.browseEntries_Table.setItem(i, 0, title)

            username = qtw.QTableWidgetItem(
                entry.username
                if VAULT_TYPE == backend.VaultType.PASSWORD
                else entry.filename
            )
            username.setFlags(username.flags() & ~qtc.Qt.ItemFlag.ItemIsEditable)
            self.browseEntries_Table.setItem(i, 1, username)

            # buttons
            widget = qtw.QWidget()
            layout = qtw.QHBoxLayout(widget)
            layout.addStretch()

            def edit(ent):
                def func():
                    self.open_edit_entry_modal(ent)
                return func
            edit_button = qtw.QPushButton()
            edit_button.setMinimumHeight(20)
            edit_button.setIcon(qtq.QIcon(qtq.QIcon.fromTheme(qtq.QIcon.ThemeIcon.DocumentOpen)))
            edit_button.clicked.connect(edit(entry))
            layout.addWidget(edit_button)

            if VAULT_TYPE == backend.VaultType.PASSWORD:
                def copy(pword):
                    def func():
                        QApplication.clipboard().setText(pword)
                    return func
                copy_button = qtw.QPushButton()
                copy_button.setMinimumHeight(20)
                copy_button.setIcon(qtq.QIcon(qtq.QIcon.fromTheme(qtq.QIcon.ThemeIcon.EditCopy)))
                copy_button.clicked.connect(copy(entry.password))
                layout.addWidget(copy_button)

            def delete(index):
                def func():
                    confirm = qtw.QMessageBox.question(self, 'Entry Deletion Confirmation', 'Are you sure you would like to delete this item?', qtw.QMessageBox.StandardButton.Yes | qtw.QMessageBox.StandardButton.No)
                    if confirm == qtw.QMessageBox.StandardButton.Yes:
                        self.current_vault['entries'].pop(index)

                        self.unsaved_changes = True
                        self.toolButton_Save.setPalette(qtq.QPalette(qtq.QColorConstants.DarkRed))
                        self.refresh_entry_list()
                return func
            delete_button = qtw.QPushButton()
            delete_button.setMinimumHeight(20)
            delete_button.setIcon(qtq.QIcon(qtq.QIcon.fromTheme(qtq.QIcon.ThemeIcon.EditDelete)))
            delete_button.clicked.connect(delete(i))
            layout.addWidget(delete_button)

            self.browseEntries_Table.setCellWidget(i, 2, widget)

        self.browseEntries_Table.setSortingEnabled(True)
        self.browseEntries_Table.resizeColumnToContents(0)
        self.browseEntries_Table.resizeColumnToContents(1)

    # ===========================
    # create vault page functions
    # ===========================

    # Opens file explorer for vault creation, updates other widgets - adapted from open_vault_browse
    def create_vault_browse(self):
        # try to load previous directory, first
        last_path = self.createVault_LabelfilePathDirectory.text()
        start_dir = str(Path(last_path).parent) if ("\\" in last_path or "/" in last_path) and Path(
            last_path).parent.is_dir() else str(Path.home())

        vault_path = qtw.QFileDialog.getOpenFileName(
            self,
            "Select File to Make a Vault",
            start_dir,
            "PNG image (*.png)"
        )[0]

        if vault_path:
            self.createVault_LabelfilePathDirectory.setText(vault_path)
            vault_valid = vault_path and steganography.check_image_path(
                vault_path,
                False,
                False
            )  # creating vault, require png
            if not vault_valid:
                self.createVault_LabelEnterMasterPassword.setText("Not a valid Vault!")

            self.create_vault_update_validity()  # update form validity

            # show preview of image
            if not self.createVault_graphicsView.scene():
                self.createVault_graphicsView.setScene(qtw.QGraphicsScene())
            self.createVault_graphicsView.scene().clear()
            new_image = qtq.QPixmap(vault_path).scaledToHeight(self.createVault_graphicsView.height() - 2)
            self.createVault_graphicsView.scene().addPixmap(new_image)
            self.createVault_graphicsView.scene().setSceneRect(new_image.rect())

    def create_vault_update_validity(self):
        """
        Hook for checking that the create vault page form is valid and
        enabling/disabling the 'Create Vault' button if it is invalid.

        Also returns the whether the vault is *invalid*
        """
        invalid = False

        if len(self.createVault_LineEditEnterMasterPassword.text()) == 0:  # nothing in the password box
            invalid = True

        if self.createVault_ComboBoxchooseVaultType.currentIndex() == 0:  # 'Choose Type'
            invalid = True

        vault_path = self.createVault_LabelfilePathDirectory.text()
        if not vault_path or not steganography.check_image_path(vault_path, False, False):
            invalid = True

        if invalid:
            self.createVault_confirmVaultDetails.setEnabled(False)
        else:
            self.createVault_confirmVaultDetails.setEnabled(True)

    def create_vault_clear(self):
        self.createVault_LineEditEnterMasterPassword.clear()
        self.createVault_LabelfilePathDirectory.setText('(Choose an image)')
        self.createVault_ComboBoxchooseVaultType.setCurrentIndex(0)  # 'Choose Type'
        if self.createVault_graphicsView.scene() is not None:
            self.createVault_graphicsView.scene().clear()
        self.createVault_showPasswordCheckbox.setChecked(False)

    def create_vault_confirm(self):
        vault_type_selection = self.createVault_ComboBoxchooseVaultType.currentIndex()
        vault_path = self.createVault_LabelfilePathDirectory.text()
        password = self.createVault_LineEditEnterMasterPassword.text()

        # set styles while loading
        self.createVault_confirmVaultDetails.setEnabled(False)
        loading_dialog = qtw.QProgressDialog(
            labelText='Creating vault...',
            minimum=0,
            maximum=0
        )
        loading_dialog.setWindowTitle('Creating Vault')
        loading_dialog.setModal(True)
        loading_dialog.setWindowFlag(qtc.Qt.WindowContextHelpButtonHint, False)
        loading_dialog.setCancelButton(None)
        loading_dialog.setRange(0, 00)

        self.current_vault['path'] = vault_path
        if vault_type_selection == 1:  # password vault
            self.current_vault['vault_type'] = backend.VaultType.PASSWORD
            entry = PasswordEntry(
                title='Sample Password Entry',
                username='username@gmail.com',
                password='password',
                notes='This is the notes section!\nYou can put whatever you like here.'
            )
        elif vault_type_selection == 2:  # data vault
            self.current_vault['vault_type'] = backend.VaultType.DATA
            entry = DataEntry(
                title='Sample Data File',
                filename='sample_data_file.txt',
                data=b'This is a sample data file! These can contain whatever you like.'
            )
        self.current_vault['entries'] = [entry]

        loading_dialog.show()

        def task():
            backend.save_vault_entries([entry], vault_path, password)

        def done():
            loading_dialog.close()

            self.home_ButtonEditVault.setVisible(True)
            self.home_ButtonEditVault.setText(f'Switch to currently open vault: {vault_path}')
            self.unsaved_changes = False
            self.toolButton_Save.setPalette(self.palette())
            self.current_password = password

            self.switch_to_vaultentries()

            self.create_vault_clear()

        self.async_do(task, done)

    # =========================
    # open vault page functions
    # =========================

    # Opens file explorer for vault opening, updates other widgets
    def open_vault_browse(self):
        # try to load previous directory, first
        last_path = self.openVault_LabelFilePath.text()
        start_dir = (
            str(Path(last_path).parent)
            if ("\\" in last_path or "/" in last_path) and Path(last_path).parent.is_dir()
            else str(Path.home())
        )

        # open file browser
        vault_path = qtw.QFileDialog.getOpenFileName(self, "Select a Vault", start_dir, "PNG image (*.png)")[0]

        if vault_path:
            # if user chose a file, check path validity and update displays
            self.openVault_LabelFilePath.setText(vault_path)
            # loading vault, require png
            vault_valid = vault_path and steganography.check_image_path(vault_path, True, True)
            if not vault_valid:
                self.openVault_LabelEnterPass.setText("ERROR: Not a valid Vault!")
                self.openVault_ButtonConfirmPassword.setEnabled(False)
            elif ("password" not in self.openVault_ComboBoxVaultType.currentText().lower() and "data" not in self.openVault_ComboBoxVaultType.currentText().lower()):
                self.openVault_LabelEnterPass.setText("")
                self.openVault_ButtonConfirmPassword.setEnabled(False)
            else:
                self.openVault_LabelEnterPass.setText("")
                self.openVault_ButtonConfirmPassword.setEnabled(True)

            # show preview of image
            if not self.openVault_graphicsView.scene():
                self.openVault_graphicsView.setScene(qtw.QGraphicsScene())
            self.openVault_graphicsView.scene().clear()
            new_image = qtq.QPixmap(vault_path).scaledToHeight(self.openVault_graphicsView.height() - 2)
            self.openVault_graphicsView.scene().addPixmap(new_image)
            self.openVault_graphicsView.scene().setSceneRect(new_image.rect())

            # refresh list to current directory
            self.openVault_VaultList.clear()
            for sub_path in Path(vault_path).parent.iterdir():
                if sub_path.is_file() and str(sub_path).endswith(".png"):
                    new_item = qtw.QListWidgetItem(sub_path.name)
                    self.openVault_VaultList.addItem(new_item)
                    if sub_path.samefile(vault_path):
                        self.openVault_VaultList.setCurrentItem(new_item)

    # Update opening vault's type and related page information
    def open_vault_type(self, new_text):
        if "password" in new_text.lower() or "data" in new_text.lower():
            # sanity checks for image validity, in case it updated
            image_path = self.openVault_LabelFilePath.text()
            if not (("\\" in image_path or "/" in image_path) and Path(image_path).parent.is_dir()):
                self.openVault_LabelFilePath.setText("(Choose an image)")
                self.openVault_LabelEnterPass.setText("")
                self.openVault_ButtonConfirmPassword.setEnabled(False)
            elif not steganography.check_image_path(image_path, True, True):  # loading vault, require png
                self.openVault_LabelEnterPass.setText("Not a valid Vault!")
                self.openVault_ButtonConfirmPassword.setEnabled(False)
            else:
                self.openVault_LabelEnterPass.setText("")
                self.openVault_ButtonConfirmPassword.setEnabled(True)

        else:
            self.openVault_LabelEnterPass.setText("Please choose a vault type")
            self.openVault_ButtonConfirmPassword.setEnabled(False)

    # Updates selected vault and related page information
    def open_vault_list_select(self, item):
        # load previous directory
        last_path = self.openVault_LabelFilePath.text()
        parent_dir = Path(last_path).parent

        # if directory no longer exists
        if not parent_dir.is_dir():
            self.openVault_VaultList.clear()
            self.openVault_LabelFilePath.setText("(Choose an image)")
            self.openVault_LabelEnterPass.setText("Choose a vault...")
        else:
            cur_path = parent_dir.joinpath(item.text())
            # if file missing, remove from list and leave everything else as-is
            if not cur_path.exists():
                self.openVault_VaultList.takeItem(self.openVault_VaultList.row(item))
            else:
                self.openVault_LabelFilePath.setText(str(cur_path))

                # check path validity and update displays
                # loading vault, require png
                vault_valid = str(cur_path) and steganography.check_image_path(str(cur_path), True, True)
                if not vault_valid:
                    self.openVault_LabelEnterPass.setText("ERROR: Not a valid Vault!")
                    self.openVault_ButtonConfirmPassword.setEnabled(False)
                elif "password" not in self.openVault_ComboBoxVaultType.currentText().lower() and "data" not in self.openVault_ComboBoxVaultType.currentText().lower():
                    self.openVault_LabelEnterPass.setText("")
                    self.openVault_ButtonConfirmPassword.setEnabled(False)
                else:
                    self.openVault_LabelEnterPass.setText("")
                    self.openVault_ButtonConfirmPassword.setEnabled(True)

                # show preview of image
                self.openVault_graphicsView.scene().clear()
                new_image = qtq.QPixmap(str(cur_path)).scaledToHeight(self.openVault_graphicsView.height() - 2)
                self.openVault_graphicsView.scene().addPixmap(new_image)
                self.openVault_graphicsView.scene().setSceneRect(new_image.rect())

                # refresh list to current directory
                self.openVault_VaultList.clear()
                for sub_path in cur_path.parent.iterdir():
                    if sub_path.is_file() and str(sub_path).endswith(".png"):
                        new_item = qtw.QListWidgetItem(sub_path.name)
                        self.openVault_VaultList.addItem(new_item)
                        if sub_path.samefile(cur_path):
                            self.openVault_VaultList.setCurrentItem(new_item)

    def openerror(self):
        error_modal = qtw.QMessageBox(qtw.QMessageBox.Icon.Warning,
                                      "Open vault",
                                      f"Vault failed to open:",
                                      qtw.QMessageBox.StandardButton.Ok,
                                      self)
        error_modal.exec()

    # Attempt to open and decrypt the selected vault
    def open_vault_decrypt(self):
        if self.current_vault["path"] and self.unsaved_changes and not self.prompt_to_discard():
            return
        else:
            entered_type = backend.VaultType.PASSWORD if (
                "password" in self.openVault_ComboBoxVaultType.currentText().lower()) else backend.VaultType.DATA

            # pull master password
            master_password = self.openVault_PasswordEntryField.text()
            vault_path = self.openVault_LabelFilePath.text()

            # attempt to get vault entries
            loading_dialog = qtw.QProgressDialog(
                labelText='Opening vault...',
                minimum=0,
                maximum=0
            )
            loading_dialog.setWindowTitle('Creating Vault')
            loading_dialog.setModal(True)
            loading_dialog.setWindowFlag(qtc.Qt.WindowContextHelpButtonHint, False)
            loading_dialog.setCancelButton(None)
            loading_dialog.setRange(0, 00)
            loading_dialog.show()

            error = threading.Event()

            def task():
                try:
                    self.current_vault["entries"], self.current_vault["vault_type"] = (
                        backend.get_vault_entries(vault_path, master_password)
                    )
                except Exception as err:
                    error.set()
                    return

            def done():
                if not error.isSet():
                    # set current vault data after entries in case the backend raises an exception
                    self.current_vault["path"] = vault_path

                    # remove unsaved changes, reset save button to default bg color
                    self.home_ButtonEditVault.setVisible(True)
                    self.home_ButtonEditVault.setText(f'Switch to currently open vault: {vault_path}')
                    self.unsaved_changes = False
                    self.toolButton_Save.setPalette(self.palette())

                    # kick the user to the entry page
                    self.switch_to_vaultentries()

                    self.current_password = master_password
                else:
                    self.entryerrorbutton.click()
                loading_dialog.close()

            self.async_do(task, done)

    # attempts to open the selected entry, opening a modal to allow viewing/editing.
    def open_entry(self, listofentries):
        current_item = self.browseEntries_listWidget.currentItem()
        vault_type = self.current_vault["vault_type"]

        if current_item:
            current_text = current_item.text()
            # iterate through the entries in the list of password entries || Replace listofpasswordentries with actual input
            for entry in self.current_vault["entries"]:
                # to find the entry title that matches the selected text.
                if entry.title == current_text:
                    if vault_type == backend.VaultType.PASSWORD:
                        # assign the text to the fields in modal
                        modal = PasswordModal(entry)
                        button_clicked = modal.exec()
                    else:
                        # assign the text to the fields in modal
                        modal = DataModal(entry)
                        button_clicked = modal.exec()

                    # if user clicked "ok" instead of "cancel"
                    if button_clicked == qtw.QDialog.DialogCode.Accepted:
                        self.refresh_entry_list()
                        self.unsaved_changes = True
                        self.toolButton_Save.setPalette(qtq.QPalette(qtq.QColorConstants.DarkRed))

    # =====================
    # browse page functions
    # =====================

    def add_entry(self):
        if self.current_vault['vault_type'] == backend.VaultType.DATA:
            entry = DataEntry('', '', b'')
            modal = DataModal(entry)
            modal.dataModal_EditCheckBox.click()
            value = modal.exec()
            if value == qtw.QDialog.DialogCode.Accepted:
                self.current_vault['entries'].append(entry)
                self.unsaved_changes = True
                self.toolButton_Save.setPalette(qtq.QPalette(qtq.QColorConstants.DarkRed))
        elif self.current_vault['vault_type'] == backend.VaultType.PASSWORD:
            entry = PasswordEntry('', '', '', '')
            modal = PasswordModal(entry)
            modal.passwordModal_EditCheckBox.click()
            value = modal.exec()
            if value == qtw.QDialog.DialogCode.Accepted:
                self.current_vault['entries'].append(entry)
                self.unsaved_changes = True
                self.toolButton_Save.setPalette(qtq.QPalette(qtq.QColorConstants.DarkRed))
        self.refresh_entry_list()

    def open_edit_entry_modal(self, entry: PasswordEntry | DataEntry):
        value = PasswordModal(entry).exec() if isinstance(entry, PasswordEntry) else DataModal(entry).exec()
        if value == qtw.QDialog.DialogCode.Accepted:
            self.refresh_entry_list()
            self.unsaved_changes = True
            self.toolButton_Save.setPalette(qtq.QPalette(qtq.QColorConstants.DarkRed))


class PasswordModal(qtw.QDialog, Ui_modal_PasswordEntry):
    def __init__(self, entry):
        super().__init__()
        self.setupUi(self)

        # entry is passed in as a pointer, so should be editing entry directly.
        self.entry = entry

        # Checkbox buttons
        # connect stateChanged signal to edit_state_changed method
        self.passwordModal_EditCheckBox.stateChanged.connect(self.edit_state_changed)
        # set readonly property of line edits and text edits based on state of edit checkbox
        self.edit_state_changed(self.passwordModal_EditCheckBox.checkState())

        # connect stateChanged signal to reveal_state_changed method
        self.passwordModal_CheckBoxRevealPassword.stateChanged.connect(self.reveal_state_changed)
        # set echoMode (**** vs pass) to on vs off based on state of reveal checkbox
        self.passwordModal_LineEditPassword.setEchoMode(qtw.QLineEdit.EchoMode.Password)

        # Buttons
        self.passwordModal_CopyPassword.clicked.connect(self.copy_to_clipboard)

        # Setters
        self.passwordModal_LineEditTitle.setText(entry.title)
        self.passwordModal_LineEditUserName.setText(entry.username)
        self.passwordModal_LineEditPassword.setText(entry.password)
        self.passwordModal_TextEditNotes.setText(entry.notes)

        # start in read-only
        self.passwordModal_LineEditTitle.setReadOnly(True)
        self.passwordModal_LineEditUserName.setReadOnly(True)
        self.passwordModal_LineEditPassword.setReadOnly(True)
        self.passwordModal_TextEditNotes.setReadOnly(True)

    def accept(self):
        # ok button was clicked, as set to signal in designer
        # get data from entry fields and update the password entry
        self.entry.title = self.passwordModal_LineEditTitle.text()
        self.entry.username = self.passwordModal_LineEditUserName.text()
        self.entry.password = self.passwordModal_LineEditPassword.text()
        self.entry.notes = self.passwordModal_TextEditNotes.toPlainText()

        # call superclass accept method to close dialog
        super().accept()

    def reject(self):
        # cancel button was clicked

        # call superclass reject method to close the dialog
        super().reject()

    def copy_to_clipboard(self):
        QApplication.clipboard().setText(self.passwordModal_LineEditPassword.text())

    # Sets all fields to readonly until this is triggered
    def edit_state_changed(self, state):
        if state == 0:
            self.passwordModal_LineEditTitle.setReadOnly(True)
            self.passwordModal_LineEditUserName.setReadOnly(True)
            self.passwordModal_LineEditPassword.setReadOnly(True)
            self.passwordModal_TextEditNotes.setReadOnly(True)
        else:
            self.passwordModal_LineEditTitle.setReadOnly(False)
            self.passwordModal_LineEditUserName.setReadOnly(False)
            self.passwordModal_LineEditPassword.setReadOnly(False)
            self.passwordModal_TextEditNotes.setReadOnly(False)

    # Sets password field to readonly until this is triggered
    def reveal_state_changed(self, state):
        if state == 0:
            self.passwordModal_LineEditPassword.setEchoMode(qtw.QLineEdit.EchoMode.Password)
        else:
            self.passwordModal_LineEditPassword.setEchoMode(qtw.QLineEdit.EchoMode.Normal)


class DataModal(qtw.QDialog, Ui_modal_DataEntry):
    def __init__(self, entry):
        super().__init__()
        self.setupUi(self)

        # entry is passed in as a pointer, so should be editing entry directly.
        self.entry = entry

        # for internal state:
        self.file_data = entry.data
        self.last_path = None

        # connect stateChanged signal to on_state_changed method
        self.dataModal_EditCheckBox.stateChanged.connect(self.on_edit_state_changed)
        # set readonly property of line edits and text edits based on state of edit checkbox
        self.on_edit_state_changed(self.dataModal_EditCheckBox.checkState())

        # pyside 6 weirdness, need to disconnect slots to make it not override the other modal
        self.dataModal_buttonBox.accepted.disconnect()
        self.dataModal_buttonBox.rejected.disconnect()

        self.dataModal_buttonBox.accepted.connect(self.dataaccept)
        self.dataModal_buttonBox.rejected.connect(self.datareject)

        self.dataModal_LineEditTitle.setText(entry.title)
        self.dataModal_LineEditFileName.setText(entry.filename)

        # start in read-only
        self.dataModal_LineEditTitle.setReadOnly(True)
        self.dataModal_LineEditFileName.setReadOnly(True)

        # for uploading, downloading file
        self.dataModal_UploadButton.clicked.connect(self.upload_file)
        self.dataModal_DownloadButton.clicked.connect(self.download_file)

        # setup filesize label
        self._update_file_size()

    def _update_file_size(self):
        size = len(self.file_data)
        LABELS = ['B', 'kB', 'MB']

        if size < 1000:
            text = f'{size} B'
        elif size < 1_000_000:
            text = f'{size/1000} kB'
        else:
            text = f'{size/1_000_000} MB'

        self.dataModal_FileSizeLabel.setText(text)

    def upload_file(self):
        file_path = qtw.QFileDialog.getOpenFileName(
            self,
            "Select File to Upload",
            str(self.get_folder_path())
        )[0]

        if file_path == '':
            return

        file = Path(file_path)
        if not file.exists() or not file.is_file():
            qtw.QErrorMessage.showMessage(f"File '{file_path}' does not exist.")
            return

        try:
            with file.open('rb') as f:
                self.file_data = f.read()
        except Exception:
            qtw.QErrorMessage.showMessage(f"Error occurred while reading file.")
            return

        self._update_file_size()
        self.dataModal_LineEditFileName.setText(file.name)
        self.dataModal_EditCheckBox.setChecked(True)
        self.last_path = file

    def dataaccept(self):
        # ok button was clicked, as set to signal in designer
        self.entry.title = self.dataModal_LineEditTitle.text()
        self.entry.filename = self.dataModal_LineEditFileName.text()
        self.entry.data = self.file_data

        super().accept()

    def datareject(self):
        # cancel button was clicked
        super().reject()

    def download_file(self):
        qtw.QFileDialog.getSaveFileUrl
        file_path = qtw.QFileDialog.getSaveFileName(
            self,
            "Download File To",
            str(self.get_folder_path() / self.dataModal_LineEditFileName.text())
        )[0]

        if file_path == '':
            return

        file = Path(file_path)

        try:
            with file.open('wb') as f:
                f.write(self.file_data)
        except Exception:
            qtw.QErrorMessage.showMessage(f"Error occurred while writing to file.")
            return

        self.last_path = file

    def on_edit_state_changed(self, state):
        if state == 0:
            self.dataModal_LineEditTitle.setReadOnly(True)
            self.dataModal_LineEditFileName.setReadOnly(True)
        else:
            self.dataModal_LineEditTitle.setReadOnly(False)
            self.dataModal_LineEditFileName.setReadOnly(False)

    def get_folder_path(self) -> Path:
        # try to get previous directory, first - adapted from open_vault_browse for consistency

        if self.last_path is None:
            return Path.home()
        else:
            return self.last_path.parent


def run():
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # allows detection of user input.
    app.installEventFilter(window)

    sys.exit(app.exec())
