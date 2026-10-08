import numpy as np
import pandas as pd

# Creating a DataFrame from a list
sample_list = [[1, 'Smith', 50000], [2, 'Jones', 60000]]
df_list = pd.DataFrame(sample_list, columns=['Empd', 'Name', 'Salary'])
print("Initial DataFrame:")
print(df_list)
print("\nDataFrame Info:")
print(df_list.info())

# Working with Employee Data
data = {
    'emp id': [1, 2, 3, 4, 5, 6, 7],
    'name': [
        'SREE VARSSINI K S',
        'SREEMATHI B',
        'SREYA G',
        'SREYASKARI MULLAPUDI',
        'SRI AKASH U G',
        'SRI HARSHAVARDHANAN R',
        'SRI HARSHAVARDHANAN R'
    ],
    'salary': [5000, 6000, 7000, 5000, 8000, 3000, 6000]
}

df = pd.DataFrame(data)

print("\nEmployee Head:")
print(df.head())

print("\nEmployee Tail:")
print(df.tail())

print("\nSalary Series:")
print(df['salary'])

print("\nSummary Statistics of Salary:")
print("Mean:", df['salary'].mean())
print("Median:", df['salary'].median())
print("Mode:\n", df['salary'].mode())
print("Variance:", df['salary'].var())
print("Standard Deviation:", df['salary'].std())

print("\nNumerical Description:")
print(df.describe())

print("\nComplete Description (include='all'):")
print(df.describe(include='all'))

print("\nColumns:", df.columns)
print("\nUnderlying Array Values:\n", df.values)