"""
Firebase Database Handler using Pyrebase4
"""

import json
import pyrebase
from config.settings import FIREBASE_CONFIG_PATH, DB_ROOT


class FirebaseDB:

    def __init__(self):
        self.firebase = None
        self.auth = None
        self.db = None
        self.user = None
        self.initialize_firebase()
    
    def initialize_firebase(self):
        """Initialize Firebase with Pyrebase4"""
        try:
            # Load Firebase configuration
            with open(FIREBASE_CONFIG_PATH, 'r') as f:
                config = json.load(f)
            
            # Initialize Firebase
            self.firebase = pyrebase.initialize_app(config)
            self.auth = self.firebase.auth()
            self.db = self.firebase.database()
            
            print(" Firebase initialized successfully with Pyrebase4")
            return True
            
        except FileNotFoundError:
            print(" Error: firebase_credentials.json not found")
            print("Please configure Firebase credentials in config/firebase_credentials.json")
            return False
        except Exception as e:
            print(f" Firebase initialization error: {e}")
            return False
    
    def sign_in(self, email, password):
        """
        Sign in user with email and password
        Returns: (success: bool, user_data: dict, error_message: str)
        """
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            self.user = user
            return True, user, None
        except Exception as e:
            error_msg = str(e)
            if "INVALID_EMAIL" in error_msg:
                return False, None, "Invalid email format"
            elif "INVALID_PASSWORD" in error_msg or "INVALID_LOGIN_CREDENTIALS" in error_msg:
                return False, None, "Invalid credentials"
            elif "EMAIL_NOT_FOUND" in error_msg:
                return False, None, "Email not found"
            else:
                return False, None, f"Login error: {error_msg}"
    
    def create_user(self, email, password):
        """
        Create new user account
        Returns: (success: bool, user_data: dict, error_message: str)
        """
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            return True, user, None
        except Exception as e:
            error_msg = str(e)
            if "EMAIL_EXISTS" in error_msg:
                return False, None, "Email already exists"
            elif "WEAK_PASSWORD" in error_msg:
                return False, None, "Password should be at least 6 characters"
            else:
                return False, None, f"Registration error: {error_msg}"
    
    def sign_out(self):
        """Sign out current user"""
        self.user = None
        return True
    
    def get_user_token(self):
        """Get current user's ID token"""
        if self.user:
            return self.user['idToken']
        return None
    
    def get_user_id(self):
        """Get current user's UID"""
        if self.user:
            return self.user['localId']
        return None
    
    # ==================== DATABASE OPERATIONS ====================
    
    def get_reference(self, path):
        """Get database reference for a path"""
        return self.db.child(DB_ROOT).child(path)
    
    def create(self, path, data):
        """
        Create new record
        Returns: (success: bool, key: str, error_message: str)
        """
        try:
            result = self.get_reference(path).push(data, self.get_user_token())
            return True, result['name'], None
        except Exception as e:
            return False, None, f"Create error: {str(e)}"
    
    def set(self, path, data):
        """
        Set data at specific path (overwrites existing)
        Returns: (success: bool, error_message: str)
        """
        try:
            self.get_reference(path).set(data, self.get_user_token())
            return True, None
        except Exception as e:
            return False, f"Set error: {str(e)}"
    
    def update(self, path, data):
        """
        Update specific fields
        Returns: (success: bool, error_message: str)
        """
        try:
            self.get_reference(path).update(data, self.get_user_token())
            return True, None
        except Exception as e:
            return False, f"Update error: {str(e)}"
    
    def get(self, path):
        """
        Get data from path
        Returns: (success: bool, data: dict, error_message: str)
        """
        try:
            data = self.get_reference(path).get(self.get_user_token()).val()
            return True, data, None
        except Exception as e:
            return False, None, f"Get error: {str(e)}"
    
    def delete(self, path):
        """
        Delete data at path
        Returns: (success: bool, error_message: str)
        """
        try:
            self.get_reference(path).remove(self.get_user_token())
            return True, None
        except Exception as e:
            return False, f"Delete error: {str(e)}"
    
    def get_all(self, path):
        """
        Get all records from a path as list of dictionaries
        Returns: (success: bool, data: list, error_message: str)
        """
        try:
            data = self.get_reference(path).get(self.get_user_token()).val()
            if data is None:
                return True, [], None
            
            # Convert to list of dicts with keys
            result = []
            for key, value in data.items():
                value['id'] = key
                result.append(value)
            
            return True, result, None
        except Exception as e:
            return False, [], f"Get all error: {str(e)}"
    
    def query(self, path, order_by, equal_to=None, start_at=None, end_at=None, limit_first=None):
        """
        Query database with filters
        Returns: (success: bool, data: list, error_message: str)
        """
        try:
            query = self.get_reference(path).order_by_child(order_by)
            
            if equal_to is not None:
                query = query.equal_to(equal_to)
            if start_at is not None:
                query = query.start_at(start_at)
            if end_at is not None:
                query = query.end_at(end_at)
            if limit_first is not None:
                query = query.limit_to_first(limit_first)
            
            data = query.get(self.get_user_token()).val()
            
            if data is None:
                return True, [], None
            
            # Convert to list
            result = []
            for key, value in data.items():
                value['id'] = key
                result.append(value)
            
            return True, result, None
        except Exception as e:
            return False, [], f"Query error: {str(e)}"
    
    # ==================== REALTIME LISTENERS ====================
    
    def stream(self, path, callback):
        """
        Stream real-time updates from a path
        callback function receives (event) with event['data'] and event['path']
        """
        try:
            stream = self.get_reference(path).stream(callback, self.get_user_token())
            return True, stream, None
        except Exception as e:
            return False, None, f"Stream error: {str(e)}"
    
    def close_stream(self, stream):
        """Close a stream"""
        try:
            stream.close()
            return True
        except Exception as e:
            print(f"Error closing stream: {e}")
            return False


# Create singleton instance
firebase_db = FirebaseDB()

