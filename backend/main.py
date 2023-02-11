from flask import Flask, jsonify, request
import joblib
import json
import numpy as np


app = Flask(__name__)

model = joblib.load(r'D:/Mini_Project/backend/clf_model')

@app.route('/predict', methods=['POST'])
def predict():
    event = json.loads(request.data)
    values = event['values']
    values = list(map(float, values))
    pre = np.array(values)
    pre = pre.reshape(1, -1)
    prediction = model.predict(pre)

    return str(prediction[0])
    


if __name__ == '__main__':
    app.run(debug=True)