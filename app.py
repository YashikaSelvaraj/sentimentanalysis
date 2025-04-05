from flask import Flask, request, jsonify, render_template
import joblib
import re

app = Flask(__name__)

# Load your trained model (you should save and load it using joblib or pickle)
# best_model = joblib.load("sentiment_model.pkl")

# For now, use directly if running in same file
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Example: mock model (replace this with real one)
best_model = joblib.load("best_svm_model.pkl")  # Saved earlier from GridSearchCV

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.strip()
    return text

@app.route("/")
def home():
    return render_template("yashi.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    cleaned = clean_text(text)
    sentiment = best_model.predict([cleaned])[0]
    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

