# Pythonic code:

# https://peps.python.org/pep-0008/#introduction

# List comprehensions: are a concise way to create lists in Python.
# They consist of brackets containing an expression followed by a for clause, and can also include optional
squares = [x**2 for x in range(10)]
print("NumberSquares:", squares)

# Filter even numbers:
evens = [x for x in range(10) if x % 2 == 0]
print("EvenNumbers:", evens)

# Lambda functions: are small anonymous functions defined with the lambda keyword.
add = lambda x, y: x + y
print("LambdaAdd(2, 3):", add(2, 3))

# map: applies a function to all items in an iterable (like a list).
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)
print("MappedSquares:", list(squares))

# filter: filters items out of an iterable based on a function.
evens = filter(lambda x: x % 2 == 0, numbers)
print("FilteredEvens:", list(evens))

# reduce: applies a rolling computation to sequential pairs of values in an iterable.
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("ReducedProduct:", product)

# Python os and sys modules: provide functions for interacting with the operating system and the Python runtime environment.
import os
import sys

# Get current working directory
current_directory = os.getcwd()
print("CurrentDirectory:", current_directory)

# List files in the current directory
files = os.listdir(current_directory)
print("FilesInCurrentDirectory:", files)

# Get Python version
python_version = sys.version
print("PythonVersion:", python_version)

print(os.getcwd()) # Get the current working directory
print(os.listdir('.')) # List files in the current directory

