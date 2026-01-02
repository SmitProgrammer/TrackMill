"""
Dashboard module
"""

from PySide6.QtWidgets import QWidget, QListWidgetItem
from PySide6.QtCore import QTimer, Qt

from ui_compiled.dashboard_ui import Ui_DashboardWidget
from database import cloud_first_db
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
            all_orders = cloud_first_db.get_all_orders()
            orders_count = len([o for o in all_orders if o.get('status') != 'Completed'])
            self.ui.lblOrdersValue.setText(str(orders_count))

            # Count inventory items
            inventory_count = len(cloud_first_db.get_all_inventory())
            self.ui.lblInventoryValue.setText(str(inventory_count))

            # Count active employees
            all_employees = cloud_first_db.get_all_employees()
            employees_count = len([e for e in all_employees if e.get('status') == 'Active'])
            self.ui.lblEmployeesValue.setText(str(employees_count))

            # Count available machines
            all_machines = cloud_first_db.get_all_machines()
            machines_count = len([m for m in all_machines if m.get('status') == 'Available'])
            self.ui.lblMachinesValue.setText(str(machines_count))

        except Exception as e:
            print(f"❌ Error loading summary stats: {e}")

    def load_recent_activity(self):
        """Load and display recent activity"""
        try:
            # Clear existing items
            self.ui.listRecentActivity.clear()

            # Show placeholder - activity logging not supported in cloud-only mode
            item = QListWidgetItem("📊 Dashboard Overview (Cloud-First)")
            item.setForeground(Qt.darkGreen)
            self.ui.listRecentActivity.addItem(item)

            # Add statistics
            try:
                all_orders = cloud_first_db.get_all_orders()
                item = QListWidgetItem(f"📦 Total Orders: {len(all_orders)}")
                self.ui.listRecentActivity.addItem(item)

                all_inventory = cloud_first_db.get_all_inventory()
                item = QListWidgetItem(f"📋 Total Inventory Items: {len(all_inventory)}")
                self.ui.listRecentActivity.addItem(item)

                all_employees = cloud_first_db.get_all_employees()
                item = QListWidgetItem(f"👥 Total Employees: {len(all_employees)}")
                self.ui.listRecentActivity.addItem(item)

                all_machines = cloud_first_db.get_all_machines()
                item = QListWidgetItem(f"⚙️ Total Machines: {len(all_machines)}")
                self.ui.listRecentActivity.addItem(item)

            except Exception as e:
                item = QListWidgetItem(f"⚠️ Error loading statistics: {str(e)}")
                self.ui.listRecentActivity.addItem(item)

        except Exception as e:
            print(f"❌ Error loading recent activity: {e}")

    def showEvent(self, event):
        """Handle widget show event"""
        super().showEvent(event)
        # Refresh data when dashboard is shown
        self.refresh_data()

