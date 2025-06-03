from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

app = FastAPI()

# Allow all origins (for testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = joblib.load("model/model.joblib")

class House(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    parking: int
    location: str  # not used in model

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.post("/predict")
def predict_price(data: House):
    df = pd.DataFrame([{
        "area": data.area,
        "bedrooms": data.bedrooms,
        "bathrooms": data.bathrooms,
        "stories": data.stories,
        "parking": data.parking
    }])
    prediction = model.predict(df)[0]
    return {"predicted_price": round(prediction, 2)}
