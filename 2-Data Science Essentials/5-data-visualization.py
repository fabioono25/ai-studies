# Data Visualization: Techniques to visualize data using various libraries.

# Matplotlib: A comprehensive library for creating static, animated, and interactive visualizations in Python.
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example data
x = [1, 2, 3, 4, 5]
y = [20, 35, 30, 35, 27]

# plt.plot(x, y, linestyle='--', marker='o', color='blue', alpha=0.7, label='Line Data')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Plot Example')
# plt.show()

# bar chart
# x = ['A', 'B', 'C', 'D', 'E']
# y = [20, 35, 30, 35, 27]
# plt.bar(x, y, color='green', alpha=0.7)
# plt.show()

# histogram
# data = np.random.randn(1000)  # Generate random data
# plt.hist(data, bins=30, color='blue', alpha=0.7)
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.title('Histogram Example')
# plt.show()

# Scatter plot
# x = np.random.rand(100)  # Generate random x values
# y = np.random.rand(100)  # Generate random y values
# plt.scatter(x, y, color='red', alpha=0.5)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Scatter Plot Example')
# plt.legend(['Data Points'])
# plt.grid(True)
# plt.show()

# Seaborn: A statistical data visualization library based on Matplotlib.
# Advantages over Matplotlib:
# 1. Easier to create complex visualizations with less code.
# 2. Built-in themes and color palettes for better aesthetics.

data = np.random.rand(5, 5)  # Generate random data for heatmap
# sns.heatmap(data, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='black')
# plt.title('Heatmap Example')
# plt.show()

# Pairplot with different markers and color palette
sns.pairplot(pd.DataFrame(data))
plt.title('Pairplot Example')
plt.show()
