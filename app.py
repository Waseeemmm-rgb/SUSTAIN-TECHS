import streamlit as st

st.set_page_config(page_title="SUSTAIN TECH AI", layout="wide")

st.title("SUSTAIN TECH AI — Plastic Detection & Pyrolysis")

st.markdown("Detect plastic using AI → simulate pyrolysis → check quality")

# -------------------------
# Teachable Machine Web App
# -------------------------

st.components.v1.html("""
<div style="text-align:center;">
    <h3>📷 Plastic Detection Camera</h3>
    <button onclick="init()">Start Camera</button>
    <div id="webcam-container"></div>
    <div id="label-container"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest"></script>
<script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest"></script>

<script>
const URL = "./my_model/";

let model, webcam, labelContainer, maxPredictions;

async function init() {
    const modelURL = URL + "model.json";
    const metadataURL = URL + "metadata.json";

    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();

    webcam = new tmImage.Webcam(250, 250, true);
    await webcam.setup();
    await webcam.play();
    window.requestAnimationFrame(loop);

    document.getElementById("webcam-container").appendChild(webcam.canvas);
    labelContainer = document.getElementById("label-container");

    for (let i = 0; i < maxPredictions; i++) {
        labelContainer.appendChild(document.createElement("div"));
    }
}

async function loop() {
    webcam.update();
    await predict();
    window.requestAnimationFrame(loop);
}

async function predict() {
    const prediction = await model.predict(webcam.canvas);

    let topClass = "";
    let topProb = 0;

    for (let i = 0; i < maxPredictions; i++) {
        let p = prediction[i];
        let text = p.className + ": " + p.probability.toFixed(2);
        labelContainer.childNodes[i].innerHTML = text;

        if (p.probability > topProb) {
            topProb = p.probability;
            topClass = p.className;
        }
    }

    // Show plastic status clearly
    if (topClass.toLowerCase().includes("plastic")) {
        document.body.style.backgroundColor = "#d4edda";
    } else {
        document.body.style.backgroundColor = "#f8d7da";
    }
}
</script>
""", height=600)

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
