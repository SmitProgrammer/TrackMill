# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_OrderDialog(object):
    def setupUi(self, OrderDialog):
        if not OrderDialog.objectName():
            OrderDialog.setObjectName(u"OrderDialog")
        OrderDialog.resize(550, 550)
        OrderDialog.setMinimumSize(QSize(550, 550))
        OrderDialog.setMaximumSize(QSize(550, 550))
        OrderDialog.setStyleSheet(u"QDialog {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 13px;\n"
"    color: #333;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit, QComboBox, QSpinBox, QDateEdit {\n"
"    padding: 8px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QComboBox:focus, QSpinBox:focus, QDateEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
"}\n"
"\n"
"QPushButton#btnSave {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    padding: 10px 25px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnSave:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#btnCancel {\n"
"    background-color: #f44336;\n"
"    color: white;\n"
"    padding: 10px 25px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    font-wei"
                        "ght: bold;\n"
"}\n"
"\n"
"QPushButton#btnCancel:hover {\n"
"    background-color: #da190b;\n"
"}")
        self.verticalLayout = QVBoxLayout(OrderDialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(OrderDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.cmbCustomer = QComboBox(OrderDialog)
        self.cmbCustomer.setObjectName(u"cmbCustomer")

        self.verticalLayout.addWidget(self.cmbCustomer)

        self.label_2 = QLabel(OrderDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.txtProductName = QLineEdit(OrderDialog)
        self.txtProductName.setObjectName(u"txtProductName")

        self.verticalLayout.addWidget(self.txtProductName)

        self.label_3 = QLabel(OrderDialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.spinQuantity = QSpinBox(OrderDialog)
        self.spinQuantity.setObjectName(u"spinQuantity")
        self.spinQuantity.setMinimum(1)
        self.spinQuantity.setMaximum(10000)

        self.verticalLayout.addWidget(self.spinQuantity)

        self.label_4 = QLabel(OrderDialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.txtSpecifications = QTextEdit(OrderDialog)
        self.txtSpecifications.setObjectName(u"txtSpecifications")
        self.txtSpecifications.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout.addWidget(self.txtSpecifications)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(OrderDialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.dateOrder = QDateEdit(OrderDialog)
        self.dateOrder.setObjectName(u"dateOrder")
        self.dateOrder.setCalendarPopup(True)
        self.dateOrder.setDate(QDate(2025, 1, 1))

        self.horizontalLayout.addWidget(self.dateOrder)

        self.label_6 = QLabel(OrderDialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.dateDelivery = QDateEdit(OrderDialog)
        self.dateDelivery.setObjectName(u"dateDelivery")
        self.dateDelivery.setCalendarPopup(True)
        self.dateDelivery.setDate(QDate(2025, 1, 1))

        self.horizontalLayout.addWidget(self.dateDelivery)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_7 = QLabel(OrderDialog)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.cmbPriority = QComboBox(OrderDialog)
        self.cmbPriority.addItem("")
        self.cmbPriority.addItem("")
        self.cmbPriority.addItem("")
        self.cmbPriority.addItem("")
        self.cmbPriority.setObjectName(u"cmbPriority")

        self.verticalLayout.addWidget(self.cmbPriority)

        self.label_8 = QLabel(OrderDialog)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.cmbStatus = QComboBox(OrderDialog)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.verticalLayout.addWidget(self.cmbStatus)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(OrderDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout_2.addWidget(self.btnSave)

        self.btnCancel = QPushButton(OrderDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout_2.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(OrderDialog)

        QMetaObject.connectSlotsByName(OrderDialog)
    # setupUi

    def retranslateUi(self, OrderDialog):
        OrderDialog.setWindowTitle(QCoreApplication.translate("OrderDialog", u"Order Details", None))
        self.label.setText(QCoreApplication.translate("OrderDialog", u"Customer:", None))
        self.label_2.setText(QCoreApplication.translate("OrderDialog", u"Product Name:", None))
        self.txtProductName.setPlaceholderText(QCoreApplication.translate("OrderDialog", u"Enter product name", None))
        self.label_3.setText(QCoreApplication.translate("OrderDialog", u"Quantity:", None))
        self.label_4.setText(QCoreApplication.translate("OrderDialog", u"Specifications:", None))
        self.txtSpecifications.setPlaceholderText(QCoreApplication.translate("OrderDialog", u"Enter product specifications", None))
        self.label_5.setText(QCoreApplication.translate("OrderDialog", u"Order Date:", None))
        self.label_6.setText(QCoreApplication.translate("OrderDialog", u"Delivery Date:", None))
        self.label_7.setText(QCoreApplication.translate("OrderDialog", u"Priority:", None))
        self.cmbPriority.setItemText(0, QCoreApplication.translate("OrderDialog", u"Low", None))
        self.cmbPriority.setItemText(1, QCoreApplication.translate("OrderDialog", u"Medium", None))
        self.cmbPriority.setItemText(2, QCoreApplication.translate("OrderDialog", u"High", None))
        self.cmbPriority.setItemText(3, QCoreApplication.translate("OrderDialog", u"Urgent", None))

        self.label_8.setText(QCoreApplication.translate("OrderDialog", u"Status:", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("OrderDialog", u"Pending", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("OrderDialog", u"In Progress", None))
        self.cmbStatus.setItemText(2, QCoreApplication.translate("OrderDialog", u"Completed", None))
        self.cmbStatus.setItemText(3, QCoreApplication.translate("OrderDialog", u"Cancelled", None))

        self.btnSave.setText(QCoreApplication.translate("OrderDialog", u"Save", None))
        self.btnCancel.setText(QCoreApplication.translate("OrderDialog", u"Cancel", None))
    # retranslateUi

