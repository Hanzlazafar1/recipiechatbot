from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()
os.environ['GOOGLE_API_KEY'] = "AIzaSyAcoGnvCodLUKvmO5Fc6qcx-hpGprK5QQ8"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Function to get response from Gemini LLM
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit App Configuration and Styling
st.set_page_config(
    page_title="Hanzla's Recipe Chatbot",
    page_icon="🍲",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# CSS for custom styling and animations
st.markdown("""
    <style>
    /* General Background */
    .stApp {
        background-color: #f2f4f8;
        background-image: linear-gradient(to right, #e0eafc, #cfdef3);
        font-family: 'Segoe UI', sans-serif;
        color: #333;
    }
    /* Header Styling */
    .header-title {
        font-size: 3.3rem;
        font-weight: bold;
        color: #333;
        text-align: center;
        padding: 20px;
        background: linear-gradient(to right, #4a90e2, #145c9e);
        border-radius: 12px;
        color: #fff;
        margin-top: -20px;
        margin-bottom: 10px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        animation: fadeIn 2s ease;
    }
    /* Input Field */
    input {
        transition: all 0.3s ease;
        border: 2px solid #a9d5e3;
        padding: 10px;
        font-size: 1.1rem;
        width: 100%;
        color: #333;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0, 123, 167, 0.2);
    }
    input:focus {
        box-shadow: 0px 0px 10px rgba(0, 123, 167, 0.4);
        border-color: #4a90e2;
    }
    /* Submit Button */
    .stButton>button {
        background-color: #145c9e;
        border-radius: 8px;
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: bold;
        padding: 10px 20px;
        transition: background-color 0.3s, transform 0.3s;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton>button:hover {
        background-color: #4a90e2;
        transform: scale(1.05);
    }
    /* Response Section */
    .response-section {
        background: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        font-size: 1rem;
        color: #333;
        text-align: left;
        animation: fadeIn 1s ease-in-out;
    }
    /* Footer */
    .footer {
        text-align: center;
        color: #333;
        font-size: 1rem;
        font-weight: bold;
        margin-top: 30px;
        padding: 10px;
        border-radius: 8px;
        background: linear-gradient(to right, #4a90e2, #145c9e);
        color: #fff;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        animation: fadeIn 2s ease;
    }
    .footer span {
        font-size: 1.3rem;
        color: #f8c42f;
        font-weight: bold;
    }
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Main UI
st.markdown("<div class='header-title'>Hanzla's Recipe Chatbot 🍲</div>", unsafe_allow_html=True)

# User Input
input_text = st.text_input("Ask me anything about recipes:", key="input")

# Submit Button
if st.button("Get Recipe Advice"):
    if input_text:
        response = get_gemini_response(input_text)
        st.markdown("<div class='response-section'><h3>Here's the suggestions:</h3><p>{}</p></div>".format(response), unsafe_allow_html=True)
    else:
        st.warning("Please enter a question!")

# Footer
st.markdown("<div class='footer'>Created with ❤️ by <span>Hanzla Zafar</span></div>", unsafe_allow_html=True)
