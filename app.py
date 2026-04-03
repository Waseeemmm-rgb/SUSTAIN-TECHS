import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
import time

# ------------------------
# Page Setup
# ------------------------
st.set_page_config(page_title="SUSTAIN TECH AI", layout="wide")
st.title("SUSTAIN TECH AI — Plastic Detection & Pyrolysis System")

# ------------------------
# Load Model
# ------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("my_model/my_model.h5")

model = load_model()

st.success("Model Loaded Successfully")

# ------------------------
# Classes (EDIT IF NEEDED)
# ------------------------
CLASS_NAMES = ["Plastic", "Not Plastic"]

# ------------------------
# Camera
# ------------------------
st.header("Camera Detection")

image = st.camera_input("Take a photo")

if image:
    img = Image.open(image)
    st.image(img)

    img_array = np.array(img)
    img_resized = cv2.resize(img_array, (224, 224))
    img_input = np.expand_dims(img_resized / 255.0, axis=0)

    prediction = model.predict(img_input)
    index = np.argmax(prediction)
    confidence = float(prediction[0][index])

    result = CLASS_NAMES[index]

    st.write(f"Result: **{result}** ({confidence:.2f})")

    if result == "Plastic":
        st.success("Plastic detected — Running Pyrolysis")

        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)

        st.success("Pyrolysis Done")

    else:
        st.error("Not Plastic")
