"""
CNC ERP System - Main Entry Point
"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from database import firebase_db, sqlite_db
from modules.auth import LoginWindow


def initialize_app():
    """Initialize application and databases"""
    print("=" * 60)
    print("  CNC ERP SYSTEM - INITIALIZING")
    print("=" * 60)

    if firebase_db.firebase is None:
        print("WARNING: Firebase not initialized. Please check firebase_credentials.json")
        print("   The app will still work with SQLite for local data.")
    else:
        print("SUCCESS: Firebase initialized successfully")

    print("SUCCESS: SQLite database ready")

    print("=" * 60)
    print("  READY TO LAUNCH")
    print("=" * 60)


def main():
    """Main application function"""
    # Create Qt Application
    app = QApplication(sys.argv)

    # Set application properties
    app.setApplicationName("CNC ERP System")
    app.setApplicationVersion("1.0.0")


    # Initialize app and databases
    initialize_app()

    # Create and show login window
    login_window = LoginWindow()
    login_window.show()

    # Run application
    exit_code = app.exec()

    print("\n" + "=" * 60)
    print("  APPLICATION CLOSING")
    print("=" * 60)
    sqlite_db.close()
    print("Thank you for using CNC ERP System!")
    print("=" * 60)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()

