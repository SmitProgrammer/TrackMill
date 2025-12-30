# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_dialog.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_StockDialog(object):
    def setupUi(self, StockDialog):
        if not StockDialog.objectName():
            StockDialog.setObjectName(u"StockDialog")
        StockDialog.resize(450, 350)
        StockDialog.setMinimumSize(QSize(450, 350))
        StockDialog.setMaximumSize(QSize(450, 350))
        StockDialog.setStyleSheet(u"QDialog {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 13px;\n"
"    color: #333;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit, QComboBox, QDoubleSpinBox {\n"
"    padding: 8px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QComboBox:focus, QDoubleSpinBox:focus {\n"
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
"    font-weight: bold;\n"
"}"
                        "\n"
"\n"
"QPushButton#btnCancel:hover {\n"
"    background-color: #da190b;\n"
"}")
        self.verticalLayout = QVBoxLayout(StockDialog)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.lblMaterialName = QLabel(StockDialog)
        self.lblMaterialName.setObjectName(u"lblMaterialName")
        self.lblMaterialName.setStyleSheet(u"font-size: 16px; color: #2196F3;")

        self.verticalLayout.addWidget(self.lblMaterialName)

        self.lblCurrentStock = QLabel(StockDialog)
        self.lblCurrentStock.setObjectName(u"lblCurrentStock")
        self.lblCurrentStock.setStyleSheet(u"font-size: 14px; color: #666;")

        self.verticalLayout.addWidget(self.lblCurrentStock)

        self.label = QLabel(StockDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.cmbOperation = QComboBox(StockDialog)
        self.cmbOperation.addItem("")
        self.cmbOperation.addItem("")
        self.cmbOperation.setObjectName(u"cmbOperation")

        self.verticalLayout.addWidget(self.cmbOperation)

        self.label_2 = QLabel(StockDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.spinQuantity = QDoubleSpinBox(StockDialog)
        self.spinQuantity.setObjectName(u"spinQuantity")
        self.spinQuantity.setMaximum(999999.000000000000000)

        self.verticalLayout.addWidget(self.spinQuantity)

        self.label_3 = QLabel(StockDialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.txtRemarks = QTextEdit(StockDialog)
        self.txtRemarks.setObjectName(u"txtRemarks")
        self.txtRemarks.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout.addWidget(self.txtRemarks)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(StockDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)

        self.btnCancel = QPushButton(StockDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(StockDialog)

        QMetaObject.connectSlotsByName(StockDialog)
    # setupUi

    def retranslateUi(self, StockDialog):
        StockDialog.setWindowTitle(QCoreApplication.translate("StockDialog", u"Update Stock", None))
        self.lblMaterialName.setText(QCoreApplication.translate("StockDialog", u"Material Name", None))
        self.lblCurrentStock.setText(QCoreApplication.translate("StockDialog", u"Current Stock: 0", None))
        self.label.setText(QCoreApplication.translate("StockDialog", u"Operation:", None))
        self.cmbOperation.setItemText(0, QCoreApplication.translate("StockDialog", u"Add", None))
        self.cmbOperation.setItemText(1, QCoreApplication.translate("StockDialog", u"Remove", None))

        self.label_2.setText(QCoreApplication.translate("StockDialog", u"Quantity:", None))
        self.label_3.setText(QCoreApplication.translate("StockDialog", u"Remarks:", None))
        self.txtRemarks.setPlaceholderText(QCoreApplication.translate("StockDialog", u"Enter remarks (optional)", None))
        self.btnSave.setText(QCoreApplication.translate("StockDialog", u"Save", None))
        self.btnCancel.setText(QCoreApplication.translate("StockDialog", u"Cancel", None))
    # retranslateUi

