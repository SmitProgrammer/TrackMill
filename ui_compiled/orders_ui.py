# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orders.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_OrdersWidget(object):
    def setupUi(self, OrdersWidget):
        if not OrdersWidget.objectName():
            OrdersWidget.setObjectName(u"OrdersWidget")
        OrdersWidget.resize(900, 600)
        OrdersWidget.setStyleSheet(u"QWidget#OrdersWidget {\n"
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
"QPushButton#btnAddOrder, QPushButton#btnEditOrder, QPushButton#btnDeleteOrder, QPushButton#btnRefresh {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnAddOrder {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnAddOrder:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnEditOrder {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnEditOrder:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QPushButton#btnDeleteOrder {\n"
"    background-color: #f44336;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnDeleteOrder:hover {\n"
"    background-color: #da190b;\n"
"}\n"
"\n"
"QPushButton#btn"
                        "Refresh {\n"
"    background-color: #607D8B;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnRefresh:hover {\n"
"    background-color: #546E7A;\n"
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
"QComboBox#cmbFilterStatus {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QComboBox#cmbFilterStatus:focus {\n"
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
"    background-color: #e3f"
                        "2fd;\n"
"    color: #000;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f5f5f5;\n"
"    padding: 10px;\n"
"    border: none;\n"
"    border-bottom: 2px solid #2196F3;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"}\n"
"\n"
"QComboBox {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2196F3;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 30px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 5px solid #333;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    selection-background-color: #2196F3;\n"
"    selection-color: white;\n"
"    border: 1px solid #ddd;\n"
"}")
        self.verticalLayout = QVBoxLayout(OrdersWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txtSearch = QLineEdit(OrdersWidget)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)

        self.cmbFilterStatus = QComboBox(OrdersWidget)
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.setObjectName(u"cmbFilterStatus")
        self.cmbFilterStatus.setMinimumSize(QSize(150, 40))

        self.horizontalLayout.addWidget(self.cmbFilterStatus)

        self.btnRefresh = QPushButton(OrdersWidget)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(100, 40))
        self.btnRefresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnRefresh)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAddOrder = QPushButton(OrdersWidget)
        self.btnAddOrder.setObjectName(u"btnAddOrder")
        self.btnAddOrder.setMinimumSize(QSize(150, 40))
        self.btnAddOrder.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnAddOrder)

        self.btnEditOrder = QPushButton(OrdersWidget)
        self.btnEditOrder.setObjectName(u"btnEditOrder")
        self.btnEditOrder.setEnabled(False)
        self.btnEditOrder.setMinimumSize(QSize(150, 40))
        self.btnEditOrder.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnEditOrder)

        self.btnDeleteOrder = QPushButton(OrdersWidget)
        self.btnDeleteOrder.setObjectName(u"btnDeleteOrder")
        self.btnDeleteOrder.setEnabled(False)
        self.btnDeleteOrder.setMinimumSize(QSize(150, 40))
        self.btnDeleteOrder.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnDeleteOrder)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lblTotalOrders = QLabel(OrdersWidget)
        self.lblTotalOrders.setObjectName(u"lblTotalOrders")
        self.lblTotalOrders.setStyleSheet(u"QWidget#OrdersWidget {\n"
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
"QPushButton#btnAddOrder, QPushButton#btnEditOrder, QPushButton#btnDeleteOrder, QPushButton#btnRefresh {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnAddOrder {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnAddOrder:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnEditOrder {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnEditOrder:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QPushButton#btnDeleteOrder {\n"
"    background-color: #f44336;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnDeleteOrder:hover {\n"
"    background-color: #da190b;\n"
"}\n"
"\n"
"QPushButton#btn"
                        "Refresh {\n"
"    background-color: #607D8B;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnRefresh:hover {\n"
"    background-color: #546E7A;\n"
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
"QComboBox#cmbFilterStatus {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QComboBox#cmbFilterStatus:focus {\n"
"    border: 2px solid #2196F3;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 5px;\n"
"    gridline-color: #e0e0e0;\n"
"}\n"
""
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
"    border: none;\n"
"    border-bottom: 2px solid #2196F3;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"}\n"
"\n"
"QComboBox {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2196F3;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 30px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 5px solid #333;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    selection-"
                        "background-color: #2196F3;\n"
"    selection-color: white;\n"
"    border: 1px solid #ddd;\n"
"}")

        self.horizontalLayout_2.addWidget(self.lblTotalOrders)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableOrders = QTableWidget(OrdersWidget)
        if (self.tableOrders.columnCount() < 8):
            self.tableOrders.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableOrders.setObjectName(u"tableOrders")
        self.tableOrders.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableOrders.setAlternatingRowColors(True)
        self.tableOrders.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableOrders.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableOrders.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableOrders)


        self.retranslateUi(OrdersWidget)

        QMetaObject.connectSlotsByName(OrdersWidget)
    # setupUi

    def retranslateUi(self, OrdersWidget):
        OrdersWidget.setWindowTitle(QCoreApplication.translate("OrdersWidget", u"Orders", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("OrdersWidget", u" Search orders by ID, customer, or product...", None))
        self.cmbFilterStatus.setItemText(0, QCoreApplication.translate("OrdersWidget", u"All Status", None))
        self.cmbFilterStatus.setItemText(1, QCoreApplication.translate("OrdersWidget", u"Pending", None))
        self.cmbFilterStatus.setItemText(2, QCoreApplication.translate("OrdersWidget", u"In Production", None))
        self.cmbFilterStatus.setItemText(3, QCoreApplication.translate("OrdersWidget", u"Completed", None))
        self.cmbFilterStatus.setItemText(4, QCoreApplication.translate("OrdersWidget", u"Cancelled", None))

        self.btnRefresh.setText(QCoreApplication.translate("OrdersWidget", u" Refresh", None))
        self.btnAddOrder.setText(QCoreApplication.translate("OrdersWidget", u" New Order", None))
        self.btnEditOrder.setText(QCoreApplication.translate("OrdersWidget", u" Edit Order", None))
        self.btnDeleteOrder.setText(QCoreApplication.translate("OrdersWidget", u" Delete", None))
        self.lblTotalOrders.setText(QCoreApplication.translate("OrdersWidget", u"Total: 0 orders", None))
        ___qtablewidgetitem = self.tableOrders.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("OrdersWidget", u"Order ID", None));
        ___qtablewidgetitem1 = self.tableOrders.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("OrdersWidget", u"Customer", None));
        ___qtablewidgetitem2 = self.tableOrders.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("OrdersWidget", u"Product", None));
        ___qtablewidgetitem3 = self.tableOrders.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("OrdersWidget", u"Quantity", None));
        ___qtablewidgetitem4 = self.tableOrders.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("OrdersWidget", u"Order Date", None));
        ___qtablewidgetitem5 = self.tableOrders.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("OrdersWidget", u"Delivery Date", None));
        ___qtablewidgetitem6 = self.tableOrders.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("OrdersWidget", u"Priority", None));
        ___qtablewidgetitem7 = self.tableOrders.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("OrdersWidget", u"Status", None));
    # retranslateUi

