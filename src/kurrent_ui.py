import streamlit as st
import requests

st.title("Kurrent HTR - Transcription Tool")
uploaded_file = st.file_uploader("Upload de manuscrito (PNG/JPG)", type=['png', 'jpg'])

if uploaded_file:
    with st.spinner('Processando via TrOCR...'):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/v1/transcribe", files=files)
        data = response.json()
        
    col1, col2 = st.columns(2)
    with col1:
        st.image(uploaded_file, caption="Original")
    with col2:
        st.text_area("Transcrição", value=data, height=400)
        st.info(f"Modelo: {data['model']} | Tempo: {data['processing_time_sec']}s")

