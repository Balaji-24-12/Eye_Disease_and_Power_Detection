import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

# ======================
# PATHS
# ======================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "disease_model.h5")

# ======================
# LOAD MODEL
# ======================
model = tf.keras.models.load_model(MODEL_PATH)

# Class index mapping (must match training output)
CLASS_NAMES = [
    'Bulging_Eyes',
    'Cataracts',
    'Crossed_Eyes',
    'Eye_diseases',
    'Glaucoma',
    'Uveitis'
]

IMG_SIZE = 224

def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    class_index = np.argmax(preds)
    confidence = float(np.max(preds))

    return CLASS_NAMES[class_index], round(confidence, 2)
