import streamlit as st
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
st.markdown("<h2 style='text-align: center;'>🏡 Boston Housing Price Estimator</h2>", unsafe_allow_html=True)

# ============================
# 🏘️ Property Input Form (Boston Housing Features)
# ============================
st.markdown("#### 🏘️ Property Features")

CRIM = st.number_input("CRIM (per capita crime rate)", min_value=0.0, value=0.1, format="%.5f")
ZN = st.number_input("ZN (proportion residential land zoned)", min_value=0.0, value=0.0, format="%.2f")
INDUS = st.number_input("INDUS (proportion non-retail acres)", min_value=0.0, value=8.0, format="%.2f")
CHAS = st.selectbox("CHAS (bounds Charles River)", options=[0, 1], index=0)
NOX = st.number_input("NOX (nitric oxides concentration)", min_value=0.0, max_value=1.0, value=0.5, format="%.4f")
RM = st.number_input("RM (average rooms per dwelling)", min_value=0.0, value=6.0, format="%.2f")
AGE = st.number_input("AGE (proportion older homes)", min_value=0.0, max_value=100.0, value=50.0, format="%.2f")
DIS = st.number_input("DIS (distance to employment centers)", min_value=0.0, value=5.0, format="%.3f")
RAD = st.number_input("RAD (accessibility to highways)", min_value=1, max_value=24, value=4)
TAX = st.number_input("TAX (property tax rate per $10,000)", min_value=0, value=300)
PTRATIO = st.number_input("PTRATIO (pupil-teacher ratio by town)", min_value=0.0, value=15.0, format="%.2f")
B = st.number_input("B (proportion of blacks by town)", min_value=0.0, value=400.0, format="%.2f")
LSTAT = st.number_input("LSTAT (% lower status of population)", min_value=0.0, max_value=40.0, value=10.0, format="%.2f")

# ===================
# 🔮 Prediction Button
# ===================
st.markdown("### ")
if st.button("🔍 Predict Price"):
    payload = {
        "CRIM": CRIM,
        "ZN": ZN,
        "INDUS": INDUS,
        "CHAS": CHAS,
        "NOX": NOX,
        "RM": RM,
        "AGE": AGE,
        "DIS": DIS,
        "RAD": RAD,
        "TAX": TAX,
        "PTRATIO": PTRATIO,
        "B": B,
        "LSTAT": LSTAT
    }
    url = os.getenv("BACKEND_URL", "https://real-estate-backend-c8g2.onrender.com/predict")
    try:
        r = requests.post(url, json=payload)
        if r.status_code == 200:
            price = r.json().get("predicted_price")
            st.success(f"💰 Estimated Price: ${price * 1000:,.2f}")  # MEDV is in $1000 units
        else:
            st.error(f"❌ Prediction failed. Status code: {r.status_code}")
    except Exception as e:
        st.error(f"⚠️ Backend error: {e}")
