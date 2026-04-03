import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
import time

st.set_page_config(page_title="SUSTAIN TECH AI", layout="wide")
st.title("SUSTAIN TECH AI — Plastic Tracking & Pyrolysis Simulation")

st.markdown("""
Prototype: Tracks plastic type using camera, simulates pyrolysis, and checks product quality.
""")

# ------------------------
# Load model
# ------------------------
@st.cache_resource
def load_model():
    # Assuming you uploaded model files in folder 'my_model' in repo
    return tf.keras.models.load_model("my_model/my_model.h5")

model = load_model()
st.success("Model loaded successfully!")

# ------------------------
# Camera input
# ------------------------
st.header("Plastic Detection")
st.markdown("Use your camera to capture plastic for classification:")

camera_image = st.camera_input("Capture an image")

if camera_image:
    # Convert to array
    img = Image.open(camera_image)
    img_array = np.array(img)
    img_resized = cv2.resize(img_array, (224, 224))  # adjust if your model input differs
    img_input = np.expand_dims(img_resized / 255.0, axis=0)  # normalize

    # Predict
    preds = model.predict(img_input)
    class_idx = np.argmax(preds)
    confidence = preds[0][class_idx]

    # You should update class names according to your trained model
    CLASS_NAMES = ["PET", "HDPE", "PVC", "LDPE", "PP", "PS", "Other"]  
    detected_class = CLASS_NAMES[class_idx]

    st.write(f"Detected Plastic Type: **{detected_class}** (Confidence: {confidence:.2f})")

    # ------------------------
    # Digital Pyrolysis Simulation (simple visualization)
    # ------------------------
    st.header("Digital Pyrolysis Simulation")
    st.progress(0)
    for i in range(101):
        time.sleep(0.02)
        st.progress(i)
    st.success("Pyrolysis simulation complete! 🔥")

    # ------------------------
    # Product Quality / Efficiency Check
    # ------------------------
    st.header("Product Quality & Efficiency")
    # For prototype, generate random metrics
    efficiency = round(np.random.uniform(70, 95), 2)
    yield_pct = round(np.random.uniform(60, 90), 2)
    impurity_pct = round(np.random.uniform(0, 10), 2)

    st.write(f"Estimated Efficiency: **{efficiency}%**")
    st.write(f"Product Yield: **{yield_pct}%**")
    st.write(f"Impurities: **{impurity_pct}%**")

    # Suggestion
    if efficiency > 85 and impurity_pct < 5:
        st.success("High quality pyrolysis product! ✅")
    else:
        st.warning("Product quality moderate — consider process optimization ⚠️")
