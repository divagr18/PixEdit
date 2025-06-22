# class_summary_dependencies.py

def get_database_connection(connection_string: str):
    """Establishes a mock database connection."""
    print(f"Connecting to DB with: {connection_string}")
    # In a real scenario, this would return a connection object.
    return {"status": "connected", "conn_str": connection_string}

def log_error_to_service(error_message: str, level: str = "ERROR"):
    """Logs an error message to an external monitoring service."""
    print(f"LOGGING [{level}]: {error_message}")
    return True

def process_user_permissions(user_id: str):
    """A function in another module that might use our class."""
    print(f"\n--- Running process_user_permissions for user: {user_id} ---")
    
    # This function will call a method on our test class
    user_manager = UserManager("prod_db_string")
    
    # This creates a dependency: process_user_permissions -> UserManager.get_user_profile
    profile = user_manager.get_user_profile(user_id)
    
    if profile:
        print(f"Successfully retrieved profile for {user_id}: {profile}")
    else:
        print(f"Failed to retrieve profile for {user_id}")
    print("--- Finished process_user_permissions ---")
