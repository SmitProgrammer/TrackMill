"" 
# CNC ERP System - College Project

A comprehensive Enterprise Resource Planning (ERP) system designed for small CNC (Computer Numerical Control) industries. This desktop application helps manage various aspects of CNC operations including orders, inventory, production, machines, and employees.

## Project Overview

This is a college-level ERP system built to demonstrate understanding of:
- Desktop application development using PySide6
- Database management (Firebase & SQLite)
- UI/UX design with Qt Designer
- Software architecture and modular design
- Authentication and authorization
- CRUD operations

## Tech Stack

- **Frontend:** PySide6 (Qt for Python)
- **UI Design:** Qt Designer (.ui files)
- **Backend Database:** 
  - Firebase Realtime Database (cloud storage)
  - SQLite (local storage)
- **Authentication:** Firebase Authentication with Pyrebase4
- **Language:** Python 3.13

## Features

### 1. Authentication Module
- Admin and Operator role-based authentication
- Admin login via desktop application
- Operator account creation by admin
- Firebase-based authentication
- Real-time block/unblock functionality

### 2. Customer Management
- Add, edit, and delete customer records
- Store customer details (name, contact, email, company, address)
- View all customers in a table

### 3. Order Management
- Create and track orders
- Link orders to customers
- Set priorities and delivery dates
- Track order status (Pending, In Progress, Completed, Cancelled)
- Filter orders by status

### 4. Inventory Management
- Manage raw materials and supplies
- Track current stock levels
- Set minimum stock thresholds
- Low stock alerts
- Add/Remove stock with remarks
- Supplier information

### 5. Production Management (Job Cards)
- Create job cards for production
- Link jobs to orders and machines
- Assign operators to jobs
- Track start and end times
- Monitor job status
- Record materials used

### 6. Machine Management
- Maintain machine records
- Track machine status (Available, In Use, Maintenance, Out of Service)
- Schedule maintenance
- Store machine specifications

### 7. Employee Management
- Add employee records
- Assign roles (Admin/Operator)
- Create operator login accounts
- Block/Unblock employees in real-time
- Track employee status

### 8. Reports Module
- Generate production summaries
- View inventory status
- Analyze order trends
- Track employee productivity

### 9. Settings Module
- Application configuration
- Account settings
- Data backup options

## Project Structure

```
CNC-ERP-System/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── compile_ui.bat         # Batch script to compile UI files
├── config/
│   ├── firebase_credentials.json  # Firebase configuration
│   └── settings.py        # Application settings
├── database/
│   ├── firebase_handler.py    # Firebase operations
│   └── sqlite_handler.py      # SQLite operations
├── modules/
│   ├── auth.py           # Authentication module
│   ├── customers.py      # Customer management
│   ├── orders.py         # Order management
│   ├── inventory.py      # Inventory management
│   ├── production.py     # Production/Job cards
│   ├── machines.py       # Machine management
│   ├── employees.py      # Employee management
│   ├── reports.py        # Reports module
│   ├── settings.py       # Settings module
│   ├── dashboard.py      # Dashboard widget
│   └── main_app.py       # Main window handler
├── ui/
│   ├── *.ui              # Qt Designer UI files
│   └── *_dialog.ui       # Dialog UI files
├── ui_compiled/
│   └── *_ui.py           # Compiled Python UI files
├── utils/
│   ├── helpers.py        # Helper functions
│   └── session.py        # Session management
└── data/
    └── cnc_erp.db        # SQLite database file

```

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Firebase account (for database)

### Installation Steps

1. **Clone the repository:**
   ```cmd
   git clone <repository-url>
   cd "Major Project"
   ```

2. **Create virtual environment:**
   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

4. **Configure Firebase:**
   - Create a Firebase project at https://console.firebase.google.com
   - Enable Firebase Realtime Database
   - Enable Email/Password authentication
   - Download service account credentials
   - Place credentials in `config/firebase_credentials.json`

5. **Compile UI files:**
   ```cmd
   compile_ui.bat
   ```

6. **Run the application:**
   ```cmd
   python main.py
   ```

## Default Admin Credentials

- **Email:** `admin@cnc.com`
- **Password:** `admin123`

These credentials are automatically created on first run.

## Usage Guide

### For Admins:
1. Login with admin credentials
2. Access all modules from the sidebar
3. Create operator accounts via Employee Management
4. Manage all aspects of the business

### For Operators:
- Operators use a separate Android app (to be developed)
- Login credentials are created by admin
- Can only access assigned features

## Database Schema

### SQLite Tables:
- `customers` - Customer information
- `orders` - Order details
- `inventory` - Material/inventory records
- `machines` - Machine information
- `employees` - Employee records
- `jobs` - Production job cards
- `maintenance` - Machine maintenance logs
- `activity_logs` - User activity tracking

### Firebase Structure:
- Used for real-time employee status updates
- Handles authentication
- Syncs critical data

## Development Notes

### UI Development Workflow:
1. Design UI in Qt Designer (.ui files)
2. Save in `ui/` folder
3. Run `compile_ui.bat` to convert to Python
4. Import compiled UI in module Python files
5. Connect signals and implement logic

### Adding New Module:
1. Create UI file in Qt Designer
2. Create corresponding Python module
3. Import UI class and implement logic
4. Add module to `main_app.py`
5. Update navigation in main window

## Future Enhancements

- Android app for operators
- QC (Quality Control) module
- Advanced reporting with charts
- PDF/Excel export functionality
- Email notifications
- Multi-language support
- Dark mode theme

## Troubleshooting

### Common Issues:

**Application won't start:**
- Check if all dependencies are installed
- Verify Firebase credentials are correct
- Ensure Python version is 3.10+

**Modules not loading:**
- Run `compile_ui.bat` to recompile UI files
- Clear Python cache: `del /S /Q __pycache__`
- Check for syntax errors in module files

**Database errors:**
- Verify Firebase configuration
- Check internet connection
- Ensure database rules allow read/write

## Credits

**Developer:** [Your Name]
**Project:** B.Tech Final Year Major Project
**Institution:** [Your College Name]
**Academic Year:** 2024-2025

## License

This is an academic project created for educational purposes.

## Contact

For any queries or support:
- Email: [your-email@example.com]
- GitHub: [your-github-profile]
