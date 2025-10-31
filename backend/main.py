from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_tables
from app.routes.cars import router as cars_router

app = FastAPI(title="AI Car Rental Platform", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cars_router)

@app.on_event("startup")
def startup_event():
    create_tables()
    # Seed database with sample data
    from seed_data import seed_database
    seed_database()

@app.get("/")
def root():
    return {"message": "AI Car Rental Platform API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)