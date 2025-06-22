# Pandas: Data Analysis Library for Python.
# Capable of handling large datasets, performing complex data manipulations, and providing powerful data analysis tools.
import pandas as pd

# Series: One-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.)
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print("Pandas Series:\n", s)

# DataFrame: Two-dimensional labeled data structure with columns of potentially different types
# Similar to a spreadsheet or SQL table, or a dict of Series objects
data = {
    'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("Pandas DataFrame:\n", df)

# read CSV file into a DataFrame
df_csv = pd.read_csv('data.csv')  # Ensure 'data.csv' exists in the current directory
df_csv.to_excel('data.xlsx', index=False)  # Save DataFrame to Excel file
print("DataFrame from CSV:\n", df_csv)

# Viewing Data
print("First 5 rows of DataFrame:\n", df.head())  # Display first 5 rows
print("Last 5 rows of DataFrame:\n", df.tail(2))  # Display last 2 rows
print("DataFrame Info:\n", df.info())  # Display DataFrame info
print("DataFrame Description:\n", df.describe())  # Display summary statistics

print("DataFrame Columns:\n", df.columns)  # Display DataFrame columns
print("DataFrame Index:\n", df.index)  # Display DataFrame index

# Accessing Data
print("Accessing a single column:\n", df['Name'])  # Access a single column
print("Accessing multiple columns:\n", df[['Name', 'Age']])  # Access multiple columns

# Selecting by Age > 20
print("Selecting rows where Age > 20:\n", df[df['Age'] > 30])  # Filter rows based on condition

print("Selecting rows by index:\n", df.iloc[0])  # Select row by index
print("Selecting rows by index range:\n", df.iloc[0:2])  # Select rows by index range

# Selecting by column and row labels
print("Selecting specific cell (row 0, column 'Name'):\n", df.at[0, 'Name'])  # Access specific cell
print("Selecting specific cell (row 0, column 1):\n", df.iloc[0, 1])  # Access specific cell by index

print("Selecting specific rows and columns:\n", df.loc[0:1, ['Name', 'Age']])  # Access specific rows and columns

