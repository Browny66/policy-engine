# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Willkommen zur Policy Engine!")

@app.route('/predict_anomaly', methods=['POST'])
def predict_anomaly():
    # Hier wäre der Anomalie-Code
    return jsonify(anomaly_detected=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
