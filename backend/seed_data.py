from app.database import SessionLocal, create_tables
from app.models.models import Car

def seed_database():
    create_tables()
    db = SessionLocal()
    
    # Check if data already exists
    if db.query(Car).count() > 0:
        print("Database already has data")
        return
    
    # Sample cars data
    cars = [
        Car(make="Toyota", model="Corolla", year=2022, price_per_day=45.0, available=True, 
            mileage=25000, seats=5, horsepower=139, bookings_count=15),
        Car(make="Honda", model="Civic", year=2023, price_per_day=50.0, available=True,
            mileage=15000, seats=5, horsepower=158, bookings_count=8),
        Car(make="BMW", model="X3", year=2021, price_per_day=85.0, available=True,
            mileage=35000, seats=5, horsepower=248, bookings_count=22),
        Car(make="Tesla", model="Model 3", year=2023, price_per_day=95.0, available=True,
            mileage=8000, seats=5, horsepower=283, bookings_count=12),
    ]
    
    db.add_all(cars)
    db.commit()
    print("Database seeded with sample cars")
    db.close()

if __name__ == "__main__":
    seed_database()