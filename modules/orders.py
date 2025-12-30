from datetime import datetime
from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt

from ui_compiled.orders_ui import Ui_OrdersWidget
from ui_compiled.order_dialog_ui import Ui_OrderDialog
from database import sqlite_db
from utils import show_error, show_success, show_warning, session


class OrderDialog(QDialog):

    def __init__(self, parent=None, order_data=None):
        super().__init__(parent)
        self.ui = Ui_OrderDialog()
        self.ui.setupUi(self)

        self.order_data = order_data
        self.setWindowTitle("Edit Order" if order_data else "Add New Order")

        self.load_customers()

        if order_data:
            self.populate_data()

        self.ui.btnSave.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

    def load_customers(self):
        self.ui.cmbCustomer.clear()
        self.ui.cmbCustomer.addItem("-- Select Customer --", None)

        customers = sqlite_db.fetch_all("SELECT id, name FROM customers ORDER BY name")
        for customer in customers:
            self.ui.cmbCustomer.addItem(customer['name'], customer['id'])

    def populate_data(self):
        if not self.order_data:
            return

        for i in range(self.ui.cmbCustomer.count()):
            if self.ui.cmbCustomer.itemData(i) == self.order_data['customer_id']:
                self.ui.cmbCustomer.setCurrentIndex(i)
                break

        self.ui.txtProductName.setText(self.order_data.get('product_name', ''))
        self.ui.spinQuantity.setValue(int(self.order_data.get('quantity', 1)))
        self.ui.txtSpecifications.setPlainText(self.order_data.get('specifications', ''))

        if self.order_data.get('order_date'):
            order_date = datetime.strptime(self.order_data['order_date'], '%Y-%m-%d')
            self.ui.dateOrder.setDate(order_date)

        if self.order_data.get('delivery_date'):
            delivery_date = datetime.strptime(self.order_data['delivery_date'], '%Y-%m-%d')
            self.ui.dateDelivery.setDate(delivery_date)

        priority = self.order_data.get('priority', 'Medium')
        self.ui.cmbPriority.setCurrentText(priority)

        status = self.order_data.get('status', 'Pending')
        self.ui.cmbStatus.setCurrentText(status)

    def validate(self):
        if self.ui.cmbCustomer.currentIndex() == 0:
            show_error(self, "Validation Error", "Please select a customer")
            return False

        if not self.ui.txtProductName.text().strip():
            show_error(self, "Validation Error", "Please enter product name")
            return False

        if self.ui.spinQuantity.value() <= 0:
            show_error(self, "Validation Error", "Quantity must be greater than 0")
            return False

        return True

    def get_data(self):
        customer_id = self.ui.cmbCustomer.currentData()
        customer_name = self.ui.cmbCustomer.currentText()

        return {
            'customer_id': customer_id,
            'customer_name': customer_name,
            'product_name': self.ui.txtProductName.text().strip(),
            'quantity': self.ui.spinQuantity.value(),
            'specifications': self.ui.txtSpecifications.toPlainText().strip(),
            'order_date': self.ui.dateOrder.date().toString('yyyy-MM-dd'),
            'delivery_date': self.ui.dateDelivery.date().toString('yyyy-MM-dd'),
            'priority': self.ui.cmbPriority.currentText(),
            'status': self.ui.cmbStatus.currentText(),
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }


class OrdersWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_OrdersWidget()
        self.ui.setupUi(self)

        self.current_order_id = None

        self.setup_table()
        self.setup_connections()
        self.load_orders()

    def setup_table(self):
        self.ui.tableOrders.setColumnWidth(0, 100)
        self.ui.tableOrders.setColumnWidth(1, 150)
        self.ui.tableOrders.setColumnWidth(2, 180)
        self.ui.tableOrders.setColumnWidth(3, 80)
        self.ui.tableOrders.setColumnWidth(4, 100)
        self.ui.tableOrders.setColumnWidth(5, 100)
        self.ui.tableOrders.setColumnWidth(6, 90)
        self.ui.tableOrders.setColumnWidth(7, 100)

        header = self.ui.tableOrders.horizontalHeader()
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        self.ui.tableOrders.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tableOrders.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    def setup_connections(self):
        self.ui.btnAddOrder.clicked.connect(self.add_order)
        self.ui.btnEditOrder.clicked.connect(self.edit_order)
        self.ui.btnDeleteOrder.clicked.connect(self.delete_order)
        self.ui.btnRefresh.clicked.connect(self.load_orders)
        if hasattr(self.ui, 'txtSearch'):
            self.ui.txtSearch.textChanged.connect(self.search_orders)
        if hasattr(self.ui, 'cmbFilterStatus'):
            self.ui.cmbFilterStatus.currentTextChanged.connect(self.filter_orders)
        self.ui.tableOrders.itemSelectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self):
        selected_items = self.ui.tableOrders.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            self.current_order_id = self.ui.tableOrders.item(row, 0).text()
        else:
            self.current_order_id = None

    def load_orders(self):
        self.ui.tableOrders.setRowCount(0)

        orders = sqlite_db.fetch_all("SELECT * FROM orders ORDER BY order_date DESC")

        for order in orders:
            self.add_order_to_table(order)

        self.ui.lblTotalOrders.setText(f"Total: {len(orders)} orders")

    def add_order_to_table(self, order):
        row = self.ui.tableOrders.rowCount()
        self.ui.tableOrders.insertRow(row)

        self.ui.tableOrders.setItem(row, 0, QTableWidgetItem(order['id']))
        self.ui.tableOrders.setItem(row, 1, QTableWidgetItem(order['customer_name'] or ''))
        self.ui.tableOrders.setItem(row, 2, QTableWidgetItem(order['product_name']))
        self.ui.tableOrders.setItem(row, 3, QTableWidgetItem(str(order['quantity'])))
        self.ui.tableOrders.setItem(row, 4, QTableWidgetItem(order['order_date'] or ''))
        self.ui.tableOrders.setItem(row, 5, QTableWidgetItem(order['delivery_date'] or ''))
        self.ui.tableOrders.setItem(row, 6, QTableWidgetItem(order['priority'] or ''))

        status_item = QTableWidgetItem(order['status'] or 'Pending')
        if order['status'] == 'Completed':
            status_item.setForeground(Qt.GlobalColor.darkGreen)
        elif order['status'] == 'In Progress':
            status_item.setForeground(Qt.GlobalColor.blue)
        elif order['status'] == 'Pending':
            status_item.setForeground(Qt.GlobalColor.darkYellow)
        elif order['status'] == 'Cancelled':
            status_item.setForeground(Qt.GlobalColor.red)

        self.ui.tableOrders.setItem(row, 7, status_item)

    def add_order(self):
        dialog = OrderDialog(self)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()
            order_id = f"ORD{datetime.now().strftime('%Y%m%d%H%M%S')}"
            data['id'] = order_id
            data['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if sqlite_db.insert('orders', data):
                show_success(self, "Success", "Order added successfully")

                user_email = session.get_user_email()
                sqlite_db.log_activity(user_email, "Add Order", "Orders", f"Added order {order_id}")

                self.load_orders()
            else:
                show_error(self, "Error", "Failed to add order")

    def edit_order(self):
        if not self.current_order_id:
            show_warning(self, "No Selection", "Please select an order to edit")
            return

        order = sqlite_db.fetch_one("SELECT * FROM orders WHERE id = ?", (self.current_order_id,))
        if not order:
            show_error(self, "Error", "Order not found")
            return

        dialog = OrderDialog(self, order)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()

            if sqlite_db.update('orders', data, "id = ?", (self.current_order_id,)):
                show_success(self, "Success", "Order updated successfully")

                user_email = session.get_user_email()
                sqlite_db.log_activity(user_email, "Edit Order", "Orders", f"Updated order {self.current_order_id}")

                self.load_orders()
            else:
                show_error(self, "Error", "Failed to update order")

    def delete_order(self):
        if not self.current_order_id:
            show_warning(self, "No Selection", "Please select an order to delete")
            return

        reply = QMessageBox.question(
            self, "Confirm Delete",
            "Are you sure you want to delete this order?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            if sqlite_db.delete('orders', "id = ?", (self.current_order_id,)):
                show_success(self, "Success", "Order deleted successfully")

                user_email = session.get_user_email()
                sqlite_db.log_activity(user_email, "Delete Order", "Orders", f"Deleted order {self.current_order_id}")

                self.current_order_id = None
                self.load_orders()
            else:
                show_error(self, "Error", "Failed to delete order")

    def search_orders(self, text):
        for row in range(self.ui.tableOrders.rowCount()):
            match = False
            for col in range(self.ui.tableOrders.columnCount()):
                item = self.ui.tableOrders.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.ui.tableOrders.setRowHidden(row, not match)

    def filter_orders(self, status):
        if status == "All":
            for row in range(self.ui.tableOrders.rowCount()):
                self.ui.tableOrders.setRowHidden(row, False)
        else:
            for row in range(self.ui.tableOrders.rowCount()):
                status_item = self.ui.tableOrders.item(row, 7)
                if status_item:
                    self.ui.tableOrders.setRowHidden(row, status_item.text() != status)


