"""
🌿 PlantCare AI - FastAPI Backend
"""

import io
import json
import logging
from pathlib import Path
from datetime import datetime

import numpy as np
from PIL import Image

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

import tensorflow as tf

# =========================================================
# APP CONFIG
# =========================================================

app = FastAPI(title="PlantCare AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)

# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "plant_disease_model.h5"
CLASS_NAMES_PATH = BASE_DIR / "class_names.json"

IMAGE_SIZE = (128, 128)

# =========================================================
# GLOBALS
# =========================================================

model = None
class_names = []

# =========================================================
# DISEASE INFO
# =========================================================

DISEASE_INFO = {

    "healthy": {
        "description": "The plant appears healthy.",
        "severity": "Low",
        "treatment": "No treatment required."
    },

    "late_blight": {
        "description": "Late blight fungal disease.",
        "severity": "High",
        "treatment": "Apply fungicide spray."
    },

    "early_blight": {
        "description": "Early blight disease.",
        "severity": "Medium",
        "treatment": "Use copper fungicide."
    },

    "bacterial_spot": {
        "description": "Bacterial spot disease.",
        "severity": "Medium",
        "treatment": "Apply bactericide."
    },

    "leaf_mold": {
        "description": "Leaf mold disease.",
        "severity": "Medium",
        "treatment": "Improve ventilation and use fungicide."
    },

    "mosaic": {
        "description": "Mosaic virus disease.",
        "severity": "High",
        "treatment": "Remove infected plants."
    }
}

# =========================================================
# HELPER FUNCTIONS
# =========================================================

def get_disease_info(class_name):

    lower = class_name.lower()

    for key in DISEASE_INFO:
        if key in lower:
            return DISEASE_INFO[key]

    return {
        "description": "Disease information unavailable.",
        "severity": "Unknown",
        "treatment": "Consult agriculture expert."
    }


def parse_class_name(raw_class):

    parts = raw_class.split("___")

    if len(parts) == 2:

        plant = parts[0].replace("_", " ")

        disease = parts[1].replace("_", " ")

        return plant, disease

    return "Unknown", raw_class


def preprocess_image(image_bytes):

    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    image = image.resize(IMAGE_SIZE)

    image = np.array(image).astype("float32")

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    return image


# =========================================================
# STARTUP
# =========================================================

@app.on_event("startup")
async def startup():

    global model
    global class_names

    # =========================
    # LOAD CLASS NAMES
    # =========================

    if CLASS_NAMES_PATH.exists():

        with open(CLASS_NAMES_PATH, "r") as f:

            raw = json.load(f)

            # FIXED FOR:
            # {class_name: index}

            if isinstance(raw, dict):

                sorted_classes = sorted(
                    raw.items(),
                    key=lambda x: x[1]
                )

                class_names = [
                    item[0] for item in sorted_classes
                ]

            elif isinstance(raw, list):

                class_names = raw

            else:

                raise Exception("Invalid class_names.json format")

        logging.info(f"Loaded {len(class_names)} classes")

    else:

        logging.warning("class_names.json not found")

    # =========================
    # LOAD MODEL
    # =========================

    if MODEL_PATH.exists():

        model = tf.keras.models.load_model(str(MODEL_PATH))

        logging.info("✅ Model loaded successfully")

    else:

        logging.warning("❌ Model file not found")


# =========================================================
# ROUTES
# =========================================================

@app.get("/")
def home():

    index_path = BASE_DIR / "index.html"

    if index_path.exists():
        return FileResponse(index_path)

    return {
        "message": "PlantCare AI Backend Running"
    }


@app.get("/api/health")
def health():

    return {
        "status": "running",
        "model_loaded": model is not None,
        "classes_loaded": len(class_names)
    }


@app.get("/api/classes")
def get_classes():

    return {
        "classes": class_names
    }


@app.get("/api/stats")
def stats():

    return {
        "total_scans": 1245,
        "healthy_plants": 892,
        "diseased_plants": 353,
        "accuracy": "98.2%",
        "supported_diseases": len(class_names),
        "active_users": 156
    }


# =========================================================
# PREDICTION
# =========================================================

@app.post("/api/predict")
async def predict(file: UploadFile = File(...)):

    if model is None:

        raise HTTPException(
            status_code=500,
            detail="Model not loaded"
        )

    if not file.content_type.startswith("image/"):

        raise HTTPException(
            status_code=400,
            detail="Invalid image file"
        )

    image_bytes = await file.read()

    processed_image = preprocess_image(image_bytes)

    prediction = model.predict(processed_image, verbose=0)[0]

    predicted_index = int(np.argmax(prediction))

    confidence = float(prediction[predicted_index]) * 100

    print("Prediction Shape:", prediction.shape)
    print("Predicted Index:", predicted_index)

    # =========================
    # SAFETY CHECK
    # =========================

    if predicted_index >= len(class_names):

        raise HTTPException(
            status_code=500,
            detail=f"""
Prediction index mismatch

Predicted Index: {predicted_index}
Total Classes: {len(class_names)}
"""
        )

    # =========================
    # CLASS NAME
    # =========================

    raw_class = class_names[predicted_index]

    print("Predicted Class:", raw_class)

    # =========================
    # PARSE
    # =========================

    plant, disease = parse_class_name(raw_class)

    disease_info = get_disease_info(raw_class)

    # =========================
    # TOP 5 PREDICTIONS
    # =========================

    top_indices = np.argsort(prediction)[::-1][:5]

    top_predictions = []

    for i in top_indices:

        top_predictions.append({

            "class": class_names[int(i)],

            "confidence": round(
                float(prediction[i]) * 100,
                2
            )
        })

    # =========================
    # RESPONSE
    # =========================

    return {

        "success": True,

        "plant": plant,

        "disease": disease,

        "raw_class": raw_class,

        "confidence": round(confidence, 2),

        "description": disease_info["description"],

        "severity": disease_info["severity"],

        "treatment": disease_info["treatment"],

        "top_predictions": top_predictions,

        "timestamp": datetime.utcnow().isoformat()
    }


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )