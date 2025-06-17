# AI-Based Image Classification Web App

This project is a full-stack AI web application that classifies images into categories (e.g., Cat or Dog).

## 🧠 Features
- Trained TensorFlow model
- FastAPI backend for prediction
- Flask frontend for image upload
- Displays prediction and confidence
- Clean UI with image preview, loader, and clear button

Here's a complete README.md file you can use for your image classifier project. It explains each component, how to run it, and provides full documentation suitable for GitHub or personal deployment.

📄 README.md — Cat vs Dog Image Classifier

# 🐱🐶 Image Classifier (Cats vs Dogs)

A simple full-stack machine learning project to classify images of cats and dogs using TensorFlow, FastAPI, and Flask.

* 📦 Model: Convolutional Neural Network (CNN) with Keras/TensorFlow
* 🔙 Backend API: FastAPI
* 🌐 Frontend Web UI: Flask + Bootstrap
* 🗂 Data: Cat/Dog image dataset (custom split)

---

## 🚀 Project Structure

```
image_classifier_project/
├── api.py                 # FastAPI backend
├── app.py                 # Flask frontend
├── models/
│   └── model.h5           # Trained CNN model
├── dataset/
│   ├── train/
│   ├── validation/
├── templates/
│   └── index.html         # HTML frontend (Bootstrap)
├── static/
│   └── style.css          # Optional styles
├── train_model.py         # Script to train CNN model
├── requirements.txt       # All dependencies
└── README.md              # This file
```


## ⚙️ Setup Instructions

### 1. Clone & Set Up

```bash
git clone https://github.com/yourusername/image-classifier.git

cd image-classifier

python -m venv venv

venv\Scripts\activate  # Windows


pip install -r requirements.txt
```

### 2. Prepare Dataset

Organize dataset like this:

```
dataset/
├── train/
│   ├── cat/
│   └── dog/
├── validation/
│   ├── cat/
│   └── dog/
```

Split training/validation manually or use:

```powershell
# PowerShell example
Get-ChildItem -Path .\dataset\train\cat\*.jpg | Sort-Object LastWriteTime -Descending | Select-Object -First 30 | ForEach-Object { Copy-Item $_.FullName .\dataset\validation\cat\ }
Get-ChildItem -Path .\dataset\train\dog\*.jpg | Sort-Object LastWriteTime -Descending | Select-Object -First 30 | ForEach-Object { Copy-Item $_.FullName .\dataset\validation\dog\ }
```

### 3. Train Model

```bash
python train_model.py
```

The trained model is saved as models/model.h5

---

## 🔙 Run Backend (FastAPI)

```bash
uvicorn api:app --reload
```

Runs on [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🌐 Run Frontend (Flask UI)

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

Upload a cat/dog image to get prediction!

---

## 🧪 API Reference

📮 POST /predict

* Accepts: multipart/form-data with image file
* Returns: JSON with prediction & confidence


## 🛠 Dependencies

Main libraries:

* fastapi
* uvicorn
* flask
* tensorflow
* keras
* python-multipart
* pillow
* requests

Install via:

```bash
pip install -r requirements.txt
```

'''

### 1. Install Requirements

```bash(terminal)

pip install -r requirements.txt

### 2. Start FastAPI Backend
```bash(terminal)
uvicorn api:app --reload

### 3.Start Flask Frontend
Open a second terminal:
```bash(terminal)
python app.py

### 4. Open in Browser
Visit: http://127.0.0.1:5000(like this you may get one port number)


'''
