# cSeg-Bot 🤖

Customer Segmentation Chatbot — a mini project to classify customers into High-Value Loyalists or Budget-Conscious/Low-Engagement based on their purchase behavior.

---

## Overview

This project demonstrates a simple machine learning classifier that predicts a customer segment from a few key features:

- Income
- Non-essential and essential spending
- Online, store, and catalog purchases
- Campaign response

The goal: help businesses understand customer behavior and optimize marketing campaigns.

---

## Features

- Step-by-step chatbot-like interface using Streamlit
- Automatic feature scaling and prediction using a trained LightGBM model
- Highlights insights for each predicted segment:
  - High-Value Loyalists → Target with loyalty perks and special offers
  - Budget-Conscious Customers → Adjust campaigns for cost-effective engagement

---

## Tech Stack

- Python (3.x)
- LightGBM (for the classifier)
- Joblib (model & scaler persistence)
- Streamlit (frontend interface)
- NumPy & Pandas (data handling)

---

## How to Run Locally

How to Run Locally

1. Clone the repository:
   git clone https://github.com/Fizakh3n/cSeg-Bot.git
   cd cSeg-Bot

2. Install required packages:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app.py

4. Answer the questions step-by-step and see your customer segment prediction.


---

## Project Structure

cSeg-Bot/
│
├─ app.py                  # Streamlit app
├─ model/
│   ├─ lightgbm_customer_segmentation_model.pkl
│   └─ scaler.pkl
├─ utils/
│   └─ predictor.py        # Prediction function             
└─ README.md

---

## Future Scope

- Automate classification from live Excel/Database data
- Real-time prediction as new customer data arrives
- Integrate with marketing tools to automatically trigger campaigns
- Add dashboards for analytics and engagement insights

---

## Notes

- This is a demo/miniproject, safe for portfolio purposes.
- Data used for prediction is simulated or user-inputted — no private customer data is included.

---

## License

This project is for educational and portfolio purposes only.
