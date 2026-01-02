from datetime import datetime
from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt

from ui_compiled.employees_ui import Ui_EmployeesWidget
from ui_compiled.employee_dialog_ui import Ui_EmployeeDialog
from database import cloud_first_db
from utils import show_error, show_success, show_warning, validate_email, session


class EmployeeDialog(QDialog):

    def __init__(self, parent=None, employee_data=None):
        super().__init__(parent)
        self.ui = Ui_EmployeeDialog()
        self.ui.setupUi(self)

        self.employee_data = employee_data
        self.setWindowTitle("Edit Employee" if employee_data else "Add New Employee")

        if employee_data:
            self.populate_data()
            if employee_data.get('has_login') == 1:
                self.ui.chkHasLogin.setEnabled(False)
                self.ui.txtEmail.setEnabled(False)

        self.ui.cmbRole.currentTextChanged.connect(self.on_role_changed)
        self.ui.chkHasLogin.stateChanged.connect(self.on_login_checkbox_changed)

        self.on_role_changed(self.ui.cmbRole.currentText())
        self.on_login_checkbox_changed()

        self.ui.btnSave.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

    def on_role_changed(self, role):
        if role == "Operator":
            self.ui.chkHasLogin.setEnabled(True)
        else:
            self.ui.chkHasLogin.setChecked(False)
            self.ui.chkHasLogin.setEnabled(False)

    def on_login_checkbox_changed(self):
        has_login = self.ui.chkHasLogin.isChecked()
        self.ui.txtEmail.setEnabled(has_login)
        self.ui.txtPassword.setEnabled(has_login)

        if not has_login:
            self.ui.txtEmail.clear()
            self.ui.txtPassword.clear()

    def populate_data(self):
        if not self.employee_data:
            return

        self.ui.txtName.setText(self.employee_data.get('name', ''))

        role = self.employee_data.get('role', 'Admin')
        self.ui.cmbRole.setCurrentText(role)

        self.ui.txtContact.setText(self.employee_data.get('contact', ''))
        self.ui.txtEmail.setText(self.employee_data.get('email', ''))
        self.ui.txtAddress.setPlainText(self.employee_data.get('address', ''))

        status = self.employee_data.get('status', 'Active')
        self.ui.cmbStatus.setCurrentText(status)

        has_login = self.employee_data.get('has_login', 0)
        self.ui.chkHasLogin.setChecked(has_login == 1)

    def validate(self):
        if not self.ui.txtName.text().strip():
            show_error(self, "Validation Error", "Please enter employee name")
            return False

        if self.ui.chkHasLogin.isChecked():
            email = self.ui.txtEmail.text().strip()
            password = self.ui.txtPassword.text().strip()

            if not email:
                show_error(self, "Validation Error", "Please enter email for login")
                return False

            if not validate_email(email):
                show_error(self, "Validation Error", "Please enter a valid email")
                return False

            if not self.employee_data and not password:
                show_error(self, "Validation Error", "Please enter password for login")
                return False

            if password and len(password) < 6:
                show_error(self, "Validation Error", "Password must be at least 6 characters")
                return False

        return True

    def get_data(self):
        data = {
            'name': self.ui.txtName.text().strip(),
            'role': self.ui.cmbRole.currentText(),
            'contact': self.ui.txtContact.text().strip(),
            'email': self.ui.txtEmail.text().strip() if self.ui.chkHasLogin.isChecked() else '',
            'address': self.ui.txtAddress.toPlainText().strip(),
            'status': self.ui.cmbStatus.currentText(),
            'has_login': 1 if self.ui.chkHasLogin.isChecked() else 0,
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        password = self.ui.txtPassword.text().strip()
        if password:
            data['password'] = password

        return data


class EmployeesWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_EmployeesWidget()
        self.ui.setupUi(self)

        self.current_employee_id = None

        self.setup_table()
        self.setup_connections()

        # Set initial button states
        self.ui.btnEditEmployee.setEnabled(False)
        self.ui.btnDeleteEmployee.setEnabled(False)
        if hasattr(self.ui, 'btnBlockUnblock'):
            self.ui.btnBlockUnblock.setEnabled(False)
        if hasattr(self.ui, 'btnCreateAccount'):
            self.ui.btnCreateAccount.setEnabled(False)

        self.load_employees()

    def setup_table(self):
        self.ui.tableEmployees.setColumnWidth(0, 100)
        self.ui.tableEmployees.setColumnWidth(1, 150)
        self.ui.tableEmployees.setColumnWidth(2, 100)
        self.ui.tableEmployees.setColumnWidth(3, 120)
        self.ui.tableEmployees.setColumnWidth(4, 180)
        self.ui.tableEmployees.setColumnWidth(5, 100)
        self.ui.tableEmployees.setColumnWidth(6, 100)

        header = self.ui.tableEmployees.horizontalHeader()
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

        self.ui.tableEmployees.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tableEmployees.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    def setup_connections(self):
        self.ui.btnAddEmployee.clicked.connect(self.add_employee)
        self.ui.btnEditEmployee.clicked.connect(self.edit_employee)
        self.ui.btnDeleteEmployee.clicked.connect(self.delete_employee)
        if hasattr(self.ui, 'btnBlockUnblock'):
            self.ui.btnBlockUnblock.clicked.connect(self.toggle_employee_status)
        if hasattr(self.ui, 'btnCreateAccount'):
            self.ui.btnCreateAccount.clicked.connect(self.create_login_account)
        self.ui.btnRefresh.clicked.connect(self.load_employees)
        if hasattr(self.ui, 'txtSearch'):
            self.ui.txtSearch.textChanged.connect(self.search_employees)
        if hasattr(self.ui, 'cmbFilterStatus'):
            self.ui.cmbFilterStatus.currentTextChanged.connect(self.filter_employees)
        self.ui.tableEmployees.itemSelectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self):
        selected_items = self.ui.tableEmployees.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            self.current_employee_id = self.ui.tableEmployees.item(row, 0).text()
            self.ui.btnEditEmployee.setEnabled(True)
            self.ui.btnDeleteEmployee.setEnabled(True)

            employee = cloud_first_db.get_employee(self.current_employee_id)
            if employee:
                if hasattr(self.ui, 'btnBlockUnblock'):
                    self.ui.btnBlockUnblock.setEnabled(True)
                    if employee.get('status') == 'Active':
                        self.ui.btnBlockUnblock.setText("Block Employee")
                    else:
                        self.ui.btnBlockUnblock.setText("Unblock Employee")

                if hasattr(self.ui, 'btnCreateAccount'):
                    # Enable create login only for operators without login
                    if employee.get('role') == 'Operator' and employee.get('has_login') == 0:
                        self.ui.btnCreateAccount.setEnabled(True)
                    else:
                        self.ui.btnCreateAccount.setEnabled(False)
        else:
            self.current_employee_id = None
            self.ui.btnEditEmployee.setEnabled(False)
            self.ui.btnDeleteEmployee.setEnabled(False)
            if hasattr(self.ui, 'btnBlockUnblock'):
                self.ui.btnBlockUnblock.setEnabled(False)
                self.ui.btnBlockUnblock.setText("Block/Unblock")
            if hasattr(self.ui, 'btnCreateAccount'):
                self.ui.btnCreateAccount.setEnabled(False)

    def load_employees(self):
        print("\n[EMPLOYEES] ========== REFRESH STARTED ==========")
        self.ui.tableEmployees.setRowCount(0)

        # Fetch from Firebase only (Cloud-first approach)
        print("[EMPLOYEES] Fetching employees from Firebase...")
        employees = cloud_first_db.get_all_employees()
        print(f"[EMPLOYEES] Firebase employees count: {len(employees)}")

        if not employees:
            print("[EMPLOYEES] No employees found in Firebase")
            self.ui.lblTotalEmployees.setText("Total: 0 employees")
            print("[EMPLOYEES] ========== REFRESH COMPLETED ==========\n")
            return

        # Show employees list
        employees_sorted = sorted(employees, key=lambda e: e.get('name', ''))
        print(f"[EMPLOYEES] Displaying {len(employees_sorted)} employees in UI")
        for employee in employees_sorted:
            self.add_employee_to_table(employee)
        self.ui.lblTotalEmployees.setText(f"Total: {len(employees_sorted)} employees")
        print("[EMPLOYEES] ========== REFRESH COMPLETED ==========\n")

    def add_employee_to_table(self, employee):
        row = self.ui.tableEmployees.rowCount()
        self.ui.tableEmployees.insertRow(row)

        self.ui.tableEmployees.setItem(row, 0, QTableWidgetItem(employee['id']))
        self.ui.tableEmployees.setItem(row, 1, QTableWidgetItem(employee['name']))
        self.ui.tableEmployees.setItem(row, 2, QTableWidgetItem(employee['role'] or ''))
        self.ui.tableEmployees.setItem(row, 3, QTableWidgetItem(employee['contact'] or ''))
        self.ui.tableEmployees.setItem(row, 4, QTableWidgetItem(employee['email'] or ''))

        has_login = "Yes" if employee['has_login'] == 1 else "No"
        self.ui.tableEmployees.setItem(row, 5, QTableWidgetItem(has_login))

        status_item = QTableWidgetItem(employee['status'] or 'Active')
        if employee['status'] == 'Active':
            status_item.setForeground(Qt.GlobalColor.darkGreen)
        else:
            status_item.setForeground(Qt.GlobalColor.red)

        self.ui.tableEmployees.setItem(row, 6, status_item)

    def add_employee(self):
        dialog = EmployeeDialog(self)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()
            employee_id = f"EMP{datetime.now().strftime('%Y%m%d%H%M%S')}"

            if data['has_login'] == 1 and data.get('password'):
                email = data['email']
                password = data.pop('password')

                success, user_data, error = firebase_db.create_user(email, password)

                if success:
                    uid = user_data.get('localId', '')
                    data['firebase_uid'] = uid

                    # Store user data in Firebase Realtime DB for mobile app
                    if firebase_db.firebase:
                        try:
                            firebase_db.db.child('users').child(uid).set({
                                'employee_id': employee_id,
                                'name': data['name'],
                                'role': data['role'],
                                'email': email,
                                'status': data['status'],
                                'created_at': data.get('created_at')
                            })
                            print(f"User data stored in Firebase for {email}")
                        except Exception as e:
                            print(f"Error storing user data in Firebase: {e}")
                else:
                    show_error(self, "Firebase Error", f"Failed to create login: {error}")
                    return

            if cloud_first_db.create_employee(employee_id, data):
                show_success(self, "Success", "Employee added successfully")

                self.load_employees()
            else:
                show_error(self, "Error", "Failed to add employee")

    def edit_employee(self):
        if not self.current_employee_id:
            show_warning(self, "No Selection", "Please select an employee to edit")
            return

        # Fetch from cloud
        employee = cloud_first_db.get_employee(self.current_employee_id)
        if not employee:
            show_error(self, "Error", "Employee not found")
            return

        dialog = EmployeeDialog(self, employee)

        if dialog.exec() == QDialog.Accepted:
            if not dialog.validate():
                return

            data = dialog.get_data()

            # Update cloud only
            if cloud_first_db.update_employee(self.current_employee_id, data):
                show_success(self, "Success", "Employee updated successfully")

                self.load_employees()
            else:
                show_error(self, "Error", "Failed to update employee")

    def delete_employee(self):
        if not self.current_employee_id:
            show_warning(self, "No Selection", "Please select an employee to delete")
            return

        reply = QMessageBox.question(
            self, "Confirm Delete",
            "Are you sure you want to delete this employee?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            if cloud_first_db.delete_employee(self.current_employee_id):
                show_success(self, "Success", "Employee deleted successfully")

                self.current_employee_id = None
                self.load_employees()
            else:
                show_error(self, "Error", "Failed to delete employee")

    def toggle_employee_status(self):
        if not self.current_employee_id:
            show_warning(self, "No Selection", "Please select an employee to block/unblock")
            return

        employee = cloud_first_db.get_employee(self.current_employee_id)
        if not employee:
            show_error(self, "Error", "Employee not found")
            return

        new_status = 'Blocked' if employee['status'] == 'Active' else 'Active'

        data = {
            'status': new_status
        }

        # Update cloud
        if cloud_first_db.update_employee(self.current_employee_id, data):
            action = "blocked" if new_status == 'Blocked' else "unblocked"
            show_success(self, "Success", f"Employee {action} successfully")

            if employee.get('has_login') == 1 and employee.get('firebase_uid'):
                # Update Firebase Auth status
                firebase_db.update_user_status(employee['firebase_uid'], new_status == 'Active')

                # Update Firebase Realtime DB status for mobile app
                if firebase_db.firebase:
                    try:
                        firebase_db.db.child('users').child(employee['firebase_uid']).update({
                            'status': new_status,
                            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        })
                        print(f"User status updated in Firebase: {new_status}")
                    except Exception as e:
                        print(f"Error updating user status in Firebase: {e}")

            self.load_employees()
        else:
            show_error(self, "Error", "Failed to update employee status")

    def create_login_account(self):
        """Create login account for selected operator employee"""
        if not self.current_employee_id:
            show_warning(self, "No Selection", "Please select an employee to create login")
            return

        employee = cloud_first_db.get_employee(self.current_employee_id)
        if not employee:
            show_error(self, "Error", "Employee not found")
            return

        if employee.get('role') != 'Operator':
            show_error(self, "Error", "Only operators can have login accounts")
            return

        if employee.get('has_login') == 1:
            show_warning(self, "Already Exists", "This employee already has a login account")
            return

        # Prompt for email and password
        from PySide6.QtWidgets import QInputDialog, QLineEdit

        email, ok = QInputDialog.getText(self, "Create Login", "Enter email:", QLineEdit.Normal, "")
        if not ok or not email.strip():
            return

        if not validate_email(email.strip()):
            show_error(self, "Invalid Email", "Please enter a valid email address")
            return

        password, ok = QInputDialog.getText(self, "Create Login", "Enter password (min 6 chars):", QLineEdit.Password, "")
        if not ok or not password.strip():
            return

        if len(password.strip()) < 6:
            show_error(self, "Invalid Password", "Password must be at least 6 characters")
            return

        # Create Firebase account
        success, user_data, error = firebase_db.create_user(email.strip(), password.strip())

        if success:
            uid = user_data.get('localId', '')

            update_data = {
                'email': email.strip(),
                'has_login': 1,
                'firebase_uid': uid
            }

            if cloud_first_db.update_employee(self.current_employee_id, update_data):
                # Store user data in Firebase Realtime DB for mobile app
                if firebase_db.firebase:
                    try:
                        firebase_db.db.child('users').child(uid).set({
                            'employee_id': self.current_employee_id,
                            'name': employee.get('name'),
                            'role': employee.get('role'),
                            'email': email.strip(),
                            'status': employee.get('status'),
                            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        })
                    except Exception as e:
                        print(f"Error storing user data in Firebase: {e}")

                show_success(self, "Success", "Login account created successfully")


                self.load_employees()
            else:
                show_error(self, "Error", "Failed to update employee record")
        else:
            show_error(self, "Firebase Error", f"Failed to create login: {error}")

    def search_employees(self, text):
        for row in range(self.ui.tableEmployees.rowCount()):
            match = False
            for col in range(self.ui.tableEmployees.columnCount()):
                item = self.ui.tableEmployees.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.ui.tableEmployees.setRowHidden(row, not match)

    def filter_employees(self, status):
        if status == "All Employees" or status == "All":
            for row in range(self.ui.tableEmployees.rowCount()):
                self.ui.tableEmployees.setRowHidden(row, False)
        else:
            for row in range(self.ui.tableEmployees.rowCount()):
                status_item = self.ui.tableEmployees.item(row, 6)
                if status_item:
                    self.ui.tableEmployees.setRowHidden(row, status_item.text() != status)
