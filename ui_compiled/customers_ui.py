# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customers.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_CustomersWidget(object):
    def setupUi(self, CustomersWidget):
        if not CustomersWidget.objectName():
            CustomersWidget.setObjectName(u"CustomersWidget")
        CustomersWidget.resize(900, 600)
        CustomersWidget.setStyleSheet(u"QWidget#CustomersWidget {\n"
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
"QPushButton#btnAddCustomer, QPushButton#btnEditCustomer, QPushButton#btnDeleteCustomer, QPushButton#btnRefresh {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnAddCustomer {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnAddCustomer:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnEditCustomer {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnEditCustomer:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QPushButton#btnDeleteCustomer {\n"
"    background-color: #f44336;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnDeleteCustomer:hover {\n"
"    background-color: #da190b;\n"
""
                        "}\n"
"\n"
"QPushButton#btnRefresh {\n"
"    background-color: #FF9800;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnRefresh:hover {\n"
"    background-color: #e68900;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #cccccc;\n"
"    color: #666666;\n"
"    cursor: not-allowed;\n"
"}\n"
"\n"
"QLineEdit#txtSearch {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit#txtSearch:focus {\n"
"    border: 2px solid #2196F3;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 5px;\n"
"    gridline-color: #e0e0e0;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #e3f2fd;\n"
"    color: #000;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f5f5f5;\n"
"    padding: 10px;\n"
"    border:"
                        " none;\n"
"    border-bottom: 2px solid #2196F3;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"}")
        self.verticalLayout = QVBoxLayout(CustomersWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txtSearch = QLineEdit(CustomersWidget)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)

        self.btnRefresh = QPushButton(CustomersWidget)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(100, 40))
        self.btnRefresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnRefresh)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAddCustomer = QPushButton(CustomersWidget)
        self.btnAddCustomer.setObjectName(u"btnAddCustomer")
        self.btnAddCustomer.setMinimumSize(QSize(150, 40))
        self.btnAddCustomer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnAddCustomer)

        self.btnEditCustomer = QPushButton(CustomersWidget)
        self.btnEditCustomer.setObjectName(u"btnEditCustomer")
        self.btnEditCustomer.setEnabled(False)
        self.btnEditCustomer.setMinimumSize(QSize(150, 40))
        self.btnEditCustomer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnEditCustomer)

        self.btnDeleteCustomer = QPushButton(CustomersWidget)
        self.btnDeleteCustomer.setObjectName(u"btnDeleteCustomer")
        self.btnDeleteCustomer.setEnabled(False)
        self.btnDeleteCustomer.setMinimumSize(QSize(150, 40))
        self.btnDeleteCustomer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnDeleteCustomer)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lblTotalCustomers = QLabel(CustomersWidget)
        self.lblTotalCustomers.setObjectName(u"lblTotalCustomers")
        self.lblTotalCustomers.setStyleSheet(u"font-size: 13px; color: #666; padding: 10px;")

        self.horizontalLayout_2.addWidget(self.lblTotalCustomers)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableCustomers = QTableWidget(CustomersWidget)
        if (self.tableCustomers.columnCount() < 6):
            self.tableCustomers.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableCustomers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableCustomers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableCustomers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableCustomers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableCustomers.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableCustomers.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableCustomers.setObjectName(u"tableCustomers")
        self.tableCustomers.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCustomers.setAlternatingRowColors(True)
        self.tableCustomers.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableCustomers.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCustomers.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableCustomers)


        self.retranslateUi(CustomersWidget)

        QMetaObject.connectSlotsByName(CustomersWidget)
    # setupUi

    def retranslateUi(self, CustomersWidget):
        CustomersWidget.setWindowTitle(QCoreApplication.translate("CustomersWidget", u"Customers", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("CustomersWidget", u" Search customers by name, contact, or company...", None))
        self.btnRefresh.setText(QCoreApplication.translate("CustomersWidget", u" Refresh", None))
        self.btnAddCustomer.setText(QCoreApplication.translate("CustomersWidget", u" Add Customer", None))
        self.btnEditCustomer.setText(QCoreApplication.translate("CustomersWidget", u" Edit Customer", None))
        self.btnDeleteCustomer.setText(QCoreApplication.translate("CustomersWidget", u" Delete", None))
        self.lblTotalCustomers.setText(QCoreApplication.translate("CustomersWidget", u"Total: 0 customers", None))
        ___qtablewidgetitem = self.tableCustomers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CustomersWidget", u"ID", None));
        ___qtablewidgetitem1 = self.tableCustomers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CustomersWidget", u"Name", None));
        ___qtablewidgetitem2 = self.tableCustomers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CustomersWidget", u"Contact", None));
        ___qtablewidgetitem3 = self.tableCustomers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CustomersWidget", u"Email", None));
        ___qtablewidgetitem4 = self.tableCustomers.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CustomersWidget", u"Company", None));
        ___qtablewidgetitem5 = self.tableCustomers.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("CustomersWidget", u"Address", None));
    # retranslateUi

