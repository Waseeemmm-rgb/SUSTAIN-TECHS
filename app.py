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

st.markdown("""
AI system to:
1. Detect plastic using camera  
2. Classify type  
3. Simulate pyrolysis process  
4. Evaluate output quality  
""")

# ------------------------
# Load Model
# ------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("my_model/my_model.h5")

model = load_model()
st.success("✅ Model Loaded Successfully")

# ------------------------
# Class Names (EDIT THIS!)
# ------------------------
CLASS_NAMES = ["Plastic", "Not Plastic"]
# If your model has more classes, change this list

# ------------------------
# Camera Input
# ------------------------
st.header("📷 Plastic Detection")

camera_image = st.camera_input("Capture plastic image")

if camera_image:

    # Convert image
    img = Image.open(camera_image)
    st.image(img, caption="Captured Image", use_column_width=True)

    img_array = np.array(img)
    img_resized = cv2.resize(img_array, (224, 224))
    img_input = np.expand_dims(img_resized / 255.0, axis=0)

    # ------------------------
    # Prediction
    # ------------------------
    preds = model.predict(img_input)
    class_idx = np.argmax(preds)
    confidence = float(preds[0][class_idx])

    detected_class = CLASS_NAMES[class_idx]

    st.subheader("🔍 Detection Result")
    st.write(f"**{detected_class}** (Confidence: {confidence:.2f})")

    # ------------------------
    # Pyrolysis Simulation
    # ------------------------
    if detected_class == "Plastic":

        st.header("🔥 Pyrolysis Simulation")

        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.02)
            progress_bar.progress(i)

        st.success("Pyrolysis Complete!")

        # ------------------------
        # Output Products
        # ------------------------
        st.subheader("🧪 Output Products")

        oil = round(np.random.uniform(50, 80), 2)
        gas = round(np.random.uniform(10, 30), 2)
        char = round(100 - oil - gas, 2)

        st.write(f"Oil Yield: **{oil}%**")
        st.write(f"Gas Yield: **{gas}%**")
        st.write(f"Char Residue: **{char}%**")

        # ------------------------
        # Quality Check
        # ------------------------
        st.header("📊 Quality Check")

        efficiency = round(np.random.uniform(75, 95), 2)
        impurity = round(np.random.uniform(1, 10), 2)

        st.write(f"Efficiency: **{efficiency}%**")
        st.write(f"Impurities: **{impurity}%**")

        if efficiency > 85 and impurity < 5:
            st.success("✅ High Quality Output")
        else:
            st.warning("⚠️ Moderate Quality — Optimization Needed")

    else:
        st.error("❌ Not Plastic — Pyrolysis Not Applicable")
