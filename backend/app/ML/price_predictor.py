import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

class PricePredictor:
    def __init__(self, model_path="data/models/price_model.pkl"):
        self.model_path = model_path
        self.model = None
        self.load_model()
    
    def load_model(self):
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
        else:
            self.train_model()
    
    def train_model(self):
        try:
            df = pd.read_csv('data/raw/cars.csv')
            df = df.dropna()
            
            features = ['year', 'mileage', 'seats', 'horsepower', 'bookings_count']
            X = df[features]
            y = df['predicted_price']
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
            self.model.fit(X_train, y_train)
            
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            joblib.dump(self.model, self.model_path)
            
            mae = mean_absolute_error(y_test, self.model.predict(X_test))
            print(f"Model trained with MAE: {mae:.2f}")
        except Exception as e:
            print(f"Error training model: {e}")
            self.model = None
    
    def predict(self, features):
        if self.model is None:
            return 50.0
        return self.model.predict([features])[0]

predictor = PricePredictor()

def predict_price(car, days):
    features = [car.year, 50000, 5, 150, 10]
    base_price = predictor.predict(features)
    return base_price * days