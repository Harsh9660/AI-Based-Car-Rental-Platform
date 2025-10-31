from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.models import Car
from ..ML.price_predictor import predict_price

router = APIRouter(prefix="/api/cars", tags=["cars"])

@router.get("/")
def get_cars(db: Session = Depends(get_db)):
    return db.query(Car).filter(Car.available == True).all()

@router.get("/{car_id}")
def get_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.get("/{car_id}/price")
def get_car_price(car_id: int, days: int, db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    
    predicted_price = predict_price(car, days)
    return {"car_id": car_id, "days": days, "predicted_price": predicted_price}