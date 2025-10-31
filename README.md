# AI-Based Car Rental Platform

A modern car rental platform with AI-powered price prediction and fraud detection.

## Features

- **AI Price Prediction**: Machine learning model predicts rental prices
- **Modern API**: FastAPI backend with SQLAlchemy ORM
- **React Frontend**: Clean UI with Tailwind CSS
- **Database**: SQLite for development, easily configurable for production

## Quick Start

### Backend Setup
```bash
cd backend
pip install -r ../requirements.txt
python main.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

- `GET /api/cars` - List available cars
- `GET /api/cars/{id}` - Get car details
- `GET /api/cars/{id}/price?days=X` - Get predicted price

## Project Structure

```
├── backend/
│   ├── app/
│   │   ├── ML/           # Machine learning models
│   │   ├── models/       # Database models
│   │   ├── routes/       # API routes
│   │   └── config.py     # Configuration
│   └── main.py          # FastAPI app
├── frontend/
│   └── src/
│       └── App.jsx      # React app
└── data/               # Dataset and trained models
```