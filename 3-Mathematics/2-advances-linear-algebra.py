# Determinants: are a scalar value that can be computed from the elements of a square matrix.
# They provide important information about the matrix, such as whether it is invertible (a non-zero determinant indicates that the matrix is invertible) and the volume scaling factor of the linear transformation described by the matrix.
# Singular Value Decomposition (SVD): A factorization of a matrix into three matrices, revealing important properties such as rank, range, and null space.

# Formule of a determinant:
# For a 2x2 matrix:
# | a  b |
# | c  d | = ad - bc  
# For a 3x3 matrix:
# | a  b  c |
# | d  e  f |
# | g  h  i | = a(ei - fh) - b(di - fg) + c(dh - eg)

import numpy as np

# Determinant of a 2x2 matrix
A = np.array([[2, 3], [1, 4]])
det_A = np.linalg.det(A)
print("Determinant of A (2x2 matrix):", det_A)

# Inverse of a Matrix: # The inverse of a matrix A is denoted as A^(-1) and satisfies the equation A * A^(-1) = I, where I is the identity matrix.
# For a 2x2 matrix:
# | a  b |
# | c  d |, the inverse is given by:
# A^(-1) = (1/det(A)) * | d  -b |
#                     | -c  a  |  

inverse = np.linalg.inv(A)
print("Inverse of A (2x2 matrix):\n", inverse)

# Eigenvalues and Eigenvectors: # Eigenvalues are scalars that indicate how much a matrix stretches or compresses space, while eigenvectors are the directions in which this stretching or compressing occurs.
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A (2x2 matrix):\n", eigenvalues)
print("Eigenvectors of A (2x2 matrix):\n", eigenvectors)

B = np.array([[4, 2], [1, 1]])
eigval, eigvec = np.linalg.eig(B)
print("Eigenvalues of B (2x2 matrix):\n", eigval)
print("Eigenvectors of B (2x2 matrix):\n", eigvec)

# Matrix Decomposition: # Matrix decomposition is the process of breaking down a matrix into simpler, constituent matrices that can be more easily analyzed or manipulated.
# Common types of matrix decomposition include:
# 1. LU Decomposition: Decomposes a matrix into a lower triangular matrix (L) and an upper triangular matrix (U).
# 2. QR Decomposition: Decomposes a matrix into an orthogonal matrix (Q) and an upper triangular matrix (R).

# Singular Value Decomposition (SVD) is a factorization of a matrix into three matrices, revealing important properties such as rank, range, and null space.
# SVD is a powerful tool in linear algebra, particularly for dimensionality reduction and data compression.

U, S, Vt = np.linalg.svd(A)
print("U matrix from SVD:\n", U)  # U matrix from SVD
print("Singular values from SVD:\n", S)  # Singular values from SVD
print("Vt matrix from SVD:\n", Vt)  # Vt matrix from SVD