# Application Configuration Settings

# Application Info
APP_NAME = "CNC ERP System"
APP_VERSION = "1.0.0"

# Window Settings
WINDOW_TITLE = "ERP for CNC Industries"
WINDOW_MIN_WIDTH = 1200
WINDOW_MIN_HEIGHT = 700

# Firebase Settings (Pyrebase4)
FIREBASE_CONFIG_PATH = "config/firebase_credentials.json"

# Database Root Node
DB_ROOT = "cnc_erp"

# User Roles
ROLE_ADMIN = "admin"
ROLE_OPERATOR = "operator"

# Default Admin Credentials (Change after first login)
DEFAULT_ADMIN_USERNAME = "admin@cnc.com"
DEFAULT_ADMIN_PASSWORD = "admin123"

# Session Settings
SESSION_TIMEOUT = 3600  # 1 hour in seconds

# Date Format
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Pagination
ITEMS_PER_PAGE = 50

# Order Priority Levels
PRIORITY_LOW = "Low"
PRIORITY_MEDIUM = "Medium"
PRIORITY_HIGH = "High"

# Order Status
ORDER_STATUS_PENDING = "Pending"
ORDER_STATUS_IN_PRODUCTION = "In Production"
ORDER_STATUS_COMPLETED = "Completed"
ORDER_STATUS_CANCELLED = "Cancelled"

# Job Status
JOB_STATUS_QUEUED = "Queued"
JOB_STATUS_IN_PROGRESS = "In Progress"
JOB_STATUS_COMPLETED = "Completed"
JOB_STATUS_FAILED = "Failed"

# Machine Status
MACHINE_STATUS_AVAILABLE = "Available"
MACHINE_STATUS_RUNNING = "Running"
MACHINE_STATUS_MAINTENANCE = "Under Maintenance"
MACHINE_STATUS_BREAKDOWN = "Breakdown"

# Employee/Operator Status
EMPLOYEE_STATUS_ACTIVE = "Active"
EMPLOYEE_STATUS_BLOCKED = "Blocked"

