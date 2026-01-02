from datetime import datetime
from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt

from ui_compiled.machines_ui import Ui_MachinesWidget
from ui_compiled.machine_dialog_ui import Ui_MachineDialog
from database import cloud_first_db
from utils import show_error, show_success, show_warning, session


class MachineDialog(QDialog):

    def __init__(self, parent=None, machine_data=None):
        super().__init__(parent)
        self.ui = Ui_MachineDialog()
        self.ui.setupUi(self)

        self.machine_data = machine_data
        self.setWindowTitle("Edit Machine" if machine_data else "Add New Machine")

        if machine_data:
            self.populate_data()

        self.ui.btnSave.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

    def populate_data(self):
        if not self.machine_data:
            return

        self.ui.txtMachineName.setText(self.machine_data.get('machine_name', ''))
        self.ui.txtMachineType.setText(self.machine_data.get('machine_type', ''))
        self.ui.txtModel.setText(self.machine_data.get('model', ''))

        status = self.machine_data.get('status', 'Available')
        self.ui.cmbStatus.setCurrentText(status)

        if self.machine_data.get('last_maintenance'):
            last_maintenance = datetime.strptime(self.machine_data['last_maintenance'], '%Y-%m-%d')
            self.ui.dateLastMaintenance.setDate(last_maintenance)

        if self.machine_data.get('next_maintenance'):
            next_maintenance = datetime.strptime(self.machine_data['next_maintenance'], '%Y-%m-%d')
            self.ui.dateNextMaintenance.setDate(next_maintenance)

        self.ui.txtSpecifications.setPlainText(self.machine_data.get('specifications', ''))

    def validate(self):
        if not self.ui.txtMachineName.text().strip():
            show_error(self, "Validation Error", "Please enter machine name")
            return False

        return True

    def get_data(self):
        return {
            'machine_name': self.ui.txtMachineName.text().strip(),
            'machine_type': self.ui.txtMachineType.text().strip(),
            'model': self.ui.txtModel.text().strip(),
            'status': self.ui.cmbStatus.currentText(),
            'last_maintenance': self.ui.dateLastMaintenance.date().toString('yyyy-MM-dd'),
            'next_maintenance': self.ui.dateNextMaintenance.date().toString('yyyy-MM-dd'),
            'specifications': self.ui.txtSpecifications.toPlainText().strip(),
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }


class MachinesWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MachinesWidget()
        self.ui.setupUi(self)

        self.current_machine_id = None

        self.setup_table()
        self.setup_connections()

        # Set initial button states
        self.ui.btnEditMachine.setEnabled(False)
        self.ui.btnDeleteMachine.setEnabled(False)
        if hasattr(self.ui, 'btnMaintenance'):
            self.ui.btnMaintenance.setEnabled(False)

        self.load_machines()

    def setup_table(self):
        self.ui.tableMachines.setColumnWidth(0, 100)
        self.ui.tableMachines.setColumnWidth(1, 150)
        self.ui.tableMachines.setColumnWidth(2, 120)
        self.ui.tableMachines.setColumnWidth(3, 120)
        self.ui.tableMachines.setColumnWidth(4, 100)
        self.ui.tableMachines.setColumnWidth(5, 120)
        self.ui.tableMachines.setColumnWidth(6, 120)

        header = self.ui.tableMachines.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        self.ui.tableMachines.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tableMachines.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    def setup_connections(self):
        self.ui.btnAddMachine.clicked.connect(self.add_machine)
        self.ui.btnEditMachine.clicked.connect(self.edit_machine)
        self.ui.btnDeleteMachine.clicked.connect(self.delete_machine)
        if hasattr(self.ui, 'btnMaintenance'):
            self.ui.btnMaintenance.clicked.connect(self.schedule_maintenance)
        self.ui.btnRefresh.clicked.connect(self.load_machines)
        if hasattr(self.ui, 'txtSearch'):
            self.ui.txtSearch.textChanged.connect(self.search_machines)
        if hasattr(self.ui, 'cmbFilterStatus'):
            self.ui.cmbFilterStatus.currentTextChanged.connect(self.filter_machines)
        self.ui.tableMachines.itemSelectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self):
        selected_items = self.ui.tableMachines.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            self.current_machine_id = self.ui.tableMachines.item(row, 0).text()
            self.ui.btnEditMachine.setEnabled(True)
            self.ui.btnDeleteMachine.setEnabled(True)
            if hasattr(self.ui, 'btnMaintenance'):
                self.ui.btnMaintenance.setEnabled(True)
        else:
            self.current_machine_id = None
            self.ui.btnEditMachine.setEnabled(False)
            self.ui.btnDeleteMachine.setEnabled(False)
            if hasattr(self.ui, 'btnMaintenance'):
                self.ui.btnMaintenance.setEnabled(False)

    def load_machines(self):
        self.ui.tableMachines.setRowCount(0)

        # Fetch from Firebase (Cloud-only)
        machines = cloud_first_db.get_all_machines()

        for machine in machines:
            self.add_machine_to_table(machine)

        self.ui.lblTotalMachines.setText(f"Total: {len(machines)} machines")

    def add_machine_to_table(self, machine):
        row = self.ui.tableMachines.rowCount()
        self.ui.tableMachines.insertRow(row)

        self.ui.tableMachines.setItem(row, 0, QTableWidgetItem(machine['id']))
        self.ui.tableMachines.setItem(row, 1, QTableWidgetItem(machine['machine_name']))
        self.ui.tableMachines.setItem(row, 2, QTableWidgetItem(machine['machine_type'] or ''))
        self.ui.tableMachines.setItem(row, 3, QTableWidgetItem(machine['model'] or ''))

        status_item = QTableWidgetItem(machine['status'] or 'Available')
        if machine['status'] == 'Available':
            status_item.setForeground(Qt.GlobalColor.darkGreen)
        elif machine['status'] == 'In Use':
            status_item.setForeground(Qt.GlobalColor.blue)
        elif machine['status'] == 'Maintenance':
            status_item.setForeground(Qt.GlobalColor.darkYellow)
        elif machine['status'] == 'Out of Service':
            status_item.setForeground(Qt.GlobalColor.red)

        self.ui.tableMachines.setItem(row, 4, status_item)
        self.ui.tableMachines.setItem(row, 5, QTableWidgetItem(machine['last_maintenance'] or ''))
        self.ui.tableMachines.setItem(row, 6, QTableWidgetItem(machine['next_maintenance'] or ''))

    def add_machine(self):
        dialog = MachineDialog(self)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()
            machine_id = f"MCH{datetime.now().strftime('%Y%m%d%H%M%S')}"

            if cloud_first_db.create_machine(machine_id, data):
                show_success(self, "Success", "Machine added successfully")
                self.load_machines()
            else:
                show_error(self, "Error", "Failed to add machine")

    def edit_machine(self):
        if not self.current_machine_id:
            show_warning(self, "No Selection", "Please select a machine to edit")
            return

        machine = cloud_first_db.get_machine(self.current_machine_id)
        if not machine:
            show_error(self, "Error", "Machine not found")
            return

        dialog = MachineDialog(self, machine)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()

            if cloud_first_db.update_machine(self.current_machine_id, data):
                show_success(self, "Success", "Machine updated successfully")
                self.load_machines()
            else:
                show_error(self, "Error", "Failed to update machine")

    def delete_machine(self):
        if not self.current_machine_id:
            show_warning(self, "No Selection", "Please select a machine to delete")
            return

        reply = QMessageBox.question(
            self, "Confirm Delete",
            "Are you sure you want to delete this machine?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            if cloud_first_db.delete_machine(self.current_machine_id):
                show_success(self, "Success", "Machine deleted successfully")
                self.current_machine_id = None
                self.load_machines()
            else:
                show_error(self, "Error", "Failed to delete machine")

    def schedule_maintenance(self):
        """Schedule maintenance for selected machine"""
        if not self.current_machine_id:
            show_warning(self, "No Selection", "Please select a machine for maintenance")
            return

        machine = cloud_first_db.get_machine(self.current_machine_id)
        if not machine:
            show_error(self, "Error", "Machine not found")
            return

        reply = QMessageBox.question(
            self, "Schedule Maintenance",
            f"Mark '{machine['machine_name']}' as under maintenance?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            from datetime import timedelta

            update_data = {
                'status': 'Maintenance',
                'last_maintenance': datetime.now().strftime('%Y-%m-%d'),
                'next_maintenance': (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d')
            }

            if cloud_first_db.update_machine(self.current_machine_id, update_data):
                show_success(self, "Success", "Maintenance scheduled successfully")

                self.load_machines()
            else:
                show_error(self, "Error", "Failed to schedule maintenance")

    def search_machines(self, text):
        for row in range(self.ui.tableMachines.rowCount()):
            match = False
            for col in range(self.ui.tableMachines.columnCount()):
                item = self.ui.tableMachines.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.ui.tableMachines.setRowHidden(row, not match)

    def filter_machines(self, status):
        if status == "All":
            for row in range(self.ui.tableMachines.rowCount()):
                self.ui.tableMachines.setRowHidden(row, False)
        else:
            for row in range(self.ui.tableMachines.rowCount()):
                status_item = self.ui.tableMachines.item(row, 4)
                if status_item:
                    self.ui.tableMachines.setRowHidden(row, status_item.text() != status)

