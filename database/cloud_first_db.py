"""
Firebase-Only Database Handler
All operations use Firebase exclusively - No SQLite
Firebase is the single source of truth
"""

from datetime import datetime
from database import firebase_db


class CloudFirstDB:
    """
    Database access layer that uses Firebase as the only data source.
    All read and write operations exclusively use Firebase.
    No local SQLite backup or fallback - pure cloud-only approach.
    """

    def __init__(self):
        self.firebase = firebase_db
        self.use_firebase = firebase_db.firebase is not None
        if not self.use_firebase:
            print("[DB] WARNING: Firebase not available! App will not work properly.")

    # ==================== CUSTOMERS ====================

    def get_all_customers(self):
        """Get all customers from Firebase"""
        try:
            success, data, error = self.firebase.get_all('customers')
            if success and data:
                print(f"[DB] Loaded {len(data)} customers from Firebase")
                return data
            elif success and not data:
                print("[DB] No customers in Firebase")
                return []
            else:
                print(f"[DB] Firebase error getting customers: {error}")
                return []
        except Exception as e:
            print(f"[DB] Firebase exception getting customers: {e}")
            return []

    def get_customer(self, customer_id):
        """Get single customer from Firebase"""
        try:
            success, data, error = self.firebase.get(f'customers/{customer_id}')
            if success and data:
                data['id'] = customer_id
                return data
            else:
                print(f"[DB] Firebase error getting customer {customer_id}: {error}")
                return None
        except Exception as e:
            print(f"[DB] Firebase exception getting customer {customer_id}: {e}")
            return None

    def create_customer(self, customer_id, data):
        """Create customer in Firebase"""
        data['id'] = customer_id
        data['created_at'] = datetime.now().isoformat()
        data['updated_at'] = datetime.now().isoformat()

        try:
            success, error = self.firebase.set(f'customers/{customer_id}', data)
            if success:
                print(f"[DB] Customer {customer_id} created in Firebase")
                return True
            else:
                print(f"[DB] Firebase error creating customer: {error}")
                return False
        except Exception as e:
            print(f"[DB] Firebase exception creating customer: {e}")
            return False

    def update_customer(self, customer_id, data):
        """Update customer in Firebase"""
        data['updated_at'] = datetime.now().isoformat()

        try:
            success, error = self.firebase.update(f'customers/{customer_id}', data)
            if success:
                print(f"[DB] Customer {customer_id} updated in Firebase")
                return True
            else:
                print(f"[DB] Firebase error updating customer: {error}")
                return False
        except Exception as e:
            print(f"[DB] Firebase exception updating customer: {e}")
            return False

    def delete_customer(self, customer_id):
        """Delete customer from Firebase"""
        try:
            success, error = self.firebase.delete(f'customers/{customer_id}')
            if success:
                print(f"[DB] Customer {customer_id} deleted from Firebase")
                return True
            else:
                print(f"[DB] Firebase error deleting customer: {error}")
                return False
        except Exception as e:
            print(f"[DB] Firebase exception deleting customer: {e}")
            return False

    # ==================== ORDERS ====================

    def get_all_orders(self):
        """Get all orders from Firebase"""
        try:
            success, data, error = self.firebase.get_all('orders')
            if success and data:
                print(f"[DB] Loaded {len(data)} orders from Firebase")
                return data
            elif success and not data:
                print("[DB] No orders in Firebase")
                return []
            else:
                print(f"[DB] Firebase error getting orders: {error}")
                return []
        except Exception as e:
            print(f"[DB] Firebase exception getting orders: {e}")
            return []

    def get_order(self, order_id):
        """Get single order from Firebase"""
        try:
            success, data, error = self.firebase.get(f'orders/{order_id}')
            if success and data:
                data['id'] = order_id
                return data
            else:
                print(f"[DB] Firebase error getting order {order_id}: {error}")
                return None
        except Exception as e:
            print(f"[DB] Firebase exception getting order {order_id}: {e}")
            return None

    def create_order(self, order_id, data):
        """Create order in Firebase"""
        data['id'] = order_id
        data['created_at'] = datetime.now().isoformat()
        data['updated_at'] = datetime.now().isoformat()

        try:
            success, error = self.firebase.set(f'orders/{order_id}', data)
            if success:
                print(f"[DB] Order {order_id} created in Firebase")
                return True
            else:
                print(f"[DB] Firebase error creating order: {error}")
                return False
        except Exception as e:
            print(f"[DB] Firebase exception creating order: {e}")
            return False

    def update_order(self, order_id, data):
        """Update order in Firebase"""
        data['updated_at'] = datetime.now().isoformat()

        try:
            success, error = self.firebase.update(f'orders/{order_id}', data)
            if success:
                print(f"[DB] Order {order_id} updated in Firebase")
                return True
            else:
                print(f"[DB] Firebase error updating order: {error}")
                return False
        except Exception as e:
            print(f"[DB] Firebase exception updating order: {e}")
            return False

    def delete_order(self, order_id):
        """Delete order from Firebase"""
        try:
            success, error = self.firebase.delete(f'orders/{order_id}')
            if success:
                print(f"[DB] Order {order_id} deleted from Firebase")
                return True
            else:
                print(f"[DB] Firebase error deleting order: {error}")
                return False
        except Exception as e:
            print(f"[DB] Firebase exception deleting order: {e}")
            return False

    # ==================== MACHINES ====================

    def get_all_machines(self):
        """Get all machines from Firebase"""
        try:
            success, data, error = self.firebase.get_all('machines')
            if success and data:
                print(f"[DB] Loaded {len(data)} machines from Firebase")
                return data
            elif success and not data:
                return []
        except Exception as e:
            print(f"[DB] Firebase error getting machines: {e}")
        return []

    def get_machine(self, machine_id):
        """Get single machine from Firebase"""
        try:
            success, data, error = self.firebase.get(f'machines/{machine_id}')
            if success and data:
                data['id'] = machine_id
                return data
        except Exception as e:
            print(f"[DB] Firebase error getting machine {machine_id}: {e}")
        return None

    def create_machine(self, machine_id, data):
        """Create machine in Firebase"""
        data['id'] = machine_id
        data['created_at'] = datetime.now().isoformat()
        data['updated_at'] = datetime.now().isoformat()

        try:
            success, error = self.firebase.set(f'machines/{machine_id}', data)
            if success:
                print(f"[DB] Machine {machine_id} created in Firebase")
                return True
        except Exception as e:
            print(f"[DB] Firebase exception creating machine: {e}")
        return False

    def update_machine(self, machine_id, data):
        """Update machine in Firebase"""
        data['updated_at'] = datetime.now().isoformat()

        try:
            success, error = self.firebase.update(f'machines/{machine_id}', data)
            if success:
                print(f"[DB] Machine {machine_id} updated in Firebase")
                return True
        except Exception as e:
            print(f"[DB] Firebase exception updating machine: {e}")
        return False

    def delete_machine(self, machine_id):
        """Delete machine from Firebase"""
        try:
            success, error = self.firebase.delete(f'machines/{machine_id}')
            if success:
                print(f"[DB] Machine {machine_id} deleted from Firebase")
                return True
        except Exception as e:
            print(f"[DB] Firebase exception deleting machine: {e}")
        return False

    # ==================== INVENTORY ====================

    def get_all_inventory(self):
        """Get all inventory from Firebase"""
        try:
            success, data, error = self.firebase.get_all('inventory')
            if success and data:
                print(f"[DB] Loaded {len(data)} inventory items from Firebase")
                # Ensure each item has an 'id' field
                for item in data:
                    if 'id' not in item:
                        print(f"[DB] WARNING: Inventory item missing 'id' field")
                return data
            elif success and not data:
                print("[DB] No inventory in Firebase")
                return []
            else:
                print(f"[DB] Firebase error getting inventory: {error}")
                return []
        except Exception as e:
            print(f"[DB] Firebase exception getting inventory: {e}")
            return []

    def get_inventory(self, inventory_id):
        """Get single inventory item from Firebase"""
        try:
            success, data, error = self.firebase.get(f'inventory/{inventory_id}')
            if success and data:
                data['id'] = inventory_id
                return data
        except Exception as e:
            print(f"[DB] Firebase error getting inventory {inventory_id}: {e}")
        return None

    def create_inventory(self, inventory_id, data):
        """Create inventory in Firebase"""
        data['id'] = inventory_id
        data['created_at'] = datetime.now().isoformat()
        data['updated_at'] = datetime.now().isoformat()

        try:
            success, error = self.firebase.set(f'inventory/{inventory_id}', data)
            if success:
                print(f"[DB] Inventory {inventory_id} created in Firebase")
                return True
        except Exception as e:
            print(f"[DB] Firebase exception creating inventory: {e}")
        return False

    def update_inventory(self, inventory_id, data):
        """Update inventory in Firebase"""
        data['updated_at'] = datetime.now().isoformat()

        try:
            success, error = self.firebase.update(f'inventory/{inventory_id}', data)
            if success:
                print(f"[DB] Inventory {inventory_id} updated in Firebase")
                return True
        except Exception as e:
            print(f"[DB] Firebase exception updating inventory: {e}")
        return False

    def delete_inventory(self, inventory_id):
        """Delete inventory from Firebase"""
        try:
            success, error = self.firebase.delete(f'inventory/{inventory_id}')
            if success:
                print(f"[DB] Inventory {inventory_id} deleted from Firebase")
                return True
        except Exception as e:
            print(f"[DB] Firebase exception deleting inventory: {e}")
        return False

    # ==================== EMPLOYEES ====================

    def get_all_employees(self):
        """Get all employees from Firebase"""
        try:
            success, data, error = self.firebase.get_all('employees')
            if success and data:
                print(f"[DB] Loaded {len(data)} employees from Firebase")
                return data
            elif success and not data:
                return []
        except Exception as e:
            print(f"[DB] Firebase error getting employees: {e}")
        return []

    def get_employee(self, employee_id):
        """Get single employee from Firebase"""
        try:
            success, data, error = self.firebase.get(f'employees/{employee_id}')
            if success and data:
                data['id'] = employee_id
                return data
        except Exception as e:
            print(f"[DB] Firebase error getting employee {employee_id}: {e}")
        return None

    def create_employee(self, employee_id, data):
        """Create employee in Firebase"""
        data['id'] = employee_id
        data['created_at'] = datetime.now().isoformat()
        data['updated_at'] = datetime.now().isoformat()

        try:
            success, error = self.firebase.set(f'employees/{employee_id}', data)
            if success:
                print(f"[DB] Employee {employee_id} created in Firebase")
                return True
        except Exception as e:
            print(f"[DB] Firebase exception creating employee: {e}")
        return False

    def update_employee(self, employee_id, data):
        """Update employee in Firebase"""
        data['updated_at'] = datetime.now().isoformat()

        try:
            success, error = self.firebase.update(f'employees/{employee_id}', data)
            if success:
                print(f"[DB] Employee {employee_id} updated in Firebase")
                return True
        except Exception as e:
            print(f"[DB] Firebase exception updating employee: {e}")
        return False

    def delete_employee(self, employee_id):
        """Delete employee from Firebase"""
        try:
            success, error = self.firebase.delete(f'employees/{employee_id}')
            if success:
                print(f"[DB] Employee {employee_id} deleted from Firebase")
                return True
        except Exception as e:
            print(f"[DB] Firebase exception deleting employee: {e}")
        return False

    # ==================== JOBS ====================

    def get_all_jobs(self):
        """Get all jobs from Firebase"""
        try:
            success, data, error = self.firebase.get_all('jobs')
            if success and data:
                print(f"[DB] Loaded {len(data)} jobs from Firebase")
                # Ensure each item has an 'id' field
                for item in data:
                    if 'id' not in item:
                        print(f"[DB] WARNING: Job item missing 'id' field")
                return data
            elif success and not data:
                print("[DB] No jobs in Firebase")
                return []
            else:
                print(f"[DB] Firebase error getting jobs: {error}")
                return []
        except Exception as e:
            print(f"[DB] Firebase exception getting jobs: {e}")
            return []

    def get_job(self, job_id):
        """Get single job from Firebase"""
        try:
            success, data, error = self.firebase.get(f'jobs/{job_id}')
            if success and data:
                data['id'] = job_id
                return data
        except Exception as e:
            print(f"[DB] Firebase error getting job {job_id}: {e}")
        return None

    def create_job(self, job_id, data):
        """Create job in Firebase"""
        data['id'] = job_id
        data['created_at'] = datetime.now().isoformat()
        data['updated_at'] = datetime.now().isoformat()

        try:
            success, error = self.firebase.set(f'jobs/{job_id}', data)
            if success:
                print(f"[DB] Job {job_id} created in Firebase")
                return True
        except Exception as e:
            print(f"[DB] Firebase exception creating job: {e}")
        return False

    def update_job(self, job_id, data):
        """Update job in Firebase"""
        data['updated_at'] = datetime.now().isoformat()

        try:
            success, error = self.firebase.update(f'jobs/{job_id}', data)
            if success:
                print(f"[DB] Job {job_id} updated in Firebase")
                return True
        except Exception as e:
            print(f"[DB] Firebase exception updating job: {e}")
        return False

    def delete_job(self, job_id):
        """Delete job from Firebase"""
        try:
            success, error = self.firebase.delete(f'jobs/{job_id}')
            if success:
                print(f"[DB] Job {job_id} deleted from Firebase")
                return True
        except Exception as e:
            print(f"[DB] Firebase exception deleting job: {e}")
        return False

    # ==================== MATERIALS (alias for inventory) ====================

    def get_all_materials(self):
        """Get all materials from inventory - alias method"""
        return self.get_all_inventory()

    def get_material(self, material_id):
        """Get single material from inventory - alias method"""
        return self.get_inventory(material_id)

    def create_material(self, material_id, data):
        """Create material in inventory - alias method"""
        return self.create_inventory(material_id, data)

    def update_material(self, material_id, data):
        """Update material in inventory - alias method"""
        return self.update_inventory(material_id, data)

    def delete_material(self, material_id):
        """Delete material from inventory - alias method"""
        return self.delete_inventory(material_id)


# Create singleton instance
cloud_first_db = CloudFirstDB()

