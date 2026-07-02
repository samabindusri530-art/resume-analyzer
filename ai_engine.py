import requests
import streamlit as st

HF_TOKEN = st.secrets["HF_TOKEN"]

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def analyze_resume_ai(resume_text):

    prompt = f"""
    Analyze this resume.

    Give:
    1. 3 improvements needed
    2. Missing technical skills
    3. Career suggestions

    Resume:
    {resume_text}
    """

    payload = {
        "inputs": prompt
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload
    )

    return response.json()
