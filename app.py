import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# --- 1. SET UP THE PAGE ---
st.set_page_config(page_title="Sustain-Tech AI", page_icon="🌱")

st.title("🌱 Sustain-Tech AI: Plastic to Fuel")
st.markdown("### Sustainable Technology for the Future of Oman")
st.write("Scan plastic waste to calculate its potential as a clean energy source.")

# --- 2. THE AI PREDICTION FUNCTION ---
def predict_waste(image_data, model):
    size = (224, 224)    
    image = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)
    img_array = np.asarray(image)
    # Normalize the image (standard for Teachable Machine)
    normalized_image_array = (img_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    prediction = model.predict(data)
    return prediction

# --- 3. LOAD THE MODEL & LABELS ---
@st.cache_resource
def load_my_model():
    # These names must match exactly what you upload to GitHub
    model = tf.keras.models.load_model("keras_model.h5", compile=False)
    with open("labels.txt", "r") as f:
        class_names = [line.strip() for line in f.readlines()]
    return model, class_names

try:
    model, class_names = load_my_model()
except Exception as e:
    st.error("⚠️ Error: Missing 'keras_model.h5' or 'labels.txt' in GitHub!")
    st.stop()

# --- 4. THE USER INTERFACE ---
img_file_buffer = st.camera_input("📸 Scan a waste item (Bottle, Bag, etc.)")

if img_file_buffer is not None:
    # Get image and predict
    image = Image.open(img_file_buffer)
    prediction = predict_waste(image, model)
    
    # Get the result
    index = np.argmax(prediction)
    label = class_names[index]
    confidence = prediction[0][index]

    # Show results
    st.divider()
    st.subheader(f"Detection Result: {label}")
    st.info(f"AI Confidence Score: {round(confidence * 100, 2)}%")

    # --- 5. DIGITAL PYROLYSIS SIMULATION ---
    # We check if the word "Plastic" is in the label name
    if "Plastic" in label:
        st.success("✅ HIGH FUEL POTENTIAL DETECTED")
        
        # Simulation Sliders
        st.write("### 🔬 Digital Pyrolysis Reactor")
        temp = st.slider("Set Reactor Temperature (°C)", 0, 600, 250)
        
        col1, col2 = st.columns(2)
        
        if temp < 300:
            col1.metric("Reactor Status", "Heating...")
            col2.metric("Fuel Yield", "0%")
        elif 300 <= temp <= 500:
            col1.metric("Reactor Status", "Converting...", delta="Optimal")
            col2.metric("Fuel Yield", "85%", delta="High")
            st.balloons()
        else:
            st.error("⚠️ SAFETY ALERT: Temperature too high! Risk of overheating.")
            col1.metric("Reactor Status", "CRITICAL")
            col2.metric("Fuel Yield", "N/A")
            
        st.write("**Note:** This is a digital simulation. No physical reactor is required for this demo.")
    else:
        st.warning("⚠️ This material is not suitable for plastic-to-fuel conversion.")

# --- 6. FOOTER ---
st.sidebar.title("About Sustain-Tech AI")
st.sidebar.info("This project uses AI to promote recycling and energy innovation in line with Oman's sustainability goals.")
