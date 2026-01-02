"""
CNC ERP System - Main Entry Point
Firebase-Only Architecture (No SQLite)
"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from database import firebase_db
from modules.auth import LoginWindow


def initialize_app():
    """Initialize Firebase (Firebase-Only Architecture)"""
    print("=" * 60)
    print("  CNC ERP SYSTEM - INITIALIZING")
    print("=" * 60)

    if firebase_db.firebase is None:
        print("ERROR: Firebase not initialized!")
        print("Please check firebase_credentials.json in config folder")
        print("The app REQUIRES Firebase to function.")
        print("=" * 60)
        return False
    else:
        print("SUCCESS: Firebase initialized successfully")
        print("Architecture: Firebase-Only (Pure Cloud)")
        print("All data stored and retrieved from Firebase")

    print("=" * 60)
    print("  READY TO LAUNCH")
    print("=" * 60)
    return True


def main():
    """Main application function"""
    # Create Qt Application
    app = QApplication(sys.argv)

    # Set application properties
    app.setApplicationName("CNC ERP System")
    app.setApplicationVersion("1.0.0")

    # Initialize Firebase
    if not initialize_app():
        print("Failed to initialize Firebase. Exiting.")
        sys.exit(1)

    # Create and show login window
    login_window = LoginWindow()
    login_window.show()

    # Run application
    exit_code = app.exec()

    print("\n" + "=" * 60)
    print("  APPLICATION CLOSING")
    print("=" * 60)
    print("Thank you for using CNC ERP System!")
    print("=" * 60)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()

