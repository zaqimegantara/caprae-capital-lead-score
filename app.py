import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("lead_scorer_smote.pkl")
preprocessor = joblib.load("preprocessor.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.title("🔍 Lead Scoring Prediction Tool")

st.markdown("Enter company information below to predict lead quality (High, Medium, Low).")

# Input fields
business_type = st.selectbox("Business Type", ["B2B", "B2B2C", "B2C"])
revenue = st.number_input("Revenue (in million USD)", min_value=0.0, step=0.1)
employees = st.number_input("Employees Count", min_value=1, step=1)
year_founded = st.number_input("Year Founded", min_value=1900, max_value=2025, step=1)
owner_title = st.selectbox("Owner's Title", ["CEO", "Founder", "President", "Owner", "Manager", "Partner"])
bbb_rating = st.selectbox("BBB Rating", ["A+", "A", "B", "C", "D", "F", "NR"])

# Predict button
if st.button("Predict Lead Quality"):
    # Create input DataFrame
    input_df = pd.DataFrame([{
        "Business Type": business_type,
        "Revenue": revenue,
        "Employees Count": employees,
        "Year Founded": year_founded,
        "Owner's Title": owner_title,
        "BBB Rating": bbb_rating
    }])

    # Preprocess
    input_processed = preprocessor.transform(input_df)

    # Predict
    prediction = model.predict(input_processed)
    prediction_label = label_encoder.inverse_transform(prediction)[0]

    st.success(f"✅ Predicted Lead Quality: **{prediction_label}**")
