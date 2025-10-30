"""
Dashboard module
"""

from PySide6.QtWidgets import QWidget, QListWidgetItem
from PySide6.QtCore import QTimer, Qt

from ui_compiled.dashboard_ui import Ui_DashboardWidget
from database import sqlite_db
from utils import format_datetime


class DashboardWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_DashboardWidget()
        self.ui.setupUi(self)

        # Setup auto-refresh timer (every 30 seconds)
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.refresh_data)
        self.refresh_timer.start(30000)  # 30 seconds

        # Load initial data
        self.refresh_data()

    def refresh_data(self):
        """Refresh dashboard data"""
        self.load_summary_stats()
        self.load_recent_activity()

    def load_summary_stats(self):
        """Load and display summary statistics"""
        try:
            # Count active orders
            orders_count = sqlite_db.count('orders', "status != ?", ('Completed',))
            self.ui.lblOrdersValue.setText(str(orders_count))

            # Count inventory items
            inventory_count = sqlite_db.count('inventory')
            self.ui.lblInventoryValue.setText(str(inventory_count))

            # Count active employees
            employees_count = sqlite_db.count('employees', "status = ?", ('Active',))
            self.ui.lblEmployeesValue.setText(str(employees_count))

            # Count available machines
            machines_count = sqlite_db.count('machines', "status = ?", ('Available',))
            self.ui.lblMachinesValue.setText(str(machines_count))

        except Exception as e:
            print(f"❌ Error loading summary stats: {e}")

    def load_recent_activity(self):
        """Load and display recent activity"""
        try:
            # Clear existing items
            self.ui.listRecentActivity.clear()

            # Get recent activities from database
            activities = sqlite_db.get_recent_activities(limit=10)

            if not activities:
                # Show placeholder if no activity
                item = QListWidgetItem("No recent activity")
                item.setForeground(Qt.gray)
                self.ui.listRecentActivity.addItem(item)
            else:
                # Add activities to list
                for activity in activities:
                    timestamp = format_datetime(activity['timestamp'],
                                                "%Y-%m-%d %H:%M:%S",
                                                "%d-%m-%Y %I:%M %p")

                    text = f"{activity['action']} - {activity['module']}"
                    if activity['details']:
                        text += f" ({activity['details']})"
                    text += f"\n{timestamp} by {activity['user_email']}"

                    item = QListWidgetItem(text)
                    self.ui.listRecentActivity.addItem(item)

        except Exception as e:
            print(f"❌ Error loading recent activity: {e}")

    def showEvent(self, event):
        """Handle widget show event"""
        super().showEvent(event)
        # Refresh data when dashboard is shown
        self.refresh_data()

