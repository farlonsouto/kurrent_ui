import os

import requests
import streamlit as st

# Debug: Show the URL in the sidebar so you can be 100% sure what's being used
backend_url = os.getenv("BACKEND_URL", "http://localhost:8000/v1/transcribe")
st.sidebar.write(f"Connecting to: `{backend_url}`")

st.set_page_config(page_title="Kurrent HTR", layout="wide")
st.title("Kurrent HTR - Transcription Tool")

uploaded_file = st.file_uploader("Upload de manuscrito (PNG/JPG)", type=['png', 'jpg'])

if uploaded_file:
    with st.spinner('Processando via TrOCR...'):
        try:
            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
            }
            # 2. Use the variable backend_url here
            response = requests.post(backend_url, files=files)
            response.raise_for_status()  # Check for errors
            data = response.json()

            col1, col2 = st.columns(2)
            with col1:
                st.image(uploaded_file, caption="Original")
            with col2:
                # 3. Access only the 'text' key for the text area
                st.text_area("Transcrição", value=data.get('text', ''), height=400)

                # Using .get() for safety prevents crashes if keys are missing
                st.info(f"**Modelo:** {data.get('model')} | **Tempo:** {data.get('processing_time_sec')}s")

        except Exception as e:
            st.error(f"Erro na conexão com o backend: {e}")
