"""
Main application window
"""

from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from ui_compiled.main_window_ui import Ui_MainWindow
from utils import show_info, confirm_dialog, session
from database import sqlite_db

from modules.dashboard import DashboardWidget
from modules.customers import CustomersWidget
from modules.orders import OrdersWidget
from modules.inventory import InventoryWidget
from modules.production import ProductionWidget
from modules.machines import MachinesWidget
from modules.employees import EmployeesWidget
from modules.reports import ReportsWidget
from modules.settings import SettingsWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Window settings
        self.setWindowTitle("CNC ERP System - Admin Panel")
        self.setMinimumSize(1200, 700)

        # Center window
        self.center_window()

        # Maximize window
        self.showMaximized()

        # Store module instances
        self.modules = {}

        # Setup navigation
        self.setup_connections()

        # Update user info
        self.update_user_info()

        # Load dashboard by default
        self.load_module('dashboard')

        # Log activity
        user_email = session.get_user_email()
        sqlite_db.log_activity(user_email, "Open Application", "Main Window", "User opened main window")

    def center_window(self):
        """Center window on screen"""
        screen = QApplication.primaryScreen().geometry()
        window_geo = self.frameGeometry()
        x = (screen.width() - window_geo.width()) // 2
        y = (screen.height() - window_geo.height()) // 2
        self.move(x, y)

    def setup_connections(self):
        """Connect navigation buttons to handlers"""
        # Create button group for exclusive selection
        self.nav_buttons = [
            self.ui.btnDashboard,
            self.ui.btnCustomers,
            self.ui.btnOrders,
            self.ui.btnInventory,
            self.ui.btnProduction,
            self.ui.btnMachines,
            self.ui.btnEmployees,
            self.ui.btnReports,
            self.ui.btnSettings
        ]

        # Connect each button
        self.ui.btnDashboard.clicked.connect(lambda: self.load_module('dashboard'))
        self.ui.btnCustomers.clicked.connect(lambda: self.load_module('customers'))
        self.ui.btnOrders.clicked.connect(lambda: self.load_module('orders'))
        self.ui.btnInventory.clicked.connect(lambda: self.load_module('inventory'))
        self.ui.btnProduction.clicked.connect(lambda: self.load_module('production'))
        self.ui.btnMachines.clicked.connect(lambda: self.load_module('machines'))
        self.ui.btnEmployees.clicked.connect(lambda: self.load_module('employees'))
        self.ui.btnReports.clicked.connect(lambda: self.load_module('reports'))
        self.ui.btnSettings.clicked.connect(lambda: self.load_module('settings'))

        # Logout button
        self.ui.btnLogout.clicked.connect(self.on_logout_clicked)

    def update_user_info(self):
        """Update user information in top bar"""
        user_email = session.get_user_email()
        if user_email:
            # Extract username from email
            username = user_email.split('@')[0].title()
            self.ui.lblUserInfo.setText(f"👤 {username}")

    def load_module(self, module_name):
        """Load and display a module"""
        # Update active button
        self.update_active_button(module_name)

        # Update page title
        titles = {
            'dashboard': 'Dashboard',
            'customers': 'Customer Management',
            'orders': 'Order Management',
            'inventory': 'Inventory Management',
            'production': 'Production & Job Cards',
            'machines': 'Machine Management',
            'employees': 'Employee Management',
            'reports': 'Reports & Analytics',
            'settings': 'System Settings'
        }
        self.ui.lblPageTitle.setText(titles.get(module_name, 'Dashboard'))

        # Load module widget
        try:
            # Get or create module widget
            if module_name not in self.modules:
                self.modules[module_name] = self.create_module_widget(module_name)

            widget = self.modules[module_name]

            # Clear stacked widget and add new widget
            while self.ui.stackedWidget.count() > 0:
                old_widget = self.ui.stackedWidget.widget(0)
                self.ui.stackedWidget.removeWidget(old_widget)

            self.ui.stackedWidget.addWidget(widget)
            self.ui.stackedWidget.setCurrentWidget(widget)

        except Exception as e:
            print(f"❌ Error loading module '{module_name}': {e}")
            show_info(self, "Module Loading", f"Module '{module_name}' is under development")

    def create_module_widget(self, module_name):
        if module_name == 'dashboard':
            return DashboardWidget()
        elif module_name == 'customers':
            return CustomersWidget()
        elif module_name == 'orders':
            return OrdersWidget()
        elif module_name == 'inventory':
            return InventoryWidget()
        elif module_name == 'production':
            return ProductionWidget()
        elif module_name == 'machines':
            return MachinesWidget()
        elif module_name == 'employees':
            return EmployeesWidget()
        elif module_name == 'reports':
            return ReportsWidget()
        elif module_name == 'settings':
            return SettingsWidget()
        else:
            placeholder = QWidget()
            placeholder.setStyleSheet("background-color: #f5f5f5;")
            return placeholder

    def update_active_button(self, module_name):
        """Update active navigation button"""
        # Uncheck all buttons
        for btn in self.nav_buttons:
            btn.setChecked(False)

        # Check the active button
        button_map = {
            'dashboard': self.ui.btnDashboard,
            'customers': self.ui.btnCustomers,
            'orders': self.ui.btnOrders,
            'inventory': self.ui.btnInventory,
            'production': self.ui.btnProduction,
            'machines': self.ui.btnMachines,
            'employees': self.ui.btnEmployees,
            'reports': self.ui.btnReports,
            'settings': self.ui.btnSettings
        }

        if module_name in button_map:
            button_map[module_name].setChecked(True)

    def on_logout_clicked(self):
        """Handle logout button click"""
        # Confirm logout
        if confirm_dialog(self, "Logout", "Are you sure you want to logout?"):
            # Log activity
            user_email = session.get_user_email()
            sqlite_db.log_activity(user_email, "Logout", "Authentication", "User logged out")

            # Clear session
            session.logout()

            # Close main window
            self.close()

            # Show login window
            from modules.auth import LoginWindow
            self.login_window = LoginWindow()
            self.login_window.show()

    def closeEvent(self, event):
        """Handle window close event"""
        # Confirm exit
        if confirm_dialog(self, "Exit Application", "Are you sure you want to exit?"):
            # Log activity
            user_email = session.get_user_email()
            if user_email:
                sqlite_db.log_activity(user_email, "Exit Application", "Main Window", "User closed application")

            # Clear session
            session.logout()

            event.accept()
        else:
            event.ignore()

