import pickle
import json
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load the trained model
with open('rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def generate_random_transaction():
    transaction = {
        "indegree": random.randint(1, 10),
        "outdegree": random.randint(1, 10),
        "in_btc": round(random.uniform(0.01, 10.0), 4),
        "out_btc": round(random.uniform(0.01, 10.0), 4),
        "total_btc": round(random.uniform(0.01, 20.0), 4),
        "mean_in_btc": round(random.uniform(0.001, 5.0), 4),
        "mean_out_btc": round(random.uniform(0.001, 5.0), 4)
    }
    return transaction

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = generate_random_transaction()
    features = list(data.values())
    
    # Make a prediction
    prediction = model.predict([features])
    result = "Fraudulent Transaction" if prediction[0] == 1 else "Legitimate Transaction"
    
    return render_template('index.html', message=result)

if __name__ == '__main__':
    app.run(debug=True)
