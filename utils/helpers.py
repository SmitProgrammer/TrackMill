"""
Utility helper functions
"""

from PySide6.QtWidgets import QMessageBox, QInputDialog, QLineEdit
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from datetime import datetime
import re


def show_message(parent, title, message, msg_type="info"):
    """
    Show a message box

    Args:
        parent: Parent widget
        title: Message box title
        message: Message to display
        msg_type: Type of message (info, warning, error, success)
    """
    msg_box = QMessageBox(parent)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)

    if msg_type == "info":
        msg_box.setIcon(QMessageBox.Information)
    elif msg_type == "warning":
        msg_box.setIcon(QMessageBox.Warning)
    elif msg_type == "error":
        msg_box.setIcon(QMessageBox.Critical)
    elif msg_type == "success":
        msg_box.setIcon(QMessageBox.Information)

    msg_box.exec()


def show_error(parent, title, message):
    """Show error message"""
    show_message(parent, title, message, "error")


def show_warning(parent, title, message):
    """Show warning message"""
    show_message(parent, title, message, "warning")


def show_info(parent, title, message):
    """Show info message"""
    show_message(parent, title, message, "info")


def show_success(parent, title, message):
    """Show success message"""
    show_message(parent, title, message, "success")


def confirm_dialog(parent, title, message):
    """
    Show confirmation dialog

    Returns:
        bool: True if user clicked Yes, False otherwise
    """
    reply = QMessageBox.question(
        parent,
        title,
        message,
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No
    )
    return reply == QMessageBox.Yes


def validate_email(email):
    """
    Validate email format

    Args:
        email: Email string to validate

    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_phone(phone):
    """
    Validate phone number (Indian format)

    Args:
        phone: Phone number string

    Returns:
        bool: True if valid, False otherwise
    """
    # Remove spaces and dashes
    phone = phone.replace(" ", "").replace("-", "")

    # Check if it's 10 digits
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, phone) is not None


def format_date(date_str, input_format="%Y-%m-%d", output_format="%d-%m-%Y"):
    """
    Format date string

    Args:
        date_str: Date string to format
        input_format: Current format
        output_format: Desired format

    Returns:
        str: Formatted date string
    """
    try:
        date_obj = datetime.strptime(date_str, input_format)
        return date_obj.strftime(output_format)
    except:
        return date_str


def format_datetime(datetime_str, input_format="%Y-%m-%d %H:%M:%S", output_format="%d-%m-%Y %I:%M %p"):
    """
    Format datetime string

    Args:
        datetime_str: Datetime string to format
        input_format: Current format
        output_format: Desired format

    Returns:
        str: Formatted datetime string
    """
    try:
        dt_obj = datetime.strptime(datetime_str, input_format)
        return dt_obj.strftime(output_format)
    except:
        return datetime_str


def get_current_date():
    """Get current date in YYYY-MM-DD format"""
    return datetime.now().strftime("%Y-%m-%d")


def get_current_datetime():
    """Get current datetime in YYYY-MM-DD HH:MM:SS format"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_current_timestamp():
    """Get current timestamp"""
    return int(datetime.now().timestamp())


def truncate_text(text, max_length=50):
    """
    Truncate text to max length

    Args:
        text: Text to truncate
        max_length: Maximum length

    Returns:
        str: Truncated text with ... if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."


def is_empty(value):
    """Check if value is empty or None"""
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() == ""
    return False


def get_email_validator():
    """Get QValidator for email input"""
    regex = QRegularExpression(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return QRegularExpressionValidator(regex)


def get_phone_validator():
    """Get QValidator for phone input (10 digits)"""
    regex = QRegularExpression(r'^[6-9]\d{9}$')
    return QRegularExpressionValidator(regex)


def get_number_validator():
    """Get QValidator for number input"""
    regex = QRegularExpression(r'^\d+$')
    return QRegularExpressionValidator(regex)


def get_decimal_validator():
    """Get QValidator for decimal input"""
    regex = QRegularExpression(r'^\d+\.?\d{0,2}$')
    return QRegularExpressionValidator(regex)

