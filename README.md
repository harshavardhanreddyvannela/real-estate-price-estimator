# 🏡 Boston Real Estate Price Estimator

A machine learning-powered web application to predict Boston housing prices based on property features.  
Built with **scikit-learn**, **FastAPI** (backend), and **Streamlit** (frontend).

---

## 🚀 Features

- Predicts property prices using the Boston Housing dataset
- Interactive web UI for user input and visualization
- REST API backend for model inference
- End-to-end ML pipeline: data preprocessing, model training, evaluation, and deployment
- Dockerized frontend and backend for easy deployment

---

## 🗂️ Project Structure

```
.
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── model/
│       └── model.joblib
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── model_training/
│   ├── data.csv
│   └── notebook.ipynb
└── README.md
```

---

## ⚙️ Setup & Usage

### 1. Clone the repository

```sh
git clone https://github.com/your-username/real-estate-price-estimator.git
cd real-estate-price-estimator
```

### 2. Train the Model

- Open `model_training/notebook.ipynb` and run all cells to preprocess data, train, evaluate, and export the model to `backend/model/model.joblib`.

### 3. Start the Backend API

```sh
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

### 4. Start the Frontend

```sh
cd ../frontend
pip install -r requirements.txt
streamlit run app.py
```

### 5. Using Docker (Optional)

Build and run both services using Docker:

```sh
# Backend
cd backend
docker build -t real-estate-backend .
docker run -p 8000:8000 real-estate-backend

# Frontend (in a new terminal)
cd ../frontend
docker build -t real-estate-frontend .
docker run -p 8501:8501 real-estate-frontend
```

---

## 🧑‍💻 API Reference

- **POST** `/predict`  
  Expects JSON with property features, returns predicted price.

---

## 📊 Model Training

- Data: Boston Housing dataset (`model_training/data.csv`)
- Preprocessing: Imputation, feature engineering, scaling (see `model_training/notebook.ipynb`)
- Model: RandomForestRegressor (best performance after comparison)
- Evaluation: Cross-validation and test set RMSE

---

## 📸 Sample Screenshot

![Sample UI Screenshot](![alt text](https://github.com/harshavardhanreddyvannela/real-estate-price-estimator/blob/Result.jpg?raw=true)
)

---

## 🌐 Live Demo

- [Frontend (Streamlit App)](https://real-estate-frontend-e6jn.onrender.com)

---

## 📚 References

- [scikit-learn documentation](https://scikit-learn.org/)
- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Streamlit documentation](https://docs.streamlit.io/)
- [Boston Housing Dataset](https://www.kaggle.com/datasets/altavish/boston-housing-dataset)

---

## 👤 Author

Harshavardhan Reddy  
Manipal Institute of Technology  
Email: harshavardhanr0710@gmail.com