# class_summary_test.py

# These imports create dependencies that Helix should identify.
from class_summary_dependencies import get_database_connection, log_error_to_service

class UserManager:
    """
    Manages user data, profiles, and authentication against a database.
    This main class docstring might be used for context if we enhance the prompt later.
    """

    def __init__(self, db_connection_string: str, cache_enabled: bool = True):
        """Initializes the user manager with database settings."""
        self.db_conn_str = db_connection_string
        self.cache_enabled = cache_enabled
        self.db_connection = get_database_connection(self.db_conn_str)
        self.user_cache = {}

    def get_user_profile(self, user_id: str) -> dict | None:
        """Retrieves a user's profile from the cache or database."""
        if self.cache_enabled and user_id in self.user_cache:
            return self.user_cache[user_id]
        
        try:
            # Mock database query
            print(f"Querying DB for user {user_id}...")
            profile_data = {"user_id": user_id, "name": "John Doe", "email": "john.doe@example.com"}
            if self.cache_enabled:
                self.user_cache[user_id] = profile_data
            return profile_data
        except Exception as e:
            # This creates a dependency on an external logging service
            log_error_to_service(f"Failed to get profile for {user_id}: {e}")
            return None

    def update_user_email(self, user_id: str, new_email: str) -> bool:
        """Updates a user's email address in the database."""
        if not self._is_email_valid(new_email):
            log_error_to_service(f"Invalid email format: {new_email}", level="WARN")
            return False
        
        print(f"Updating email for {user_id} to {new_email} in DB...")
        return True # Mock success

    def _is_email_valid(self, email: str) -> bool:
        """A private helper method to validate email format."""
        # A very simple validation for demonstration purposes.
        return '@' in email and '.' in email.split('@')[1]
