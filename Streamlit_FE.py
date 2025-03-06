import streamlit as st
import requests

# Streamlit Page Configuration
st.set_page_config(page_title="Implementation of Artificial Intelligence (AI) in Business-Decision Making: Pharma & Healthcare Applications", page_icon="💡", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
        color: #2c3e50;
    }
    .stTextInput>div>div>input {
        font-size: 18px;
        padding: 12px;
        border-radius: 10px;
        border: 2px solid #2c3e50;
        background-color: #ecf0f1;
    }
    .stButton>button {
        background-color: #27ae60;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stMarkdown h1 {
        text-align: left;
        font-size: 26px;
        color: #2c3e50;
        font-weight: bold;
    }
    .response-container {
        background-color: #dff9fb;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #27ae60;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown("# 💬 Implementation of Artificial Intelligence (AI) in Business-Decision Making: Pharma & Healthcare Applications")
st.write("Ask Business-related questions and get AI-generated responses!")

# User Input at the Bottom
user_input = st.text_input("Enter your question:", "What is Acromegaly?")

# AI Response Section
if user_input:
    with st.spinner("Processing..."):
        try:
            # Google Colab API URL
            api_url = "YOUR_COLAB_API_URL_HERE"  # Replace with your Colab endpoint
            response = requests.post(api_url, json={"user_prompt": user_input})
            
            if response.status_code == 200:
                st.success("Response received!")
                st.markdown("### AI's Response:")
                st.markdown(f'<div class="response-container">{response.json()["response"]}</div>', unsafe_allow_html=True)
            else:
                st.error("Failed to get a response from the AI model.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer
st.markdown("""
    ---
    🔹 *Powered by Hugging Face & Streamlit*  
    🔹 *Developed by Piyush Hemant Kadethankar*
""")
