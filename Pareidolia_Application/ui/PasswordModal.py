# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PasswordModal.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QTextEdit,
    QToolButton, QVBoxLayout, QWidget)

class Ui_modal_PasswordEntry(object):
    def setupUi(self, modal_PasswordEntry):
        if not modal_PasswordEntry.objectName():
            modal_PasswordEntry.setObjectName(u"modal_PasswordEntry")
        modal_PasswordEntry.setWindowModality(Qt.WindowModality.WindowModal)
        modal_PasswordEntry.resize(451, 370)
        modal_PasswordEntry.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(modal_PasswordEntry)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.passwordModal_LabelTitle = QLabel(modal_PasswordEntry)
        self.passwordModal_LabelTitle.setObjectName(u"passwordModal_LabelTitle")
        self.passwordModal_LabelTitle.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.passwordModal_LabelTitle.setAutoFillBackground(False)
        self.passwordModal_LabelTitle.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.passwordModal_LabelTitle)

        self.passwordModal_LineEditTitle = QLineEdit(modal_PasswordEntry)
        self.passwordModal_LineEditTitle.setObjectName(u"passwordModal_LineEditTitle")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.passwordModal_LineEditTitle)

        self.passwordModal_LabelUserName = QLabel(modal_PasswordEntry)
        self.passwordModal_LabelUserName.setObjectName(u"passwordModal_LabelUserName")
        self.passwordModal_LabelUserName.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.passwordModal_LabelUserName)

        self.passwordModal_LineEditUserName = QLineEdit(modal_PasswordEntry)
        self.passwordModal_LineEditUserName.setObjectName(u"passwordModal_LineEditUserName")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.passwordModal_LineEditUserName)

        self.passwordModal_LabelPassword = QLabel(modal_PasswordEntry)
        self.passwordModal_LabelPassword.setObjectName(u"passwordModal_LabelPassword")
        self.passwordModal_LabelPassword.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.passwordModal_LabelPassword)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.passwordModal_LineEditPassword = QLineEdit(modal_PasswordEntry)
        self.passwordModal_LineEditPassword.setObjectName(u"passwordModal_LineEditPassword")
        self.passwordModal_LineEditPassword.setEchoMode(QLineEdit.EchoMode.Normal)

        self.horizontalLayout.addWidget(self.passwordModal_LineEditPassword)

        self.passwordModal_CopyPassword = QToolButton(modal_PasswordEntry)
        self.passwordModal_CopyPassword.setObjectName(u"passwordModal_CopyPassword")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.passwordModal_CopyPassword.setIcon(icon)

        self.horizontalLayout.addWidget(self.passwordModal_CopyPassword)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)

        self.passwordModal_LabelNotes = QLabel(modal_PasswordEntry)
        self.passwordModal_LabelNotes.setObjectName(u"passwordModal_LabelNotes")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordModal_LabelNotes.sizePolicy().hasHeightForWidth())
        self.passwordModal_LabelNotes.setSizePolicy(sizePolicy)
        self.passwordModal_LabelNotes.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.passwordModal_LabelNotes)

        self.passwordModal_TextEditNotes = QTextEdit(modal_PasswordEntry)
        self.passwordModal_TextEditNotes.setObjectName(u"passwordModal_TextEditNotes")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.passwordModal_TextEditNotes)

        self.passwordModal_CheckBoxRevealPassword = QCheckBox(modal_PasswordEntry)
        self.passwordModal_CheckBoxRevealPassword.setObjectName(u"passwordModal_CheckBoxRevealPassword")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.passwordModal_CheckBoxRevealPassword)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.passwordModal_EditCheckBox = QCheckBox(modal_PasswordEntry)
        self.passwordModal_EditCheckBox.setObjectName(u"passwordModal_EditCheckBox")

        self.horizontalLayout_2.addWidget(self.passwordModal_EditCheckBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.passwordModal_buttonBox = QDialogButtonBox(modal_PasswordEntry)
        self.passwordModal_buttonBox.setObjectName(u"passwordModal_buttonBox")
        self.passwordModal_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.passwordModal_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.horizontalLayout_2.addWidget(self.passwordModal_buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(modal_PasswordEntry)
        self.passwordModal_buttonBox.accepted.connect(modal_PasswordEntry.accept)
        self.passwordModal_buttonBox.rejected.connect(modal_PasswordEntry.reject)

        QMetaObject.connectSlotsByName(modal_PasswordEntry)
    # setupUi

    def retranslateUi(self, modal_PasswordEntry):
        modal_PasswordEntry.setWindowTitle(QCoreApplication.translate("modal_PasswordEntry", u"Edit/View Password Entry", None))
        self.passwordModal_LabelTitle.setText(QCoreApplication.translate("modal_PasswordEntry", u"Title", None))
        self.passwordModal_LabelUserName.setText(QCoreApplication.translate("modal_PasswordEntry", u"Username", None))
        self.passwordModal_LabelPassword.setText(QCoreApplication.translate("modal_PasswordEntry", u"Password", None))
        self.passwordModal_LineEditPassword.setText("")
        self.passwordModal_CopyPassword.setText(QCoreApplication.translate("modal_PasswordEntry", u"...", None))
        self.passwordModal_LabelNotes.setText(QCoreApplication.translate("modal_PasswordEntry", u"Notes", None))
        self.passwordModal_CheckBoxRevealPassword.setText(QCoreApplication.translate("modal_PasswordEntry", u"Show Password", None))
        self.passwordModal_EditCheckBox.setText(QCoreApplication.translate("modal_PasswordEntry", u"Enable Editing", None))
    # retranslateUi

