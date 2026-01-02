# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_CustomerDialog(object):
    def setupUi(self, CustomerDialog):
        if not CustomerDialog.objectName():
            CustomerDialog.setObjectName(u"CustomerDialog")
        CustomerDialog.resize(500, 450)
        CustomerDialog.setMinimumSize(QSize(500, 450))
        CustomerDialog.setMaximumSize(QSize(500, 450))
        CustomerDialog.setStyleSheet(u"QDialog {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 13px;\n"
"    color: #333;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit, QSpinBox, QDoubleSpinBox {\n"
"    padding: 8px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus {\n"
"    border: 2px solid #2196F3;\n"
"}\n"
"\n"
"QComboBox {\n"
"    padding: 8px;\n"
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
"    margi"
                        "n-right: 10px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    selection-background-color: #2196F3;\n"
"    selection-color: white;\n"
"    border: 1px solid #ddd;\n"
"}\n"
"\n"
"QDateEdit, QDateTimeEdit {\n"
"    padding: 8px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QDateEdit:focus, QDateTimeEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
"}\n"
"\n"
"QDateEdit::drop-down, QDateTimeEdit::drop-down {\n"
"    border: none;\n"
"    width: 30px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow, QDateTimeEdit::down-arrow {\n"
"    image: none;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 5px solid #333;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView, QDateTimeEdit QAbstractItemView {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    selection-background-co"
                        "lor: #2196F3;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 13px;\n"
"    color: #333;\n"
"    spacing: 8px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 3px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #2196F3;\n"
"    border-color: #2196F3;\n"
"    image: none;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:after {\n"
"    content: \"\u2713\";\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
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
"    padding: 10px 25"
                        "px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnCancel:hover {\n"
"    background-color: #da190b;\n"
"}")
        self.verticalLayout = QVBoxLayout(CustomerDialog)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(CustomerDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.txtName = QLineEdit(CustomerDialog)
        self.txtName.setObjectName(u"txtName")

        self.verticalLayout.addWidget(self.txtName)

        self.label_2 = QLabel(CustomerDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.txtContact = QLineEdit(CustomerDialog)
        self.txtContact.setObjectName(u"txtContact")

        self.verticalLayout.addWidget(self.txtContact)

        self.label_3 = QLabel(CustomerDialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.txtEmail = QLineEdit(CustomerDialog)
        self.txtEmail.setObjectName(u"txtEmail")

        self.verticalLayout.addWidget(self.txtEmail)

        self.label_4 = QLabel(CustomerDialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.txtCompany = QLineEdit(CustomerDialog)
        self.txtCompany.setObjectName(u"txtCompany")

        self.verticalLayout.addWidget(self.txtCompany)

        self.label_5 = QLabel(CustomerDialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.txtAddress = QTextEdit(CustomerDialog)
        self.txtAddress.setObjectName(u"txtAddress")
        self.txtAddress.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout.addWidget(self.txtAddress)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(CustomerDialog)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 40))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnSave)

        self.btnCancel = QPushButton(CustomerDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 40))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CustomerDialog)

        QMetaObject.connectSlotsByName(CustomerDialog)
    # setupUi

    def retranslateUi(self, CustomerDialog):
        CustomerDialog.setWindowTitle(QCoreApplication.translate("CustomerDialog", u"Customer Details", None))
        self.label.setText(QCoreApplication.translate("CustomerDialog", u"Customer Name:", None))
        self.txtName.setPlaceholderText(QCoreApplication.translate("CustomerDialog", u"Enter customer name", None))
        self.label_2.setText(QCoreApplication.translate("CustomerDialog", u"Contact Number:", None))
        self.txtContact.setPlaceholderText(QCoreApplication.translate("CustomerDialog", u"Enter contact number", None))
        self.label_3.setText(QCoreApplication.translate("CustomerDialog", u"Email:", None))
        self.txtEmail.setPlaceholderText(QCoreApplication.translate("CustomerDialog", u"Enter email address", None))
        self.label_4.setText(QCoreApplication.translate("CustomerDialog", u"Company:", None))
        self.txtCompany.setPlaceholderText(QCoreApplication.translate("CustomerDialog", u"Enter company name", None))
        self.label_5.setText(QCoreApplication.translate("CustomerDialog", u"Address:", None))
        self.txtAddress.setPlaceholderText(QCoreApplication.translate("CustomerDialog", u"Enter address", None))
        self.btnSave.setText(QCoreApplication.translate("CustomerDialog", u"Save", None))
        self.btnCancel.setText(QCoreApplication.translate("CustomerDialog", u"Cancel", None))
    # retranslateUi

