def perform_operation(num1, num2, operation):
    """Performs a basic arithmetic operation based on the operation string."""
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zeror."
        return num1 / num2
    else:
        return "Error: Invalid operation"
    