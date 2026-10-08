import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
dataset = pd.read_csv('50_Startups.csv')
print("Dataset Head:\n", dataset.head())
print("\nDataset Info:")
dataset.info()

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Encode categorical data (State column at index 3)
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Avoiding Dummy Variable Trap (remove one dummy column)
X = X[:, 1:]

# Split the dataset into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Fit Multiple Linear Regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict test results
y_pred = regressor.predict(X_test)

print("\nModel Training R^2 Score:", regressor.score(X_train, y_train))
print("Model Testing R^2 Score:", regressor.score(X_test, y_test))
print("\nCoefficients:", regressor.coef_)
print("Intercept:", regressor.intercept_)

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\nActual vs Predicted Profit:\n", comparison)