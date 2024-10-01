import streamlit as st
import requests

st.title("Brain MRI Metastasis Segmentation")

uploaded_file = st.file_uploader("Choose a brain MRI image...", type="tif")

if uploaded_file is not None:
    files = {'file': uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:8000/predict", files=files)
    st.image(uploaded_file, caption='Uploaded MRI.', use_column_width=True)
    st.write(f"Metastasis Segmentation Result: {response.json()}")
