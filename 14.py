import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler

df = pd.read_csv('pre-process_datasample.csv')
print("Initial Dataset:\n", df)

# Impute missing Country with mode
df['Country'] = df['Country'].fillna(df['Country'].mode()[0])

features = df.iloc[:, :-1].values
label = df.iloc[:, -1].values

# Impute missing numerical values using Mean
imputer = SimpleImputer(strategy="mean", missing_values=np.nan)
features[:, [1]] = imputer.fit_transform(features[:, [1]])
features[:, [2]] = imputer.fit_transform(features[:, [2]])
print("\nFeatures after Imputation:\n", features)

# One-hot encode Country
oh = OneHotEncoder(sparse_output=False)
country_encoded = oh.fit_transform(features[:, [0]])

# Concatenate encoded features with Age and Salary
final_set = np.concatenate((country_encoded, features[:, [1, 2]]), axis=1)
print("\nFinal Feature Set before Scaling:\n", final_set)

# 1. Standard Scaler
sc = StandardScaler()
feat_standard_scaler = sc.fit_transform(final_set)
print("\nStandard Scaled Features:\n", feat_standard_scaler)

# 2. MinMax Scaler
mms = MinMaxScaler(feature_range=(0, 1))
feat_minmax_scaler = mms.fit_transform(final_set)
print("\nMinMax Scaled Features:\n", feat_minmax_scaler)