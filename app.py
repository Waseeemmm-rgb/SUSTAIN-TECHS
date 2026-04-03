import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# 1. Setup the Website Look
st.set_page_config(page_title="Sustain-Tech AI", page_icon="🌱")
st.title("🌱 Sustain-Tech AI: Plastic to Fuel")
st.write("Welcome to the future of sustainability in Oman. Scan plastic to see its fuel potential!")

# 2. Function to predict what the image is
def predict_plastic(image_data, model):
    size = (224, 224)    
    image = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)
    img_array = np.asarray(image)
    normalized_image_array = (img_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    prediction = model.predict(data)
    return prediction

# 3. Load your Teachable Machine Model
@st.cache_resource
def load_my_model():
    model = tf.keras.models.load_model("keras_model.h5", compile=False)
    with open("labels.txt", "r") as f:
        class_names = f.readlines()
    return model, class_names

# Try to load the files
try:
    model, class_names = load_my_model()
except Exception as e:
    st.error("Error: Make sure 'keras_model.h5' and 'labels.txt' are in the same folder!")
    st.stop()

# 4. The Webcam Interface
img_file_buffer = st.camera_input("Scan your waste item here")

if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    prediction = predict_plastic(image, model)
    
    index = np.argmax(prediction)
    label = class_names[index].strip()
    conf = prediction[0][index]

    st.subheader(f"Result: {label}")
    st.progress(float(conf))

    # 5. Digital Simulation Logic
    if "Plastic" in label:
        st.success("✅ This can be converted to Fuel!")
        temp = st.slider("Simulated Pyrolysis Temp (°C)", 0, 500, 20)
        
        # Simple Logic for Oman Sustainability
        if temp > 350:
            st.write("🔥 **Status:** Converting to Liquid Fuel...")
            st.metric("Estimated Yield", "82%", "+2% Efficiency")
        else:
            st.write("❄️ **Status:** Heating the reactor...")
    else:
        st.warning("⚠️ This item is not suitable for the Pyrolysis simulation.")

st.info("Project for Oman Sustainable Tech - Focus: Salalah Waste Management")
