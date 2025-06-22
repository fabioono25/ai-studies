# 🐍 Python Learning Journey

This repository contains a comprehensive study guide for Python programming and Data Science essentials. The content is organized into structured chapters with practical examples and hands-on coding exercises.

## 📚 Table of Contents

- [Chapter 1: Python Basics](#chapter-1-python-basics)
- [Chapter 2: Data Science Essentials](#chapter-2-data-science-essentials)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)

---

## Chapter 1: Python Basics

### 🚀 Introduction to Python
**File:** [`1-intro_python.py`](1-Python%20Basics/1-intro_python.py)

**Concepts Covered:**
- **Data Types**: integers, floats, strings, booleans
- **Data Structures**: lists, tuples, dictionaries, sets
- **Variables and Assignment**: storing and accessing data
- **Type Checking**: using `type()` function to inspect variable types
- **None Type**: understanding Python's null value

**Key Examples:**
```python
# Basic data types
age = 25                    # int
height = 5.9               # float
name = "Alice"             # str
is_student = True          # bool

# Collections
fruits = ["apple", "banana", "cherry"]          # list
coordinates = (10.0, 20.0)                     # tuple
person = {"name": "Alice", "age": 25}           # dict
unique_numbers = {1, 2, 3, 4, 5}              # set
```

### 🔄 Control Flow
**File:** [`2-flow_python.py`](1-Python%20Basics/2-flow_python.py)

**Concepts Covered:**
- **Conditional Statements**: if, elif, else
- **Loops**: for loops, while loops, range() function
- **Function Definition**: creating reusable code blocks
- **Algorithm Implementation**: prime number detection
- **Iteration Patterns**: looping through lists and ranges

**Key Examples:**
```python
# Conditional logic
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")

# Prime number algorithm
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### 🔧 Functions and Modules
**Files:** [`3-functions_modules.py`](1-Python%20Basics/3-functions_modules.py), [`math_operations.py`](1-Python%20Basics/math_operations.py)

**Concepts Covered:**
- **Function Definition**: creating custom functions with parameters and return values
- **Module Creation**: organizing code into reusable modules
- **Module Import**: importing built-in and custom modules
- **Docstrings**: documenting functions for better code readability
- **Recursion**: implementing factorial using recursive approach

**Key Examples:**
```python
# Custom module usage
import math_operations as mo
import math as m

# Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Module functions
mo.add(10, 5)        # Custom module
m.sqrt(16)           # Built-in module
```

### 📦 Collections Deep Dive
**File:** [`4-collections.py`](1-Python%20Basics/4-collections.py)

**Concepts Covered:**
- **Lists**: mutable sequences with indexing, slicing, and modification methods
- **Tuples**: immutable sequences for fixed data
- **Dictionaries**: key-value mappings with CRUD operations
- **Sets**: unique element collections with mathematical operations
- **Collection Operations**: append, remove, sort, pop, union, intersection

**Key Examples:**
```python
# List operations
numbers = [1, 2, 3, 4, 5]
numbers.append(6)           # Add element
numbers.remove(2)           # Remove element
print(numbers[1:3])         # Slicing

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a | set_b       # Union: {1, 2, 3, 4, 5}
intersection = set_a & set_b # Intersection: {3}

# Dictionary operations
student = {"name": "Alice", "age": 20}
student["major"] = "CS"     # Add new key-value pair
del student["age"]          # Remove key-value pair
```

### 🔤 String Manipulation
**File:** [`5-strings.py`](1-Python%20Basics/5-strings.py)

**Concepts Covered:**
- **String Operations**: concatenation, slicing, formatting
- **String Methods**: split, join, replace, strip
- **F-string Formatting**: modern string interpolation
- **Regular Expressions**: pattern matching and text processing
- **Text Processing**: finding, replacing, and extracting patterns

**Key Examples:**
```python
# String slicing and formatting
text = "Hello World bla bla"
print(text[1:3])            # Slicing
print(f"I am {first} and I am {second}")  # F-strings

# Regular expressions
import re
pattern = r"\b\w{3}\b"      # Match 3-character words
matches = re.findall(pattern, text)
replaced = re.sub(r"\d", "*", "123abc")  # Replace digits
```

### 📁 File Handling
**Files:** [`6-file_handling.py`](1-Python%20Basics/6-file_handling.py), [`input.txt`](1-Python%20Basics/input.txt), [`output.txt`](1-Python%20Basics/output.txt)

**Concepts Covered:**
- **File I/O Operations**: reading from and writing to files
- **Context Managers**: using `with` statements for proper file handling
- **Error Handling**: managing FileNotFoundError exceptions
- **Text Processing**: counting words in files
- **File Modes**: read ('r'), write ('w'), append ('a')

**Key Examples:**
```python
# Reading files
with open("input.txt", "r") as file:
    content = file.read()

# Writing files
with open("output.txt", "w") as file:
    file.write("This is a test output file.\n")
    file.writelines(["Line 1\n", "Line 2\n"])

# Word counting function
def count_words_in_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return 0
```

### ✨ Pythonic Code
**File:** [`pythonic_code.py`](1-Python%20Basics/pythonic_code.py)

**Concepts Covered:**
- **List Comprehensions**: concise list creation with filtering
- **Lambda Functions**: anonymous functions for simple operations
- **Higher-order Functions**: map, filter, reduce
- **Functional Programming**: applying functions to iterables
- **System Modules**: os and sys for system interaction

**Key Examples:**
```python
# List comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]

# Lambda and higher-order functions
add = lambda x, y: x + y
squares = map(lambda x: x**2, numbers)
evens = filter(lambda x: x % 2 == 0, numbers)

# System interaction
import os, sys
current_dir = os.getcwd()
files = os.listdir('.')
python_version = sys.version
```

### 📓 Interactive Learning
**File:** [`1-first-test.ipynb`](1-Python%20Basics/1-first-test.ipynb)

A Jupyter notebook for interactive Python experimentation and testing concepts learned in the chapter.

---

## Chapter 2: Data Science Essentials

### 🔢 NumPy Fundamentals
**File:** [`1-numpy.py`](2-Data%20Science%20Essentials/1-numpy.py)

**Concepts Covered:**
- **Array Creation**: 1D, 2D, and 3D arrays
- **Array Generation**: zeros, ranges, linspace, reshape operations
- **Mathematical Operations**: element-wise operations, aggregation functions
- **Array Indexing**: slicing, boolean indexing, advanced selection
- **Broadcasting**: operations between arrays of different shapes
- **Random Number Generation**: random arrays, seeds for reproducibility
- **Statistical Functions**: mean, standard deviation, variance, min/max

**Key Examples:**
```python
import numpy as np

# Array creation
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
zeros_matrix = np.zeros((3, 3))
range_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 1, 5)

# Mathematical operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a + b  # Element-wise addition

# Statistical operations
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(np.mean(matrix))      # Mean
print(np.std(matrix))       # Standard deviation
print(np.sum(matrix, axis=0))  # Sum along columns

# Broadcasting example
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, 1])
result = matrix + vector    # Adds vector to each row

