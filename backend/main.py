from flask import Flask, jsonify, request
import joblib
import json



app = Flask(__name__)

model = joblib.load(r'D:/Mini_Project/backend/clf_model')

@app.route('/predict', methods=['POST'])
def predict():
    event = json.loads(request.data)
    print(event)
    return "1"
    


if __name__ == '__main__':
    app.run(debug=True)