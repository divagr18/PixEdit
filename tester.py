def used_function_a():
    """Execute the primary action for used_function_a.

    Called by main_caller to perform its designated task, this function prints a message to the console and returns a result string.

    Returns:
        str: A message indicating the result of used_function_a execution."""
    print("Executing used_function_a")
    return "Result from A"


def another_used_function_b(param1, param2="default"):
    """Perform a sample operation with param1 and param2, returning param1 incremented by 10.

    Args:
        param1 (int): The primary integer input.
        param2 (str, optional): An optional string parameter, defaults to "default".

    Returns:
        int: The value of param1 plus 10."""
    print(f"Executing another_used_function_b with {param1} and {param2}")
    return param1 + 10


def an_orphan_function():
    """Executes a standalone example function that prints a message and returns a computed value.

    This function is not called by any other function within the `tester.py` module and demonstrates an orphan function.

    Returns:
        int: Twice the secret value (84)."""
    secret_value = 42
    print(f"Executing an_orphan_function. Secret is {secret_value}")
    return secret_value * 2


class UtilityClass:
    """A class with some utility methods."""

    def __init__(self, name):
        """Initializes a UtilityClass instance with the specified name.

        Args:
            name (str): The name to assign to the instance.

        Sets the instance's name attribute and prints a confirmation message upon initialization."""
        self.name = name
        print(f"UtilityClass '{self.name}' initialized.")

    def used_method_x(self, value):
        """Executes a processing routine using the provided value and logs the action.

        Args:
            value: The input data to be processed by this method.

        Returns:
            str: A string indicating that the value has been processed by method X.

        Note:
            This method is called by the main_caller function as part of the workflow involving UtilityClass instances."""
        print(f"UtilityClass '{self.name}' executing used_method_x with value: {value}")
        return f"X processed {value}"

    def an_orphan_method(self):
        """Executes an isolated utility method that prints a message and returns a fixed string.

        This method outputs a message indicating it is running, including the instance's `name` attribute.
        It is intentionally designed as an orphan method, not called by any other code within the module.

        Returns:
            str: The fixed result string "Orphan method result"."""
        print(f"UtilityClass '{self.name}' executing an_orphan_method.")
        return "Orphan method result"


def main_caller():
    """Executes a sequence of utility functions and methods, serving as the main entry point.

    Calls `used_function_a` and prints its result.
    Calls `another_used_function_b` with specific arguments and prints its result.
    Creates a `UtilityClass` instance and invokes its `used_method_x` and `another_used_method_y` methods, printing results where applicable.

    This function does not accept any arguments or return a value. It orchestrates calls and outputs results to standard output."""
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


if __name__ == "__main__":
    main_caller()
