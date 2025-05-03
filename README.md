# 🛡️ phishKavach - Phishing URL Detection Web App

**phishKavach** is a machine learning-based web application that detects whether a given URL is potentially malicious (phishing) or safe. It uses Natural Language Processing (NLP) and a logistic regression classifier to analyze URLs and classify them accurately.

---

## 🚀 Demo

![Phishing Detection UI Screenshot](https://cdn.activestate.com/wp-content/uploads/2021/02/phishing-detection-with-Python.jpg)

> 📌 Replace the image above with a screenshot or demo gif of your app once hosted.

---

## 🧠 How It Works

1. **Input**: User enters a URL in the web interface.
2. **Processing**: The backend uses a pre-trained Logistic Regression model to analyze the input.
3. **Prediction**: The model predicts whether the URL is phishing or safe.
4. **Output**: The result is returned and displayed on the page dynamically using JavaScript.

---

## 🗂️ Project Structure

```bash
phishKavach/
├── app.py                # Main Flask server
├── model.pkl             # Pre-trained phishing detection model
├── phishing_detection.csv # Dataset used for training
├── features.py           # Model training and evaluation script
├── static/
│   └── script.js         # JavaScript to handle frontend logic
├── templates/
│   └── index.html        # HTML frontend
└── README.md             # Project documentation
```

## Technologies Used:
- Python (Flask, scikit-learn, pandas, joblib)
- Machine Learning (Logistic Regression, TF-IDF Vectorization)
- Frontend: HTML, JavaScript (Fetch API)
- Data: Phishing dataset (phishing_detection.csv)

# Setup instructions
1. Clone the repository:
```
git clone https://github.com/your-username/phishKavach.git
cd phishKavach
```
2. Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Running the application:
```
python app.py
```

## Model Overview
- Vectorizer: ```TfidfVectorizer``` transforms URL text data into TF-IDF features.
- Model: LogisticRegression is trained on the vectorized features.
- Evaluation: Accuracy, precision, recall, and F1 score are calculated to assess performance.
- Model Saving: The trained model is saved using joblib to model.pkl.


## Future Improvements
- Integrate real-time URL analysis using third-party threat intelligence APIs.
- Add user authentication and history tracking.
- Improve model accuracy with advanced NLP and deep learning.
- Host the app on platforms like Heroku or Render.

## Inspiration
Cybersecurity is a growing concern with phishing being one of the most common threats. phishKavach aims to provide a simple, fast, and effective tool to detect such malicious links and raise awareness.

``` Contributing
Feel free to fork this repository and submit a pull request. Contributions, issues, and feature requests are welcome!
```
