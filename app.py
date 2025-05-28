import streamlit as st
import pandas as pd
import joblib


model = joblib.load("data/model.pkl")
le_gender = joblib.load("data/le_gender.pkl")
le_region = joblib.load("data/le_region.pkl")
le_service = joblib.load("data/le_service.pkl")

st.title("Customer Satisfaction Prediction")


age = st.number_input("Age", min_value=18, max_value=100, value=30)
subscription_length = st.number_input("Subscription Length (months)", min_value=0, max_value=120, value=12)

gender = st.selectbox("Gender", le_gender.classes_)
region = st.selectbox("Region", le_region.classes_)
service_type = st.selectbox("Service Type", le_service.classes_)

if st.button("Predict Satisfaction Rating"):

    gender_encoded = le_gender.transform([gender])[0]
    region_encoded = le_region.transform([region])[0]
    service_encoded = le_service.transform([service_type])[0]

  
    input_df = pd.DataFrame({
        "Age": [age],
        "SubscriptionLengthMonths": [subscription_length],
        "Gender": [gender_encoded],
        "Region": [region_encoded],
        "ServiceType": [service_encoded]
    })

  
    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Satisfaction Rating: {prediction}")
