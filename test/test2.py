import pandas as pd

# This is a commonly used, cleaned version of the heart disease dataset
url = "https://raw.githubusercontent.com/robolyst/studyforrest/master/datasets/heart-disease-uci/heart.csv"
heart_data = pd.read_csv(url)

# Check the data
print(heart_data.head())
print(heart_data.info())