# Boolean indexing
evens = array_1d[array_1d % 2 == 0]  # Select even numbers
array_1d[array_1d > 2] = 10          # Modify elements conditionally

# Random number generation
np.random.seed(42)  # Set seed for reproducibility
random_array = np.random.rand(3, 3)           # Random 0-1
random_integers = np.random.randint(1, 10, size=(3, 3))  # Random integers
random_normal = np.random.randn(3, 3)         # Normal distribution
```

---

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Basic understanding of programming concepts
- Text editor or IDE (VS Code recommended)

### Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd ai-studies
   ```

2. Install required packages:
   ```bash
   pip install numpy
   ```

3. Run any Python file:
   ```bash
   python "1-Python Basics/1-intro_python.py"
   ```

4. For Jupyter notebooks:
   ```bash
   pip install jupyter
   jupyter notebook "1-Python Basics/1-first-test.ipynb"
   ```

---

## Project Structure

```
ai-studies/
├── 1-Python Basics/
│   ├── 1-first-test.ipynb      # Interactive notebook for experimentation
│   ├── 1-intro_python.py       # Data types and basic concepts
│   ├── 2-flow_python.py        # Control flow and functions
│   ├── 3-functions_modules.py  # Functions and module imports
│   ├── 4-collections.py        # Lists, tuples, dicts, sets
│   ├── 5-strings.py            # String manipulation and regex
│   ├── 6-file_handling.py      # File I/O operations
│   ├── math_operations.py      # Custom module with math functions
│   ├── pythonic_code.py        # Pythonic programming patterns
│   ├── input.txt              # Sample input file
│   └── output.txt             # Generated output file
├── 2-Data Science Essentials/
│   └── 1-numpy.py             # NumPy arrays and operations
└── README.md                   # This file
```

---

## Learning Path

### For Beginners:
1. Start with **Chapter 1: Python Basics** in order
2. Practice each concept in the interactive notebook
3. Experiment with the provided examples
4. Move to **Chapter 2** once comfortable with Python fundamentals

### For Intermediate Learners:
1. Review **Pythonic Code** concepts first
2. Focus on **Collections** and **String Manipulation**
3. Dive deep into **NumPy** for data science foundation

---

## Contributing

Feel free to contribute by:
- Adding more examples to existing files
- Creating new chapters for advanced topics
- Improving documentation and comments
- Adding exercises and solutions

---

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [NumPy Documentation](https://numpy.org/doc/)
- [PEP 8 - Python Style Guide](https://peps.python.org/pep-0008/)
- [Real Python Tutorials](https://realpython.com/)

---

*Happy Learning! 🚀*
