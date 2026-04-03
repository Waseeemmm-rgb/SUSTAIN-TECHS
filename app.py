import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import numpy as np
import cv2

st.set_page_config(page_title="SUSTAIN TECH AI", layout="wide")
st.title("SUSTAIN TECH AI — Plastic Detection + Pyrolysis")

st.markdown("Live webcam → detect plastic → simulate pyrolysis")

# -------------------------
# Dummy AI (replace later)
# -------------------------
CLASS_NAMES = ["Plastic", "Not Plastic"]

def fake_model(frame):
    # For now: random prediction (replace later with real model)
    if np.mean(frame) > 100:
        return "Plastic", 0.85
    else:
        return "Not Plastic", 0.80

# -------------------------
# Webcam Class
# -------------------------
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        label, conf = fake_model(img)

        # Display prediction on frame
        cv2.putText(
            img,
            f"{label} ({conf:.2f})",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0) if label == "Plastic" else (0, 0, 255),
            2,
        )

        return img

# -------------------------
# Start Webcam
# -------------------------
st.header("📷 Live Camera Detection")

webrtc_streamer(key="camera", video_transformer_factory=VideoTransformer)

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
