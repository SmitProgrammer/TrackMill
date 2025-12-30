from datetime import datetime, timedelta
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

from ui_compiled.reports_ui import Ui_ReportsWidget
from database import sqlite_db


class ReportsWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ReportsWidget()
        self.ui.setupUi(self)

        self.setup_connections()

    def setup_connections(self):
        if hasattr(self.ui, 'btnGenerateReport'):
            self.ui.btnGenerateReport.clicked.connect(self.generate_report)

    def generate_report(self):
        print("Generate report clicked")


