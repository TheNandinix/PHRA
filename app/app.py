import streamlit as st
import numpy as np
import joblib

# load model
model = joblib.load("model.pkl")
st.markdown("## 🏥 Personal Health Risk Analyzer")
st.markdown("Analyze your lifestyle and predict health risk")

st.title("Personal Health Risk Analyzer 🏥")

# inputs
age = st.slider("Age", 18, 60)
bmi = st.slider("BMI", 15.0, 40.0)
sleep = st.slider("Sleep Hours", 3, 10)
exercise = st.slider("Exercise Days per Week", 0, 7)
smoking = st.selectbox("Smoking (0=No,1=Yes)", [0,1])
alcohol = st.selectbox("Alcohol (0=No,1=Yes)", [0,1])
stress = st.slider("Stress Level (1-10)", 1, 10)
water = st.slider("Water Intake (glasses/day)", 1, 12)
# previous risk (for trend)
prev_risk = st.slider("Previous Risk Score", 0, 100)

# predict button
if st.button("Predict"):

    data = np.array([[age,bmi,sleep,exercise,smoking,alcohol,stress,water]])

    risk = model.predict(data)[0]

    # rule correction
    if bmi > 30:
        risk += 10
    if sleep < 5:
        risk += 10
    if smoking == 1:
        risk += 10

    risk = min(risk, 100)

    st.metric(label="Risk Score", value=round(risk,2))