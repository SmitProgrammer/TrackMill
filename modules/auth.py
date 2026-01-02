"""
Login/Authentication module
"""

import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon

from ui_compiled.login_ui import Ui_LoginWindow
from database import firebase_db
from utils import show_error, show_info, validate_email, session
from config.settings import DEFAULT_ADMIN_USERNAME, DEFAULT_ADMIN_PASSWORD


class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        # Window settings
        self.setWindowTitle("CNC ERP - Admin Login")
        self.setFixedSize(450, 550)

        # Center window on screen
        self.center_window()

        # Connect signals
        self.setup_connections()

        # Clear error label
        self.ui.lblError.setText("")

        # Auto-fill for testing (remove in production)
        self.ui.txtEmail.setText(DEFAULT_ADMIN_USERNAME)
        self.ui.txtPassword.setText(DEFAULT_ADMIN_PASSWORD)

        # Focus on login button
        self.ui.btnLogin.setFocus()

    def center_window(self):
        """Center window on screen"""
        screen = QApplication.primaryScreen().geometry()
        window_geo = self.geometry()
        x = (screen.width() - window_geo.width()) // 2
        y = (screen.height() - window_geo.height()) // 2
        self.move(x, y)

    def setup_connections(self):
        """Connect UI signals to slots"""
        self.ui.btnLogin.clicked.connect(self.on_login_clicked)
        self.ui.txtPassword.returnPressed.connect(self.on_login_clicked)
        self.ui.txtEmail.returnPressed.connect(self.ui.txtPassword.setFocus)

    def on_login_clicked(self):
        """Handle login button click"""
        # Get input values
        email = self.ui.txtEmail.text().strip()
        password = self.ui.txtPassword.text().strip()

        # Clear previous error
        self.ui.lblError.setText("")

        # Validate inputs
        if not email:
            self.show_login_error("Please enter your email address")
            self.ui.txtEmail.setFocus()
            return

        if not validate_email(email):
            self.show_login_error("Please enter a valid email address")
            self.ui.txtEmail.setFocus()
            return

        if not password:
            self.show_login_error("Please enter your password")
            self.ui.txtPassword.setFocus()
            return

        if len(password) < 6:
            self.show_login_error("Password must be at least 6 characters")
            self.ui.txtPassword.setFocus()
            return

        # Disable login button during authentication
        self.ui.btnLogin.setEnabled(False)
        self.ui.btnLogin.setText("Logging in...")

        # Authenticate with Firebase
        QTimer.singleShot(100, lambda: self.authenticate(email, password))

    def authenticate(self, email, password):
        """Authenticate user with Firebase"""
        try:
            # Sign in with Firebase
            success, user_data, error = firebase_db.sign_in(email, password)

            if success:
                # Store session
                session.login(user_data)


                # Show success and open main window
                self.login_success(email)
            else:
                # Show error
                self.show_login_error(error or "Invalid credentials")
                self.ui.btnLogin.setEnabled(True)
                self.ui.btnLogin.setText("LOGIN")

        except Exception as e:
            self.show_login_error(f"Login failed: {str(e)}")
            self.ui.btnLogin.setEnabled(True)
            self.ui.btnLogin.setText("LOGIN")

    def login_success(self, email):
        """Handle successful login"""
        # Import here to avoid circular import
        from modules.main_app import MainWindow

        # Create and show main window
        self.main_window = MainWindow()
        self.main_window.show()

        # Close login window
        self.close()

    def show_login_error(self, message):
        """Show error message on login screen"""
        self.ui.lblError.setText(message)
        self.ui.lblError.setStyleSheet("color: #f44336; font-size: 12px;")

    def keyPressEvent(self, event):
        """Handle key press events"""
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if self.ui.btnLogin.isEnabled():
                self.on_login_clicked()

