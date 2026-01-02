# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventory_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_InventoryDialog(object):
    def setupUi(self, InventoryDialog):
        if not InventoryDialog.objectName():
            InventoryDialog.setObjectName(u"InventoryDialog")
        InventoryDialog.resize(500, 500)
        InventoryDialog.setMinimumSize(QSize(500, 500))
        InventoryDialog.setMaximumSize(QSize(500, 500))
        InventoryDialog.setStyleSheet(u"QDialog {\n"
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
        self.verticalLayout = QVBoxLayout(InventoryDialog)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(InventoryDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.txtMaterialName = QLineEdit(InventoryDialog)
        self.txtMaterialName.setObjectName(u"txtMaterialName")

        self.verticalLayout.addWidget(self.txtMaterialName)

        self.label_2 = QLabel(InventoryDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.txtMaterialType = QLineEdit(InventoryDialog)
        self.txtMaterialType.setObjectName(u"txtMaterialType")

        self.verticalLayout.addWidget(self.txtMaterialType)

        self.label_3 = QLabel(InventoryDialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.spinCurrentStock = QDoubleSpinBox(InventoryDialog)
        self.spinCurrentStock.setObjectName(u"spinCurrentStock")
        self.spinCurrentStock.setMaximum(999999.000000000000000)

        self.verticalLayout.addWidget(self.spinCurrentStock)

        self.label_4 = QLabel(InventoryDialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.txtUnit = QLineEdit(InventoryDialog)
        self.txtUnit.setObjectName(u"txtUnit")

        self.verticalLayout.addWidget(self.txtUnit)

        self.label_5 = QLabel(InventoryDialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.spinMinStock = QDoubleSpinBox(InventoryDialog)
        self.spinMinStock.setObjectName(u"spinMinStock")
        self.spinMinStock.setMaximum(999999.000000000000000)

        self.verticalLayout.addWidget(self.spinMinStock)

        self.label_6 = QLabel(InventoryDialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.txtSupplier = QLineEdit(InventoryDialog)
        self.txtSupplier.setObjectName(u"txtSupplier")

        self.verticalLayout.addWidget(self.txtSupplier)

        self.label_7 = QLabel(InventoryDialog)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.cmbStatus = QComboBox(InventoryDialog)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.verticalLayout.addWidget(self.cmbStatus)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(InventoryDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)

        self.btnCancel = QPushButton(InventoryDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(InventoryDialog)

        QMetaObject.connectSlotsByName(InventoryDialog)
    # setupUi

    def retranslateUi(self, InventoryDialog):
        InventoryDialog.setWindowTitle(QCoreApplication.translate("InventoryDialog", u"Material Details", None))
        self.label.setText(QCoreApplication.translate("InventoryDialog", u"Material Name:", None))
        self.txtMaterialName.setPlaceholderText(QCoreApplication.translate("InventoryDialog", u"Enter material name", None))
        self.label_2.setText(QCoreApplication.translate("InventoryDialog", u"Material Type:", None))
        self.txtMaterialType.setPlaceholderText(QCoreApplication.translate("InventoryDialog", u"Enter material type", None))
        self.label_3.setText(QCoreApplication.translate("InventoryDialog", u"Current Stock:", None))
        self.label_4.setText(QCoreApplication.translate("InventoryDialog", u"Unit:", None))
        self.txtUnit.setPlaceholderText(QCoreApplication.translate("InventoryDialog", u"kg, meters, pieces, etc.", None))
        self.label_5.setText(QCoreApplication.translate("InventoryDialog", u"Minimum Stock:", None))
        self.label_6.setText(QCoreApplication.translate("InventoryDialog", u"Supplier:", None))
        self.txtSupplier.setPlaceholderText(QCoreApplication.translate("InventoryDialog", u"Enter supplier name", None))
        self.label_7.setText(QCoreApplication.translate("InventoryDialog", u"Status:", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("InventoryDialog", u"Available", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("InventoryDialog", u"Low Stock", None))
        self.cmbStatus.setItemText(2, QCoreApplication.translate("InventoryDialog", u"Out of Stock", None))

        self.btnSave.setText(QCoreApplication.translate("InventoryDialog", u"Save", None))
        self.btnCancel.setText(QCoreApplication.translate("InventoryDialog", u"Cancel", None))
    # retranslateUi

