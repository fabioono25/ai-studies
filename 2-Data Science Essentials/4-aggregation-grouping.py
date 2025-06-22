# grouping data: grouping data by a specific column and performing aggregation functions like sum, mean, count, etc.

import pandas as pd
# Example DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles']
}
df = pd.DataFrame(data)
grouped = df.groupby('City').agg({
    'Age': ['mean', 'sum', 'count'],  # Aggregate Age column
    'Name': 'count'  # Count number of names in each city
}).reset_index()  # Reset index to get a clean DataFrame

print("Grouped DataFrame:\n", grouped)

grouped2 = df.groupby("City")

for name, group in grouped2:
    print(f"Group Name: {name}")
    print(group)
    
# grouped2.mean()  # Calculate mean of each group
# grouped2.sum()  # Calculate sum of each group

grouped3 = df.groupby("City")["Age"].mean()  # Calculate mean age for each city
print("Mean Age by City:\n", grouped3)

# pivot table: create a pivot table to summarize data
pivot_table = df.pivot_table(index='City', values='Age', aggfunc='mean')  # Create a pivot table to calculate mean age by city
print("Pivot Table:\n", pivot_table)

def range_func(x):
    return x.max() - x.min()  # Custom function to calculate range

grouped4 = df.groupby('City').agg({
    'Age': ['mean', 'sum', range_func]  # Aggregate Age column with custom range function
}).reset_index()  # Reset index to get a clean DataFrame
print("Grouped DataFrame with Custom Function:\n", grouped4)

# Summary Statistics for Grouped Data
summary_stats = df.groupby('City')["Age"].agg(range_func) # Calculate range of ages by city
print("Summary Statistics (Range of Ages by City):\n", summary_stats)
df.groupby('City')["Age"].mean()  # Calculate mean age by city
df.groupby('City')["Age"].sum()  # Calculate sum of ages by city    
df.groupby('City')["Age"].count()  # Count number of entries by city

print("Grouped DataFrame with Multiple Aggregations:\n", grouped)