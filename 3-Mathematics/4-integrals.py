# Integrals: compute the area under a curve, representing the accumulation of quantities.
# Example of Integral: ∫_a^b f(x) dx, where f(x) is a function and [a, b] is the interval of integration.

import sympy as sp

x = sp.symbols('x')
f = x**2
definite_integral = sp.integrate(f, (x, 0, 2))  # Definite integral from 0 to 2
print("Definite integral of f(x) = x^2 from 0 to 2 is:", definite_integral)

indefinite_integral = sp.integrate(f, x)  # Indefinite integral
print("Indefinite integral of f(x) = x^2 is:", indefinite_integral)

# Stochastic Gradient Descent: A variant of gradient descent that uses a random subset of data to compute the gradient, making it more efficient for large datasets.
# It is particularly useful in machine learning and deep learning applications.

# Example of Stochastic Gradient Descent
import numpy as np
def stochastic_gradient_descent(X, y, learning_rate=0.01, epochs=1000):
    m = len(y)
    theta = np.zeros(X.shape[1])  # Initialize parameters
    for epoch in range(epochs):
        for i in range(m):
            gradient = (X[i].dot(theta) - y[i]) * X[i]  # Compute gradient
            theta -= learning_rate * gradient  # Update parameters
    return theta
  
# Example usage of Stochastic Gradient Descent
X = np.array([[1, 1], [1, 2], [1, 3]])  # Feature matrix (with bias term)
y = np.array([1, 2, 3])  # Target variable
theta = stochastic_gradient_descent(X, y)
print("Parameters learned by Stochastic Gradient Descent:", theta)