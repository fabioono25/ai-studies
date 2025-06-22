def add(a, b):
    """Function to add two numbers."""
    return a + b


def subtract(a, b):
    """Function to subtract two numbers."""
    return a - b


def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b


def divide(a, b):
    """Function to divide two numbers."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def modulus(a, b):
    """Function to find the modulus of two numbers."""
    return a % b


def exponentiate(base, exponent):
    """Function to raise a number to the power of another."""
    return base ** exponent
