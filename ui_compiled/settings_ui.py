# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(900, 600)
        SettingsWidget.setStyleSheet(u"QWidget#SettingsWidget {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #333;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    color: #333;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings, QPushButton#btnChangePassword {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
""
                        "}\n"
"\n"
"QGroupBox {\n"
"    background-color: white;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    margin-top: 15px;\n"
"    padding-top: 15px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px 10px;\n"
"    color: #2196F3;\n"
"}")
        self.verticalLayout = QVBoxLayout(SettingsWidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(SettingsWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QWidget#SettingsWidget {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #333;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    color: #333;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings, QPushButton#btnChangePassword {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
""
                        "}\n"
"\n"
"QGroupBox {\n"
"    background-color: white;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    margin-top: 15px;\n"
"    padding-top: 15px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px 10px;\n"
"    color: #2196F3;\n"
"}")

        self.verticalLayout.addWidget(self.label)

        self.groupCompany = QGroupBox(SettingsWidget)
        self.groupCompany.setObjectName(u"groupCompany")
        self.formLayout = QFormLayout(self.groupCompany)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(15, 15, 15, 15)
        self.label_2 = QLabel(self.groupCompany)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QWidget#SettingsWidget {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #333;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    color: #333;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings, QPushButton#btnChangePassword {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
""
                        "}\n"
"\n"
"QGroupBox {\n"
"    background-color: white;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    margin-top: 15px;\n"
"    padding-top: 15px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px 10px;\n"
"    color: #2196F3;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.txtCompanyName = QLineEdit(self.groupCompany)
        self.txtCompanyName.setObjectName(u"txtCompanyName")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtCompanyName)

        self.label_3 = QLabel(self.groupCompany)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QWidget#SettingsWidget {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #333;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    color: #333;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings, QPushButton#btnChangePassword {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
""
                        "}\n"
"\n"
"QGroupBox {\n"
"    background-color: white;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    margin-top: 15px;\n"
"    padding-top: 15px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px 10px;\n"
"    color: #2196F3;\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.txtCompanyAddress = QLineEdit(self.groupCompany)
        self.txtCompanyAddress.setObjectName(u"txtCompanyAddress")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtCompanyAddress)

        self.label_4 = QLabel(self.groupCompany)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QWidget#SettingsWidget {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #333;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    color: #333;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings, QPushButton#btnChangePassword {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
""
                        "}\n"
"\n"
"QGroupBox {\n"
"    background-color: white;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    margin-top: 15px;\n"
"    padding-top: 15px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px 10px;\n"
"    color: #2196F3;\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.txtCompanyContact = QLineEdit(self.groupCompany)
        self.txtCompanyContact.setObjectName(u"txtCompanyContact")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtCompanyContact)

        self.label_5 = QLabel(self.groupCompany)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QWidget#SettingsWidget {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #333;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    color: #333;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings, QPushButton#btnChangePassword {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
""
                        "}\n"
"\n"
"QGroupBox {\n"
"    background-color: white;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    margin-top: 15px;\n"
"    padding-top: 15px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px 10px;\n"
"    color: #2196F3;\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.txtCompanyEmail = QLineEdit(self.groupCompany)
        self.txtCompanyEmail.setObjectName(u"txtCompanyEmail")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtCompanyEmail)


        self.verticalLayout.addWidget(self.groupCompany)

        self.groupAccount = QGroupBox(SettingsWidget)
        self.groupAccount.setObjectName(u"groupAccount")
        self.verticalLayout_2 = QVBoxLayout(self.groupAccount)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.groupAccount)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QWidget#SettingsWidget {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #333;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    color: #333;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings, QPushButton#btnChangePassword {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
""
                        "}\n"
"\n"
"QGroupBox {\n"
"    background-color: white;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    margin-top: 15px;\n"
"    padding-top: 15px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px 10px;\n"
"    color: #2196F3;\n"
"}")

        self.horizontalLayout.addWidget(self.label_6)

        self.lblCurrentUser = QLabel(self.groupAccount)
        self.lblCurrentUser.setObjectName(u"lblCurrentUser")
        self.lblCurrentUser.setStyleSheet(u"QWidget#SettingsWidget {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #333;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    color: #333;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings, QPushButton#btnChangePassword {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnSaveSettings:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnChangePassword:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
""
                        "}\n"
"\n"
"QGroupBox {\n"
"    background-color: white;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    margin-top: 15px;\n"
"    padding-top: 15px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px 10px;\n"
"    color: #2196F3;\n"
"}")

        self.horizontalLayout.addWidget(self.lblCurrentUser)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnChangePassword = QPushButton(self.groupAccount)
        self.btnChangePassword.setObjectName(u"btnChangePassword")
        self.btnChangePassword.setMinimumSize(QSize(0, 40))
        self.btnChangePassword.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnChangePassword)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupAccount)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btnSaveSettings = QPushButton(SettingsWidget)
        self.btnSaveSettings.setObjectName(u"btnSaveSettings")
        self.btnSaveSettings.setMinimumSize(QSize(200, 45))
        self.btnSaveSettings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btnSaveSettings)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Settings", None))
        self.label.setText(QCoreApplication.translate("SettingsWidget", u"System Settings", None))
        self.groupCompany.setTitle(QCoreApplication.translate("SettingsWidget", u"Company Information", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWidget", u"Company Name:", None))
        self.txtCompanyName.setPlaceholderText(QCoreApplication.translate("SettingsWidget", u"Enter company name", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWidget", u"Address:", None))
        self.txtCompanyAddress.setPlaceholderText(QCoreApplication.translate("SettingsWidget", u"Enter company address", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWidget", u"Contact:", None))
        self.txtCompanyContact.setPlaceholderText(QCoreApplication.translate("SettingsWidget", u"Enter contact number", None))
        self.label_5.setText(QCoreApplication.translate("SettingsWidget", u"Email:", None))
        self.txtCompanyEmail.setPlaceholderText(QCoreApplication.translate("SettingsWidget", u"Enter company email", None))
        self.groupAccount.setTitle(QCoreApplication.translate("SettingsWidget", u"Account Settings", None))
        self.label_6.setText(QCoreApplication.translate("SettingsWidget", u"Current User:", None))
        self.lblCurrentUser.setText(QCoreApplication.translate("SettingsWidget", u"admin@cnc.com", None))
        self.btnChangePassword.setText(QCoreApplication.translate("SettingsWidget", u" Change Password", None))
        self.btnSaveSettings.setText(QCoreApplication.translate("SettingsWidget", u" Save Settings", None))
    # retranslateUi

