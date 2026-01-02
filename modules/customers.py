from datetime import datetime
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QDialog, QAbstractItemView
from PySide6.QtCore import Qt
from datetime import datetime

from ui_compiled.customers_ui import Ui_CustomersWidget
from ui_compiled.customer_dialog_ui import Ui_CustomerDialog
from database import cloud_first_db
from utils import show_error, show_success, confirm_dialog, validate_email, validate_phone, is_empty, session


class CustomerDialog(QDialog):
    def __init__(self, parent=None, customer_data=None):
        super().__init__(parent)
        self.ui = Ui_CustomerDialog()
        self.ui.setupUi(self)

        self.customer_data = customer_data

        if customer_data:
            self.setWindowTitle("Edit Customer")
            self.load_data()
        else:
            self.setWindowTitle("Add New Customer")

        self.ui.btnSave.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

    def load_data(self):
        if self.customer_data:
            self.ui.txtName.setText(self.customer_data.get('name', ''))
            self.ui.txtContact.setText(self.customer_data.get('contact', ''))
            self.ui.txtEmail.setText(self.customer_data.get('email', ''))
            self.ui.txtCompany.setText(self.customer_data.get('company', ''))
            self.ui.txtAddress.setText(self.customer_data.get('address', ''))

    def get_data(self):
        return {
            'name': self.ui.txtName.text().strip(),
            'contact': self.ui.txtContact.text().strip(),
            'email': self.ui.txtEmail.text().strip(),
            'company': self.ui.txtCompany.text().strip(),
            'address': self.ui.txtAddress.toPlainText().strip()
        }

    def validate(self):
        data = self.get_data()

        if is_empty(data['name']):
            show_error(self, "Validation Error", "Customer name is required")
            return False

        if data['contact'] and not validate_phone(data['contact']):
            show_error(self, "Validation Error", "Invalid phone number format")
            return False

        if data['email'] and not validate_email(data['email']):
            show_error(self, "Validation Error", "Invalid email format")
            return False

        return True


class CustomersWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_CustomersWidget()
        self.ui.setupUi(self)

        self.current_customer_id = None

        self.setup_table()
        self.setup_connections()

        # Set initial button states
        self.ui.btnEditCustomer.setEnabled(False)
        self.ui.btnDeleteCustomer.setEnabled(False)

        self.load_customers()

    def setup_table(self):
        self.ui.tableCustomers.setColumnWidth(0, 100)
        self.ui.tableCustomers.setColumnWidth(1, 150)
        self.ui.tableCustomers.setColumnWidth(2, 120)
        self.ui.tableCustomers.setColumnWidth(3, 180)
        self.ui.tableCustomers.setColumnWidth(4, 150)
        self.ui.tableCustomers.setColumnWidth(5, 200)

        header = self.ui.tableCustomers.horizontalHeader()
        header.setSectionResizeMode(5, QHeaderView.Stretch)

        self.ui.tableCustomers.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tableCustomers.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    def setup_connections(self):
        self.ui.btnAddCustomer.clicked.connect(self.add_customer)
        self.ui.btnEditCustomer.clicked.connect(self.edit_customer)
        self.ui.btnDeleteCustomer.clicked.connect(self.delete_customer)
        self.ui.btnRefresh.clicked.connect(self.load_customers)
        self.ui.txtSearch.textChanged.connect(self.search_customers)
        self.ui.tableCustomers.itemSelectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self):
        selected_items = self.ui.tableCustomers.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            self.current_customer_id = self.ui.tableCustomers.item(row, 0).text()
            self.ui.btnEditCustomer.setEnabled(True)
            self.ui.btnDeleteCustomer.setEnabled(True)
        else:
            self.current_customer_id = None
            self.ui.btnEditCustomer.setEnabled(False)
            self.ui.btnDeleteCustomer.setEnabled(False)

    def load_customers(self):
        print("\n[CUSTOMERS] ========== LOADING CUSTOMERS (CLOUD-FIRST) ==========")
        self.ui.tableCustomers.setRowCount(0)

        # Cloud-first approach: always fetch from cloud, fallback to SQLite
        print("[CUSTOMERS] Fetching from Firebase (primary)...")
        customers = cloud_first_db.get_all_customers()

        if customers:
            print(f"[CUSTOMERS] Successfully loaded {len(customers)} customers")
        else:
            print("[CUSTOMERS] No customers found")

        # Display in table
        for customer in customers:
            self.add_customer_to_table(customer)

        self.ui.lblTotalCustomers.setText(f"Total: {len(customers)} customers")
        print("[CUSTOMERS] ========== LOAD COMPLETED ==========\n")

    def add_customer_to_table(self, customer):
        row = self.ui.tableCustomers.rowCount()
        self.ui.tableCustomers.insertRow(row)

        self.ui.tableCustomers.setItem(row, 0, QTableWidgetItem(customer['id']))
        self.ui.tableCustomers.setItem(row, 1, QTableWidgetItem(customer['name']))
        self.ui.tableCustomers.setItem(row, 2, QTableWidgetItem(customer['contact'] or ''))
        self.ui.tableCustomers.setItem(row, 3, QTableWidgetItem(customer['email'] or ''))
        self.ui.tableCustomers.setItem(row, 4, QTableWidgetItem(customer['company'] or ''))
        self.ui.tableCustomers.setItem(row, 5, QTableWidgetItem(customer['address'] or ''))

    def search_customers(self):
        search_text = self.ui.txtSearch.text().strip().lower()

        for row in range(self.ui.tableCustomers.rowCount()):
            show_row = False

            for col in range(self.ui.tableCustomers.columnCount()):
                item = self.ui.tableCustomers.item(row, col)
                if item and search_text in item.text().lower():
                    show_row = True
                    break

            self.ui.tableCustomers.setRowHidden(row, not show_row)

    def add_customer(self):
        dialog = CustomerDialog(self)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()
            customer_id = f"CUST{datetime.now().strftime('%Y%m%d%H%M%S')}"

            # Cloud-first: write to Firebase first
            if cloud_first_db.create_customer(customer_id, data):
                show_success(self, "Success", "Customer created successfully")
            else:
                show_error(self, "Error", "Failed to create customer")

            self.load_customers()

    def edit_customer(self):
        if not self.current_customer_id:
            return

        # Get fresh data from cloud
        customer = cloud_first_db.get_customer(self.current_customer_id)

        if not customer:
            show_error(self, "Error", "Customer not found")
            return

        dialog = CustomerDialog(self, customer)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()

            # Cloud-first: update Firebase first
            if cloud_first_db.update_customer(self.current_customer_id, data):
                show_success(self, "Success", "Customer updated successfully")
            else:
                show_error(self, "Error", "Failed to update customer")

            self.load_customers()

    def delete_customer(self):
        if not self.current_customer_id:
            return

        # Get fresh data from cloud
        customer = cloud_first_db.get_customer(self.current_customer_id)

        if not customer:
            show_error(self, "Error", "Customer not found")
            return

        if confirm_dialog(self, "Confirm Delete", f"Are you sure you want to delete customer '{customer['name']}'?"):
            # Cloud-first: delete from Firebase
            if cloud_first_db.delete_customer(self.current_customer_id):
                show_success(self, "Success", "Customer deleted successfully")
            else:
                show_error(self, "Error", "Failed to delete customer")

            self.load_customers()

    def showEvent(self, event):
        super().showEvent(event)
        self.load_customers()
