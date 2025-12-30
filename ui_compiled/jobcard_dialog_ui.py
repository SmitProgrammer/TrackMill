# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jobcard_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_JobCardDialog(object):
    def setupUi(self, JobCardDialog):
        if not JobCardDialog.objectName():
            JobCardDialog.setObjectName(u"JobCardDialog")
        JobCardDialog.resize(550, 600)
        JobCardDialog.setMinimumSize(QSize(550, 600))
        JobCardDialog.setMaximumSize(QSize(550, 600))
        JobCardDialog.setStyleSheet(u"QDialog {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 13px;\n"
"    color: #333;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit, QComboBox, QDateTimeEdit {\n"
"    padding: 8px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    background-color: white;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QComboBox:focus, QDateTimeEdit:focus {\n"
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
""
                        "\n"
"QPushButton#btnCancel:hover {\n"
"    background-color: #da190b;\n"
"}")
        self.verticalLayout = QVBoxLayout(JobCardDialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(JobCardDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.cmbOrder = QComboBox(JobCardDialog)
        self.cmbOrder.setObjectName(u"cmbOrder")

        self.verticalLayout.addWidget(self.cmbOrder)

        self.label_2 = QLabel(JobCardDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.txtProductName = QLineEdit(JobCardDialog)
        self.txtProductName.setObjectName(u"txtProductName")

        self.verticalLayout.addWidget(self.txtProductName)

        self.label_3 = QLabel(JobCardDialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.cmbMachine = QComboBox(JobCardDialog)
        self.cmbMachine.setObjectName(u"cmbMachine")

        self.verticalLayout.addWidget(self.cmbMachine)

        self.label_4 = QLabel(JobCardDialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.cmbOperator = QComboBox(JobCardDialog)
        self.cmbOperator.setObjectName(u"cmbOperator")

        self.verticalLayout.addWidget(self.cmbOperator)

        self.label_5 = QLabel(JobCardDialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.dateTimeStart = QDateTimeEdit(JobCardDialog)
        self.dateTimeStart.setObjectName(u"dateTimeStart")
        self.dateTimeStart.setCalendarPopup(True)
        self.dateTimeStart.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))

        self.verticalLayout.addWidget(self.dateTimeStart)

        self.label_6 = QLabel(JobCardDialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.dateTimeEnd = QDateTimeEdit(JobCardDialog)
        self.dateTimeEnd.setObjectName(u"dateTimeEnd")
        self.dateTimeEnd.setCalendarPopup(True)
        self.dateTimeEnd.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))

        self.verticalLayout.addWidget(self.dateTimeEnd)

        self.label_7 = QLabel(JobCardDialog)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.cmbStatus = QComboBox(JobCardDialog)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.verticalLayout.addWidget(self.cmbStatus)

        self.label_8 = QLabel(JobCardDialog)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.txtMaterialUsed = QTextEdit(JobCardDialog)
        self.txtMaterialUsed.setObjectName(u"txtMaterialUsed")
        self.txtMaterialUsed.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.txtMaterialUsed)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(JobCardDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)

        self.btnCancel = QPushButton(JobCardDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(JobCardDialog)

        QMetaObject.connectSlotsByName(JobCardDialog)
    # setupUi

    def retranslateUi(self, JobCardDialog):
        JobCardDialog.setWindowTitle(QCoreApplication.translate("JobCardDialog", u"Job Card Details", None))
        self.label.setText(QCoreApplication.translate("JobCardDialog", u"Order:", None))
        self.label_2.setText(QCoreApplication.translate("JobCardDialog", u"Product Name:", None))
        self.txtProductName.setPlaceholderText(QCoreApplication.translate("JobCardDialog", u"Enter product name", None))
        self.label_3.setText(QCoreApplication.translate("JobCardDialog", u"Machine:", None))
        self.label_4.setText(QCoreApplication.translate("JobCardDialog", u"Operator:", None))
        self.label_5.setText(QCoreApplication.translate("JobCardDialog", u"Start Time:", None))
        self.label_6.setText(QCoreApplication.translate("JobCardDialog", u"End Time:", None))
        self.label_7.setText(QCoreApplication.translate("JobCardDialog", u"Status:", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("JobCardDialog", u"Pending", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("JobCardDialog", u"In Progress", None))
        self.cmbStatus.setItemText(2, QCoreApplication.translate("JobCardDialog", u"Completed", None))

        self.label_8.setText(QCoreApplication.translate("JobCardDialog", u"Material Used:", None))
        self.txtMaterialUsed.setPlaceholderText(QCoreApplication.translate("JobCardDialog", u"Enter materials used", None))
        self.btnSave.setText(QCoreApplication.translate("JobCardDialog", u"Save", None))
        self.btnCancel.setText(QCoreApplication.translate("JobCardDialog", u"Cancel", None))
    # retranslateUi

