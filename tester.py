# orphans_example.py

def used_function_a():
    """This function is used by main_caller."""
    print("Executing used_function_a")
    return "Result from A"

def another_used_function_b(param1, param2="default"):
    """
    This function is also used.
    It takes parameters.
    """
    print(f"Executing another_used_function_b with {param1} and {param2}")
    return param1 + 10

def an_orphan_function():
    """
    This function is NOT called by any other function in this file.
    It should be detected as an orphan.
    """
    secret_value = 42
    print(f"Executing an_orphan_function. Secret is {secret_value}")
    return secret_value * 2

class UtilityClass:
    """A class with some utility methods."""

    def __init__(self, name):
        """Constructor, called on instantiation."""
        self.name = name
        print(f"UtilityClass '{self.name}' initialized.")

    def used_method_x(self, value):
        """This method is called by main_caller."""
        print(f"UtilityClass '{self.name}' executing used_method_x with value: {value}")
        return f"X processed {value}"

    def an_orphan_method(self):
        """
        This method is NOT called by any other function or method in this file.
        It should be detected as an orphan.
        """
        print(f"UtilityClass '{self.name}' executing an_orphan_method.")
        return "Orphan method result"

    def _internal_helper(self):
        """
        This internal helper might be called by other methods in this class.
        Let's make it called by used_method_x to ensure it's not an orphan.
        """
        return "Internal helper data"
    
    def another_used_method_y(self):
        """This method calls an internal helper."""
        helper_data = self._internal_helper()
        print(f"another_used_method_y got: {helper_data}")
        return True


def main_caller():
    """
    This function acts as an entry point or a caller for other used functions.
    """
    print("Starting main_caller execution.")
    
    result_a = used_function_a()
    print(f"Result from used_function_a: {result_a}")
    
    result_b = another_used_function_b(5, param2="custom")
    print(f"Result from another_used_function_b: {result_b}")

    util_instance = UtilityClass("MyUtil")
    method_result_x = util_instance.used_method_x("test_value")
    print(f"Result from util_instance.used_method_x: {method_result_x}")

    util_instance.another_used_method_y()

    print("Finished main_caller execution.")

# Example of how main_caller might be invoked if this were a script.
# Helix CME's orphan detection won't typically consider this block for call graph analysis
# unless specifically configured to understand script entry points.
if __name__ == "__main__":
    main_caller()
    # an_orphan_function() # If this was uncommented, it wouldn't be an orphan
    # util = UtilityClass("Test")
    # util.an_orphan_method() # If this was uncommented, it wouldn't be an orphan
