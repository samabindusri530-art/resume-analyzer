import requests
import streamlit as st

HF_TOKEN = st.secrets["HF_TOKEN"]

API_URL = "https://api-inference.huggingface.co/models/gpt2"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def analyze_resume_ai(resume_text):

    prompt = f"Analyze this resume: {resume_text}"

    payload = {
        "inputs": prompt
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        return response.json()

    except Exception as e:
        return f"Error connecting: {e}"
