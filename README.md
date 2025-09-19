EmotionScope 🧠💬

EmotionScope is a state-of-the-art real-time sentiment analyzer that classifies text into Positive 😄, Negative 😡, or Neutral 😐 emotions instantly.
It combines Python, Scikit-learn, and Streamlit/Flask to deliver an intuitive, interactive, and professional interface, perfect for developers,
students, and ML enthusiasts. Whether analyzing single sentences, paragraphs, or multi-line inputs, EmotionScope provides accurate predictions 
powered by pre-trained models, making sentiment analysis fast, reliable, and visually appealing.

✨ Features
| Feature                 | Description                                 |
| ----------------------- | ------------------------------------------- |
| **Real-Time Analysis**  | Predict sentiment instantly from text input |
| **Multiple Sentences**  | Handles single or multiple text inputs      |
| **Pre-trained Models**  | Ready-to-use ML models for fast predictions |
| **Interactive Web App** | Clean and intuitive UI via Streamlit/Flask  |
| **Modular Code**        | Easy to customize, train, or deploy         |


📂 Project Structure
EmotionScope/
│
├── Data/               # Raw datasets (CSV/TSV)
├── Models/             # Pre-trained ML models (Pickle files)
├── Notebooks/          # Jupyter notebooks (EDA & training)
├── app.py              # Streamlit/Flask web app
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Ignore unnecessary files


🚀 Installation & Usage
 1. Clone the repository
    git clone https://github.com/yourusername/EmotionScope.git
    cd EmotionScope

 2. Create and activate virtual environment
    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate      # Windows

 3. Install dependencies
    pip install -r requirements.txt

 4. Run the web app
    python api.py


💡 Model Details

| 🔹 Component      | 🧩 Description                                       |
| ----------------- | ---------------------------------------------------- |
| **Preprocessing** | CountVectorizer / TF-IDF                             |
| **Algorithms**    | Logistic Regression / Naive Bayes                    |
| **Saved Models**  | Pre-trained models in `Models/` for fast predictions |
| **Evaluation**    | Accuracy, precision, recall metrics in notebooks     |


📸 Demo

Input: "I love this product! It's amazing."  
Output: Positive 😄

Input: "This is terrible and disappointing."  
Output: Negative 😡

Input: "It's okay, nothing special."  
Output: Neutral 😐










