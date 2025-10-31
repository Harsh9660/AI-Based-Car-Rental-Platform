import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load processed training data
data = pd.read_csv("data/processed/bookings_train.csv")

X = data[['car_id_numeric', 'rental_duration', 'demand_index']] 
y = data['price']

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "data/models/price_predictor.pkl")
print("Price prediction model trained and saved.")