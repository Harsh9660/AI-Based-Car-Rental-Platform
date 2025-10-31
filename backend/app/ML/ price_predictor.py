import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib


df = pd.read_csv('data/raw/cars.csv')
df = df.dropna()

print("Dataset loaded. Sample data:")
print(df.head())

print("\nDataset info:")
print(df.info())

# Features and target
features = ['year', 'mileage', 'seats', 'horsepower', 'bookings_count']
X = df[features]
y = df['predicted_price']   

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
x_label = x_train.columns.tolist()
y_label = 'predicted_price'