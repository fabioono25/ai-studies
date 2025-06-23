# Vector: A one-dimensional array of numbers used to represent quantities with both magnitude and direction.
# Matrix: A rectangular array of numbers arranged in rows and columns. Can be 1D (vector), 2D (traditional matrix), or higher dimensions.
# Tensor: A generalization of scalars, vectors, and matrices to higher dimensions. A scalar (0D), vector (1D), and matrix (2D) are all tensors of different orders.
# Linear Algebra: The branch of mathematics concerning linear equations, linear functions, and their representations through matrices and vector spaces.

# Example of Vector: v = [1, 2, 3]
# Example of Matrix: M = [[1, 2], [3, 4]]
# Example of Tensor: T = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

import numpy as np

A = np.array([[1, 2], [3, 4]])  # 2D array (matrix)
B = np.array([[5, 6], [7, 8]])  # 1D array (vector)

print("Addition of A and B:\n", A + B)  # Element-wise addition
print("Subtraction of A and B:\n", A - B)  # Element-wise

C = 2 * A
print("Scalar multiplication of A:\n", C)  # Scalar multiplication

result = np.dot(A, B)  # Matrix multiplication
print("Matrix multiplication of A and B:\n", result)  # Matrix multiplication

# Identity Matrix
identity_matrix = np.eye(5)  # 5x5 identity matrix
print("Identity Matrix:\n", identity_matrix)  # Identity matrix

# Zero Matrix
zero_matrix = np.zeros((3, 3))  # 3x3 zero matrix
print("Zero Matrix:\n", zero_matrix)  # Zero matrix

# Diagonal Matrix
# Diagonal matrix with specified diagonal elements
diagonal_matrix = np.diag([1, 2, 3])
print("Diagonal Matrix:\n", diagonal_matrix)  # Diagonal matrix

# Matrix-vector multiplication
vector = np.array([1, 2])  # 1D array (vector)
result_vector = np.dot(A, vector)  # Matrix-vector multiplication
print("Matrix-vector multiplication of A and vector:\n",
      result_vector)  # Matrix-vector multiplication

# Transpose of a Matrix
transpose_A = A.T  # Transpose of matrix A
print("Transpose of A:\n", transpose_A)  # Transpose of matrix A

# Inverse of a Matrix
try:
    inverse_A = np.linalg.inv(A)  # Inverse of matrix A
    print("Inverse of A:\n", inverse_A)  # Inverse of matrix A
except np.linalg.LinAlgError as e:
    print("Error inverting matrix A:", e)

# Determinant of a Matrix
det_A = np.linalg.det(A)  # Determinant of matrix A
print("Determinant of A:\n", det_A)  # Determinant of matrix A

# Eigenvalues and Eigenvectors
# Eigenvalues and eigenvectors of matrix A
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:\n", eigenvalues)  # Eigenvalues of matrix A
print("Eigenvectors of A:\n", eigenvectors)  # Eigenvectors of matrix A

# Singular Value Decomposition (SVD)
U, S, VT = np.linalg.svd(A)  # Singular Value Decomposition of matrix A
print("U matrix from SVD:\n", U)  # U matrix from SVD
print("S vector from SVD:\n", S)  # S vector from SVD
print("VT matrix from SVD:\n", VT)  # VT matrix from SVD

