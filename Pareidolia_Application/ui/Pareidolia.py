# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pareidolia.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGraphicsView, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QStatusBar, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(813, 788)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton_Home = QToolButton(self.centralwidget)
        self.toolButton_Home.setObjectName(u"toolButton_Home")
        icon = QIcon(QIcon.fromTheme(u"user-home"))
        self.toolButton_Home.setIcon(icon)

        self.horizontalLayout.addWidget(self.toolButton_Home, 0, Qt.AlignmentFlag.AlignLeft)

        self.toolButton_Settings = QToolButton(self.centralwidget)
        self.toolButton_Settings.setObjectName(u"toolButton_Settings")
        icon1 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.toolButton_Settings.setIcon(icon1)

        self.horizontalLayout.addWidget(self.toolButton_Settings)

        self.toolButton_Save = QToolButton(self.centralwidget)
        self.toolButton_Save.setObjectName(u"toolButton_Save")
        icon2 = QIcon(QIcon.fromTheme(u"document-save"))
        self.toolButton_Save.setIcon(icon2)

        self.horizontalLayout.addWidget(self.toolButton_Save)

        self.toolButton_Lock = QToolButton(self.centralwidget)
        self.toolButton_Lock.setObjectName(u"toolButton_Lock")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLockScreen))
        self.toolButton_Lock.setIcon(icon3)

        self.horizontalLayout.addWidget(self.toolButton_Lock)

        self.home_ButtonEditVault = QToolButton(self.centralwidget)
        self.home_ButtonEditVault.setObjectName(u"home_ButtonEditVault")

        self.horizontalLayout.addWidget(self.home_ButtonEditVault)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.gridLayout = QGridLayout(self.page_home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.home_ButtonOpenVault = QPushButton(self.page_home)
        self.home_ButtonOpenVault.setObjectName(u"home_ButtonOpenVault")

        self.gridLayout.addWidget(self.home_ButtonOpenVault, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.home_ButtonCreateVault = QPushButton(self.page_home)
        self.home_ButtonCreateVault.setObjectName(u"home_ButtonCreateVault")

        self.gridLayout.addWidget(self.home_ButtonCreateVault, 2, 1, 1, 1)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_browseEntries = QWidget()
        self.page_browseEntries.setObjectName(u"page_browseEntries")
        self.gridLayout_3 = QGridLayout(self.page_browseEntries)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.page_browseEntries)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 773, 664))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        font = QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_11)

        self.browseEntries_Table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.browseEntries_Table.columnCount() < 3):
            self.browseEntries_Table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.browseEntries_Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.browseEntries_Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.browseEntries_Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.browseEntries_Table.setObjectName(u"browseEntries_Table")
        self.browseEntries_Table.horizontalHeader().setCascadingSectionResizes(False)
        self.browseEntries_Table.horizontalHeader().setStretchLastSection(True)
        self.browseEntries_Table.verticalHeader().setVisible(False)
        self.browseEntries_Table.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_2.addWidget(self.browseEntries_Table)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.browsEntries_AddEntryButton = QPushButton(self.scrollAreaWidgetContents)
        self.browsEntries_AddEntryButton.setObjectName(u"browsEntries_AddEntryButton")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.browsEntries_AddEntryButton.setIcon(icon4)

        self.horizontalLayout_6.addWidget(self.browsEntries_AddEntryButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_browseEntries)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.gridLayout_2 = QGridLayout(self.page_settings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.settings_ComboBoxTimeOut = QComboBox(self.page_settings)
        self.settings_ComboBoxTimeOut.addItem("")
        self.settings_ComboBoxTimeOut.addItem("")
        self.settings_ComboBoxTimeOut.setObjectName(u"settings_ComboBoxTimeOut")

        self.gridLayout_2.addWidget(self.settings_ComboBoxTimeOut, 0, 1, 1, 1)

        self.label_6 = QLabel(self.page_settings)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_4 = QLabel(self.page_settings)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.settings_SpinBoxMinutesForTimeOut = QSpinBox(self.page_settings)
        self.settings_SpinBoxMinutesForTimeOut.setObjectName(u"settings_SpinBoxMinutesForTimeOut")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.settings_SpinBoxMinutesForTimeOut.sizePolicy().hasHeightForWidth())
        self.settings_SpinBoxMinutesForTimeOut.setSizePolicy(sizePolicy3)
        self.settings_SpinBoxMinutesForTimeOut.setMinimumSize(QSize(100, 0))
        self.settings_SpinBoxMinutesForTimeOut.setMinimum(1)
        self.settings_SpinBoxMinutesForTimeOut.setValue(5)

        self.gridLayout_2.addWidget(self.settings_SpinBoxMinutesForTimeOut, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_settings)
        self.page_createVault = QWidget()
        self.page_createVault.setObjectName(u"page_createVault")
        self.verticalLayout_6 = QVBoxLayout(self.page_createVault)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.page_createVault)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 14pt;")

        self.verticalLayout_6.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_15 = QLabel(self.page_createVault)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_6.addWidget(self.label_15)

        self.createVault_graphicsView = QGraphicsView(self.page_createVault)
        self.createVault_graphicsView.setObjectName(u"createVault_graphicsView")

        self.verticalLayout_6.addWidget(self.createVault_graphicsView)

        self.label_2 = QLabel(self.page_createVault)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.LabelChooseVaultType_2 = QLabel(self.page_createVault)
        self.LabelChooseVaultType_2.setObjectName(u"LabelChooseVaultType_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.LabelChooseVaultType_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.createVault_ButtonBrowseForVaultDir = QPushButton(self.page_createVault)
        self.createVault_ButtonBrowseForVaultDir.setObjectName(u"createVault_ButtonBrowseForVaultDir")
        sizePolicy3.setHeightForWidth(self.createVault_ButtonBrowseForVaultDir.sizePolicy().hasHeightForWidth())
        self.createVault_ButtonBrowseForVaultDir.setSizePolicy(sizePolicy3)
        self.createVault_ButtonBrowseForVaultDir.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.createVault_ButtonBrowseForVaultDir)

        self.createVault_LabelfilePathDirectory = QLabel(self.page_createVault)
        self.createVault_LabelfilePathDirectory.setObjectName(u"createVault_LabelfilePathDirectory")
        sizePolicy.setHeightForWidth(self.createVault_LabelfilePathDirectory.sizePolicy().hasHeightForWidth())
        self.createVault_LabelfilePathDirectory.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.createVault_LabelfilePathDirectory)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.LabelChooseVaultType = QLabel(self.page_createVault)
        self.LabelChooseVaultType.setObjectName(u"LabelChooseVaultType")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.LabelChooseVaultType)

        self.createVault_ComboBoxchooseVaultType = QComboBox(self.page_createVault)
        self.createVault_ComboBoxchooseVaultType.addItem("")
        self.createVault_ComboBoxchooseVaultType.addItem("")
        self.createVault_ComboBoxchooseVaultType.addItem("")
        self.createVault_ComboBoxchooseVaultType.setObjectName(u"createVault_ComboBoxchooseVaultType")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.createVault_ComboBoxchooseVaultType)

        self.createVault_LabelEnterMasterPassword = QLabel(self.page_createVault)
        self.createVault_LabelEnterMasterPassword.setObjectName(u"createVault_LabelEnterMasterPassword")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.createVault_LabelEnterMasterPassword)

        self.createVault_LineEditEnterMasterPassword = QLineEdit(self.page_createVault)
        self.createVault_LineEditEnterMasterPassword.setObjectName(u"createVault_LineEditEnterMasterPassword")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.createVault_LineEditEnterMasterPassword)

        self.label_5 = QLabel(self.page_createVault)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.createVault_showPasswordCheckbox = QCheckBox(self.page_createVault)
        self.createVault_showPasswordCheckbox.setObjectName(u"createVault_showPasswordCheckbox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.createVault_showPasswordCheckbox)


        self.verticalLayout_6.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.createVault_confirmVaultDetails = QPushButton(self.page_createVault)
        self.createVault_confirmVaultDetails.setObjectName(u"createVault_confirmVaultDetails")

        self.horizontalLayout_2.addWidget(self.createVault_confirmVaultDetails)

        self.createVault_cancel = QPushButton(self.page_createVault)
        self.createVault_cancel.setObjectName(u"createVault_cancel")

        self.horizontalLayout_2.addWidget(self.createVault_cancel)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.page_createVault)
        self.page_openVault = QWidget()
        self.page_openVault.setObjectName(u"page_openVault")
        self.formLayout_2 = QFormLayout(self.page_openVault)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.openVault_graphicsView = QGraphicsView(self.page_openVault)
        self.openVault_graphicsView.setObjectName(u"openVault_graphicsView")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.openVault_graphicsView.sizePolicy().hasHeightForWidth())
        self.openVault_graphicsView.setSizePolicy(sizePolicy4)

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.openVault_graphicsView)

        self.scrollArea_2 = QScrollArea(self.page_openVault)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 98, 76))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.openVault_VaultList = QListWidget(self.scrollAreaWidgetContents_2)
        QListWidgetItem(self.openVault_VaultList)
        QListWidgetItem(self.openVault_VaultList)
        self.openVault_VaultList.setObjectName(u"openVault_VaultList")
        font1 = QFont()
        font1.setPointSize(12)
        self.openVault_VaultList.setFont(font1)

        self.verticalLayout_5.addWidget(self.openVault_VaultList)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.formLayout_2.setWidget(5, QFormLayout.SpanningRole, self.scrollArea_2)

        self.label_9 = QLabel(self.page_openVault)
        self.label_9.setObjectName(u"label_9")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy5)
        self.label_9.setMinimumSize(QSize(60, 0))

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.openVault_ButtonbrowseForVaultDir = QPushButton(self.page_openVault)
        self.openVault_ButtonbrowseForVaultDir.setObjectName(u"openVault_ButtonbrowseForVaultDir")
        sizePolicy3.setHeightForWidth(self.openVault_ButtonbrowseForVaultDir.sizePolicy().hasHeightForWidth())
        self.openVault_ButtonbrowseForVaultDir.setSizePolicy(sizePolicy3)
        self.openVault_ButtonbrowseForVaultDir.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.openVault_ButtonbrowseForVaultDir)

        self.openVault_LabelFilePath = QLabel(self.page_openVault)
        self.openVault_LabelFilePath.setObjectName(u"openVault_LabelFilePath")

        self.horizontalLayout_3.addWidget(self.openVault_LabelFilePath)


        self.formLayout_2.setLayout(8, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.openVault_PasswordEntryField = QLineEdit(self.page_openVault)
        self.openVault_PasswordEntryField.setObjectName(u"openVault_PasswordEntryField")

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.openVault_PasswordEntryField)

        self.openVault_showPasswordCheckbox = QCheckBox(self.page_openVault)
        self.openVault_showPasswordCheckbox.setObjectName(u"openVault_showPasswordCheckbox")

        self.formLayout_2.setWidget(13, QFormLayout.FieldRole, self.openVault_showPasswordCheckbox)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.openVault_LabelEnterPass = QLabel(self.page_openVault)
        self.openVault_LabelEnterPass.setObjectName(u"openVault_LabelEnterPass")
        sizePolicy.setHeightForWidth(self.openVault_LabelEnterPass.sizePolicy().hasHeightForWidth())
        self.openVault_LabelEnterPass.setSizePolicy(sizePolicy)
        self.openVault_LabelEnterPass.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.openVault_LabelEnterPass)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.openVault_ButtonConfirmPassword = QPushButton(self.page_openVault)
        self.openVault_ButtonConfirmPassword.setObjectName(u"openVault_ButtonConfirmPassword")
        sizePolicy3.setHeightForWidth(self.openVault_ButtonConfirmPassword.sizePolicy().hasHeightForWidth())
        self.openVault_ButtonConfirmPassword.setSizePolicy(sizePolicy3)
        self.openVault_ButtonConfirmPassword.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_7.addWidget(self.openVault_ButtonConfirmPassword)


        self.formLayout_2.setLayout(15, QFormLayout.SpanningRole, self.horizontalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(16, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.label_7 = QLabel(self.page_openVault)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_7)

        self.openVault_ComboBoxVaultType = QComboBox(self.page_openVault)
        self.openVault_ComboBoxVaultType.addItem("")
        self.openVault_ComboBoxVaultType.addItem("")
        self.openVault_ComboBoxVaultType.addItem("")
        self.openVault_ComboBoxVaultType.setObjectName(u"openVault_ComboBoxVaultType")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.openVault_ComboBoxVaultType)

        self.label_8 = QLabel(self.page_openVault)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.label_8)

        self.label_10 = QLabel(self.page_openVault)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.label_10)

        self.label_12 = QLabel(self.page_openVault)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_12)

        self.label_13 = QLabel(self.page_openVault)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.page_openVault)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.stackedWidget.addWidget(self.page_openVault)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_11.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 813, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pareidolia", None))
        self.toolButton_Home.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_Settings.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_Save.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_Lock.setText("")
        self.home_ButtonEditVault.setText(QCoreApplication.translate("MainWindow", u"Switch to open vault: /foo/bar", None))
        self.home_ButtonOpenVault.setText(QCoreApplication.translate("MainWindow", u"Open Vault", None))
        self.home_ButtonCreateVault.setText(QCoreApplication.translate("MainWindow", u"Create Vault", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to Pareidolia", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Edit/View Vault Entries", None))
        ___qtablewidgetitem = self.browseEntries_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem1 = self.browseEntries_Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        self.browsEntries_AddEntryButton.setText("")
        self.settings_ComboBoxTimeOut.setItemText(0, QCoreApplication.translate("MainWindow", u"No Timeout", None))
        self.settings_ComboBoxTimeOut.setItemText(1, QCoreApplication.translate("MainWindow", u"Timeout (Minutes)", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enable Timeout", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Minutes on Standby to Close", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Create New Vault", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Image Preview:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter Vault Details:", None))
        self.LabelChooseVaultType_2.setText(QCoreApplication.translate("MainWindow", u"Vault File: ", None))
        self.createVault_ButtonBrowseForVaultDir.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.createVault_LabelfilePathDirectory.setText(QCoreApplication.translate("MainWindow", u"(Choose a Path)", None))
        self.LabelChooseVaultType.setText(QCoreApplication.translate("MainWindow", u"Vault Type: ", None))
        self.createVault_ComboBoxchooseVaultType.setItemText(0, QCoreApplication.translate("MainWindow", u"Choose Type", None))
        self.createVault_ComboBoxchooseVaultType.setItemText(1, QCoreApplication.translate("MainWindow", u"Password Vault", None))
        self.createVault_ComboBoxchooseVaultType.setItemText(2, QCoreApplication.translate("MainWindow", u"Data Vault", None))

        self.createVault_LabelEnterMasterPassword.setText(QCoreApplication.translate("MainWindow", u"Master Password: ", None))
        self.label_5.setText("")
        self.createVault_showPasswordCheckbox.setText(QCoreApplication.translate("MainWindow", u"Show Password", None))
        self.createVault_confirmVaultDetails.setText(QCoreApplication.translate("MainWindow", u"Create Vault", None))
        self.createVault_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))

        __sortingEnabled = self.openVault_VaultList.isSortingEnabled()
        self.openVault_VaultList.setSortingEnabled(False)
        ___qlistwidgetitem = self.openVault_VaultList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Vault Example", None));
        ___qlistwidgetitem1 = self.openVault_VaultList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Vault Example", None));
        self.openVault_VaultList.setSortingEnabled(__sortingEnabled)

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Vault File: ", None))
        self.openVault_ButtonbrowseForVaultDir.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.openVault_LabelFilePath.setText(QCoreApplication.translate("MainWindow", u"(Choose a Path)", None))
        self.openVault_showPasswordCheckbox.setText(QCoreApplication.translate("MainWindow", u"Show Password", None))
        self.openVault_LabelEnterPass.setText(QCoreApplication.translate("MainWindow", u"Messages go here", None))
        self.openVault_ButtonConfirmPassword.setText(QCoreApplication.translate("MainWindow", u"Open Vault", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Vault Type: ", None))
        self.openVault_ComboBoxVaultType.setItemText(0, QCoreApplication.translate("MainWindow", u"Choose Type", None))
        self.openVault_ComboBoxVaultType.setItemText(1, QCoreApplication.translate("MainWindow", u"Password Vault", None))
        self.openVault_ComboBoxVaultType.setItemText(2, QCoreApplication.translate("MainWindow", u"Data Vault", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Master Password: ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Open Existing Vault", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Enter Vault Details: ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Other images:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Image Preview:", None))
    # retranslateUi

