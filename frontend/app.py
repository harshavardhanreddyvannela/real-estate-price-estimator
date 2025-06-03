import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
import os

# ==============================
# 💄 Custom CSS for Clean Layout
# ==============================
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding: 1rem 1rem 1rem 1rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        padding: 0.6rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ======================
# 🚀 App Title and Intro
# ======================
st.markdown("<h2 style='text-align: center;'>🏡 Real Estate Price Estimator</h2>", unsafe_allow_html=True)

# ===================
# 🌍 Interactive Map
# ===================
st.markdown("#### 📍 Choose Property Location")

# Initialize map
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)
map_data = st_folium(m, height=300, width="100%")

# Get coordinates from map click or use default
if map_data and map_data.get("last_clicked"):
    coords = map_data["last_clicked"]
else:
    coords = {"lat": 40.7128, "lng": -74.0060}

# Display chosen coordinates
st.info(f"📌 Selected Location: Latitude: `{coords['lat']:.5f}`, Longitude: `{coords['lng']:.5f}`")

# ============================
# 🏘️ Responsive Input Form
# ============================
st.markdown("#### 🏘️ Property Details")

# Detect screen size for responsive layout
is_mobile = st.runtime.scriptrunner.get_script_run_context().session_info.client.display_width < 768

if is_mobile:
    area = st.number_input("Area (sqft)", value=1000, step=50)
    bedrooms = st.slider("Bedrooms", 1, 10, 3)
    bathrooms = st.slider("Bathrooms", 1, 5, 2)
    stories = st.slider("Stories", 1, 3, 1)
    parking = st.slider("Parking", 0, 5, 1)
else:
    col1, col2 = st.columns(2)
    with col1:
        area = st.number_input("Area (sqft)", value=1000, step=50)
        bedrooms = st.slider("Bedrooms", 1, 10, 3)
        stories = st.slider("Stories", 1, 3, 1)
    with col2:
        bathrooms = st.slider("Bathrooms", 1, 5, 2)
        parking = st.slider("Parking", 0, 5, 1)

# ===================
# 🔮 Prediction Button
# ===================
st.markdown("### ")
if st.button("🔍 Predict Price"):
    payload = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "parking": parking,
        "location": f"{coords['lat']},{coords['lng']}"
    }
    url = os.getenv("BACKEND_URL", "https://real-estate-backend-c8g2.onrender.com/predict")
    try:
        r = requests.post(url, json=payload)
        if r.status_code == 200:
            st.success(f"💰 Estimated Price: ${r.json()['predicted_price']}")
        else:
            st.error("❌ Prediction failed. Try again later.")
    except Exception as e:
        st.error(f"⚠️ Backend error: {e}")
