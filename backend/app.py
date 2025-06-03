from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI()
model = joblib.load("model/model.joblib")

class House(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    parking: int
    location: str  # not used in model

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
