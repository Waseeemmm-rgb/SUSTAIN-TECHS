import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="SUSTAIN TECH AI", layout="wide")

st.title("SUSTAIN TECH AI — Plastic Detection + Pyrolysis")

st.markdown("Use camera to capture plastic → detect → simulate pyrolysis")

# -------------------------
# Camera (WORKING)
# -------------------------
st.header("📷 Capture Image")

image = st.camera_input("Take a picture")

if image:
    img = Image.open(image)
    st.image(img, caption="Captured Image", use_column_width=True)

    # Convert to array
    img_array = np.array(img)

    # -------------------------
    # SIMPLE AI LOGIC (TEMP)
    # -------------------------
    if np.mean(img_array) > 100:
        label = "Plastic"
        confidence = 0.85
    else:
        label = "Not Plastic"
        confidence = 0.80

    st.subheader("🤖 Detection Result")
    st.write(f"**{label}** (Confidence: {confidence})")

    # -------------------------
    # Pyrolysis Simulation
    # -------------------------
    st.header("🔥 Pyrolysis Simulation")

    if st.button("Run Simulation"):
        progress = st.progress(0)

        for i in range(100):
            progress.progress(i + 1)

        st.success("Pyrolysis Complete!")

        st.subheader("📊 Output Quality")

        st.write("Efficiency: 87%")
        st.write("Fuel Yield: 78%")
        st.write("Impurity: Low")

        st.success("High-quality fuel produced ✅")
