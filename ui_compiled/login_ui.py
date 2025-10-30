# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(450, 550)
        LoginWindow.setMinimumSize(QSize(450, 550))
        LoginWindow.setMaximumSize(QSize(450, 550))
        LoginWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    padding: 12px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
"}\n"
"\n"
"QPushButton#btnLogin {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    padding: 12px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnLogin:hover {\n"
"    background-color: #1976D2;\n"
"}\n"
"\n"
"QPushButton#btnLogin:pressed {\n"
"    background-color: #0D47A1;\n"
"}\n"
"\n"
"QLabel#lblTitle {\n"
"    color: #333;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel#lblSubtitle {\n"
"    color: #666;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLabel#lblError {\n"
"    color: #f44336;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #666;\n"
"    font-size: 13"
                        "px;\n"
"}")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_top)

        self.loginContainer = QWidget(self.centralwidget)
        self.loginContainer.setObjectName(u"loginContainer")
        self.loginContainer.setStyleSheet(u"QWidget#loginContainer {\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.loginContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(40, 40, 40, 40)
        self.lblLogo = QLabel(self.loginContainer)
        self.lblLogo.setObjectName(u"lblLogo")
        self.lblLogo.setMinimumSize(QSize(80, 80))
        self.lblLogo.setMaximumSize(QSize(80, 80))
        self.lblLogo.setStyleSheet(u"QLabel {\n"
"    background-color: #2196F3;\n"
"    border-radius: 40px;\n"
"    color: white;\n"
"    font-size: 36px;\n"
"    font-weight: bold;\n"
"}")
        self.lblLogo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lblLogo)

        self.verticalSpacer_logo = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_logo)

        self.lblTitle = QLabel(self.loginContainer)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lblTitle)

        self.lblSubtitle = QLabel(self.loginContainer)
        self.lblSubtitle.setObjectName(u"lblSubtitle")
        self.lblSubtitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lblSubtitle)

        self.verticalSpacer_title = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_title)

        self.lblEmail = QLabel(self.loginContainer)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setStyleSheet(u"color: #333; font-size: 13px; font-weight: bold;")

        self.verticalLayout_2.addWidget(self.lblEmail)

        self.txtEmail = QLineEdit(self.loginContainer)
        self.txtEmail.setObjectName(u"txtEmail")

        self.verticalLayout_2.addWidget(self.txtEmail)

        self.verticalSpacer_email = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_email)

        self.lblPassword = QLabel(self.loginContainer)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setStyleSheet(u"color: #333; font-size: 13px; font-weight: bold;")

        self.verticalLayout_2.addWidget(self.lblPassword)

        self.txtPassword = QLineEdit(self.loginContainer)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.txtPassword)

        self.verticalSpacer_password = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_password)

        self.chkRememberMe = QCheckBox(self.loginContainer)
        self.chkRememberMe.setObjectName(u"chkRememberMe")

        self.verticalLayout_2.addWidget(self.chkRememberMe)

        self.verticalSpacer_remember = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_remember)

        self.lblError = QLabel(self.loginContainer)
        self.lblError.setObjectName(u"lblError")
        self.lblError.setAlignment(Qt.AlignCenter)
        self.lblError.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lblError)

        self.btnLogin = QPushButton(self.loginContainer)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setMinimumSize(QSize(0, 45))
        self.btnLogin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnLogin)


        self.verticalLayout.addWidget(self.loginContainer)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_bottom)

        self.lblVersion = QLabel(self.centralwidget)
        self.lblVersion.setObjectName(u"lblVersion")
        self.lblVersion.setStyleSheet(u"color: #999; font-size: 11px;")
        self.lblVersion.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblVersion)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"CNC ERP - Login", None))
        self.lblLogo.setText(QCoreApplication.translate("LoginWindow", u"CNC", None))
        self.lblTitle.setText(QCoreApplication.translate("LoginWindow", u"Welcome Back", None))
        self.lblSubtitle.setText(QCoreApplication.translate("LoginWindow", u"Sign in to access your ERP dashboard", None))
        self.lblEmail.setText(QCoreApplication.translate("LoginWindow", u"Email Address", None))
        self.txtEmail.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Enter your email", None))
        self.lblPassword.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Enter your password", None))
        self.chkRememberMe.setText(QCoreApplication.translate("LoginWindow", u"Remember me", None))
        self.lblError.setText("")
        self.btnLogin.setText(QCoreApplication.translate("LoginWindow", u"LOGIN", None))
        self.lblVersion.setText(QCoreApplication.translate("LoginWindow", u"CNC ERP System v1.0", None))
    # retranslateUi

