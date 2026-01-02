# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventory.ui'
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

class Ui_InventoryWidget(object):
    def setupUi(self, InventoryWidget):
        if not InventoryWidget.objectName():
            InventoryWidget.setObjectName(u"InventoryWidget")
        InventoryWidget.resize(900, 600)
        InventoryWidget.setStyleSheet(u"QWidget#InventoryWidget {\n"
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
"QPushButton#btnAddMaterial, QPushButton#btnAddStock, QPushButton#btnIssueStock, QPushButton#btnEditMaterial, QPushButton#btnDeleteMaterial, QPushButton#btnRefresh {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnAddMaterial {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnAddMaterial:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnAddStock {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnAddStock:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnIssueStock {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnIssueStock:hover {"
                        "\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QPushButton#btnEditMaterial {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnEditMaterial:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QPushButton#btnDeleteMaterial {\n"
"    background-color: #f44336;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnDeleteMaterial:hover {\n"
"    background-color: #da190b;\n"
"}\n"
"\n"
"QPushButton#btnRefresh {\n"
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
"QTableWidget {\n"
"    background-color: white;\n"
"    border: 1px solid"
                        " #ddd;\n"
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
"QComboBox QAbstractItemV"
                        "iew {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    selection-background-color: #2196F3;\n"
"    selection-color: white;\n"
"    border: 1px solid #ddd;\n"
"}")
        self.verticalLayout = QVBoxLayout(InventoryWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txtSearch = QLineEdit(InventoryWidget)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)

        self.btnRefresh = QPushButton(InventoryWidget)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(100, 40))
        self.btnRefresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnRefresh)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAddMaterial = QPushButton(InventoryWidget)
        self.btnAddMaterial.setObjectName(u"btnAddMaterial")
        self.btnAddMaterial.setMinimumSize(QSize(130, 40))
        self.btnAddMaterial.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnAddMaterial)

        self.btnAddStock = QPushButton(InventoryWidget)
        self.btnAddStock.setObjectName(u"btnAddStock")
        self.btnAddStock.setEnabled(False)
        self.btnAddStock.setMinimumSize(QSize(130, 40))
        self.btnAddStock.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnAddStock)

        self.btnIssueStock = QPushButton(InventoryWidget)
        self.btnIssueStock.setObjectName(u"btnIssueStock")
        self.btnIssueStock.setEnabled(False)
        self.btnIssueStock.setMinimumSize(QSize(130, 40))
        self.btnIssueStock.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnIssueStock)

        self.btnEditMaterial = QPushButton(InventoryWidget)
        self.btnEditMaterial.setObjectName(u"btnEditMaterial")
        self.btnEditMaterial.setEnabled(False)
        self.btnEditMaterial.setMinimumSize(QSize(130, 40))
        self.btnEditMaterial.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnEditMaterial)

        self.btnDeleteMaterial = QPushButton(InventoryWidget)
        self.btnDeleteMaterial.setObjectName(u"btnDeleteMaterial")
        self.btnDeleteMaterial.setEnabled(False)
        self.btnDeleteMaterial.setMinimumSize(QSize(130, 40))
        self.btnDeleteMaterial.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnDeleteMaterial)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lblLowStockAlert = QLabel(InventoryWidget)
        self.lblLowStockAlert.setObjectName(u"lblLowStockAlert")
        self.lblLowStockAlert.setStyleSheet(u"QWidget#InventoryWidget {\n"
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
"QPushButton#btnAddMaterial, QPushButton#btnAddStock, QPushButton#btnIssueStock, QPushButton#btnEditMaterial, QPushButton#btnDeleteMaterial, QPushButton#btnRefresh {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnAddMaterial {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnAddMaterial:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnAddStock {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnAddStock:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnIssueStock {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnIssueStock:hover {"
                        "\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QPushButton#btnEditMaterial {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnEditMaterial:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QPushButton#btnDeleteMaterial {\n"
"    background-color: #f44336;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnDeleteMaterial:hover {\n"
"    background-color: #da190b;\n"
"}\n"
"\n"
"QPushButton#btnRefresh {\n"
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
"QLineEdit#txtSearch:focus"
                        " {\n"
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
"    border-right: "
                        "5px solid transparent;\n"
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

        self.horizontalLayout_2.addWidget(self.lblLowStockAlert)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableInventory = QTableWidget(InventoryWidget)
        if (self.tableInventory.columnCount() < 8):
            self.tableInventory.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableInventory.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableInventory.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableInventory.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableInventory.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableInventory.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableInventory.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableInventory.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableInventory.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableInventory.setObjectName(u"tableInventory")
        self.tableInventory.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableInventory.setAlternatingRowColors(True)
        self.tableInventory.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableInventory.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableInventory.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableInventory)


        self.retranslateUi(InventoryWidget)

        QMetaObject.connectSlotsByName(InventoryWidget)
    # setupUi

    def retranslateUi(self, InventoryWidget):
        InventoryWidget.setWindowTitle(QCoreApplication.translate("InventoryWidget", u"Inventory", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("InventoryWidget", u" Search materials by name or type...", None))
        self.btnRefresh.setText(QCoreApplication.translate("InventoryWidget", u" Refresh", None))
        self.btnAddMaterial.setText(QCoreApplication.translate("InventoryWidget", u" New Material", None))
        self.btnAddStock.setText(QCoreApplication.translate("InventoryWidget", u" Add Stock", None))
        self.btnIssueStock.setText(QCoreApplication.translate("InventoryWidget", u" Issue Stock", None))
        self.btnEditMaterial.setText(QCoreApplication.translate("InventoryWidget", u" Edit", None))
        self.btnDeleteMaterial.setText(QCoreApplication.translate("InventoryWidget", u" Delete", None))
        self.lblLowStockAlert.setText(QCoreApplication.translate("InventoryWidget", u"\u26a0\ufe0f Low Stock: 0", None))
        ___qtablewidgetitem = self.tableInventory.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InventoryWidget", u"Material ID", None));
        ___qtablewidgetitem1 = self.tableInventory.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("InventoryWidget", u"Material Name", None));
        ___qtablewidgetitem2 = self.tableInventory.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("InventoryWidget", u"Type", None));
        ___qtablewidgetitem3 = self.tableInventory.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("InventoryWidget", u"Current Stock", None));
        ___qtablewidgetitem4 = self.tableInventory.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("InventoryWidget", u"Unit", None));
        ___qtablewidgetitem5 = self.tableInventory.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("InventoryWidget", u"Min Stock", None));
        ___qtablewidgetitem6 = self.tableInventory.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("InventoryWidget", u"Supplier", None));
        ___qtablewidgetitem7 = self.tableInventory.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("InventoryWidget", u"Status", None));
    # retranslateUi

