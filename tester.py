def used_function_a():
    """Execute the primary action for used_function_a.

    This function is called by main_caller to perform its designated task,
    printing a message to the console and returning a result string.

    Returns:
        str: A message indicating the result of used_function_a execution."""
    print("Executing used_function_a")
    return "Result from A"


def another_used_function_b(param1, param2="default"):
    """Execute a sample operation using param1 and param2, then return param1 incremented by 10.

    Args:
        param1 (int): The primary integer parameter to process.
        param2 (str, optional): An optional string parameter with a default value of "default".

    Returns:
        int: The result of adding 10 to param1."""
    print(f"Executing another_used_function_b with {param1} and {param2}")
    return param1 + 10


def an_orphan_function():
    """Executes a standalone function that prints and returns a value.

    This function is not invoked by any other function within the module `tester.py`
    and serves as an example of an orphan function.

    Returns:
        int: Twice the secret value (84)."""
    secret_value = 42
    print(f"Executing an_orphan_function. Secret is {secret_value}")
    return secret_value * 2


class UtilityClass:
    """A class with some utility methods."""

    def __init__(self, name):
        """Initializes the UtilityClass instance with a given name.

        Args:
            name (str): The name to assign to the instance.

        Sets the instance's name attribute and prints an initialization message."""
        self.name = name
        print(f"UtilityClass '{self.name}' initialized.")

    def used_method_x(self, value):
        """Executes a processing routine using the provided value and logs the action.

        Args:
            value: The input data to be processed by this method.

        Returns:
            A string indicating that the value has been processed by method X.

        Note:
            This method is called by the main_caller function as part of the workflow involving UtilityClass instances."""
        print(f"UtilityClass '{self.name}' executing used_method_x with value: {value}")
        return f"X processed {value}"

    def an_orphan_method(self):
        """Executes an isolated utility method that is not invoked elsewhere in the module.

        This method prints a message indicating execution along with the instance's `name` attribute,
        and returns a fixed string. It is designed to be an orphan method, meaning it is not called
        by any other function or method within the same file.

        Returns:
            str: A predefined result string "Orphan method result"."""
        print(f"UtilityClass '{self.name}' executing an_orphan_method.")
        return "Orphan method result"



def main_caller():
    """Executes a sequence of function calls and methods, serving as the primary entry point for invoking various utility and helper functions.

    Calls used_function_a and prints its result.
    Calls another_used_function_b with specific arguments and prints its result.
    Creates an instance of UtilityClass and calls its used_method_x and another_used_method_y methods, printing results where applicable.

    This function does not take any parameters or return a value. It primarily handles orchestration and displays output to standard output."""
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
