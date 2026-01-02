# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setMinimumSize(QSize(1200, 700))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QWidget {\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #333333;\n"
"}\n"
"\n"
"QStackedWidget {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"QPushButton#btnDashboard, QPushButton#btnCustomers, QPushButton#btnOrders,\n"
"QPushButton#btnInventory, QPushButton#btnProduction, QPushButton#btnMachines,\n"
"QPushButton#btnEmployees, QPushButton#btnReports, QPushButton#btnSettings {\n"
"    text-align: left;\n"
"    padding: 15px 20px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton#btnDashboard:hover, QPushButton#btnCustomers:hover, QPushButton#btnOrders:hover,\n"
"QPushButton#btnInventory:hover, QPushButton#btnProduction:hover, QPushButton#btnMachines:hover,\n"
"QPushButton#btnEmployees:hover, QPushButton#btnReports:hover, QPushButton#btnSettings:hover {\n"
"    background-color: #e3f2fd;\n"
"    color: #2196F3;\n"
"}\n"
"\n"
""
                        "QPushButton#btnDashboard:checked, QPushButton#btnCustomers:checked, QPushButton#btnOrders:checked,\n"
"QPushButton#btnInventory:checked, QPushButton#btnProduction:checked, QPushButton#btnMachines:checked,\n"
"QPushButton#btnEmployees:checked, QPushButton#btnReports:checked, QPushButton#btnSettings:checked {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnLogout {\n"
"    text-align: left;\n"
"    padding: 15px 20px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    color: #f44336;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton#btnLogout:hover {\n"
"    background-color: #ffebee;\n"
"}\n"
"\n"
"QWidget#sidebar {\n"
"    background-color: white;\n"
"    border-right: 1px solid #ddd;\n"
"}\n"
"\n"
"QWidget#topBar {\n"
"    background-color: white;\n"
"    border-bottom: 1px solid #ddd;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(250, 0))
        self.sidebar.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 20, 10, 20)
        self.lblAppTitle = QLabel(self.sidebar)
        self.lblAppTitle.setObjectName(u"lblAppTitle")
        self.lblAppTitle.setStyleSheet(u"font-size: 20px; font-weight: bold; color: #2196F3; padding: 10px;")
        self.lblAppTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblAppTitle)

        self.line = QFrame(self.sidebar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnDashboard = QPushButton(self.sidebar)
        self.btnDashboard.setObjectName(u"btnDashboard")
        self.btnDashboard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDashboard.setCheckable(True)
        self.btnDashboard.setChecked(True)

        self.verticalLayout.addWidget(self.btnDashboard)

        self.btnCustomers = QPushButton(self.sidebar)
        self.btnCustomers.setObjectName(u"btnCustomers")
        self.btnCustomers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCustomers.setCheckable(True)

        self.verticalLayout.addWidget(self.btnCustomers)

        self.btnOrders = QPushButton(self.sidebar)
        self.btnOrders.setObjectName(u"btnOrders")
        self.btnOrders.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnOrders.setCheckable(True)

        self.verticalLayout.addWidget(self.btnOrders)

        self.btnInventory = QPushButton(self.sidebar)
        self.btnInventory.setObjectName(u"btnInventory")
        self.btnInventory.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnInventory.setCheckable(True)

        self.verticalLayout.addWidget(self.btnInventory)

        self.btnProduction = QPushButton(self.sidebar)
        self.btnProduction.setObjectName(u"btnProduction")
        self.btnProduction.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnProduction.setCheckable(True)

        self.verticalLayout.addWidget(self.btnProduction)

        self.btnMachines = QPushButton(self.sidebar)
        self.btnMachines.setObjectName(u"btnMachines")
        self.btnMachines.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMachines.setCheckable(True)

        self.verticalLayout.addWidget(self.btnMachines)

        self.btnEmployees = QPushButton(self.sidebar)
        self.btnEmployees.setObjectName(u"btnEmployees")
        self.btnEmployees.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEmployees.setCheckable(True)

        self.verticalLayout.addWidget(self.btnEmployees)

        self.btnReports = QPushButton(self.sidebar)
        self.btnReports.setObjectName(u"btnReports")
        self.btnReports.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnReports.setCheckable(True)

        self.verticalLayout.addWidget(self.btnReports)

        self.btnSettings = QPushButton(self.sidebar)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSettings.setCheckable(True)

        self.verticalLayout.addWidget(self.btnSettings)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.line_2 = QFrame(self.sidebar)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.btnLogout = QPushButton(self.sidebar)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnLogout)


        self.horizontalLayout.addWidget(self.sidebar)

        self.mainContent = QWidget(self.centralwidget)
        self.mainContent.setObjectName(u"mainContent")
        self.verticalLayout_2 = QVBoxLayout(self.mainContent)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topBar = QWidget(self.mainContent)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(0, 60))
        self.topBar.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_2 = QHBoxLayout(self.topBar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblPageTitle = QLabel(self.topBar)
        self.lblPageTitle.setObjectName(u"lblPageTitle")
        self.lblPageTitle.setStyleSheet(u"font-size: 18px; font-weight: bold; color: #333;")

        self.horizontalLayout_2.addWidget(self.lblPageTitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lblUserInfo = QLabel(self.topBar)
        self.lblUserInfo.setObjectName(u"lblUserInfo")
        self.lblUserInfo.setStyleSheet(u"font-size: 14px; color: #666; padding-right: 10px;")

        self.horizontalLayout_2.addWidget(self.lblUserInfo)


        self.verticalLayout_2.addWidget(self.topBar)

        self.stackedWidget = QStackedWidget(self.mainContent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.verticalLayout_3 = QVBoxLayout(self.page_dashboard)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lblDashboardPlaceholder = QLabel(self.page_dashboard)
        self.lblDashboardPlaceholder.setObjectName(u"lblDashboardPlaceholder")
        self.lblDashboardPlaceholder.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblDashboardPlaceholder)

        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_placeholder = QWidget()
        self.page_placeholder.setObjectName(u"page_placeholder")
        self.verticalLayout_4 = QVBoxLayout(self.page_placeholder)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lblPlaceholder = QLabel(self.page_placeholder)
        self.lblPlaceholder.setObjectName(u"lblPlaceholder")
        self.lblPlaceholder.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lblPlaceholder)

        self.stackedWidget.addWidget(self.page_placeholder)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.mainContent)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CNC ERP System", None))
        self.lblAppTitle.setText(QCoreApplication.translate("MainWindow", u"CNC ERP", None))
        self.btnDashboard.setText(QCoreApplication.translate("MainWindow", u"  Dashboard", None))
        self.btnCustomers.setText(QCoreApplication.translate("MainWindow", u"  Customers", None))
        self.btnOrders.setText(QCoreApplication.translate("MainWindow", u"  Orders", None))
        self.btnInventory.setText(QCoreApplication.translate("MainWindow", u"  Inventory", None))
        self.btnProduction.setText(QCoreApplication.translate("MainWindow", u"  Production", None))
        self.btnMachines.setText(QCoreApplication.translate("MainWindow", u"  Machines", None))
        self.btnEmployees.setText(QCoreApplication.translate("MainWindow", u"  Employees", None))
        self.btnReports.setText(QCoreApplication.translate("MainWindow", u"  Reports", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
        self.btnLogout.setText(QCoreApplication.translate("MainWindow", u"  Logout", None))
        self.lblPageTitle.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.lblUserInfo.setText(QCoreApplication.translate("MainWindow", u"Admin User", None))
        self.lblDashboardPlaceholder.setText(QCoreApplication.translate("MainWindow", u"Dashboard Content Will Load Here", None))
        self.lblPlaceholder.setText(QCoreApplication.translate("MainWindow", u"Module Content Will Load Here", None))
    # retranslateUi

