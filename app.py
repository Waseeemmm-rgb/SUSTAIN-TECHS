import streamlit as st
import numpy as np
from PIL import Image
import time

st.set_page_config(page_title="SUSTAIN TECH AI", layout="wide")
st.title("SUSTAIN TECH AI — Plastic Tracking & Pyrolysis Simulation")

st.markdown("""
Prototype: Tracks plastic type using camera, simulates pyrolysis, and checks product quality.
""")

# ------------------------
# Camera input
# ------------------------
st.header("Plastic Detection")
st.markdown("Use your camera to capture plastic for classification:")

camera_image = st.camera_input("Capture an image")

if camera_image:
    # Convert to array
    img = Image.open(camera_image)
    st.image(img, caption="Captured Image", use_column_width=True)

    # ------------------------
    # Simulate model prediction
    # ------------------------
    CLASS_NAMES = ["PET", "HDPE", "PVC", "LDPE", "PP", "PS", "Other"]
    detected_class = np.random.choice(CLASS_NAMES)
    confidence = round(np.random.uniform(0.7, 0.99), 2)

    st.write(f"Detected Plastic Type: **{detected_class}** (Confidence: {confidence})")

    # ------------------------
    # Digital Pyrolysis Simulation
    # ------------------------
    st.header("Digital Pyrolysis Simulation")
    progress_bar = st.progress(0)
    for i in range(101):
        time.sleep(0.02)
        progress_bar.progress(i)
    st.success("Pyrolysis simulation complete! 🔥")

    # ------------------------
    # Product Quality / Efficiency Check
    # ------------------------
    st.header("Product Quality & Efficiency")
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
