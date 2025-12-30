# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'machines.ui'
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

class Ui_MachinesWidget(object):
    def setupUi(self, MachinesWidget):
        if not MachinesWidget.objectName():
            MachinesWidget.setObjectName(u"MachinesWidget")
        MachinesWidget.resize(900, 600)
        MachinesWidget.setStyleSheet(u"QWidget#MachinesWidget {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QPushButton#btnAddMachine, QPushButton#btnEditMachine, QPushButton#btnDeleteMachine, QPushButton#btnMaintenance, QPushButton#btnRefresh {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnAddMachine {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnEditMachine {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnDeleteMachine {\n"
"    background-color: #f44336;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnMaintenance {\n"
"    background-color: #FF9800;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnRefresh {\n"
"    background-color: #607D8B;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit#txtSearch {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
""
                        "    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QComboBox#cmbFilterStatus {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 5px;\n"
"    gridline-color: #e0e0e0;\n"
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
"}")
        self.verticalLayout = QVBoxLayout(MachinesWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txtSearch = QLineEdit(MachinesWidget)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)

        self.cmbFilterStatus = QComboBox(MachinesWidget)
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.setObjectName(u"cmbFilterStatus")
        self.cmbFilterStatus.setMinimumSize(QSize(150, 40))

        self.horizontalLayout.addWidget(self.cmbFilterStatus)

        self.btnRefresh = QPushButton(MachinesWidget)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(100, 40))
        self.btnRefresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnRefresh)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAddMachine = QPushButton(MachinesWidget)
        self.btnAddMachine.setObjectName(u"btnAddMachine")
        self.btnAddMachine.setMinimumSize(QSize(140, 40))
        self.btnAddMachine.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnAddMachine)

        self.btnEditMachine = QPushButton(MachinesWidget)
        self.btnEditMachine.setObjectName(u"btnEditMachine")
        self.btnEditMachine.setEnabled(False)
        self.btnEditMachine.setMinimumSize(QSize(140, 40))
        self.btnEditMachine.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnEditMachine)

        self.btnMaintenance = QPushButton(MachinesWidget)
        self.btnMaintenance.setObjectName(u"btnMaintenance")
        self.btnMaintenance.setEnabled(False)
        self.btnMaintenance.setMinimumSize(QSize(140, 40))
        self.btnMaintenance.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnMaintenance)

        self.btnDeleteMachine = QPushButton(MachinesWidget)
        self.btnDeleteMachine.setObjectName(u"btnDeleteMachine")
        self.btnDeleteMachine.setEnabled(False)
        self.btnDeleteMachine.setMinimumSize(QSize(140, 40))
        self.btnDeleteMachine.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnDeleteMachine)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lblTotalMachines = QLabel(MachinesWidget)
        self.lblTotalMachines.setObjectName(u"lblTotalMachines")
        self.lblTotalMachines.setStyleSheet(u"font-size: 13px; color: #666; padding: 10px;")

        self.horizontalLayout_2.addWidget(self.lblTotalMachines)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableMachines = QTableWidget(MachinesWidget)
        if (self.tableMachines.columnCount() < 7):
            self.tableMachines.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableMachines.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableMachines.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableMachines.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableMachines.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableMachines.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableMachines.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableMachines.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableMachines.setObjectName(u"tableMachines")
        self.tableMachines.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableMachines.setAlternatingRowColors(True)
        self.tableMachines.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableMachines.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableMachines.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableMachines)


        self.retranslateUi(MachinesWidget)

        QMetaObject.connectSlotsByName(MachinesWidget)
    # setupUi

    def retranslateUi(self, MachinesWidget):
        MachinesWidget.setWindowTitle(QCoreApplication.translate("MachinesWidget", u"Machines", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("MachinesWidget", u" Search machines by name or type...", None))
        self.cmbFilterStatus.setItemText(0, QCoreApplication.translate("MachinesWidget", u"All Status", None))
        self.cmbFilterStatus.setItemText(1, QCoreApplication.translate("MachinesWidget", u"Available", None))
        self.cmbFilterStatus.setItemText(2, QCoreApplication.translate("MachinesWidget", u"Running", None))
        self.cmbFilterStatus.setItemText(3, QCoreApplication.translate("MachinesWidget", u"Under Maintenance", None))
        self.cmbFilterStatus.setItemText(4, QCoreApplication.translate("MachinesWidget", u"Breakdown", None))

        self.btnRefresh.setText(QCoreApplication.translate("MachinesWidget", u" Refresh", None))
        self.btnAddMachine.setText(QCoreApplication.translate("MachinesWidget", u" Add Machine", None))
        self.btnEditMachine.setText(QCoreApplication.translate("MachinesWidget", u" Edit Machine", None))
        self.btnMaintenance.setText(QCoreApplication.translate("MachinesWidget", u" Maintenance", None))
        self.btnDeleteMachine.setText(QCoreApplication.translate("MachinesWidget", u" Delete", None))
        self.lblTotalMachines.setText(QCoreApplication.translate("MachinesWidget", u"Total: 0 machines", None))
        ___qtablewidgetitem = self.tableMachines.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MachinesWidget", u"Machine ID", None));
        ___qtablewidgetitem1 = self.tableMachines.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MachinesWidget", u"Machine Name", None));
        ___qtablewidgetitem2 = self.tableMachines.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MachinesWidget", u"Type", None));
        ___qtablewidgetitem3 = self.tableMachines.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MachinesWidget", u"Model", None));
        ___qtablewidgetitem4 = self.tableMachines.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MachinesWidget", u"Status", None));
        ___qtablewidgetitem5 = self.tableMachines.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MachinesWidget", u"Last Maintenance", None));
        ___qtablewidgetitem6 = self.tableMachines.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MachinesWidget", u"Next Maintenance", None));
    # retranslateUi

