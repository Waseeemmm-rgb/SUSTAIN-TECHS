import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
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
# Webcam Transformer
# ------------------------
CLASS_NAMES = ["Plastic", "Not Plastic"]  # Update with your actual classes

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        # Resize to model input size if needed
        img_resized = cv2.resize(img, (224, 224))
        # Dummy prediction (replace with actual model logic)
        # Here we randomly simulate prediction to show live feedback
        pred_idx = np.random.randint(len(CLASS_NAMES))
        label = CLASS_NAMES[pred_idx]

        # Draw label on frame
        cv2.putText(
            img, f"Detected: {label}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
        )
        return img

webrtc_streamer(key="camera", video_transformer_factory=VideoTransformer)

# ------------------------
# Pyrolysis Simulation
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
efficiency = round(np.random.uniform(70, 95), 2)
yield_pct = round(np.random.uniform(60, 90), 2)
impurity_pct = round(np.random.uniform(0, 10), 2)

st.write(f"Estimated Efficiency: **{efficiency}%**")
st.write(f"Product Yield: **{yield_pct}%**")
st.write(f"Impurities: **{impurity_pct}%**")

if efficiency > 85 and impurity_pct < 5:
    st.success("High quality pyrolysis product! ✅")
else:
    st.warning("Product quality moderate — consider process optimization ⚠️")
