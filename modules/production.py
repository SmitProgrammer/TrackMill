from datetime import datetime
from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt

from ui_compiled.production_ui import Ui_ProductionWidget
from ui_compiled.jobcard_dialog_ui import Ui_JobCardDialog
from database import cloud_first_db
from utils import show_error, show_success, show_warning, session


class JobCardDialog(QDialog):

    def __init__(self, parent=None, job_data=None):
        super().__init__(parent)
        self.ui = Ui_JobCardDialog()
        self.ui.setupUi(self)

        self.job_data = job_data
        self.setWindowTitle("Edit Job Card" if job_data else "Create New Job Card")

        self.load_orders()
        self.load_machines()
        self.load_operators()

        if job_data:
            self.populate_data()

        self.ui.btnSave.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

    def load_orders(self):
        self.ui.cmbOrder.clear()
        self.ui.cmbOrder.addItem("-- Select Order --", None)

        # Firebase-only: get all orders and filter
        all_orders = cloud_first_db.get_all_orders()
        orders = [o for o in all_orders if o.get('status') != 'Completed']
        for order in orders:
            self.ui.cmbOrder.addItem(f"{order['id']} - {order['product_name']}", order['id'])

    def load_machines(self):
        self.ui.cmbMachine.clear()
        self.ui.cmbMachine.addItem("-- Select Machine --", None)

        # Firebase-only: get all machines and filter
        all_machines = cloud_first_db.get_all_machines()
        machines = [m for m in all_machines if m.get('status') == 'Available']
        for machine in machines:
            self.ui.cmbMachine.addItem(machine['machine_name'], machine['id'])

    def load_operators(self):
        self.ui.cmbOperator.clear()
        self.ui.cmbOperator.addItem("-- Select Operator --", None)

        # Firebase-only: get all employees and filter
        all_employees = cloud_first_db.get_all_employees()
        operators = [e for e in all_employees if e.get('role') == 'Operator' and e.get('status') == 'Active']
        for operator in operators:
            self.ui.cmbOperator.addItem(operator['name'], operator['id'])

    def populate_data(self):
        if not self.job_data:
            return

        for i in range(self.ui.cmbOrder.count()):
            if self.ui.cmbOrder.itemData(i) == self.job_data['order_id']:
                self.ui.cmbOrder.setCurrentIndex(i)
                break

        self.ui.txtProductName.setText(self.job_data.get('product_name', ''))

        for i in range(self.ui.cmbMachine.count()):
            if self.ui.cmbMachine.itemData(i) == self.job_data['machine_id']:
                self.ui.cmbMachine.setCurrentIndex(i)
                break

        for i in range(self.ui.cmbOperator.count()):
            if self.ui.cmbOperator.itemData(i) == self.job_data['operator_id']:
                self.ui.cmbOperator.setCurrentIndex(i)
                break

        if self.job_data.get('start_time'):
            start_time = datetime.strptime(self.job_data['start_time'], '%Y-%m-%d %H:%M:%S')
            self.ui.dateTimeStart.setDateTime(start_time)

        if self.job_data.get('end_time'):
            end_time = datetime.strptime(self.job_data['end_time'], '%Y-%m-%d %H:%M:%S')
            self.ui.dateTimeEnd.setDateTime(end_time)

        status = self.job_data.get('status', 'Pending')
        self.ui.cmbStatus.setCurrentText(status)

        self.ui.txtMaterialUsed.setPlainText(self.job_data.get('material_used', ''))

    def validate(self):
        if self.ui.cmbOrder.currentIndex() == 0:
            show_error(self, "Validation Error", "Please select an order")
            return False

        if not self.ui.txtProductName.text().strip():
            show_error(self, "Validation Error", "Please enter product name")
            return False

        if self.ui.cmbMachine.currentIndex() == 0:
            show_error(self, "Validation Error", "Please select a machine")
            return False

        if self.ui.cmbOperator.currentIndex() == 0:
            show_error(self, "Validation Error", "Please select an operator")
            return False

        return True

    def get_data(self):
        order_id = self.ui.cmbOrder.currentData()
        machine_id = self.ui.cmbMachine.currentData()
        machine_name = self.ui.cmbMachine.currentText()
        operator_id = self.ui.cmbOperator.currentData()
        operator_name = self.ui.cmbOperator.currentText()

        return {
            'order_id': order_id,
            'product_name': self.ui.txtProductName.text().strip(),
            'machine_id': machine_id,
            'machine_name': machine_name,
            'operator_id': operator_id,
            'operator_name': operator_name,
            'start_time': self.ui.dateTimeStart.dateTime().toString('yyyy-MM-dd HH:mm:ss'),
            'end_time': self.ui.dateTimeEnd.dateTime().toString('yyyy-MM-dd HH:mm:ss'),
            'status': self.ui.cmbStatus.currentText(),
            'material_used': self.ui.txtMaterialUsed.toPlainText().strip(),
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }


class ProductionWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ProductionWidget()
        self.ui.setupUi(self)

        self.current_job_id = None

        self.setup_table()
        self.setup_connections()

        # Set initial button states
        self.ui.btnEditJob.setEnabled(False)
        self.ui.btnDeleteJob.setEnabled(False)

        self.load_jobs()

    def setup_table(self):
        self.ui.tableJobs.setColumnWidth(0, 100)
        self.ui.tableJobs.setColumnWidth(1, 100)
        self.ui.tableJobs.setColumnWidth(2, 150)
        self.ui.tableJobs.setColumnWidth(3, 120)
        self.ui.tableJobs.setColumnWidth(4, 120)
        self.ui.tableJobs.setColumnWidth(5, 140)
        self.ui.tableJobs.setColumnWidth(6, 140)
        self.ui.tableJobs.setColumnWidth(7, 100)

        header = self.ui.tableJobs.horizontalHeader()
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        self.ui.tableJobs.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tableJobs.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    def setup_connections(self):
        self.ui.btnNewJob.clicked.connect(self.add_job)
        self.ui.btnEditJob.clicked.connect(self.edit_job)
        self.ui.btnDeleteJob.clicked.connect(self.delete_job)
        self.ui.btnRefresh.clicked.connect(self.load_jobs)
        if hasattr(self.ui, 'txtSearch'):
            self.ui.txtSearch.textChanged.connect(self.search_jobs)
        if hasattr(self.ui, 'cmbFilterStatus'):
            self.ui.cmbFilterStatus.currentTextChanged.connect(self.filter_jobs)
        self.ui.tableJobs.itemSelectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self):
        selected_items = self.ui.tableJobs.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            self.current_job_id = self.ui.tableJobs.item(row, 0).text()
            self.ui.btnEditJob.setEnabled(True)
            self.ui.btnDeleteJob.setEnabled(True)
        else:
            self.current_job_id = None
            self.ui.btnEditJob.setEnabled(False)
            self.ui.btnDeleteJob.setEnabled(False)

    def load_jobs(self):
        try:
            print("[PRODUCTION] Loading jobs from Firebase...")
            self.ui.tableJobs.setRowCount(0)

            # Fetch from Firebase (Cloud-only)
            jobs = cloud_first_db.get_all_jobs()
            print(f"[PRODUCTION] Jobs loaded: {len(jobs)}")

            if not jobs:
                print("[PRODUCTION] No jobs found in Firebase")
                self.ui.lblTotalJobs.setText("Total: 0 job cards")
                return

            for job in jobs:
                try:
                    self.add_job_to_table(job)
                except Exception as e:
                    print(f"[PRODUCTION] Error adding job to table: {e}")
                    continue

            self.ui.lblTotalJobs.setText(f"Total: {len(jobs)} job cards")
            print(f"[PRODUCTION] Successfully displayed {len(jobs)} jobs")
        except Exception as e:
            print(f"[PRODUCTION] Error loading jobs: {e}")
            from utils import show_error
            show_error(self, "Error", f"Failed to load jobs: {str(e)}")

    def add_job_to_table(self, job):
        row = self.ui.tableJobs.rowCount()
        self.ui.tableJobs.insertRow(row)

        self.ui.tableJobs.setItem(row, 0, QTableWidgetItem(str(job.get('id', ''))))
        self.ui.tableJobs.setItem(row, 1, QTableWidgetItem(str(job.get('order_id', '') or '')))
        self.ui.tableJobs.setItem(row, 2, QTableWidgetItem(str(job.get('product_name', ''))))
        self.ui.tableJobs.setItem(row, 3, QTableWidgetItem(str(job.get('machine_name', '') or '')))
        self.ui.tableJobs.setItem(row, 4, QTableWidgetItem(str(job.get('operator_name', '') or '')))
        self.ui.tableJobs.setItem(row, 5, QTableWidgetItem(str(job.get('start_time', '') or '')))
        self.ui.tableJobs.setItem(row, 6, QTableWidgetItem(str(job.get('end_time', '') or '')))

        status_item = QTableWidgetItem(str(job.get('status', 'Pending') or 'Pending'))
        if job.get('status') == 'Completed':
            status_item.setForeground(Qt.GlobalColor.darkGreen)
        elif job.get('status') == 'In Progress':
            status_item.setForeground(Qt.GlobalColor.blue)
        elif job.get('status') == 'Pending':
            status_item.setForeground(Qt.GlobalColor.darkYellow)

        self.ui.tableJobs.setItem(row, 7, status_item)

    def add_job(self):
        dialog = JobCardDialog(self)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()
            job_id = f"JOB{datetime.now().strftime('%Y%m%d%H%M%S')}"

            # Firebase-only: create job in cloud
            if cloud_first_db.create_job(job_id, data):
                show_success(self, "Success", "Job card created in Firebase")
            else:
                show_success(self, "Success", "Job card created")

            self.load_jobs()

    def edit_job(self):
        if not self.current_job_id:
            show_warning(self, "No Selection", "Please select a job card to edit")
            return

        # Firebase-only: get fresh job data from cloud
        job = cloud_first_db.get_job(self.current_job_id)
        if not job:
            show_error(self, "Error", "Job card not found")
            return

        dialog = JobCardDialog(self, job)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()

            # Firebase-only: update job in cloud
            if cloud_first_db.update_job(self.current_job_id, data):
                show_success(self, "Success", "Job card updated in Firebase")
            else:
                show_success(self, "Success", "Job card updated")

            self.load_jobs()

    def delete_job(self):
        if not self.current_job_id:
            show_warning(self, "No Selection", "Please select a job card to delete")
            return

        reply = QMessageBox.question(
            self, "Confirm Delete",
            "Are you sure you want to delete this job card?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # Firebase-only: delete job from cloud
            if cloud_first_db.delete_job(self.current_job_id):
                show_success(self, "Success", "Job card deleted from Firebase")
            else:
                show_success(self, "Success", "Job card deleted")

            self.current_job_id = None
            self.load_jobs()

    def search_jobs(self, text):
        for row in range(self.ui.tableJobs.rowCount()):
            match = False
            for col in range(self.ui.tableJobs.columnCount()):
                item = self.ui.tableJobs.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.ui.tableJobs.setRowHidden(row, not match)

    def filter_jobs(self, status):
        if status == "All":
            for row in range(self.ui.tableJobs.rowCount()):
                self.ui.tableJobs.setRowHidden(row, False)
        else:
            for row in range(self.ui.tableJobs.rowCount()):
                status_item = self.ui.tableJobs.item(row, 7)
                if status_item:
                    self.ui.tableJobs.setRowHidden(row, status_item.text() != status)
