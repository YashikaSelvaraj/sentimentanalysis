import streamlit as st
import joblib
import re

model = joblib.load("C:/Users/bavat/Desktop/Projectbrix/best_svm_model.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    return text.strip()

st.set_page_config(page_title="Sentiment Analyzer", page_icon="💬", layout="centered")
st.write("✅ UI Loaded successfully")

st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stTextArea textarea {
        font-size: 16px;
        color: #333;
    }
    .stButton>button {
        font-size: 16px;
        border-radius: 8px;
        padding: 0.5em 1.5em;
        background-color: #4CAF50;
        color: white;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        color: #333;
    }
    .positive {
        color: green;
    }
    .negative {
        color: red;
    }
    .neutral {
        color: orange;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💬 Sentiment Analyzer")
st.write("This simple app uses Machine Learning (SVM) to predict whether a sentence is Positive, Negative, or Neutral.")

user_input = st.text_area("📥 Enter your text below:", height=150)

if st.button("🔍 Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence.")
    else:
        cleaned_text = clean_text(user_input)
        prediction = model.predict([cleaned_text])[0]

        if prediction.lower() == "positive":
            st.markdown(f"<p class='result positive'>✅ Sentiment: {prediction.upper()}</p>", unsafe_allow_html=True)
        elif prediction.lower() == "negative":
            st.markdown(f"<p class='result negative'>❌ Sentiment: {prediction.upper()}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='result neutral'>⚠️ Sentiment: {prediction.upper()}</p>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<center><small>Made with ❤️ using Streamlit</small></center>", unsafe_allow_html=True)

