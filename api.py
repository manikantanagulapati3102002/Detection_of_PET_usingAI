# api.py

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

app = FastAPI()

# Allow frontend to access this API by enabling CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model = load_model("models/model.h5")

# Here we Defines output class names based on index (0: cat, 1: dog).
class_names = ['cat', 'dog']

# Here we Converts uploaded file into a preprocessed image ready for prediction.
def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

#post api
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read() # Reads uploaded file.
    processed_image = preprocess_image(image_bytes)
    prediction = model.predict(processed_image)[0][0] #Calls model.predict(...).
    label = class_names[int(prediction > 0.5)]
    confidence = float(prediction) if label == "dog" else 1 - float(prediction) #Determines class (cat or dog) based on output threshold.
    return {"class": label, "confidence": round(confidence, 2)}
#Returns class and confidence.
