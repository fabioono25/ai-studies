# Linear Regression: A statistical method for modeling the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data.

# Applying Linear Algebra, Calculus and Statistics to Linear Regression

# Gradient Descent Algorithm: An optimization algorithm used to minimize the cost function in linear regression by iteratively adjusting the model parameters in the direction of the steepest descent.
# Steps:
# 1. Initialize the model parameters (weights) randomly.
# 2. For each iteration:
#    a. Compute the predicted values using the current model parameters.
#    b. Calculate the cost (loss) function, which measures the difference between predicted and actual values.
#    c. Compute the gradients (partial derivatives) of the cost function with respect to each model parameter.
#    d. Update the model parameters by moving them in the opposite direction of the gradients (gradient descent step).
# 3. Repeat until convergence (i.e., when the cost function is minimized).

# Evaluate the model using MSE (Mean Squared Error) and R-squared metrics.

import numpy as np

# Generate syntetic data
np.random.seed(42)  # For reproducibility
X = 2 * np.random.rand(100, 1)  # 100 samples
y = 4 + 3 * X + np.random.randn(100, 1)  # Linear relation with noise

# add a bias term (intercept) to the input features
X_b = np.c_[np.ones((100, 1)), X]

# Initialize model parameters (theta)
theta = np.random.randn(2, 1)  # Random initialization for two parameters (intercept and slope)
learning_rate = 0.1
iterations = 1000  # Number of iterations for gradient descent

# 1 - Implement the Mathematical Formula for Linear Regression

def predict(X, theta):
  return np.dot(X, theta)

# 2 - Use Gradient Descent to Optimize the Model Parameters
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)  # Number of training examples
    for _ in range(iterations):
        gradients = (1/m) * np.dot(X.T, np.dot(X, theta) - y)  # Compute gradients
        theta -= learning_rate * gradients  # Update parameters
    return theta
  
# 3 - Calculate the Valuation Metrics
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)
  
def r_squared(y_true, y_pred):
    ss_residual = np.sum((y_true - y_pred) ** 2)  # Residual sum of squares
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)  # Total sum of squares
    return 1 - (ss_residual / ss_total)  # R-squared value
  
# Perform gradient descent to optimize the model parameters
theta_optimal = gradient_descent(X_b, y, theta, learning_rate, iterations)

# Predictions and evaluation
y_pred = predict(X_b, theta_optimal)

# Calculate evaluation metrics
mse = mean_squared_error(y, y_pred)
r2 = r_squared(y, y_pred)

print("Optimal Parameters (Theta):\n", theta_optimal)
print("Mean Squared Error (MSE):", mse)
print("R-squared (R2):", r2)

# Visualize the results
import matplotlib.pyplot as plt
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, y_pred, color='red', label='Linear Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Fit')
plt.legend()
plt.show()

