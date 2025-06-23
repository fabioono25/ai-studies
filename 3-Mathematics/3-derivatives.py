# What are Derivatives: Derivatives represent the rate of change of a function with respect to a variable.
# They are fundamental in calculus and are used to find slopes of curves, optimize functions, and model dynamic systems.
# The derivative of a function f(x) at a point x is defined as the limit of the average rate of change of the function as the interval approaches zero. Mathematically, it is expressed as:
# f'(x) = lim (h -> 0) [(f(x + h) - f(x)) / h]

import sympy as sp

x = sp.symbols('x')
f = x**2
derivative_f = sp.diff(f, x)
print("Derivative of f(x) = x^2 is:", derivative_f)

# Partial Derivatives: Partial derivatives are used when dealing with functions of multiple variables. They represent the rate of change of the function with respect to one variable while keeping the other variables constant.

a, y = sp.symbols('a y')
f = a**2 + y**2
grad_a = sp.diff(f, a)
grad_y = sp.diff(f, y)
print("Partial derivative of f(a, y) = a^2 + y^2 with respect to a is:", grad_a)
print("Partial derivative of f(a, y) = a^2 + y^2 with respect to y is:", grad_y)

# Gradient Descent: Gradient descent is an optimization algorithm used to minimize a function by iteratively moving in the direction of the steepest descent, which is given by the negative gradient of the function.

x = sp.symbols('x')
f = x**3 - 5*x + 7
derivative = sp.diff(f, x)
print("Derivative of f(x) = x^3 - 5*x + 7 is:", derivative)

