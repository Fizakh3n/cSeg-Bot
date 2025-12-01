import joblib
import numpy as np
import pandas as pd

# Load the trained model and scaler
model = joblib.load("model/lightgbm_customer_segmentation_model.pkl")
scaler = joblib.load("model/scaler.pkl")

def predict_customer_segment(user_input):
    """
    Takes a dictionary of user input, converts it to DataFrame,
    scales it, and returns predicted customer segment.
    """
    try:
        # Convert to DataFrame
        input_df = pd.DataFrame([user_input])

        # Scale the input using the loaded scaler
        input_scaled = scaler.transform(input_df)

        # Predict using the model
        prediction = model.predict(input_scaled)

        # Map numeric label to segment name
        label_map = {
            1: "High-Value Loyalist",
            0: "Budget-Conscious Customer"
        }

        return label_map.get(prediction[0], "Unknown Segment")

    except Exception as e:
        return f"Error during prediction: {str(e)}"

def required_fields():
    """Returns the list of features needed for prediction."""
    return [
        'Income',
        'MntWines',
        'MntMeatProducts',
        'NumWebPurchases',
        'NumCatalogPurchases',
        'NumStorePurchases',
        'Response'
    ]
