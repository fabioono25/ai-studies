# function
import math_operations as mo
import math as m


def add(x, y):
    """Function to add two numbers."""
    return x + y


print("Addition of 5 and 3 is:", add(5, 3))


# modules: are files containing Python code that can define functions, classes, and variables. They allow you to organize your code into manageable sections and reuse code across different programs.
# You can create your own modules or use built-in modules.

# import an entire module

print("Square root of 16 is:", m.sqrt(16))


def factorial(n):
    """Function to calculate factorial of a number."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of 5 is:", factorial(5))


print("Addition using module:", mo.add(10, 5))
print("Subtraction using module:", mo.subtract(10, 5))
print("Multiplication using module:", mo.multiply(10, 5))
