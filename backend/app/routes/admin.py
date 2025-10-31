from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from ..database import get_db
from ..models.models import Car, Booking, User           

router = APIRouter(prefix="/api/admin", tags=["admin"])

class CarCreate(BaseModel):
    make: str
    model: str
    year: int
    price_per_day: float
    available: bool = True

class CarUpdate(BaseModel):
    make: str = None
    model: str = None
    year: int = None
    price_per_day: float = None
    available: bool = None

@router.post("/cars")
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@router.put("/cars/{car_id}")
def update_car(car_id: int, car: CarUpdate, db: Session = Depends(get_db)):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    
    for field, value in car.dict(exclude_unset=True).items():
        setattr(db_car, field, value)
    
    db.commit()
    db.refresh(db_car)
    return db_car

@router.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    
    db.delete(db_car)
    db.commit()
    return {"message": "Car deleted"}

@router.get("/bookings")
def get_all_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).all()

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()