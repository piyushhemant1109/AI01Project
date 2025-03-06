import streamlit as st
import requests

# Streamlit Page Configuration
st.set_page_config(page_title="Implementation of Artificial Intelligence (AI) in Business-Decision Making: Pharma & Healthcare Applications", page_icon="💡", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    .stTextInput>div>div>input {
        font-size: 18px;
        padding: 5px;
    }
    .stButton>button {
        background-color: #008f9e;
        color: white;
        font-size: 16px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("💬 Implementation of Artificial Intelligence (AI) in Business-Decision Making: Pharma & Healthcare Applications")
st.write("Ask medical-related questions and get AI-generated responses!")

# User Input
user_input = st.text_input("Enter your question:", "What is Acromegaly?")

if st.button("Get Response"):
    with st.spinner("Processing..."):
        try:
            # Google Colab API URL
            api_url = "YOUR_COLAB_API_URL_HERE"  # Replace with your Colab endpoint
            response = requests.post(api_url, json={"user_prompt": user_input})
            
            if response.status_code == 200:
                st.success("Response received!")
                st.write("**AI's Response:**")
                st.info(response.json()["response"])  # Adjust based on API response format
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
