from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

fraud_model = joblib.load('fraud_detection_model.pkl')

@app.route('/predict-fraud', methods=['POST'])
def predict_fraud():
    data = request.json  
    features = np.array(data['features']).reshape(1, -1)
    
    prediction = fraud_model.predict(features)
    
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
