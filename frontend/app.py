import streamlit as st
import requests

st.set_page_config(page_title="LLM Security Helper", layout="wide")

st.title("🔐 LLM Security Helper")

mode = st.radio(
    "Choose Analysis Mode",
    ["Code → Security Fixes", "Specs → LLM Vulnerabilities"]
)

input_label = (
    "Paste vulnerable code below"
    if mode == "Code → Security Fixes"
    else "Paste GenAI application specifications below"
)

user_input = st.text_area(input_label, height=300)

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please provide input.")
    else:
        with st.spinner("Analyzing with LLM..."):
            response = requests.post(
                "http://localhost:8000/analyze",
                json={
                    "mode": mode,
                    "content": user_input
                }
            )

        if response.status_code == 200:
            st.subheader("Analysis Result")
            st.markdown(response.json()["result"])
        else:
            st.error("Backend error. Is FastAPI running?")
