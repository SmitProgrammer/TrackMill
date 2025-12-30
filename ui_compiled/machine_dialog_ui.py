# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'machine_dialog.ui'
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
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MachineDialog(object):
    def setupUi(self, MachineDialog):
        if not MachineDialog.objectName():
            MachineDialog.setObjectName(u"MachineDialog")
        MachineDialog.resize(500, 550)
        MachineDialog.setMinimumSize(QSize(500, 550))
        MachineDialog.setMaximumSize(QSize(500, 550))
        MachineDialog.setStyleSheet(u"QDialog {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 13px;\n"
"    color: #333;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit, QComboBox, QDateEdit {\n"
"    padding: 8px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QComboBox:focus, QDateEdit:focus {\n"
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
"}\n"
"\n"
""
                        "QPushButton#btnCancel:hover {\n"
"    background-color: #da190b;\n"
"}")
        self.verticalLayout = QVBoxLayout(MachineDialog)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(MachineDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.txtMachineName = QLineEdit(MachineDialog)
        self.txtMachineName.setObjectName(u"txtMachineName")

        self.verticalLayout.addWidget(self.txtMachineName)

        self.label_2 = QLabel(MachineDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.txtMachineType = QLineEdit(MachineDialog)
        self.txtMachineType.setObjectName(u"txtMachineType")

        self.verticalLayout.addWidget(self.txtMachineType)

        self.label_3 = QLabel(MachineDialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.txtModel = QLineEdit(MachineDialog)
        self.txtModel.setObjectName(u"txtModel")

        self.verticalLayout.addWidget(self.txtModel)

        self.label_4 = QLabel(MachineDialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.cmbStatus = QComboBox(MachineDialog)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.verticalLayout.addWidget(self.cmbStatus)

        self.label_5 = QLabel(MachineDialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.dateLastMaintenance = QDateEdit(MachineDialog)
        self.dateLastMaintenance.setObjectName(u"dateLastMaintenance")
        self.dateLastMaintenance.setCalendarPopup(True)
        self.dateLastMaintenance.setDate(QDate(2025, 1, 1))

        self.verticalLayout.addWidget(self.dateLastMaintenance)

        self.label_6 = QLabel(MachineDialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.dateNextMaintenance = QDateEdit(MachineDialog)
        self.dateNextMaintenance.setObjectName(u"dateNextMaintenance")
        self.dateNextMaintenance.setCalendarPopup(True)
        self.dateNextMaintenance.setDate(QDate(2025, 1, 1))

        self.verticalLayout.addWidget(self.dateNextMaintenance)

        self.label_7 = QLabel(MachineDialog)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.txtSpecifications = QTextEdit(MachineDialog)
        self.txtSpecifications.setObjectName(u"txtSpecifications")
        self.txtSpecifications.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.txtSpecifications)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(MachineDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)

        self.btnCancel = QPushButton(MachineDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(MachineDialog)

        QMetaObject.connectSlotsByName(MachineDialog)
    # setupUi

    def retranslateUi(self, MachineDialog):
        MachineDialog.setWindowTitle(QCoreApplication.translate("MachineDialog", u"Machine Details", None))
        self.label.setText(QCoreApplication.translate("MachineDialog", u"Machine Name:", None))
        self.txtMachineName.setPlaceholderText(QCoreApplication.translate("MachineDialog", u"Enter machine name", None))
        self.label_2.setText(QCoreApplication.translate("MachineDialog", u"Machine Type:", None))
        self.txtMachineType.setPlaceholderText(QCoreApplication.translate("MachineDialog", u"Enter machine type", None))
        self.label_3.setText(QCoreApplication.translate("MachineDialog", u"Model:", None))
        self.txtModel.setPlaceholderText(QCoreApplication.translate("MachineDialog", u"Enter model number", None))
        self.label_4.setText(QCoreApplication.translate("MachineDialog", u"Status:", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("MachineDialog", u"Available", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("MachineDialog", u"In Use", None))
        self.cmbStatus.setItemText(2, QCoreApplication.translate("MachineDialog", u"Maintenance", None))
        self.cmbStatus.setItemText(3, QCoreApplication.translate("MachineDialog", u"Out of Service", None))

        self.label_5.setText(QCoreApplication.translate("MachineDialog", u"Last Maintenance Date:", None))
        self.label_6.setText(QCoreApplication.translate("MachineDialog", u"Next Maintenance Date:", None))
        self.label_7.setText(QCoreApplication.translate("MachineDialog", u"Specifications:", None))
        self.txtSpecifications.setPlaceholderText(QCoreApplication.translate("MachineDialog", u"Enter machine specifications", None))
        self.btnSave.setText(QCoreApplication.translate("MachineDialog", u"Save", None))
        self.btnCancel.setText(QCoreApplication.translate("MachineDialog", u"Cancel", None))
    # retranslateUi

