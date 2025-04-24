import pandas as pd
import numpy as np

datasets = {}
palmerpenguins_db_url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/refs/heads/main/inst/extdata/penguins.csv"
heart_disease_db_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
heart_disease_columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num"]

datasets_items = ['palmerpenguins', 'heart-disease']
datasets[datasets_items[0]] = pd.read_csv(palmerpenguins_db_url)
datasets[datasets_items[1]] = pd.read_csv(heart_disease_db_url, names=heart_disease_columns, na_values='?')

print(datasets)

heart_disease_db = datasets[datasets_items[1]]
# X = heart_disease_db.drop(['num'], axis=1)
# y = heart_disease_db['num']

from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5)
X_train, X_test = train_test_split(heart_disease_db,test_size=0.5)
print(X_train, '\n', X_test)