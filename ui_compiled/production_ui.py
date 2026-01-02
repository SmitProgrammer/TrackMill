# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'production.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_ProductionWidget(object):
    def setupUi(self, ProductionWidget):
        if not ProductionWidget.objectName():
            ProductionWidget.setObjectName(u"ProductionWidget")
        ProductionWidget.resize(900, 600)
        ProductionWidget.setStyleSheet(u"QWidget#ProductionWidget {\n"
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
"QPushButton#btnNewJob, QPushButton#btnEditJob, QPushButton#btnDeleteJob, QPushButton#btnRefresh {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnNewJob {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnNewJob:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnEditJob {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnEditJob:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QPushButton#btnDeleteJob {\n"
"    background-color: #f44336;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnDeleteJob:hover {\n"
"    background-color: #da190b;\n"
"}\n"
"\n"
"QPushButton#btnRefresh {\n"
""
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
"    background-color: #e3f2fd;\n"
"    c"
                        "olor: #000;\n"
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
        self.verticalLayout = QVBoxLayout(ProductionWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(ProductionWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QWidget#ProductionWidget {\n"
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
"QPushButton#btnNewJob, QPushButton#btnEditJob, QPushButton#btnDeleteJob, QPushButton#btnRefresh {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnNewJob {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnNewJob:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnEditJob {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnEditJob:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QPushButton#btnDeleteJob {\n"
"    background-color: #f44336;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnDeleteJob:hover {\n"
"    background-color: #da190b;\n"
"}\n"
"\n"
"QPushButton#btnRefresh {\n"
""
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
"    background-color: #e3f2fd;\n"
"    c"
                        "olor: #000;\n"
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

        self.horizontalLayout.addWidget(self.label)

        self.cmbFilterStatus = QComboBox(ProductionWidget)
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.setObjectName(u"cmbFilterStatus")
        self.cmbFilterStatus.setMinimumSize(QSize(150, 40))

        self.horizontalLayout.addWidget(self.cmbFilterStatus)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btnRefresh = QPushButton(ProductionWidget)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(100, 40))
        self.btnRefresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnRefresh)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnNewJob = QPushButton(ProductionWidget)
        self.btnNewJob.setObjectName(u"btnNewJob")
        self.btnNewJob.setMinimumSize(QSize(150, 40))
        self.btnNewJob.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnNewJob)

        self.btnEditJob = QPushButton(ProductionWidget)
        self.btnEditJob.setObjectName(u"btnEditJob")
        self.btnEditJob.setEnabled(False)
        self.btnEditJob.setMinimumSize(QSize(150, 40))
        self.btnEditJob.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnEditJob)

        self.btnDeleteJob = QPushButton(ProductionWidget)
        self.btnDeleteJob.setObjectName(u"btnDeleteJob")
        self.btnDeleteJob.setEnabled(False)
        self.btnDeleteJob.setMinimumSize(QSize(150, 40))
        self.btnDeleteJob.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnDeleteJob)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lblTotalJobs = QLabel(ProductionWidget)
        self.lblTotalJobs.setObjectName(u"lblTotalJobs")
        self.lblTotalJobs.setStyleSheet(u"QWidget#ProductionWidget {\n"
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
"QPushButton#btnNewJob, QPushButton#btnEditJob, QPushButton#btnDeleteJob, QPushButton#btnRefresh {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnNewJob {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnNewJob:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnEditJob {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnEditJob:hover {\n"
"    background-color: #0b7dda;\n"
"}\n"
"\n"
"QPushButton#btnDeleteJob {\n"
"    background-color: #f44336;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnDeleteJob:hover {\n"
"    background-color: #da190b;\n"
"}\n"
"\n"
"QPushButton#btnRefresh {\n"
""
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
"\n"
"QTable"
                        "Widget::item {\n"
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
"    selection-background-"
                        "color: #2196F3;\n"
"    selection-color: white;\n"
"    border: 1px solid #ddd;\n"
"}")

        self.horizontalLayout_2.addWidget(self.lblTotalJobs)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableJobs = QTableWidget(ProductionWidget)
        if (self.tableJobs.columnCount() < 8):
            self.tableJobs.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableJobs.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableJobs.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableJobs.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableJobs.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableJobs.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableJobs.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableJobs.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableJobs.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableJobs.setObjectName(u"tableJobs")
        self.tableJobs.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableJobs.setAlternatingRowColors(True)
        self.tableJobs.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableJobs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableJobs.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableJobs)


        self.retranslateUi(ProductionWidget)

        QMetaObject.connectSlotsByName(ProductionWidget)
    # setupUi

    def retranslateUi(self, ProductionWidget):
        ProductionWidget.setWindowTitle(QCoreApplication.translate("ProductionWidget", u"Production", None))
        self.label.setText(QCoreApplication.translate("ProductionWidget", u"Filter by Status:", None))
        self.cmbFilterStatus.setItemText(0, QCoreApplication.translate("ProductionWidget", u"All Jobs", None))
        self.cmbFilterStatus.setItemText(1, QCoreApplication.translate("ProductionWidget", u"Queued", None))
        self.cmbFilterStatus.setItemText(2, QCoreApplication.translate("ProductionWidget", u"In Progress", None))
        self.cmbFilterStatus.setItemText(3, QCoreApplication.translate("ProductionWidget", u"Completed", None))
        self.cmbFilterStatus.setItemText(4, QCoreApplication.translate("ProductionWidget", u"Failed", None))

        self.btnRefresh.setText(QCoreApplication.translate("ProductionWidget", u" Refresh", None))
        self.btnNewJob.setText(QCoreApplication.translate("ProductionWidget", u" New Job Card", None))
        self.btnEditJob.setText(QCoreApplication.translate("ProductionWidget", u" Edit Job", None))
        self.btnDeleteJob.setText(QCoreApplication.translate("ProductionWidget", u" Delete", None))
        self.lblTotalJobs.setText(QCoreApplication.translate("ProductionWidget", u"Total: 0 jobs", None))
        ___qtablewidgetitem = self.tableJobs.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ProductionWidget", u"Job ID", None));
        ___qtablewidgetitem1 = self.tableJobs.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ProductionWidget", u"Order ID", None));
        ___qtablewidgetitem2 = self.tableJobs.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ProductionWidget", u"Product", None));
        ___qtablewidgetitem3 = self.tableJobs.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ProductionWidget", u"Machine", None));
        ___qtablewidgetitem4 = self.tableJobs.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ProductionWidget", u"Operator", None));
        ___qtablewidgetitem5 = self.tableJobs.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ProductionWidget", u"Start Time", None));
        ___qtablewidgetitem6 = self.tableJobs.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ProductionWidget", u"End Time", None));
        ___qtablewidgetitem7 = self.tableJobs.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ProductionWidget", u"Status", None));
    # retranslateUi

