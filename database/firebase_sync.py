"""
Firebase Sync Service
Syncs SQLite data to Firebase for mobile app access
"""

import threading
import time
from datetime import datetime
from database import sqlite_db, firebase_db


class FirebaseSyncService:
    def __init__(self, sync_interval=60):
        self.sync_interval = sync_interval
        self.running = False
        self.thread = None

    def start(self):
        """Start the sync service"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._sync_loop, daemon=True)
            self.thread.start()
            print("Firebase sync service started")

    def stop(self):
        """Stop the sync service"""
        self.running = False
        if self.thread:
            self.thread.join()
            print("Firebase sync service stopped")

    def _sync_loop(self):
        """Main sync loop"""
        while self.running:
            try:
                self.sync_all_data()
            except Exception as e:
                print(f"Sync error: {e}")
            time.sleep(self.sync_interval)

    def sync_all_data(self):
        """Sync all tables to Firebase"""
        print(f"[SYNC] Syncing data to Firebase... {datetime.now().strftime('%H:%M:%S')}")

        try:
            self.sync_jobs()
            self.sync_orders()
            self.sync_machines()
            self.sync_materials()
            self.sync_employees()
            print("[SYNC] Sync completed successfully")
        except Exception as e:
            print(f"[SYNC] Error during sync: {e}")

    def sync_jobs(self):
        """Sync jobs to Firebase"""
        jobs = sqlite_db.fetch_all("SELECT * FROM jobs")

        for job in jobs:
            job_dict = dict(job)
            try:
                firebase_db.db.child('jobs').child(job['id']).set(job_dict)
            except Exception as e:
                print(f"[SYNC] Error syncing job {job['id']}: {e}")

    def sync_orders(self):
        """Sync orders to Firebase"""
        orders = sqlite_db.fetch_all("SELECT * FROM orders")

        for order in orders:
            order_dict = dict(order)
            try:
                firebase_db.db.child('orders').child(order['id']).set(order_dict)
            except Exception as e:
                print(f"[SYNC] Error syncing order {order['id']}: {e}")

    def sync_machines(self):
        """Sync machines to Firebase"""
        machines = sqlite_db.fetch_all("SELECT * FROM machines")

        for machine in machines:
            machine_dict = dict(machine)
            try:
                firebase_db.db.child('machines').child(machine['id']).set(machine_dict)
            except Exception as e:
                print(f"[SYNC] Error syncing machine {machine['id']}: {e}")

    def sync_materials(self):
        """Sync materials to Firebase"""
        materials = sqlite_db.fetch_all("SELECT * FROM inventory")

        for material in materials:
            material_dict = dict(material)
            try:
                firebase_db.db.child('materials').child(material['id']).set(material_dict)
            except Exception as e:
                print(f"[SYNC] Error syncing material {material['id']}: {e}")

    def sync_employees(self):
        """Sync employees to Firebase (operators only)"""
        employees = sqlite_db.fetch_all(
            "SELECT * FROM employees WHERE role = 'Operator'"
        )

        for emp in employees:
            if emp['firebase_uid']:
                user_data = {
                    'employee_id': emp['id'],
                    'name': emp['name'],
                    'role': emp['role'],
                    'email': emp['email'],
                    'status': emp['status'],
                    'created_at': emp['created_at']
                }
                try:
                    firebase_db.db.child('users').child(emp['firebase_uid']).set(user_data)
                except Exception as e:
                    print(f"[SYNC] Error syncing employee {emp['id']}: {e}")

    def sync_single_job(self, job_id):
        """Sync a single job immediately"""
        job = sqlite_db.fetch_one("SELECT * FROM jobs WHERE id = ?", (job_id,))
        if job:
            job_dict = dict(job)
            try:
                firebase_db.db.child('jobs').child(job_id).set(job_dict)
                print(f"[SYNC] Job {job_id} synced to Firebase")
            except Exception as e:
                print(f"[SYNC] Error syncing job {job_id}: {e}")

    def sync_single_order(self, order_id):
        """Sync a single order immediately"""
        order = sqlite_db.fetch_one("SELECT * FROM orders WHERE id = ?", (order_id,))
        if order:
            order_dict = dict(order)
            try:
                firebase_db.db.child('orders').child(order_id).set(order_dict)
                print(f"[SYNC] Order {order_id} synced to Firebase")
            except Exception as e:
                print(f"[SYNC] Error syncing order {order_id}: {e}")

    def sync_single_employee(self, employee_id):
        """Sync a single employee immediately"""
        emp = sqlite_db.fetch_one("SELECT * FROM employees WHERE id = ?", (employee_id,))
        if emp and emp['firebase_uid']:
            user_data = {
                'employee_id': emp['id'],
                'name': emp['name'],
                'role': emp['role'],
                'email': emp['email'],
                'status': emp['status'],
                'created_at': emp['created_at']
            }
            try:
                firebase_db.db.child('users').child(emp['firebase_uid']).set(user_data)
                print(f"[SYNC] Employee {employee_id} synced to Firebase")
            except Exception as e:
                print(f"[SYNC] Error syncing employee {employee_id}: {e}")


sync_service = FirebaseSyncService()

