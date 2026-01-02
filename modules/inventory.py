from datetime import datetime
from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt

from ui_compiled.inventory_ui import Ui_InventoryWidget
from ui_compiled.inventory_dialog_ui import Ui_InventoryDialog
from ui_compiled.stock_dialog_ui import Ui_StockDialog
from database import cloud_first_db
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

        # Set initial button states
        self.ui.btnEditMaterial.setEnabled(False)
        self.ui.btnDeleteMaterial.setEnabled(False)
        self.ui.btnAddStock.setEnabled(False)
        if hasattr(self.ui, 'btnIssueStock'):
            self.ui.btnIssueStock.setEnabled(False)

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
        if hasattr(self.ui, 'btnIssueStock'):
            self.ui.btnIssueStock.clicked.connect(self.update_stock)
        self.ui.btnRefresh.clicked.connect(self.load_inventory)
        if hasattr(self.ui, 'txtSearch'):
            self.ui.txtSearch.textChanged.connect(self.search_materials)
        self.ui.tableInventory.itemSelectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self):
        selected_items = self.ui.tableInventory.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            self.current_material_id = self.ui.tableInventory.item(row, 0).text()
            self.ui.btnEditMaterial.setEnabled(True)
            self.ui.btnDeleteMaterial.setEnabled(True)
            self.ui.btnAddStock.setEnabled(True)
            if hasattr(self.ui, 'btnIssueStock'):
                self.ui.btnIssueStock.setEnabled(True)
        else:
            self.current_material_id = None
            self.ui.btnEditMaterial.setEnabled(False)
            self.ui.btnDeleteMaterial.setEnabled(False)
            self.ui.btnAddStock.setEnabled(False)
            if hasattr(self.ui, 'btnIssueStock'):
                self.ui.btnIssueStock.setEnabled(False)

    def load_inventory(self):
        print("\n[INVENTORY] ========== REFRESH STARTED ==========")
        self.ui.tableInventory.setRowCount(0)

        try:
            # Fetch from Firebase (Cloud-only approach)
            print("[INVENTORY] Fetching materials from Firebase...")
            materials = cloud_first_db.get_all_materials()
            print(f"[INVENTORY] Firebase materials count: {len(materials)}")

            if not materials:
                print("[INVENTORY] No materials found in Firebase")
                self.ui.lblLowStockAlert.setText("⚠️ Low Stock: 0")
                print("[INVENTORY] ========== REFRESH COMPLETED ==========\n")
                return

            low_stock_count = 0
            materials_sorted = sorted(materials, key=lambda m: m.get('material_name', ''))
            print(f"[INVENTORY] Displaying {len(materials_sorted)} materials in UI")
            for material in materials_sorted:
                try:
                    self.add_material_to_table(material)
                    if material.get('current_stock', 0) <= material.get('min_stock', 0):
                        low_stock_count += 1
                except Exception as e:
                    print(f"[INVENTORY] Error adding material to table: {e}")
                    continue

            self.ui.lblLowStockAlert.setText(f"⚠️ Low Stock: {low_stock_count}")
            print("[INVENTORY] ========== REFRESH COMPLETED ==========\n")
        except Exception as e:
            print(f"[INVENTORY] Error loading inventory: {e}")
            from utils import show_error
            show_error(self, "Error", f"Failed to load inventory: {str(e)}")

    def add_material_to_table(self, material):
        row = self.ui.tableInventory.rowCount()
        self.ui.tableInventory.insertRow(row)

        self.ui.tableInventory.setItem(row, 0, QTableWidgetItem(str(material.get('id', ''))))
        self.ui.tableInventory.setItem(row, 1, QTableWidgetItem(str(material.get('material_name', ''))))
        self.ui.tableInventory.setItem(row, 2, QTableWidgetItem(str(material.get('material_type') or '')))

        stock_item = QTableWidgetItem(f"{material.get('current_stock', 0):.2f}")
        if material.get('current_stock', 0) <= material.get('min_stock', 0):
            stock_item.setForeground(Qt.GlobalColor.red)
        self.ui.tableInventory.setItem(row, 3, stock_item)

        self.ui.tableInventory.setItem(row, 4, QTableWidgetItem(str(material.get('unit') or '')))
        self.ui.tableInventory.setItem(row, 5, QTableWidgetItem(f"{material.get('min_stock', 0):.2f}"))
        self.ui.tableInventory.setItem(row, 6, QTableWidgetItem(str(material.get('supplier') or '')))

        status_item = QTableWidgetItem(str(material.get('status', 'Available') or 'Available'))
        if material.get('status') == 'Available':
            status_item.setForeground(Qt.GlobalColor.darkGreen)
        elif material.get('status') == 'Low Stock':
            status_item.setForeground(Qt.GlobalColor.darkYellow)
        elif material.get('status') == 'Out of Stock':
            status_item.setForeground(Qt.GlobalColor.red)

        self.ui.tableInventory.setItem(row, 7, status_item)

    def add_material(self):
        dialog = InventoryDialog(self)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()
            material_id = f"MAT{datetime.now().strftime('%Y%m%d%H%M%S')}"

            if cloud_first_db.create_material(material_id, data):
                show_success(self, "Success", "Material added to inventory")
            else:
                show_error(self, "Error", "Failed to add material")

            self.load_inventory()

    def edit_material(self):
        if not self.current_material_id:
            show_warning(self, "No Selection", "Please select a material to edit")
            return

        material = cloud_first_db.get_material(self.current_material_id)
        if not material:
            show_error(self, "Error", "Material not found")
            return

        dialog = InventoryDialog(self, material)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()

            if cloud_first_db.update_material(self.current_material_id, data):
                show_success(self, "Success", "Material updated successfully")

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
            if cloud_first_db.delete_material(self.current_material_id):
                show_success(self, "Success", "Material deleted from inventory")
                self.current_material_id = None
                self.load_inventory()
            else:
                show_error(self, "Error", "Failed to delete material")

    def update_stock(self):
        if not self.current_material_id:
            show_warning(self, "No Selection", "Please select a material")
            return

        material = cloud_first_db.get_material(self.current_material_id)
        if not material:
            show_error(self, "Error", "Material not found")
            return

        dialog = StockDialog(self, self.current_material_id, material['material_name'], material['current_stock'])

        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()

            update_data = {
                'current_stock': data['new_stock'],
                'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            if cloud_first_db.update_material(self.current_material_id, update_data):
                show_success(self, "Success", f"Stock {data['operation'].lower()}ed successfully")

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
