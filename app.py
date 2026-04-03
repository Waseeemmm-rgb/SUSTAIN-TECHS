# ------------------------
# Load model
# ------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("my_model/my_model.h5")

model = load_model()
st.success("Model loaded successfully!")

# ------------------------
# Prediction
# ------------------------
CLASS_NAMES = ["Plastic", "Not Plastic"]  # <- adjust to match your trained model

if camera_image:
    img = Image.open(camera_image)
    img_array = np.array(img)
    img_resized = cv2.resize(img_array, (224, 224))
    img_input = np.expand_dims(img_resized / 255.0, axis=0)

    preds = model.predict(img_input)
    class_idx = np.argmax(preds)
    confidence = preds[0][class_idx]
    detected_class = CLASS_NAMES[class_idx]

    st.write(f"Detected: **{detected_class}** (Confidence: {confidence:.2f})")
