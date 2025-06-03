import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
import os

st.title("🏡 Real Estate Price Estimator")

# Map
st.subheader("📍 Choose location")
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)
map_data = st_folium(m, height=400)
coords = map_data.get("last_clicked", {"lat": 40.7128, "lng": -74.0060})

# Input
st.subheader("🏘️ Property Details")
area = st.number_input("Area (sqft)", value=1000)
bedrooms = st.slider("Bedrooms", 1, 10, 3)
bathrooms = st.slider("Bathrooms", 1, 5, 2)
stories = st.slider("Stories", 1, 3, 1)
parking = st.slider("Parking", 0, 5, 1)

if st.button("Predict Price"):
    payload = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "parking": parking,
        "location": f"{coords['lat']},{coords['lng']}"
    }
    url = os.getenv("BACKEND_URL", "http://localhost:8000/predict")
    r = requests.post(url, json=payload)
    if r.status_code == 200:
        st.success(f"💰 Estimated Price: ${r.json()['predicted_price']}")
    else:
        st.error("Prediction failed.")