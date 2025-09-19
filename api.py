from flask import Flask, request, jsonify, send_file, render_template
import re
from io import BytesIO
import pandas as pd
import pickle
import base64
import matplotlib
matplotlib.use('Agg')  # Set backend before importing pyplot
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

app = Flask(__name__)
STOPWORDS = set(stopwords.words("english"))

# Load models once at startup
with open("Models/model_xgb.pkl", "rb") as f:
    predictor = pickle.load(f)
with open("Models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
with open("Models/countVectorizer.pkl", "rb") as f:
    cv = pickle.load(f)

def preprocess_text(text):
    stemmer = PorterStemmer()
    text = re.sub("[^a-zA-Z]", " ", text)
    words = [stemmer.stem(word) for word in text.lower().split() if word not in STOPWORDS]
    return " ".join(words)

@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "file" in request.files:
            file = request.files["file"]
            data = pd.read_csv(file)
            data["Predicted"] = data["Sentence"].apply(lambda x: predict_sentiment(x))
            
            # Generate graph
            plt.figure(figsize=(5,5))
            data["Predicted"].value_counts().plot(kind="pie", autopct="%1.1f%%")
            img = BytesIO()
            plt.savefig(img, format="png")
            plt.close()
            img.seek(0)
            
            # Prepare response
            output = BytesIO()
            data.to_csv(output, index=False)
            output.seek(0)
            
            response = send_file(output, mimetype="text/csv", 
                               as_attachment=True, download_name="predictions.csv")
            response.headers["X-Graph"] = base64.b64encode(img.getvalue()).decode("utf-8")
            return response
        
        elif "text" in request.json:
            text = request.json["text"]
            return jsonify({"result": predict_sentiment(text)})
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def predict_sentiment(text):
    processed = preprocess_text(text)
    vectorized = cv.transform([processed]).toarray()
    scaled = scaler.transform(vectorized)
    prediction = predictor.predict(scaled)[0]
    return "Positive" if prediction == 1 else "Negative"

if __name__ == "__main__":
    app.run(port=5000, debug=True)