"""
Customer management module
"""

from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PySide6.QtCore import Qt
from datetime import datetime

from ui_compiled.customers_ui import Ui_CustomersWidget
from database import sqlite_db
from utils import show_error, show_success, show_info, confirm_dialog, validate_email, validate_phone, is_empty, session


class CustomerDialog(QDialog):
    def __init__(self, parent=None, customer_data=None):
        super().__init__(parent)
        self.customer_data = customer_data
        self.setup_ui()

        if customer_data:
            self.setWindowTitle("Edit Customer")
            self.load_data()
        else:
            self.setWindowTitle("Add New Customer")

    def setup_ui(self):
        self.setFixedSize(500, 400)
        layout = QVBoxLayout()

        # Name
        layout.addWidget(QLabel("Customer Name:"))
        self.txt_name = QLineEdit()
        layout.addWidget(self.txt_name)

        # Contact
        layout.addWidget(QLabel("Contact Number:"))
        self.txt_contact = QLineEdit()
        layout.addWidget(self.txt_contact)

        # Email
        layout.addWidget(QLabel("Email:"))
        self.txt_email = QLineEdit()
        layout.addWidget(self.txt_email)

        # Company
        layout.addWidget(QLabel("Company:"))
        self.txt_company = QLineEdit()
        layout.addWidget(self.txt_company)

        # Address
        layout.addWidget(QLabel("Address:"))
        self.txt_address = QTextEdit()
        self.txt_address.setMaximumHeight(80)
        layout.addWidget(self.txt_address)

        # Buttons
        btn_layout = QHBoxLayout()
        btn_save = QPushButton("Save")
        btn_cancel = QPushButton("Cancel")
        btn_save.clicked.connect(self.accept)
        btn_cancel.clicked.connect(self.reject)
        btn_layout.addWidget(btn_save)
        btn_layout.addWidget(btn_cancel)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def load_data(self):
        self.txt_name.setText(self.customer_data.get('name', ''))
        self.txt_contact.setText(self.customer_data.get('contact', ''))
        self.txt_email.setText(self.customer_data.get('email', ''))
        self.txt_company.setText(self.customer_data.get('company', ''))
        self.txt_address.setText(self.customer_data.get('address', ''))

    def get_data(self):
        return {
            'name': self.txt_name.text().strip(),
            'contact': self.txt_contact.text().strip(),
            'email': self.txt_email.text().strip(),
            'company': self.txt_company.text().strip(),
            'address': self.txt_address.toPlainText().strip()
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

    def setup_connections(self):
        self.ui.btnAddCustomer.clicked.connect(self.add_customer)
        self.ui.btnEditCustomer.clicked.connect(self.edit_customer)
        self.ui.btnDeleteCustomer.clicked.connect(self.delete_customer)
        self.ui.btnRefresh.clicked.connect(self.load_customers)
        self.ui.txtSearch.textChanged.connect(self.search_customers)
        self.ui.tableCustomers.itemSelectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self):
        selected = len(self.ui.tableCustomers.selectedItems()) > 0
        self.ui.btnEditCustomer.setEnabled(selected)
        self.ui.btnDeleteCustomer.setEnabled(selected)

        if selected:
            row = self.ui.tableCustomers.currentRow()
            self.current_customer_id = self.ui.tableCustomers.item(row, 0).text()
        else:
            self.current_customer_id = None

    def load_customers(self):
        self.ui.tableCustomers.setRowCount(0)

        customers = sqlite_db.fetch_all("SELECT * FROM customers ORDER BY created_at DESC")

        for customer in customers:
            self.add_customer_to_table(customer)

        self.ui.lblTotalCustomers.setText(f"Total: {len(customers)} customers")

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
            data['id'] = customer_id

            if sqlite_db.insert('customers', data):
                show_success(self, "Success", "Customer added successfully")

                user_email = session.get_user_email()
                sqlite_db.log_activity(user_email, "Add Customer", "Customers", f"Added {data['name']}")

                self.load_customers()
            else:
                show_error(self, "Error", "Failed to add customer")

    def edit_customer(self):
        if not self.current_customer_id:
            return

        customer = sqlite_db.fetch_one("SELECT * FROM customers WHERE id = ?", (self.current_customer_id,))

        if not customer:
            show_error(self, "Error", "Customer not found")
            return

        dialog = CustomerDialog(self, customer)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()

            if sqlite_db.update('customers', data, "id = ?", (self.current_customer_id,)):
                show_success(self, "Success", "Customer updated successfully")

                user_email = session.get_user_email()
                sqlite_db.log_activity(user_email, "Edit Customer", "Customers", f"Updated {data['name']}")

                self.load_customers()
            else:
                show_error(self, "Error", "Failed to update customer")

    def delete_customer(self):
        if not self.current_customer_id:
            return

        customer = sqlite_db.fetch_one("SELECT name FROM customers WHERE id = ?", (self.current_customer_id,))

        if not customer:
            show_error(self, "Error", "Customer not found")
            return

        if confirm_dialog(self, "Confirm Delete", f"Are you sure you want to delete customer '{customer['name']}'?"):
            if sqlite_db.delete('customers', "id = ?", (self.current_customer_id,)):
                show_success(self, "Success", "Customer deleted successfully")

                user_email = session.get_user_email()
                sqlite_db.log_activity(user_email, "Delete Customer", "Customers", f"Deleted {customer['name']}")

                self.load_customers()
            else:
                show_error(self, "Error", "Failed to delete customer")

    def showEvent(self, event):
        super().showEvent(event)
        self.load_customers()

