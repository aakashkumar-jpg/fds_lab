import numpy as np
import pandas as pd

df = pd.read_csv("Hotel_Dataset.csv")
print("Original Dataset:\n", df)

print("\nDuplicate Rows Check:\n", df.duplicated())

df.drop_duplicates(inplace=True)
print("\nAfter Dropping Duplicates:\n", df)

df.reset_index(drop=True, inplace=True)

df.drop(['Age_Group.1'], axis=1, inplace=True)
print("\nAfter Dropping Redundant Column:\n", df)

df.loc[df['CustomerID'] < 0, 'CustomerID'] = np.nan
df.loc[df['Bill'] < 0, 'Bill'] = np.nan
df.loc[df['EstimatedSalary'] < 0, 'EstimatedSalary'] = np.nan
df.loc[(df['Rating(1-5)'] < 1) | (df['Rating(1-5)'] > 5), 'Rating(1-5)'] = np.nan
df.loc[(df['NoOfPax'] < 1) | (df['NoOfPax'] > 20), 'NoOfPax'] = np.nan

df['Hotel'] = df['Hotel'].replace(['Ibys'], 'Ibis')
df['FoodPreference'] = df['FoodPreference'].replace(['Vegetarian', 'veg'], 'Veg')
df['FoodPreference'] = df['FoodPreference'].replace(['non-Veg'], 'Non-Veg')

df['EstimatedSalary'] = df['EstimatedSalary'].fillna(round(df['EstimatedSalary'].mean()))
df['NoOfPax'] = df['NoOfPax'].fillna(round(df['NoOfPax'].median()))
df['Rating(1-5)'] = df['Rating(1-5)'].fillna(round(df['Rating(1-5)'].median()))
df['Bill'] = df['Bill'].fillna(round(df['Bill'].mean()))

print("\nCleaned and Processed Dataset:\n", df)