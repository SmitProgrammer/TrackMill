from datetime import datetime
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt

from ui_compiled.settings_ui import Ui_SettingsWidget
from database import sqlite_db
from utils import show_error, show_success, show_warning, session
from config.settings import DEFAULT_ADMIN_USERNAME


class SettingsWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)

        self.setup_connections()
        self.load_settings()

    def setup_connections(self):
        self.ui.btnSaveSettings.clicked.connect(self.save_settings)
        self.ui.btnClearLogs.clicked.connect(self.clear_activity_logs)

    def load_settings(self):
        user_email = session.get_user_email()
        self.ui.lblCurrentUser.setText(f"Logged in as: {user_email}")

        self.ui.txtAdminEmail.setText(user_email)

        total_customers = sqlite_db.count('customers')
        total_orders = sqlite_db.count('orders')
        total_inventory = sqlite_db.count('inventory')
        total_machines = sqlite_db.count('machines')
        total_employees = sqlite_db.count('employees')
        total_jobs = sqlite_db.count('jobs')

        self.ui.lblCustomersCount.setText(str(total_customers))
        self.ui.lblOrdersCount.setText(str(total_orders))
        self.ui.lblInventoryCount.setText(str(total_inventory))
        self.ui.lblMachinesCount.setText(str(total_machines))
        self.ui.lblEmployeesCount.setText(str(total_employees))
        self.ui.lblJobsCount.setText(str(total_jobs))

        log_count = sqlite_db.count('activity_logs')
        self.ui.lblLogsCount.setText(f"{log_count} activity logs")

    def save_settings(self):
        show_success(self, "Success", "Settings saved successfully")

        user_email = session.get_user_email()
        sqlite_db.log_activity(user_email, "Update Settings", "Settings", "Updated application settings")

    def clear_activity_logs(self):
        reply = QMessageBox.question(
            self, "Confirm Clear Logs",
            "Are you sure you want to clear all activity logs? This action cannot be undone.",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            try:
                sqlite_db.cursor.execute("DELETE FROM activity_logs")
                sqlite_db.conn.commit()

                show_success(self, "Success", "Activity logs cleared successfully")

                user_email = session.get_user_email()
                sqlite_db.log_activity(user_email, "Clear Logs", "Settings", "Cleared all activity logs")

                self.load_settings()
            except Exception as e:
                show_error(self, "Error", f"Failed to clear logs: {str(e)}")

