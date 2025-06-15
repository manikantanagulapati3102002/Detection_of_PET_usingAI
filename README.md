# AI-Based Image Classification Web App

This project is a full-stack AI web application that classifies images into categories (e.g., Cat or Dog).

## 🧠 Features
- Trained TensorFlow model
- FastAPI backend for prediction
- Flask frontend for image upload
- Displays prediction and confidence
- Clean UI with image preview, loader, and clear button

## 🚀 Getting Started

### 1. Install Requirements
```bash
pip install -r requirements.txt

### 2. Start FastAPI Backend
```bash
uvicorn api:app --reload

### 3.Start Flask Frontend
Open a second terminal:
```bash
python app.py

### 4. Open in Browser
Visit: http://127.0.0.1:5000(like this you may get one port number)