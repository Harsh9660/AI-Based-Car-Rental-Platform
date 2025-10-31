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
        Car(make="Toyota", model="Corolla", year=2022, price_per_day=45.0, available=True),
        Car(make="Honda", model="Civic", year=2023, price_per_day=50.0, available=True),
        Car(make="BMW", model="X3", year=2021, price_per_day=85.0, available=True),
        Car(make="Tesla", model="Model 3", year=2023, price_per_day=95.0, available=True),
    ]
    
    db.add_all(cars)
    db.commit()
    print("Database seeded with sample cars")
    db.close()

if __name__ == "__main__":
    seed_database()