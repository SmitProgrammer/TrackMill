# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employee_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_EmployeeDialog(object):
    def setupUi(self, EmployeeDialog):
        if not EmployeeDialog.objectName():
            EmployeeDialog.setObjectName(u"EmployeeDialog")
        EmployeeDialog.resize(500, 600)
        EmployeeDialog.setMinimumSize(QSize(500, 600))
        EmployeeDialog.setMaximumSize(QSize(500, 600))
        EmployeeDialog.setStyleSheet(u"QDialog {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 13px;\n"
"    color: #333;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit, QComboBox, QCheckBox {\n"
"    padding: 8px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QComboBox:focus {\n"
"    border: 2px solid #2196F3;\n"
"}\n"
"\n"
"QPushButton#btnSave {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    padding: 10px 25px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnSave:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnCancel {\n"
"    background-color: #f44336;\n"
"    color: white;\n"
"    padding: 10px 25px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnCa"
                        "ncel:hover {\n"
"    background-color: #da190b;\n"
"}")
        self.verticalLayout = QVBoxLayout(EmployeeDialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(EmployeeDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.txtName = QLineEdit(EmployeeDialog)
        self.txtName.setObjectName(u"txtName")

        self.verticalLayout.addWidget(self.txtName)

        self.label_2 = QLabel(EmployeeDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.cmbRole = QComboBox(EmployeeDialog)
        self.cmbRole.addItem("")
        self.cmbRole.addItem("")
        self.cmbRole.setObjectName(u"cmbRole")

        self.verticalLayout.addWidget(self.cmbRole)

        self.label_3 = QLabel(EmployeeDialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.txtContact = QLineEdit(EmployeeDialog)
        self.txtContact.setObjectName(u"txtContact")

        self.verticalLayout.addWidget(self.txtContact)

        self.label_4 = QLabel(EmployeeDialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.txtAddress = QTextEdit(EmployeeDialog)
        self.txtAddress.setObjectName(u"txtAddress")
        self.txtAddress.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout.addWidget(self.txtAddress)

        self.label_5 = QLabel(EmployeeDialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.cmbStatus = QComboBox(EmployeeDialog)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.verticalLayout.addWidget(self.cmbStatus)

        self.chkHasLogin = QCheckBox(EmployeeDialog)
        self.chkHasLogin.setObjectName(u"chkHasLogin")

        self.verticalLayout.addWidget(self.chkHasLogin)

        self.label_6 = QLabel(EmployeeDialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.txtEmail = QLineEdit(EmployeeDialog)
        self.txtEmail.setObjectName(u"txtEmail")

        self.verticalLayout.addWidget(self.txtEmail)

        self.label_7 = QLabel(EmployeeDialog)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.txtPassword = QLineEdit(EmployeeDialog)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.txtPassword)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(EmployeeDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)

        self.btnCancel = QPushButton(EmployeeDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(EmployeeDialog)

        QMetaObject.connectSlotsByName(EmployeeDialog)
    # setupUi

    def retranslateUi(self, EmployeeDialog):
        EmployeeDialog.setWindowTitle(QCoreApplication.translate("EmployeeDialog", u"Employee Details", None))
        self.label.setText(QCoreApplication.translate("EmployeeDialog", u"Employee Name:", None))
        self.txtName.setPlaceholderText(QCoreApplication.translate("EmployeeDialog", u"Enter employee name", None))
        self.label_2.setText(QCoreApplication.translate("EmployeeDialog", u"Role:", None))
        self.cmbRole.setItemText(0, QCoreApplication.translate("EmployeeDialog", u"Admin", None))
        self.cmbRole.setItemText(1, QCoreApplication.translate("EmployeeDialog", u"Operator", None))

        self.label_3.setText(QCoreApplication.translate("EmployeeDialog", u"Contact Number:", None))
        self.txtContact.setPlaceholderText(QCoreApplication.translate("EmployeeDialog", u"Enter contact number", None))
        self.label_4.setText(QCoreApplication.translate("EmployeeDialog", u"Address:", None))
        self.txtAddress.setPlaceholderText(QCoreApplication.translate("EmployeeDialog", u"Enter address", None))
        self.label_5.setText(QCoreApplication.translate("EmployeeDialog", u"Status:", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("EmployeeDialog", u"Active", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("EmployeeDialog", u"Blocked", None))

        self.chkHasLogin.setText(QCoreApplication.translate("EmployeeDialog", u"Create Login Account (Operator only)", None))
        self.label_6.setText(QCoreApplication.translate("EmployeeDialog", u"Email (for login):", None))
        self.txtEmail.setPlaceholderText(QCoreApplication.translate("EmployeeDialog", u"Enter email for login", None))
        self.label_7.setText(QCoreApplication.translate("EmployeeDialog", u"Password:", None))
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("EmployeeDialog", u"Enter password (min 6 characters)", None))
        self.btnSave.setText(QCoreApplication.translate("EmployeeDialog", u"Save", None))
        self.btnCancel.setText(QCoreApplication.translate("EmployeeDialog", u"Cancel", None))
    # retranslateUi

