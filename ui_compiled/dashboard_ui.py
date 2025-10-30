# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DashboardWidget(object):
    def setupUi(self, DashboardWidget):
        if not DashboardWidget.objectName():
            DashboardWidget.setObjectName(u"DashboardWidget")
        DashboardWidget.resize(900, 600)
        DashboardWidget.setStyleSheet(u"QWidget#DashboardWidget {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QWidget#cardOrders, QWidget#cardInventory, QWidget#cardEmployees, QWidget#cardMachines {\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"QLabel#lblOrdersValue, QLabel#lblInventoryValue, QLabel#lblEmployeesValue, QLabel#lblMachinesValue {\n"
"    font-size: 32px;\n"
"    font-weight: bold;\n"
"    color: #2196F3;\n"
"}\n"
"\n"
"QLabel#lblOrdersLabel, QLabel#lblInventoryLabel, QLabel#lblEmployeesLabel, QLabel#lblMachinesLabel {\n"
"    font-size: 14px;\n"
"    color: #666;\n"
"}\n"
"\n"
"QLabel#lblOrdersIcon, QLabel#lblInventoryIcon, QLabel#lblEmployeesIcon, QLabel#lblMachinesIcon {\n"
"    font-size: 40px;\n"
"}\n"
"\n"
"QWidget#recentActivityCard {\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"QLabel#lblRecentTitle {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLis"
                        "tWidget {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 10px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #f5f5f5;\n"
"}")
        self.verticalLayout = QVBoxLayout(DashboardWidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.lblWelcome = QLabel(DashboardWidget)
        self.lblWelcome.setObjectName(u"lblWelcome")
        self.lblWelcome.setStyleSheet(u"font-size: 20px; font-weight: bold; color: #333;")

        self.verticalLayout.addWidget(self.lblWelcome)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cardOrders = QWidget(DashboardWidget)
        self.cardOrders.setObjectName(u"cardOrders")
        self.cardOrders.setMinimumSize(QSize(0, 120))
        self.horizontalLayout = QHBoxLayout(self.cardOrders)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.lblOrdersIcon = QLabel(self.cardOrders)
        self.lblOrdersIcon.setObjectName(u"lblOrdersIcon")
        self.lblOrdersIcon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lblOrdersIcon)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblOrdersValue = QLabel(self.cardOrders)
        self.lblOrdersValue.setObjectName(u"lblOrdersValue")
        self.lblOrdersValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lblOrdersValue)

        self.lblOrdersLabel = QLabel(self.cardOrders)
        self.lblOrdersLabel.setObjectName(u"lblOrdersLabel")
        self.lblOrdersLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lblOrdersLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.cardOrders, 0, 0, 1, 1)

        self.cardInventory = QWidget(DashboardWidget)
        self.cardInventory.setObjectName(u"cardInventory")
        self.cardInventory.setMinimumSize(QSize(0, 120))
        self.horizontalLayout_2 = QHBoxLayout(self.cardInventory)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.lblInventoryIcon = QLabel(self.cardInventory)
        self.lblInventoryIcon.setObjectName(u"lblInventoryIcon")
        self.lblInventoryIcon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblInventoryIcon)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lblInventoryValue = QLabel(self.cardInventory)
        self.lblInventoryValue.setObjectName(u"lblInventoryValue")
        self.lblInventoryValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lblInventoryValue)

        self.lblInventoryLabel = QLabel(self.cardInventory)
        self.lblInventoryLabel.setObjectName(u"lblInventoryLabel")
        self.lblInventoryLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lblInventoryLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.cardInventory, 0, 1, 1, 1)

        self.cardEmployees = QWidget(DashboardWidget)
        self.cardEmployees.setObjectName(u"cardEmployees")
        self.cardEmployees.setMinimumSize(QSize(0, 120))
        self.horizontalLayout_3 = QHBoxLayout(self.cardEmployees)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.lblEmployeesIcon = QLabel(self.cardEmployees)
        self.lblEmployeesIcon.setObjectName(u"lblEmployeesIcon")
        self.lblEmployeesIcon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lblEmployeesIcon)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lblEmployeesValue = QLabel(self.cardEmployees)
        self.lblEmployeesValue.setObjectName(u"lblEmployeesValue")
        self.lblEmployeesValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.lblEmployeesValue)

        self.lblEmployeesLabel = QLabel(self.cardEmployees)
        self.lblEmployeesLabel.setObjectName(u"lblEmployeesLabel")
        self.lblEmployeesLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.lblEmployeesLabel)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.cardEmployees, 1, 0, 1, 1)

        self.cardMachines = QWidget(DashboardWidget)
        self.cardMachines.setObjectName(u"cardMachines")
        self.cardMachines.setMinimumSize(QSize(0, 120))
        self.horizontalLayout_4 = QHBoxLayout(self.cardMachines)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.lblMachinesIcon = QLabel(self.cardMachines)
        self.lblMachinesIcon.setObjectName(u"lblMachinesIcon")
        self.lblMachinesIcon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lblMachinesIcon)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lblMachinesValue = QLabel(self.cardMachines)
        self.lblMachinesValue.setObjectName(u"lblMachinesValue")
        self.lblMachinesValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.lblMachinesValue)

        self.lblMachinesLabel = QLabel(self.cardMachines)
        self.lblMachinesLabel.setObjectName(u"lblMachinesLabel")
        self.lblMachinesLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.lblMachinesLabel)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.gridLayout.addWidget(self.cardMachines, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.recentActivityCard = QWidget(DashboardWidget)
        self.recentActivityCard.setObjectName(u"recentActivityCard")
        self.verticalLayout_6 = QVBoxLayout(self.recentActivityCard)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.lblRecentTitle = QLabel(self.recentActivityCard)
        self.lblRecentTitle.setObjectName(u"lblRecentTitle")

        self.verticalLayout_6.addWidget(self.lblRecentTitle)

        self.listRecentActivity = QListWidget(self.recentActivityCard)
        self.listRecentActivity.setObjectName(u"listRecentActivity")
        self.listRecentActivity.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.listRecentActivity)


        self.verticalLayout.addWidget(self.recentActivityCard)


        self.retranslateUi(DashboardWidget)

        QMetaObject.connectSlotsByName(DashboardWidget)
    # setupUi

    def retranslateUi(self, DashboardWidget):
        DashboardWidget.setWindowTitle(QCoreApplication.translate("DashboardWidget", u"Dashboard", None))
        self.lblWelcome.setText(QCoreApplication.translate("DashboardWidget", u"Welcome to CNC ERP Dashboard", None))
        self.lblOrdersIcon.setText("")
        self.lblOrdersValue.setText(QCoreApplication.translate("DashboardWidget", u"0", None))
        self.lblOrdersLabel.setText(QCoreApplication.translate("DashboardWidget", u"Active Orders", None))
        self.lblInventoryIcon.setText("")
        self.lblInventoryValue.setText(QCoreApplication.translate("DashboardWidget", u"0", None))
        self.lblInventoryLabel.setText(QCoreApplication.translate("DashboardWidget", u"Inventory Items", None))
        self.lblEmployeesIcon.setText("")
        self.lblEmployeesValue.setText(QCoreApplication.translate("DashboardWidget", u"0", None))
        self.lblEmployeesLabel.setText(QCoreApplication.translate("DashboardWidget", u"Active Employees", None))
        self.lblMachinesIcon.setText("")
        self.lblMachinesValue.setText(QCoreApplication.translate("DashboardWidget", u"0", None))
        self.lblMachinesLabel.setText(QCoreApplication.translate("DashboardWidget", u"Available Machines", None))
        self.lblRecentTitle.setText(QCoreApplication.translate("DashboardWidget", u"Recent Activity", None))
    # retranslateUi

