"""
SQLite database handler
"""

import sqlite3
import os
from datetime import datetime


class SQLiteDB:

    def __init__(self, db_path="data/cnc_erp.db"):
        """Initialize database connection"""
        self.db_path = db_path
        self.connection = None
        self.cursor = None
        self.ensure_db_directory()
        self.connect()
        self.create_tables()

    def ensure_db_directory(self):
        """Ensure database directory exists"""
        db_dir = os.path.dirname(self.db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)

    def connect(self):
        """Connect to SQLite database"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
            print(f"SQLite database connected: {self.db_path}")
            return True
        except Exception as e:
            print(f"SQLite connection error: {e}")
            return False

    def create_tables(self):
        """Create all required tables"""
        try:
            # Customers table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    contact TEXT,
                    email TEXT,
                    company TEXT,
                    address TEXT,
                    created_at TEXT,
                    updated_at TEXT
                )
            ''')

            # Orders table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS orders (
                    id TEXT PRIMARY KEY,
                    customer_id TEXT,
                    customer_name TEXT,
                    product_name TEXT NOT NULL,
                    quantity INTEGER,
                    specifications TEXT,
                    order_date TEXT,
                    delivery_date TEXT,
                    priority TEXT,
                    status TEXT,
                    created_at TEXT,
                    updated_at TEXT,
                    FOREIGN KEY (customer_id) REFERENCES customers (id)
                )
            ''')

            # Inventory/Materials table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS inventory (
                    id TEXT PRIMARY KEY,
                    material_name TEXT NOT NULL,
                    material_type TEXT,
                    current_stock REAL,
                    unit TEXT,
                    min_stock REAL,
                    supplier TEXT,
                    status TEXT,
                    created_at TEXT,
                    updated_at TEXT
                )
            ''')

            # Machines table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS machines (
                    id TEXT PRIMARY KEY,
                    machine_name TEXT NOT NULL,
                    machine_type TEXT,
                    model TEXT,
                    status TEXT,
                    last_maintenance TEXT,
                    next_maintenance TEXT,
                    specifications TEXT,
                    created_at TEXT,
                    updated_at TEXT
                )
            ''')

            # Employees table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS employees (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    role TEXT,
                    contact TEXT,
                    email TEXT,
                    address TEXT,
                    has_login INTEGER DEFAULT 0,
                    firebase_uid TEXT,
                    status TEXT DEFAULT 'Active',
                    created_at TEXT,
                    updated_at TEXT
                )
            ''')

            # Jobs/Production table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS jobs (
                    id TEXT PRIMARY KEY,
                    order_id TEXT,
                    product_name TEXT,
                    machine_id TEXT,
                    machine_name TEXT,
                    operator_id TEXT,
                    operator_name TEXT,
                    start_time TEXT,
                    end_time TEXT,
                    status TEXT,
                    material_used TEXT,
                    created_at TEXT,
                    updated_at TEXT,
                    FOREIGN KEY (order_id) REFERENCES orders (id),
                    FOREIGN KEY (machine_id) REFERENCES machines (id),
                    FOREIGN KEY (operator_id) REFERENCES employees (id)
                )
            ''')

            # Maintenance logs table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS maintenance (
                    id TEXT PRIMARY KEY,
                    machine_id TEXT,
                    machine_name TEXT,
                    maintenance_type TEXT,
                    maintenance_date TEXT,
                    performed_by TEXT,
                    notes TEXT,
                    cost REAL,
                    created_at TEXT,
                    FOREIGN KEY (machine_id) REFERENCES machines (id)
                )
            ''')

            # Activity logs table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS activity_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_email TEXT,
                    action TEXT,
                    module TEXT,
                    details TEXT,
                    timestamp TEXT
                )
            ''')

            # Settings table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value TEXT
                )
            ''')

            self.connection.commit()
            print("SQLite tables created/verified")
            return True

        except Exception as e:
            print(f"Error creating tables: {e}")
            return False

    def execute(self, query, params=None):
        """Execute a query"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f" Query execution error: {e}")
            return False

    def fetch_one(self, query, params=None):
        """Fetch one row"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            row = self.cursor.fetchone()
            if row:
                return dict(row)
            return None
        except Exception as e:
            print(f" Fetch one error: {e}")
            return None

    def fetch_all(self, query, params=None):
        """Fetch all rows"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            print(f" Fetch all error: {e}")
            return []

    def insert(self, table, data):
        """Insert data into table"""
        try:
            data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            columns = ', '.join(data.keys())
            placeholders = ', '.join(['?' for _ in data])
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

            self.cursor.execute(query, list(data.values()))
            self.connection.commit()
            return True
        except Exception as e:
            print(f" Insert error: {e}")
            return False

    def update(self, table, data, where_clause, where_params=None):
        """Update data in table"""
        try:
            data['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
            query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"

            params = list(data.values())
            if where_params:
                params.extend(where_params)

            self.cursor.execute(query, params)
            self.connection.commit()
            return True
        except Exception as e:
            print(f" Update error: {e}")
            return False

    def delete(self, table, where_clause, where_params=None):
        """Delete data from table"""
        try:
            query = f"DELETE FROM {table} WHERE {where_clause}"
            if where_params:
                self.cursor.execute(query, where_params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f" Delete error: {e}")
            return False

    def count(self, table, where_clause=None, where_params=None):
        """Count rows in table"""
        try:
            query = f"SELECT COUNT(*) as count FROM {table}"
            if where_clause:
                query += f" WHERE {where_clause}"

            if where_params:
                self.cursor.execute(query, where_params)
            else:
                self.cursor.execute(query)

            result = self.cursor.fetchone()
            return result['count'] if result else 0
        except Exception as e:
            print(f" Count error: {e}")
            return 0

    def log_activity(self, user_email, action, module, details=""):
        """Log user activity"""
        try:
            query = '''
                INSERT INTO activity_logs (user_email, action, module, details, timestamp)
                VALUES (?, ?, ?, ?, ?)
            '''
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute(query, (user_email, action, module, details, timestamp))
            self.connection.commit()
            return True
        except Exception as e:
            print(f" Log activity error: {e}")
            return False

    def get_recent_activities(self, limit=10):
        """Get recent activity logs"""
        query = f'''
            SELECT * FROM activity_logs 
            ORDER BY timestamp DESC 
            LIMIT {limit}
        '''
        return self.fetch_all(query)

    def get_setting(self, key, default=None):
        """Get setting value"""
        result = self.fetch_one("SELECT value FROM settings WHERE key = ?", (key,))
        if result:
            return result['value']
        return default

    def set_setting(self, key, value):
        """Set setting value"""
        existing = self.get_setting(key)
        if existing is not None:
            return self.execute("UPDATE settings SET value = ? WHERE key = ?", (value, key))
        else:
            return self.execute("INSERT INTO settings (key, value) VALUES (?, ?)", (key, value))

    def clear_all_data(self):
        """Clear all data from tables (for testing)"""
        tables = ['customers', 'orders', 'inventory', 'machines', 'employees', 'jobs', 'maintenance', 'activity_logs']
        try:
            for table in tables:
                self.cursor.execute(f"DELETE FROM {table}")
            self.connection.commit()
            print(" All data cleared")
            return True
        except Exception as e:
            print(f" Clear data error: {e}")
            return False

    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print(" SQLite connection closed")


# Create singleton instance
sqlite_db = SQLiteDB()

