import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json

#load model and feature columns
#model, feature_columns = joblib.load("models/marketing_response_model.pkl") # used as baseline
#model, feature_names = joblib.load("models/xgboost_response_model.pkl") 
model = joblib.load("models/xgboost_response_model.pkl")  #only the model
with open("models/feature_columns.json", "r") as f:
    feature_columns = json.load(f)  #feature column names saved separately

# Streamlit Page Config
st.set_page_config(page_title="Marketing Campaign Response Predictor", layout="centered")
st.title("Will the Customer Respond to the Campaign?")
st.markdown("This app uses a trained machine learning model to predict whether a customer is likely to respond to a marketing campaign.")

#sidebar inputs
st.sidebar.header("Customer Profile")

education = st.sidebar.selectbox("Education", ["Basic", "Graduation", "2n Cycle", "Master", "PhD"])
marital_status = st.sidebar.selectbox("Marital Status", ["Single", "Together", "Married", "Divorced", "Widow"])
income = st.sidebar.slider("Income", 0, 120000, 30000, step=1000)
kidhome = st.sidebar.selectbox("Number of Kids at Home", [0, 1, 2])
teenhome = st.sidebar.selectbox("Number of Teens at Home", [0, 1, 2])
recency = st.sidebar.slider("Days Since Last Purchase", 0, 100, 10)
cust_days = st.sidebar.slider("Days Since Joined as Customer", 0, 3000, 1000)
total_spent = st.sidebar.slider("Total Amount Spent on Products", 0, 2500, 500)
mnt_wines = st.sidebar.slider("Spent on Wines", 0, 1000, 0)
mnt_meat = st.sidebar.slider("Spent on Meat", 0, 1000, 0)
num_web = st.sidebar.slider("Number of Web Purchases", 0, 20, 0)
num_catalog = st.sidebar.slider("Number of Catalog Purchases", 0, 20, 0)
accepted_cmp1 = st.sidebar.selectbox("Accepted Campaign 1?", [0, 1])
accepted_cmp5 = st.sidebar.selectbox("Accepted Campaign 5?", [0, 1])

#building input dictionary
input_dict = {
    'Income': income,
    'Kidhome': kidhome,
    'Teenhome': teenhome,
    'Recency': recency,
    'Customer_Duration': cust_days,
    'Total_Spent': total_spent,
    'MntWines': mnt_wines,
    'MntMeatProducts': mnt_meat,
    'NumWebPurchases': num_web,
    'NumCatalogPurchases': num_catalog,
    'AcceptedCmp1': accepted_cmp1,
    'AcceptedCmp5': accepted_cmp5,
    #one-hot encoded features
    'Education_Basic': int(education == "Basic"),
    'Education_Graduation': int(education == "Graduation"),
    'Education_Master': int(education == "Master"),
    'Education_PhD': int(education == "PhD"),
    'Marital_Status_Divorced': int(marital_status == "Divorced"),
    'Marital_Status_Married': int(marital_status == "Married"),
    'Marital_Status_Single': int(marital_status == "Single"),
    'Marital_Status_Together': int(marital_status == "Together"),
    'Marital_Status_Widow': int(marital_status == "Widow")
}

# full input vector with all expected features
full_input = pd.DataFrame([0]*len(feature_columns), index=feature_columns).T  # 1 row of zeros
for key, value in input_dict.items():
    if key in full_input.columns:
        full_input.at[0, key] = value

# show user input for debugging
with st.expander("See Feature Vector Sent to Model"):
    st.dataframe(full_input.T)

# predict button
if st.button("Predict Response"):
    prediction = model.predict(full_input)[0]
    proba = model.predict_proba(full_input)[0][1]  #probability of class 1

    #a custom probability threshold to decide positive class
    threshold = 0.25

    if proba >= threshold:
        st.success(f"YES — Likely to respond! ({proba:.0%} confidence)")
    else:
        st.warning(f"NO — Unlikely to respond. ({proba:.0%} confidence)")

st.markdown("---")
st.caption("Built by Saiful | ML: XGBoost + SMOTE | App: Streamlit")
