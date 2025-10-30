"""
Session manager
"""

from datetime import datetime


class Session:

    _instance = None
    _user_data = None
    _login_time = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Session, cls).__new__(cls)
        return cls._instance

    def login(self, user_data):
        """
        Store user data on login

        Args:
            user_data: Dictionary containing user information
        """
        self._user_data = user_data
        self._login_time = datetime.now()

    def logout(self):
        """Clear session data"""
        self._user_data = None
        self._login_time = None

    def is_logged_in(self):
        """Check if user is logged in"""
        return self._user_data is not None

    def get_user_email(self):
        """Get logged-in user email"""
        if self._user_data:
            return self._user_data.get('email', '')
        return None

    def get_user_id(self):
        """Get logged-in user ID"""
        if self._user_data:
            return self._user_data.get('localId', '')
        return None

    def get_user_token(self):
        """Get user authentication token"""
        if self._user_data:
            return self._user_data.get('idToken', '')
        return None

    def get_login_time(self):
        """Get login timestamp"""
        return self._login_time

    def get_session_duration(self):
        """Get session duration in seconds"""
        if self._login_time:
            return (datetime.now() - self._login_time).total_seconds()
        return 0

    def get_user_data(self):
        """Get all user data"""
        return self._user_data


# Create singleton instance
session = Session()

