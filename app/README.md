# 🏥 Personal Health Risk Analyzer (PHRA)

## 📌 Overview

The **Personal Health Risk Analyzer (PHRA)** is a machine learning-based system designed to evaluate an individual's lifestyle habits and estimate their potential health risk.

The system analyzes factors such as sleep, BMI, exercise, stress, and lifestyle habits to generate a **risk score**, provide **trend insights**, and suggest **improvements** for better health.

---

## 🚨 Problem Statement

In modern lifestyles, individuals often ignore early warning signs such as poor sleep, high stress, and lack of physical activity. This leads to long-term health risks that could have been prevented with early awareness.

There is a lack of simple, accessible tools that:

* Analyze lifestyle holistically
* Provide early risk indication
* Offer actionable suggestions

---

## 🎯 Objective

* To build a system that predicts a **health risk score** based on lifestyle factors
* To provide **personalized suggestions** for improvement
* To demonstrate the application of **machine learning in preventive healthcare**

---

## ⚙️ Features

* ✅ Lifestyle-based risk prediction using Machine Learning
* ✅ Hybrid approach (ML + rule-based adjustments)
* ✅ Risk level classification (Low / Moderate / High)
* ✅ Personalized health suggestions
* ✅ Interactive web interface using Streamlit

---

## 🧠 Methodology

### 1. Data Preparation

A structured dataset was created with the following features:

* Age
* BMI
* Sleep hours
* Exercise frequency
* Smoking habit
* Alcohol consumption
* Stress level
* Water intake

---

### 2. Machine Learning Model

* Algorithm: **Random Forest Regressor**
* Type: Supervised Learning (Regression)
* Purpose: Predict a numerical **risk score (0–100)**

---

### 3. Hybrid Risk Adjustment

To improve logical accuracy, rule-based corrections were applied:

* High BMI increases risk
* Low sleep increases risk
* Smoking increases risk

---

### 4. User Interface

A simple and interactive UI was built using **Streamlit**, allowing users to:

* Input lifestyle data
* View risk score
* Get suggestions instantly

---

## 🧪 Results

The system successfully:

* Predicts a lifestyle-based risk score
* Differentiates between low and high-risk profiles
* Provides meaningful suggestions based on user input

---

## 🧰 Tech Stack

* **Python**
* **Pandas, NumPy** (Data Handling)
* **Scikit-learn** (Machine Learning)
* **Matplotlib** (Visualization)
* **Streamlit** (Web UI)
* **Joblib** (Model Saving)
* **Git & GitHub** (Version Control)

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd PHRA
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app/app.py
```

---

## 📊 Output

* Risk Score (0–100)
* Risk Level (Low / Moderate / High)
* Personalized Suggestions

---

## ⚠️ Limitations

* Uses synthetic dataset (not real clinical data)
* Not a substitute for professional medical advice
* Accuracy depends on data quality

---

## 🚀 Future Scope

* Integration with real healthcare datasets
* User history tracking and analytics
* Mobile application development
* Integration with wearable devices
* Advanced AI-based personalized recommendations

---

## 📸 Screenshots

*(Add screenshots of your app here)*

---

## 📚 Learning Outcomes

* Understanding of ML workflow (data → model → prediction)
* Application of regression models
* Importance of feature selection
* Building an end-to-end ML application
* Debugging and problem-solving

---

## 👩‍💻 Author

**Nandini Nigam**
BTech CSE (Health Informatics)
