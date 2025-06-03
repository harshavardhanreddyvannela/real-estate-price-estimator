import streamlit as st
import requests
import os

# 💄 Custom CSS for Layout & Inputs
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding: 1rem;
    }
    input[type="number"] {
        width: 100% !important;
        max-width: 200px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        padding: 0.6rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 🚀 App Title and Intro
st.markdown("<h2 style='text-align: center;'>🏡 Boston Housing Price Estimator</h2>", unsafe_allow_html=True)
st.markdown("#### 🏘️ Enter Property Features")

# 🧾 Input Features in Two Columns
col1, col2 = st.columns(2)

with col1:
    CRIM = st.number_input("CRIM (crime rate)", min_value=0.0, value=0.1, format="%.5f")
    ZN = st.number_input("ZN (residential land)", min_value=0.0, value=0.0, format="%.2f")
    INDUS = st.number_input("INDUS (non-retail acres)", min_value=0.0, value=8.0, format="%.2f")
    CHAS = st.selectbox("CHAS (near Charles River)", options=[0, 1], index=0)
    NOX = st.number_input("NOX (nitric oxides)", min_value=0.0, max_value=1.0, value=0.5, format="%.4f")
    RM = st.number_input("RM (rooms per dwelling)", min_value=0.0, value=6.0, format="%.2f")
    AGE = st.number_input("AGE (% older homes)", min_value=0.0, max_value=100.0, value=50.0, format="%.2f")

with col2:
    DIS = st.number_input("DIS (to employment centers)", min_value=0.0, value=5.0, format="%.3f")
    RAD = st.number_input("RAD (highway access)", min_value=1, max_value=24, value=4)
    TAX = st.number_input("TAX (property tax rate)", min_value=0, value=300)
    PTRATIO = st.number_input("PTRATIO (pupil-teacher ratio)", min_value=0.0, value=15.0, format="%.2f")
    B = st.number_input("B (proportion of Black residents)", min_value=0.0, value=400.0, format="%.2f")
    LSTAT = st.number_input("LSTAT (% lower status)", min_value=0.0, max_value=40.0, value=10.0, format="%.2f")

# 🔮 Prediction Button
st.markdown("### ")
if st.button("🔍 Predict Price"):
    payload = {
        "CRIM": CRIM, "ZN": ZN, "INDUS": INDUS, "CHAS": CHAS, "NOX": NOX, "RM": RM,
        "AGE": AGE, "DIS": DIS, "RAD": RAD, "TAX": TAX, "PTRATIO": PTRATIO, "B": B, "LSTAT": LSTAT
    }

    base_url = os.getenv("BACKEND_URL", "https://real-estate-backend-c8g2.onrender.com").rstrip("/")
    url = f"{base_url}/predict"

    try:
        r = requests.post(url, json=payload)
        if r.status_code == 200:
            price = r.json().get("predicted_price")
            st.success(f"💰 Estimated Price: ${price * 1000:,.2f}")
        else:
            st.error(f"❌ Prediction failed (status {r.status_code}): {r.text}")
    except Exception as e:
        st.error(f"⚠️ Backend error: {e}")
