# Numpy: A fundamental package for scientific computing in Python.
import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Create a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", array_3d)

# create a matrix of zeros
zeros_matrix = np.zeros((3, 3))
print("Zeros Matrix:\n", zeros_matrix)

# range array: create an array with a range of values
range = np.arange(1, 10)  # Creates an array with values from 0 to 9
print("Range Array:", range)

range_array = np.arange(0, 10, 2)
print("Range Array:", range_array)

range_array2 = np.arange(0, 10, 3)
print("Range Array 2:", range_array2)

# linspace array: create an array with evenly spaced values over a specified interval
# creates an array of 5 evenly spaced values between 0 and 1. 5 means the number of samples to generate.
linspace_array = np.linspace(0, 1, 5)
print("Linspace Array:", linspace_array)

# Reshape the array to 2 rows and 3 columns
arr = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print("Reshaped Array:\n", arr)

# adding dimensions to an array
arr2 = np.array([1, 2, 3, 4, 5])
arr2 = arr2[:, np.newaxis]  # Adds a new axis, converting it to a column vector
print("Array with New Axis:\n", arr2)

# operations on arrays

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Array Addition:", a + b)  # Element-wise addition
print("Array Subtraction:", a - b)  # Element-wise subtraction
print("Array Multiplication:", a * b)  # Element-wise multiplication
print("Array Division:", a / b)  # Element-wise division

arr3 = np.array([1, 2, 3, 4, 5])
print(np.sqrt(arr3))  # Square root of each element
print(np.exp(arr3))  # Exponential of each element
print(np.sum(arr3))  # Sum of all elements
print(np.mean(arr3))  # Mean of the elements
print(np.std(arr3))  # Standard deviation of the elements
print(np.var(arr3))  # Variance of the elements
print(np.min(arr3))  # Minimum value
print(np.max(arr3))  # Maximum value

# Indexing and slicing
arr4 = np.array([10, 20, 30, 40, 50, 60])
print(arr4[2])
print(arr4[1:4])
print(arr4[-2])

reshape = arr4.reshape(2, 3)
print("Reshaped Array:\n", reshape)

# convert a list to a numpy array
list_data = [1, 2, 3, 4, 5]
numpy_array = np.array(list_data)
print("Numpy Array:", numpy_array)

# convert a numpy array to a list
numpy_array2 = np.array([1, 2, 3, 4, 5])
list_data2 = numpy_array2.tolist()
print("List Data 2:", list_data2)

# Advanced operations

# Broadcasting: allows numpy to perform operations on arrays of different shapes
# Rules of broadcasting:
# 1. If the arrays have different numbers of dimensions, the shape of the smaller-dimensional array is padded with ones on the left side until both shapes are the same length.
# 2. If the sizes of the dimensions are different, the array with size 1 in that dimension is stretched to match the size of the other array.

a = np.array([[1, 2, 3]])
print(a + 5)  # Broadcasting: adds 5 to each element of the array

matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, 1])
# Broadcasting: adds vector to each row of the matrix
print("Matrix + Vector:\n", matrix + vector)

# aggregation functions
# Sum of all elements in the matrix
print("Sum of all elements:", np.sum(matrix))
print("Sum along axis 0 (columns):", np.sum(matrix, axis=0))  # Sum along columns
print("Sum along axis 1 (rows):", np.sum(matrix, axis=1))
# Mean of all elements in the matrix
print("Mean of all elements:", np.mean(matrix))
print("Max of all elements:", np.max(matrix))  # Maximum value in the matrix
print("Min of all elements:", np.min(matrix))  # Minimum value in the matrix

# standard deviation. it is a measure of the amount of variation or dispersion of a set of values.
# Standard deviation of the matrix
print("Standard Deviation:", np.std(matrix))

# Boolean Indexing
print("Boolean Indexing (elements > 4):", matrix[matrix > 4])

array_5 = np.array([1, 2, 3, 4, 5])
evens = array_5[array_5 % 2 == 0]  # Select even numbers
print("Even Numbers:", evens)

array_5[array_5 > 2] = 10  # Set elements greater than 2 to 10
print("Modified Array:", array_5)

# random number generation
random_array = np.random.rand(3, 3)  # Generate a 3x3 array of random numbers between 0 and 1
print("Random Array:\n", random_array)

random_integers = np.random.randint(1, 10, size=(3, 3))  # Generate a 3x3 array of random integers between 1 and 10
print("Random Integers Array:\n", random_integers)

np.random.seed(42)  # Set seed for reproducibility
random_normal = np.random.randn(3, 3)  # Generate a 3x3 array of random numbers from a normal distribution
print("Random Normal Distribution Array:\n", random_normal)

