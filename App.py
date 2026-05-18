import streamlit as st
import pandas as pd
import numpy as np
import joblib

models = {
    "Decision Tree": joblib.load("decision_tree_model.pkl"),
    "Random Forest": joblib.load("random_forest_model.pkl"),
    "Logistic Regression": joblib.load("logistic_regression_model.pkl"),
    "GBoost": joblib.load("gboost_model.pkl")
}

medians = joblib.load("medians.pkl")

zero_cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

st.title(" Diabetes Prediction App")

selected_model = st.selectbox(
    "Choose Model",
    ["Random Forest", "Decision Tree", "Logistic Regression", "GBoost"]
)

st.write("Enter patient data:")

preg = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose", 0, 200, 120)
bp = st.number_input("Blood Pressure", 0, 140, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 1, 120, 30)

if st.button("Predict"):

    input_df = pd.DataFrame([{
        "Pregnancies": preg,
        "Glucose": glucose,
        "BloodPressure": bp,
        "SkinThickness": skin,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }])


    input_df[zero_cols] = input_df[zero_cols].replace(0, np.nan)

    for col in zero_cols:
        input_df[col] = input_df[col].fillna(medians[col])

    model = models[selected_model]

    prediction = model.predict(input_df)[0]

    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(input_df)[0][1]
    else:
        prob = None

    if prediction == 1:
        if prob is not None:
            st.error(f"!!! High Risk of Diabetes using {selected_model} (Probability: {prob:.2f})")
        else:
            st.error(f"!!! High Risk of Diabetes using {selected_model}")
    else:
        if prob is not None:
            st.success(f" Low Risk of Diabetes using {selected_model} (Probability: {prob:.2f})")
        else:
            st.success(f" Low Risk of Diabetes using {selected_model}")