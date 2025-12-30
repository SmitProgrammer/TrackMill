from PySide6.QtWidgets import QWidget, QMessageBox

from ui_compiled.settings_ui import Ui_SettingsWidget
from database import sqlite_db
from utils import show_success, session


class SettingsWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)

        self.setup_connections()
        self.load_settings()

    def setup_connections(self):
        if hasattr(self.ui, 'btnSaveSettings'):
            self.ui.btnSaveSettings.clicked.connect(self.save_settings)
        if hasattr(self.ui, 'btnChangePassword'):
            self.ui.btnChangePassword.clicked.connect(self.change_password)
        if hasattr(self.ui, 'btnBackupData'):
            self.ui.btnBackupData.clicked.connect(self.backup_data)
        if hasattr(self.ui, 'btnRestoreData'):
            self.ui.btnRestoreData.clicked.connect(self.restore_data)

    def load_settings(self):
        user_email = session.get_user_email()
        if hasattr(self.ui, 'txtAdminEmail'):
            self.ui.txtAdminEmail.setText(user_email)

    def save_settings(self):
        show_success(self, "Success", "Settings saved successfully")

        user_email = session.get_user_email()
        sqlite_db.log_activity(user_email, "Update Settings", "Settings", "Updated application settings")

    def change_password(self):
        print("Change password clicked")

    def backup_data(self):
        print("Backup data clicked")

    def restore_data(self):
        print("Restore data clicked")


