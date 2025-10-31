import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
np.random.seed(42)
random.seed(42)

# === CONFIG ===
N_CARS = 10000
N_USERS = 2000
N_BOOKINGS = 15000
# ==============

# --- 1. Generate CARS ---
makes = ['Toyota','Honda','Ford','Tesla','BMW','Mercedes','Chevrolet','Nissan','Hyundai','Audi']
models = {'Sedan':['Camry','Civic','Accord','Corolla','Altima'], 'SUV':['RAV4','CR-V','Explorer','Model Y','X5'], 
          'Truck':['F-150','Silverado','Ram 1500'], 'Sports':['Mustang','Challenger','911']}
locations = ['New York','Los Angeles','Chicago','Miami','Seattle','Dallas','Boston','Denver','Phoenix','Atlanta']
fuel_types = ['Gas','Electric','Hybrid','Diesel']
features_pool = ['AC','GPS','Bluetooth','Sunroof','Leather','Backup Cam','Autopilot']

cars = []
for i in range(1, N_CARS + 1):
    cat = random.choice(list(models.keys()))
    cars.append({
        'car_id': i,
        'make': random.choice(makes),
        'model': random.choice(models[cat]),
        'year': random.randint(2018, 2025),
        'price_per_day': round(random.uniform(30, 250), 2),
        'mileage': random.randint(5000, 150000),
        'availability': random.choices([True, False], [0.7, 0.3])[0],
        'location': random.choice(locations),
        'fuel_type': random.choice(fuel_types),
        'category': cat,
        'transmission': random.choice(['Automatic','Manual']),
        'seats': random.choice([4,5,7]),
        'horsepower': random.randint(150, 600),
        'features': ', '.join(random.sample(features_pool, random.randint(2,5))),
        'image_url': fake.image_url(width=600, height=400),
        'rating': round(random.uniform(3.5, 5.0), 1),
        'bookings_count': random.randint(0, 300),
        'predicted_price': 0  # placeholder
    })

df_cars = pd.DataFrame(cars)
df_cars['predicted_price'] = df_cars['price_per_day'] * (1 + np.random.normal(0, 0.15, N_CARS))
df_cars.to_csv('cars.csv', index=False)
print(f"Generated cars.csv ({len(df_cars):,} rows)")

# --- 2. Generate USERS ---
users = []
tiers = ['Bronze','Silver','Gold','Platinum']
for i in range(1, N_USERS + 1):
    users.append({
        'user_id': i,
        'username': fake.user_name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'location': random.choice(locations),
        'preferred_fuel': random.choice(fuel_types),
        'preferred_category': random.choice(list(models.keys())),
        'loyalty_tier': random.choices(tiers, [0.4, 0.3, 0.2, 0.1])[0],
        'total_spent': round(random.uniform(0, 10000), 2),
        'join_date': fake.date_between(start_date='-3y', end_date='today'),
        'last_login': fake.date_time_this_month()
    })

pd.DataFrame(users).to_csv('users.csv', index=False)
print(f"Generated users.csv ({len(users):,} rows)")

# --- 3. Generate BOOKINGS ---
bookings = []
statuses = ['completed','upcoming','cancelled']
for i in range(1, N_BOOKINGS + 1):
    car = random.choice(cars)
    user = random.choice(users)
    days = random.randint(1, 7)
    start = fake.date_between(start_date='-6m', end_date='+3m')
    end = start + timedelta(days=days)
    price = car['price_per_day'] * days * random.uniform(0.8, 1.2)
    bookings.append({
        'booking_id': i,
        'user_id': user['user_id'],
        'car_id': car['car_id'],
        'start_date': start,
        'end_date': end,
        'total_price': round(price, 2),
        'status': random.choices(statuses, [0.7, 0.2, 0.1])[0],
        'pickup_location': car['location'],
        'return_location': car['location'],
        'created_at': fake.date_time_between(start_date='-6m', end_date='now')
    })

pd.DataFrame(bookings).to_csv('bookings.csv', index=False)
print(f"Generated bookings.csv ({len(bookings):,} rows)")

print("\nAll CSVs generated: cars.csv, users.csv, bookings.csv")