# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataModal.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_modal_DataEntry(object):
    def setupUi(self, modal_DataEntry):
        if not modal_DataEntry.objectName():
            modal_DataEntry.setObjectName(u"modal_DataEntry")
        modal_DataEntry.setWindowModality(Qt.WindowModality.WindowModal)
        modal_DataEntry.resize(394, 208)
        modal_DataEntry.setModal(True)
        self.verticalLayout = QVBoxLayout(modal_DataEntry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.dataModal_LabelTitle = QLabel(modal_DataEntry)
        self.dataModal_LabelTitle.setObjectName(u"dataModal_LabelTitle")
        self.dataModal_LabelTitle.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.dataModal_LabelTitle.setAutoFillBackground(False)
        self.dataModal_LabelTitle.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.dataModal_LabelTitle)

        self.dataModal_LineEditTitle = QLineEdit(modal_DataEntry)
        self.dataModal_LineEditTitle.setObjectName(u"dataModal_LineEditTitle")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dataModal_LineEditTitle)

        self.dataModal_LabelFileName = QLabel(modal_DataEntry)
        self.dataModal_LabelFileName.setObjectName(u"dataModal_LabelFileName")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.dataModal_LabelFileName)

        self.dataModal_LineEditFileName = QLineEdit(modal_DataEntry)
        self.dataModal_LineEditFileName.setObjectName(u"dataModal_LineEditFileName")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dataModal_LineEditFileName)

        self.label_3 = QLabel(modal_DataEntry)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dataModal_UploadButton = QPushButton(modal_DataEntry)
        self.dataModal_UploadButton.setObjectName(u"dataModal_UploadButton")

        self.horizontalLayout.addWidget(self.dataModal_UploadButton)

        self.dataModal_DownloadButton = QPushButton(modal_DataEntry)
        self.dataModal_DownloadButton.setObjectName(u"dataModal_DownloadButton")

        self.horizontalLayout.addWidget(self.dataModal_DownloadButton)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer)

        self.dataModal_FileSizeLabel = QLabel(modal_DataEntry)
        self.dataModal_FileSizeLabel.setObjectName(u"dataModal_FileSizeLabel")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dataModal_FileSizeLabel)

        self.label = QLabel(modal_DataEntry)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(60, 0))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dataModal_EditCheckBox = QCheckBox(modal_DataEntry)
        self.dataModal_EditCheckBox.setObjectName(u"dataModal_EditCheckBox")

        self.horizontalLayout_2.addWidget(self.dataModal_EditCheckBox)

        self.dataModal_buttonBox = QDialogButtonBox(modal_DataEntry)
        self.dataModal_buttonBox.setObjectName(u"dataModal_buttonBox")
        self.dataModal_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.dataModal_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.horizontalLayout_2.addWidget(self.dataModal_buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(modal_DataEntry)
        self.dataModal_buttonBox.accepted.connect(modal_DataEntry.accept)
        self.dataModal_buttonBox.rejected.connect(modal_DataEntry.reject)

        QMetaObject.connectSlotsByName(modal_DataEntry)
    # setupUi

    def retranslateUi(self, modal_DataEntry):
        modal_DataEntry.setWindowTitle(QCoreApplication.translate("modal_DataEntry", u"Edit/View Data Entry", None))
        self.dataModal_LabelTitle.setText(QCoreApplication.translate("modal_DataEntry", u"Title:", None))
        self.dataModal_LabelFileName.setText(QCoreApplication.translate("modal_DataEntry", u"Filename:", None))
        self.label_3.setText(QCoreApplication.translate("modal_DataEntry", u"File Contents: ", None))
        self.dataModal_UploadButton.setText(QCoreApplication.translate("modal_DataEntry", u"Upload", None))
        self.dataModal_DownloadButton.setText(QCoreApplication.translate("modal_DataEntry", u"Download", None))
        self.dataModal_FileSizeLabel.setText(QCoreApplication.translate("modal_DataEntry", u"X kB", None))
        self.label.setText(QCoreApplication.translate("modal_DataEntry", u"File Size:", None))
        self.dataModal_EditCheckBox.setText(QCoreApplication.translate("modal_DataEntry", u"Edit", None))
    # retranslateUi

