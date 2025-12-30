from datetime import datetime
from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt

from ui_compiled.inventory_ui import Ui_InventoryWidget
from ui_compiled.inventory_dialog_ui import Ui_InventoryDialog
from ui_compiled.stock_dialog_ui import Ui_StockDialog
from database import sqlite_db
from utils import show_error, show_success, show_warning, session


class InventoryDialog(QDialog):

    def __init__(self, parent=None, material_data=None):
        super().__init__(parent)
        self.ui = Ui_InventoryDialog()
        self.ui.setupUi(self)

        self.material_data = material_data
        self.setWindowTitle("Edit Material" if material_data else "Add New Material")

        if material_data:
            self.populate_data()

        self.ui.btnSave.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

    def populate_data(self):
        if not self.material_data:
            return

        self.ui.txtMaterialName.setText(self.material_data.get('material_name', ''))
        self.ui.txtMaterialType.setText(self.material_data.get('material_type', ''))
        self.ui.spinCurrentStock.setValue(float(self.material_data.get('current_stock', 0)))
        self.ui.txtUnit.setText(self.material_data.get('unit', ''))
        self.ui.spinMinStock.setValue(float(self.material_data.get('min_stock', 0)))
        self.ui.txtSupplier.setText(self.material_data.get('supplier', ''))

        status = self.material_data.get('status', 'Available')
        self.ui.cmbStatus.setCurrentText(status)

    def validate(self):
        if not self.ui.txtMaterialName.text().strip():
            show_error(self, "Validation Error", "Please enter material name")
            return False

        if not self.ui.txtUnit.text().strip():
            show_error(self, "Validation Error", "Please enter unit")
            return False

        return True

    def get_data(self):
        return {
            'material_name': self.ui.txtMaterialName.text().strip(),
            'material_type': self.ui.txtMaterialType.text().strip(),
            'current_stock': self.ui.spinCurrentStock.value(),
            'unit': self.ui.txtUnit.text().strip(),
            'min_stock': self.ui.spinMinStock.value(),
            'supplier': self.ui.txtSupplier.text().strip(),
            'status': self.ui.cmbStatus.currentText(),
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }


class StockDialog(QDialog):

    def __init__(self, parent=None, material_id=None, material_name=None, current_stock=0):
        super().__init__(parent)
        self.ui = Ui_StockDialog()
        self.ui.setupUi(self)

        self.material_id = material_id
        self.material_name = material_name
        self.current_stock = current_stock

        self.setWindowTitle(f"Update Stock - {material_name}")
        self.ui.lblMaterialName.setText(material_name)
        self.ui.lblCurrentStock.setText(f"Current Stock: {current_stock}")

        self.ui.btnSave.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

    def get_data(self):
        operation = self.ui.cmbOperation.currentText()
        quantity = self.ui.spinQuantity.value()

        if operation == "Add":
            new_stock = self.current_stock + quantity
        else:
            new_stock = self.current_stock - quantity

        return {
            'operation': operation,
            'quantity': quantity,
            'new_stock': new_stock,
            'remarks': self.ui.txtRemarks.toPlainText().strip()
        }


class InventoryWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_InventoryWidget()
        self.ui.setupUi(self)

        self.current_material_id = None

        self.setup_table()
        self.setup_connections()
        self.load_inventory()

    def setup_table(self):
        self.ui.tableInventory.setColumnWidth(0, 100)
        self.ui.tableInventory.setColumnWidth(1, 180)
        self.ui.tableInventory.setColumnWidth(2, 120)
        self.ui.tableInventory.setColumnWidth(3, 100)
        self.ui.tableInventory.setColumnWidth(4, 80)
        self.ui.tableInventory.setColumnWidth(5, 100)
        self.ui.tableInventory.setColumnWidth(6, 150)
        self.ui.tableInventory.setColumnWidth(7, 100)

        header = self.ui.tableInventory.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        self.ui.tableInventory.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tableInventory.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    def setup_connections(self):
        self.ui.btnAddMaterial.clicked.connect(self.add_material)
        self.ui.btnEditMaterial.clicked.connect(self.edit_material)
        self.ui.btnDeleteMaterial.clicked.connect(self.delete_material)
        self.ui.btnAddStock.clicked.connect(self.update_stock)
        self.ui.btnRefresh.clicked.connect(self.load_inventory)
        if hasattr(self.ui, 'txtSearch'):
            self.ui.txtSearch.textChanged.connect(self.search_materials)
        self.ui.tableInventory.itemSelectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self):
        selected_items = self.ui.tableInventory.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            self.current_material_id = self.ui.tableInventory.item(row, 0).text()
        else:
            self.current_material_id = None

    def load_inventory(self):
        self.ui.tableInventory.setRowCount(0)

        materials = sqlite_db.fetch_all("SELECT * FROM inventory ORDER BY material_name")

        low_stock_count = 0
        for material in materials:
            self.add_material_to_table(material)
            if material['current_stock'] <= material['min_stock']:
                low_stock_count += 1

        self.ui.lblLowStockAlert.setText(f"Total: {len(materials)} materials")
        if low_stock_count > 0:
            pass  # self.ui.lblLowStock.setText(f"Low Stock: {low_stock_count} items")
            self.ui.lblLowStock.setStyleSheet("color: #f44336; font-weight: bold;")
        else:
            pass  # self.ui.lblLowStock.setText("All stock levels good")
            self.ui.lblLowStock.setStyleSheet("color: #4CAF50; font-weight: bold;")

    def add_material_to_table(self, material):
        row = self.ui.tableInventory.rowCount()
        self.ui.tableInventory.insertRow(row)

        self.ui.tableInventory.setItem(row, 0, QTableWidgetItem(material['id']))
        self.ui.tableInventory.setItem(row, 1, QTableWidgetItem(material['material_name']))
        self.ui.tableInventory.setItem(row, 2, QTableWidgetItem(material['material_type'] or ''))

        stock_item = QTableWidgetItem(f"{material['current_stock']:.2f}")
        if material['current_stock'] <= material['min_stock']:
            stock_item.setForeground(Qt.GlobalColor.red)
        self.ui.tableInventory.setItem(row, 3, stock_item)

        self.ui.tableInventory.setItem(row, 4, QTableWidgetItem(material['unit'] or ''))
        self.ui.tableInventory.setItem(row, 5, QTableWidgetItem(f"{material['min_stock']:.2f}"))
        self.ui.tableInventory.setItem(row, 6, QTableWidgetItem(material['supplier'] or ''))

        status_item = QTableWidgetItem(material['status'] or 'Available')
        if material['status'] == 'Available':
            status_item.setForeground(Qt.GlobalColor.darkGreen)
        elif material['status'] == 'Low Stock':
            status_item.setForeground(Qt.GlobalColor.darkYellow)
        elif material['status'] == 'Out of Stock':
            status_item.setForeground(Qt.GlobalColor.red)

        self.ui.tableInventory.setItem(row, 7, status_item)

    def add_material(self):
        dialog = InventoryDialog(self)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()
            material_id = f"MAT{datetime.now().strftime('%Y%m%d%H%M%S')}"
            data['id'] = material_id
            data['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if sqlite_db.insert('inventory', data):
                show_success(self, "Success", "Material added successfully")

                user_email = session.get_user_email()
                sqlite_db.log_activity(user_email, "Add Material", "Inventory", f"Added {data['material_name']}")

                self.load_inventory()
            else:
                show_error(self, "Error", "Failed to add material")

    def edit_material(self):
        if not self.current_material_id:
            show_warning(self, "No Selection", "Please select a material to edit")
            return

        material = sqlite_db.fetch_one("SELECT * FROM inventory WHERE id = ?", (self.current_material_id,))
        if not material:
            show_error(self, "Error", "Material not found")
            return

        dialog = InventoryDialog(self, material)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()

            if sqlite_db.update('inventory', data, "id = ?", (self.current_material_id,)):
                show_success(self, "Success", "Material updated successfully")

                user_email = session.get_user_email()
                sqlite_db.log_activity(user_email, "Edit Material", "Inventory", f"Updated {data['material_name']}")

                self.load_inventory()
            else:
                show_error(self, "Error", "Failed to update material")

    def delete_material(self):
        if not self.current_material_id:
            show_warning(self, "No Selection", "Please select a material to delete")
            return

        reply = QMessageBox.question(
            self, "Confirm Delete",
            "Are you sure you want to delete this material?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            if sqlite_db.delete('inventory', "id = ?", (self.current_material_id,)):
                show_success(self, "Success", "Material deleted successfully")

                user_email = session.get_user_email()
                sqlite_db.log_activity(user_email, "Delete Material", "Inventory", f"Deleted material {self.current_material_id}")

                self.current_material_id = None
                self.load_inventory()
            else:
                show_error(self, "Error", "Failed to delete material")

    def update_stock(self):
        if not self.current_material_id:
            show_warning(self, "No Selection", "Please select a material to update stock")
            return

        material = sqlite_db.fetch_one("SELECT * FROM inventory WHERE id = ?", (self.current_material_id,))
        if not material:
            show_error(self, "Error", "Material not found")
            return

        dialog = StockDialog(self, material['id'], material['material_name'], material['current_stock'])

        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()

            update_data = {
                'current_stock': data['new_stock'],
                'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            if sqlite_db.update('inventory', update_data, "id = ?", (self.current_material_id,)):
                show_success(self, "Success", f"Stock {data['operation'].lower()}ed successfully")

                user_email = session.get_user_email()
                sqlite_db.log_activity(user_email, "Update Stock", "Inventory",
                                      f"{data['operation']} {data['quantity']} {material['unit']} - {material['material_name']}")

                self.load_inventory()
            else:
                show_error(self, "Error", "Failed to update stock")

    def search_materials(self, text):
        for row in range(self.ui.tableInventory.rowCount()):
            match = False
            for col in range(self.ui.tableInventory.columnCount()):
                item = self.ui.tableInventory.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.ui.tableInventory.setRowHidden(row, not match)



