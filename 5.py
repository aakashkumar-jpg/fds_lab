import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
db = pd.read_csv("diabetes.csv")

# 1. Initial Exploration
print(db.head())
print(db.info())
print(db.describe())

# 2. Histogram Visualization
db.hist(bins=50, figsize=(20, 15))
plt.show()

# 3. Pairplot Visualization
sns.pairplot(db)
plt.show()