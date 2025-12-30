# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employees.ui'
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

class Ui_EmployeesWidget(object):
    def setupUi(self, EmployeesWidget):
        if not EmployeesWidget.objectName():
            EmployeesWidget.setObjectName(u"EmployeesWidget")
        EmployeesWidget.resize(900, 600)
        EmployeesWidget.setStyleSheet(u"QWidget#EmployeesWidget {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QPushButton#btnAddEmployee, QPushButton#btnEditEmployee, QPushButton#btnDeleteEmployee, QPushButton#btnBlockUnblock, QPushButton#btnCreateAccount, QPushButton#btnRefresh {\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnAddEmployee {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnEditEmployee {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnDeleteEmployee {\n"
"    background-color: #f44336;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnBlockUnblock {\n"
"    background-color: #FF9800;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnCreateAccount {\n"
"    background-color: #9C27B0;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btnRefresh {\n"
"   "
                        " background-color: #607D8B;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit#txtSearch {\n"
"    padding: 10px;\n"
"    border: 2px solid #ddd;\n"
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
        self.verticalLayout = QVBoxLayout(EmployeesWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txtSearch = QLineEdit(EmployeesWidget)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)

        self.cmbFilterStatus = QComboBox(EmployeesWidget)
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.addItem("")
        self.cmbFilterStatus.setObjectName(u"cmbFilterStatus")
        self.cmbFilterStatus.setMinimumSize(QSize(150, 40))

        self.horizontalLayout.addWidget(self.cmbFilterStatus)

        self.btnRefresh = QPushButton(EmployeesWidget)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(100, 40))
        self.btnRefresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnRefresh)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAddEmployee = QPushButton(EmployeesWidget)
        self.btnAddEmployee.setObjectName(u"btnAddEmployee")
        self.btnAddEmployee.setMinimumSize(QSize(130, 40))
        self.btnAddEmployee.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnAddEmployee)

        self.btnCreateAccount = QPushButton(EmployeesWidget)
        self.btnCreateAccount.setObjectName(u"btnCreateAccount")
        self.btnCreateAccount.setEnabled(False)
        self.btnCreateAccount.setMinimumSize(QSize(150, 40))
        self.btnCreateAccount.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnCreateAccount)

        self.btnBlockUnblock = QPushButton(EmployeesWidget)
        self.btnBlockUnblock.setObjectName(u"btnBlockUnblock")
        self.btnBlockUnblock.setEnabled(False)
        self.btnBlockUnblock.setMinimumSize(QSize(130, 40))
        self.btnBlockUnblock.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnBlockUnblock)

        self.btnEditEmployee = QPushButton(EmployeesWidget)
        self.btnEditEmployee.setObjectName(u"btnEditEmployee")
        self.btnEditEmployee.setEnabled(False)
        self.btnEditEmployee.setMinimumSize(QSize(130, 40))
        self.btnEditEmployee.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnEditEmployee)

        self.btnDeleteEmployee = QPushButton(EmployeesWidget)
        self.btnDeleteEmployee.setObjectName(u"btnDeleteEmployee")
        self.btnDeleteEmployee.setEnabled(False)
        self.btnDeleteEmployee.setMinimumSize(QSize(130, 40))
        self.btnDeleteEmployee.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnDeleteEmployee)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lblTotalEmployees = QLabel(EmployeesWidget)
        self.lblTotalEmployees.setObjectName(u"lblTotalEmployees")
        self.lblTotalEmployees.setStyleSheet(u"font-size: 13px; color: #666; padding: 10px;")

        self.horizontalLayout_2.addWidget(self.lblTotalEmployees)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableEmployees = QTableWidget(EmployeesWidget)
        if (self.tableEmployees.columnCount() < 7):
            self.tableEmployees.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableEmployees.setObjectName(u"tableEmployees")
        self.tableEmployees.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableEmployees.setAlternatingRowColors(True)
        self.tableEmployees.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableEmployees.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableEmployees.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableEmployees)


        self.retranslateUi(EmployeesWidget)

        QMetaObject.connectSlotsByName(EmployeesWidget)
    # setupUi

    def retranslateUi(self, EmployeesWidget):
        EmployeesWidget.setWindowTitle(QCoreApplication.translate("EmployeesWidget", u"Employees", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("EmployeesWidget", u" Search employees by name, role, or contact...", None))
        self.cmbFilterStatus.setItemText(0, QCoreApplication.translate("EmployeesWidget", u"All Employees", None))
        self.cmbFilterStatus.setItemText(1, QCoreApplication.translate("EmployeesWidget", u"Active", None))
        self.cmbFilterStatus.setItemText(2, QCoreApplication.translate("EmployeesWidget", u"Blocked", None))

        self.btnRefresh.setText(QCoreApplication.translate("EmployeesWidget", u" Refresh", None))
        self.btnAddEmployee.setText(QCoreApplication.translate("EmployeesWidget", u" Add Employee", None))
        self.btnCreateAccount.setText(QCoreApplication.translate("EmployeesWidget", u" Create Login", None))
        self.btnBlockUnblock.setText(QCoreApplication.translate("EmployeesWidget", u" Block/Unblock", None))
        self.btnEditEmployee.setText(QCoreApplication.translate("EmployeesWidget", u" Edit", None))
        self.btnDeleteEmployee.setText(QCoreApplication.translate("EmployeesWidget", u" Delete", None))
        self.lblTotalEmployees.setText(QCoreApplication.translate("EmployeesWidget", u"Total: 0 employees", None))
        ___qtablewidgetitem = self.tableEmployees.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EmployeesWidget", u"Employee ID", None));
        ___qtablewidgetitem1 = self.tableEmployees.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EmployeesWidget", u"Name", None));
        ___qtablewidgetitem2 = self.tableEmployees.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EmployeesWidget", u"Role", None));
        ___qtablewidgetitem3 = self.tableEmployees.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EmployeesWidget", u"Contact", None));
        ___qtablewidgetitem4 = self.tableEmployees.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EmployeesWidget", u"Email", None));
        ___qtablewidgetitem5 = self.tableEmployees.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("EmployeesWidget", u"Has Login", None));
        ___qtablewidgetitem6 = self.tableEmployees.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("EmployeesWidget", u"Status", None));
    # retranslateUi

