import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("model/lightgbm_customer_segmentation_model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.set_page_config(page_title="Customer Segmentation Assistant", page_icon="🤖")

st.title(" 💻Customer Segmentation Chatbot")
st.write("Answer the questions below and I’ll predict the customer segment!")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = {}
if "current_input" not in st.session_state:
    st.session_state.current_input = 0   # Always resets for new question

questions = [
    ("Income", "What is the customer's Income?", "number"),
    ("MntWines", "How much have they spent on non-essential items?", "number"),
    ("MntMeatProducts", "How much on essential food items?", "number"),
    ("NumWebPurchases", "How many times have they shopped online?", "number"),
    ("NumCatalogPurchases", "Catalog purchases?", "number"),
    ("NumStorePurchases", "Store purchases?", "number"),
    ("Response", "Did they respond to past campaigns? (Yes = 1 / No = 0)", "number")

]


st.write(f"**Question {st.session_state.step + 1} / {len(questions)}**")

# Ask questions one-by-one
if st.session_state.step < len(questions):

    key, q_text, q_type = questions[st.session_state.step]

    # ✨ Pop-in effect using markdown spacing
    st.markdown("### 🤖 " + q_text)

    # Reset input to 0 every time a new question appears
    st.session_state.current_input = 0

    ans = st.number_input(
        "Your answer:",
        value=st.session_state.current_input,
        key=f"input_{st.session_state.step}"
    )

    if st.button("Next ➜"):
        st.session_state.answers[key] = ans
        st.session_state.step += 1
        st.rerun()

# After all inputs → predict
else:
    st.success("All questions answered! Generating prediction...")

    values = list(st.session_state.answers.values())
    data = np.array(values).reshape(1, -1)

        # Extract individual values
    income = values[0]
    mnt_wines = values[1]
    mnt_meat = values[2]
    web = values[3]
    catalog = values[4]
    store = values[5]
    response = values[6]

    # Rule-based segmentation
    total_spend = mnt_wines + mnt_meat
    total_purchases = web + catalog + store

    if income > 60000 and total_spend > 500 and total_purchases > 10:
        final_pred = 1   # High-value customer
    else:
        final_pred = 0   # Budget-conscious

    st.subheader(f"🔍 Predicted Customer Segment: **{final_pred}**")


    if final_pred == 1:
        st.info("This customer spends well and responds to campaigns.")
    else:
        st.warning("This customer is more value-conscious and needs targeted campaigns.")

    if st.button("🔄 Restart"):
        st.session_state.step = 0
        st.session_state.answers = {}
        st.session_state.current_input = 0
        st.rerun()

