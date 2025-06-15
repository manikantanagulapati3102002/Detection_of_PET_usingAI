# api.py

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

app = FastAPI()

# Allow frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model = load_model("models/model.h5")

# Define class labels (update if you're not using cat/dog)
class_names = ['cat', 'dog']

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    processed_image = preprocess_image(image_bytes)
    prediction = model.predict(processed_image)[0][0]
    label = class_names[int(prediction > 0.5)]
    confidence = float(prediction) if label == "dog" else 1 - float(prediction)
    return {"class": label, "confidence": round(confidence, 2)}
