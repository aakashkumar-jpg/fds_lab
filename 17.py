import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('Salary_data.csv')
print("Dataset Head:\n", df.head())
print("\nDataset Info:")
df.info()

df.dropna(inplace=True)
print("\nSummary Statistics:\n", df.describe())

features = df.iloc[:, [0]].values
label = df.iloc[:, [1]].values

x_train, x_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

print("\nTraining Score (R^2):", model.score(x_train, y_train))
print("Testing Score (R^2):", model.score(x_test, y_test))
print("Coefficient (Slope):", model.coef_)
print("Intercept:", model.intercept_)

with open('SalaryPred.model', 'wb') as f:
    pickle.dump(model, f)

with open('SalaryPred.model', 'rb') as f:
    loaded_model = pickle.load(f)

yr_of_exp = float(input("\nEnter Years of Experience: "))
yr_of_exp_np = np.array([[yr_of_exp]])
salary = loaded_model.predict(yr_of_exp_np)

print("Estimated Salary for {} years of experience is: {}".format(yr_of_exp, salary))