import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print("First 5 rows:\n", tips.head())

sns.displot(tips['total_bill'], kde=True)
plt.title('Distribution of Total Bill (with KDE)')
plt.show()

sns.displot(tips['total_bill'], kde=False)
plt.title('Distribution of Total Bill (without KDE)')
plt.show()

sns.jointplot(x='tip', y='total_bill', data=tips)
plt.show()

sns.jointplot(x='tip', y='total_bill', data=tips, kind='reg')
plt.show()

sns.jointplot(x='tip', y='total_bill', data=tips, kind='hex')
plt.show()

sns.pairplot(tips)
plt.show()

print("\nTime Value Counts:\n", tips['time'].value_counts())

sns.pairplot(tips, hue='time')
plt.show()

sns.pairplot(tips, hue='day')
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

sns.boxplot(x=tips['total_bill'])
plt.title('Boxplot of Total Bill')
plt.show()

sns.boxplot(x=tips['tip'])
plt.title('Boxplot of Tip')
plt.show()

sns.countplot(x='day', data=tips)
plt.title('Count of Records by Day')
plt.show()

sns.countplot(x='sex', data=tips)
plt.title('Count of Records by Sex')
plt.show()

tips['sex'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Sex Distribution (Pie Chart)')
plt.ylabel('')
plt.show()

tips['sex'].value_counts().plot(kind='bar')
plt.title('Sex Distribution (Bar Chart)')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()

sns.countplot(x='day', data=tips[tips['time'] == 'Dinner'])
plt.title('Dinner Counts by Day')
plt.show()