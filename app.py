import streamlit as st
from pathlib import Path

st.title("Sustain-Tech AI - Plastic Detection")

# Read the HTML file
html_file = Path("index.html").read_text()

# Display it in Streamlit
st.components.v1.html(html_file, height=600)
