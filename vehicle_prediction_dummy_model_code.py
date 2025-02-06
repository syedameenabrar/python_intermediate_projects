# Price Prediction for Used Vehicles
# 💡 Goal: Predict the price of second-hand vehicles based on input data.

# To predict the price of used vehicles, you'll need a Flask API where you send vehicle details via Postman, and it returns the predicted price. Here’s a step-by-step approach:

# Steps:
# Train a model (for simplicity, we'll use a dummy model here).
# Create a Flask API.
# Send vehicle details in Postman.
# Get the predicted price.

# 🔥 How to Run the Flask API
# Install dependencies:

# pip install flask numpy pickle
# Run the Flask server:

# python app.py
# Your API will be live at http://127.0.0.1:5000/predict


import numpy as np
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy Model (You should replace this with a trained model)
class DummyModel:
    def predict(self, features):
        return [500000 + 2000 * features[0][0]]  # Simple linear formula

# Load trained model (or use a dummy one)
try:
    model = pickle.load(open("vehicle_price_model.pkl", "rb"))
except:
    model = DummyModel()  # Use dummy model if no trained model is found

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Extract input features
    year = data.get("year", 2020)  # Example: Manufacturing year
    mileage = data.get("mileage", 15.0)  # kmpl
    brand = data.get("brand", "Maruti")  # Brand name
    fuel_type = data.get("fuel_type", "Petrol")  # Fuel type

    # Convert categorical data (Brand & Fuel Type) into numerical (Dummy encoding)
    brand_encoded = {"Maruti": 1, "Hyundai": 2, "Tata": 3}.get(brand, 0)
    fuel_encoded = {"Petrol": 1, "Diesel": 2, "Electric": 3}.get(fuel_type, 0)

    # Create feature array
    features = np.array([[year, mileage, brand_encoded, fuel_encoded]])

    # Predict price
    predicted_price = model.predict(features)[0]

    return jsonify({"predicted_price": predicted_price})

if __name__ == "__main__":
    app.run(debug=True)
