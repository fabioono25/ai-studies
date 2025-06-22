# Why Handling Missing Values: Because missing values can lead to biased results, inaccurate predictions, and reduced model performance.


# 1- Handling Missing Values: Techniques to handle missing values in datasets.
# drop, fill, interpolate, and replace methods.
import pandas as pd
import numpy as np

# Example: create or load a DataFrame before using it
# df = pd.read_csv('your_data.csv')
df = pd.DataFrame({
	'column_name': [1, np.nan, 3, 4, None],
	'old_name': [10, 20, np.nan, 40, 50]
})

df = df.dropna()  # Drop rows with any missing values
df = df.dropna(axis=1)  # Drop columns with any missing values
df = df.fillna(0)  # Fill missing values with 0

df["column_name"] = df["column_name"].fillna(df["column_name"].mean())  # Fill missing values with the mean of the column
df["column_name"] = df["column_name"].fillna(df["column_name"].median())  # Fill missing values with the median of the column
df["column_name"] = df["column_name"].fillna(df["column_name"].mode()[0])  # Fill missing values with the mode of the column

# mode: the most frequently occurring value in a column
# interpolate: fill missing values using interpolation

df.fillna(method='ffill', inplace=True)  # Forward fill: propagate the last valid observation forward
df.fillna(method='bfill', inplace=True)  # Backward fill: use the next valid observation to fill gaps

df["column_name"] = df["column_name"].replace({None: 0})  # Replace None with 0 in a specific column
df["column_name"] = df["column_name"].interpolate()  # Interpolate missing values in a specific column

print("DataFrame after dropping missing values:\n", df)

# 2 - Data Transformation: Techniques to transform data for better analysis.
# renaming columns, changing data types, and normalizing data.
df.rename(columns={'old_name': 'new_name'}, inplace=True)  # Rename columns

df["column_name"] = df["column_name"].astype(int)  # Change data type of a column to int
df["column_name"] = pd.to_datetime(df["column_name"])  # Convert a column to datetime type
df["column_name"] = df["column_name"].str.lower()  # Convert string column
df["column_name"] = df["column_name"].str.upper()  # Convert string column to uppercase

df["new_column"] = df["existing_column"] * 2 # Create a new column based on an existing column
df["new_column"] = df["column_name"].apply(lambda x: x * 2)  # Apply a function to a column

# combining and mergind DataFrames
df2 = pd.DataFrame({
    'new_name': [1, 2, 3, 4, 5],
    'another_column': ['A', 'B', 'C', 'D', 'E']
})

df_combined = pd.concat([df, df2], axis=0)  # Concatenate DataFrames along rows
df_combined = pd.concat([df, df2], axis=1)  # Concatenate DataFrames along columns
df_merged = pd.merge(df, df2, on='new_name', how='inner')  # Merge DataFrames on a common column

# merging with left join
df_merged_left = pd.merge(df, df2, on='new_name', how='left')  # Left join merge

# join DataFrames using index
df_joined = df.join(df2, how='inner')  # Join DataFrames on index

print("DataFrame after transformation:\n", df)