from flask import Flask, render_template, request, jsonify
import joblib


app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check():
    url = request.json['url']
  
    is_phishing = model.predict([[0, 1]])  # Replace with actual features
    result = "Phishing URL" if is_phishing else "Safe URL"
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
