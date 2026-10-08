import numpy as np
import pandas as pd

df = pd.read_csv("pre-process_datasample.csv")
print("Original Dataset:\n", df)
print("\nDataset Info:")
print(df.info())

print("\nCountry Mode:\n", df['Country'].mode())
print("Most Frequent Country:", df['Country'].mode()[0])

df['Country'] = df['Country'].fillna(df['Country'].mode()[0])
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(round(df['Salary'].mean()))

print("\nDataset After Handling Missing Values:\n", df)

dummies = pd.get_dummies(df['Country'])
print("\nDummy Variables for Country:\n", dummies)

updated_dataset = pd.concat([pd.get_dummies(df['Country']), df.iloc[:, [1, 2, 3]]], axis=1)

updated_dataset['Purchased'] = updated_dataset['Purchased'].replace({'No': 0, 'Yes': 1})

print("\nFinal Preprocessed Dataset:\n", updated_dataset)
print("\nUpdated Dataset Info:")
print(updated_dataset.info())