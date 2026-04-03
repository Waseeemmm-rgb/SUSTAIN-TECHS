import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="SUSTAIN TECH AI", layout="wide")
st.title("SUSTAIN TECH AI — Plastic Tracking & Pyrolysis Simulation")

st.markdown("""
Prototype: Tracks plastic type using camera, simulates pyrolysis, and checks product quality.
""")

# ------------------------
# Camera / Model
# ------------------------
st.header("Plastic Detection (Browser Model)")
st.markdown(
    "Your live camera detection runs in the browser. Open the camera below:"
)

# Embed browser camera page
st.components.v1.iframe("index.html", height=500)

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
