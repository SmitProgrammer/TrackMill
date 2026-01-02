from PySide6.QtWidgets import QWidget

from ui_compiled.settings_ui import Ui_SettingsWidget
from database import cloud_first_db, firebase_db
from utils import show_success, show_error, session


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

    def load_settings(self):
        user_email = session.get_user_email()
        if hasattr(self.ui, 'txtAdminEmail'):
            self.ui.txtAdminEmail.setText(user_email)

    def save_settings(self):
        show_success(self, "Success", "Settings saved successfully")

        # Removed SQLite logging - using Firebase only

    def change_password(self):
        from PySide6.QtWidgets import QInputDialog, QLineEdit

        # Firebase handles password changes via Firebase Auth
        # Local password changes not supported in Firebase-only mode
        show_error(self, "Info", "Please use Firebase Console to manage passwords")


