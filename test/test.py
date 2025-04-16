from ucimlrepo import fetch_ucirepo
import pandas as pd

# fetch dataset
heart_disease = fetch_ucirepo(id=45)

# data (as pandas dataframes)
X = heart_disease.data.features
y = heart_disease.data.targets

# metadata
print(heart_disease.metadata)

print("Helo")

# variable information
print(heart_disease.variables)
df = pd.concat([X, y], axis=1)
print("X: ")
print(X)
print("y: ")
print(y)
print("DF: ")
print(df)
df.to_csv('heart_disease.csv', index=False)