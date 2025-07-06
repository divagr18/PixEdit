from class_summary_dependencies import get_database_connection, log_error_to_service


class UserManager:
    """
    Manages user data, profiles, and authentication against a database.
    This main class docstring might be used for context if we enhance the prompt later.
    """

    def __init__(self, db_connection_string: str, cache_enabled: bool = True):
        """Initializes the UserManager with the specified database connection and cache settings.

        Args:
            db_connection_string (str): The connection string used to connect to the database.
            cache_enabled (bool, optional): Flag to enable or disable user caching. Defaults to True.

        Sets up the database connection and initializes an empty user cache dictionary."""
        self.db_conn_str = db_connection_string
        self.cache_enabled = cache_enabled
        self.db_connection = get_database_connection(self.db_conn_str)
        self.user_cache = {}

    def get_user_profile(self, user_id: str) -> dict | None:
        """Retrieves the profile of a user by user ID, using cache if available.

        Args:
            user_id (str): The unique identifier of the user whose profile is requested.

        Returns:
            dict or None: A dictionary containing user profile information if found; otherwise, None.

        This method first attempts to retrieve the user profile from an internal cache if caching is enabled.
        If the profile is not cached, it queries the database (simulated here) to fetch the profile data,
        caching the result if caching is enabled. In case of an exception during retrieval, it logs the error
        to an external service and returns None."""
        if self.cache_enabled and user_id in self.user_cache:
            return self.user_cache[user_id]
        try:
            print(f"Querying DB for user {user_id}...")
            profile_data = {
                "user_id": user_id,
                "name": "John Doe",
                "email": "john.doe@example.com",
            }
            if self.cache_enabled:
                self.user_cache[user_id] = profile_data
            return profile_data
        except Exception as e:
            log_error_to_service(f"Failed to get profile for {user_id}: {e}")
            return None

    def update_user_email(self, user_id: str, new_email: str) -> bool:
        """Updates the email address for a specified user in the database.

        Validates the new email format before attempting to update. If the email format is invalid,
        logs a warning to the error service and does not perform the update.

        Args:
            user_id (str): The unique identifier of the user whose email is to be updated.
            new_email (str): The new email address to associate with the user.

        Returns:
            bool: True if the email was successfully updated (mocked as always True when valid),
            False if the new email format is invalid and update is not performed."""
        if not self._is_email_valid(new_email):
            log_error_to_service(f"Invalid email format: {new_email}", level="WARN")
            return False
        print(f"Updating email for {user_id} to {new_email} in DB...")
        return True

    def _is_email_valid(self, email: str) -> bool:
        """Checks if the given email address has a valid format.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email contains an '@' character and a '.' in the domain part; False otherwise.

        Note:
            This is a simplified validation intended for internal use and may not cover all valid email formats."""
        return "@" in email and "." in email.split("@")[1]
