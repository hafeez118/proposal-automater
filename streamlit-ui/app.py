import streamlit as st
import requests

st.title("AI Proposal Generator")

client_name = st.text_input("Client Name")
company_name = st.text_input("Your Company Name")
prompt = st.text_area("Enter proposal requirement prompt")

if st.button("Generate Proposal"):
    res = requests.post("http://faiss-api:8000/generate", json={"prompt": prompt})
    proposal_text = res.json().get("proposal", "")

    template = f"""
Proposal for {client_name}

Dear {client_name},

Based on your request, we propose the following:

{proposal_text}

Sincerely,  
{company_name}
    """

    st.success("Proposal Generated")
    st.text_area("Generated Proposal", template, height=300)