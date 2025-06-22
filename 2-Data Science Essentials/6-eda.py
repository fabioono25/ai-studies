# Exploration Data Analysis (EDA): Techniques to explore and analyze data to summarize its main characteristics, often using visual methods.
# EDA: Techniques to explore and analyze data to summarize its main characteristics, often using visual methods.
# Steps in EDA:
# 1. Data Cleaning: Handling missing values, duplicates, and inconsistencies.
# 2. Data Transformation: Normalization, scaling, and encoding categorical variables.
# 3. Data Visualization: Creating plots to understand data distributions and relationships.
# 4. Statistical Analysis: Calculating summary statistics and correlations.

# https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv


# Step 1: Perform data cleaning, aggregation and filtering

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Load the Titanic dataset
df = pd.read_csv(
    'https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')

# inspect data
print(df.info())  # Display DataFrame info
print(df.head())  # Display first 5 rows

# Handle missing values
# Fill missing Age with median
df["Age"].fillna(df["Age"].median(), inplace=True)
# Fill missing Embarked with mode (mode: most common value)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Filter data: Passengers in first class
first_class_passengers = df[df['Pclass'] == 1]
print("First class passengers:\n", first_class_passengers.head())

# Step 2: Generate Visualizations to Illustrate Key Insights

# Bar Chart: Survival rate by class
# survival_rate_by_class = df.groupby('Pclass')['Survived'].mean()
# survival_rate_by_class.plot(kind='bar', color='skyblue')
# plt.title('Survival Rate by Class')
# plt.xlabel('Passenger Class')
# plt.ylabel('Survival Rate')
# plt.xticks(rotation=0)
# plt.show()

# Histogram: Age distribution of passengers
# sns.histplot(df['Age'], bins=30, kde=True, color='purple')
# plt.title('Age Distribution of Passengers')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()

# Scatter Plot: Age vs Fare
# sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived', alpha=0.6)
plt.scatter(df['Age'], df['Fare'], c=df['Survived'],
            cmap='coolwarm', alpha=0.6)
plt.title('Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.colorbar(label='Survived')
plt.show()

# Step 3: Identify and Interpret Patterns or Anomalies

# Step 4: Summarize Findings in a Report

# Summary of Findings
summary = {
    "Total Passengers": len(df),
    "Total Survived": df['Survived'].sum(),
    "Survival Rate": df['Survived'].mean(),
    "Average Age": df['Age'].mean(),
    "Most Common Embarked Port": df['Embarked'].mode()[0],
}
print("Summary of Findings:")
for key, value in summary.items():
    print(f"{key}: {value}")

# Step 5: Save the cleaned data to a new CSV file
df.to_csv('cleaned_titanic_data.csv', index=False)
print("Cleaned data saved to 'cleaned_titanic_data.csv'")
