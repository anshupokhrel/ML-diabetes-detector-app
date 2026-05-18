#  Diabetes Prediction App

A machine learning web application that predicts the risk of diabetes based on clinical patient data, built with **Streamlit** and trained on the **PIMA Indians Diabetes Dataset**.

---

##  Overview

This project compares four machine learning classifiers to predict whether a patient is at risk of diabetes, providing real-time predictions through an interactive web interface.

  | Model         | Training Accuracy   
  Decision Tree   | 79.84% |
  Random Forest   | 84.27% |
  Logistic Regression | 71.14% |
  Gradient Boosting (XGBoost) | 99% |

---

##  Features

- **Multi-model comparison** — switch between 4 classifiers in real time
- **Probability output** — models display confidence score alongside prediction
- **Smart data preprocessing** — zero values in clinical fields are replaced with feature medians (clinically meaningful imputation)
- **Clean UI** — built with Streamlit for a fast, interactive experience

---
##  Hybrid Approach (ML + Expert System)

In addition to machine learning models, a rule-based expert system was implemented using domain-inspired medical logic.

This allows comparison between:
- Human-like reasoning (Expert System)
- Data-driven learning (Machine Learning)

### Expert Rules

- If Glucose > 125 → Diabetic  
- If BMI > 35 → Diabetic  
- If BMI > 30 and Age > 35 → Diabetic  

📌 This highlights the trade-off between interpretability and predictive power.

##  Project Structure

```
diabetes-prediction/

├── App.py                        # Streamlit web application
├── Training.csv                   # PIMA Indians Diabetes Dataset
├── medians.pkl                    # Saved feature medians for imputation

├── decision_tree_model.pkl        # Trained Decision Tree
├── random_forest_model.pkl        # Trained Random Forest
├── logistic_regression_model.pkl  # Trained Logistic Regression
├── gboost_model.pkl               # Trained XGBoost Classifier

├── ML__expert_system.ipynb                # Full training notebook (EDA + modeling)
└── README.md
```

---

##  Dataset

- **Source:** PIMA Indians Diabetes Dataset
- **Samples:** 2,460 patient records
- **Features:** 8 clinical attributes
- **Target:** `Outcome` — 0 (No Diabetes) / 1 (Diabetes)

### Input Features

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure (mm Hg) |
| SkinThickness | Triceps skinfold thickness (mm) |
| Insulin | 2-Hour serum insulin (mu U/ml) |
| BMI | Body mass index (kg/m²) |
| DiabetesPedigreeFunction | Genetic diabetes risk score |
| Age | Age in years |

---

##  Preprocessing

Zero values in the following clinical columns are biologically implausible and are replaced with the **median** of each feature (computed from the training set):

- `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI`

---

##  Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/anshupokhrel/ML-diabetes-prediction-app.git
cd diabetes-prediction
```

### 2. Install dependencies

```bash
pip install streamlit pandas numpy scikit-learn xgboost joblib
```

### 3. Run the app

```bash
streamlit run App.py
```

Then open your browser at `http://localhost:8501`

---

##  Dependencies

```
streamlit
pandas
numpy
scikit-learn
xgboost
joblib
```

---

##  Contact

Feel free to connect on [LinkedIn](https://www.linkedin.com/in/YOUR_PROFILE) or open an issue for questions and suggestions.

---

>  **Disclaimer:** This app is for educational purposes only and is not a substitute for professional medical advice.
