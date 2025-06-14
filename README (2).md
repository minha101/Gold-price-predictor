# 📊 Gold Price Prediction App

This is a **machine learning web application** built with **Streamlit** that predicts the **closing price of gold** based on financial indicators like Open, High, Low, Volume, and Dividends. The model behind the scenes is an **SVM (Support Vector Machine)** trained using historical gold prices.

---

## 🚀 Features

- 📈 Predicts the **Close Price** of gold.
- 📊 Takes user inputs for:
  - Open Price
  - High Price
  - Low Price
  - Volume
  - Dividends
- ✅ Displays the predicted price instantly.
- 🧠 Uses a trained SVM model saved as `.pkl`.
- 🌐 Interactive UI powered by **Streamlit**.

---

## 🧠 Machine Learning Model

- **Algorithm Used**: Support Vector Machine (SVM)
- **Training Data**: Historical gold prices from `Gold Prices.csv`
- **Model File**: `svm_gold_model.pkl`
- **Target Variable**: `Close` (closing price of gold)

---

## 🗂️ Project Structure

---
├── app.py                  # Streamlit app

├── goldprice.ipynb         # Model training and EDA notebook
├── Gold Prices.csv         # Dataset

├── svm_gold_model.pkl      # Trained ML model (not included in this repo)

└── README.md               # Project documentation

---

---

## 💻 How to Run

### 📌 Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip
- Streamlit
- pandas
- scikit-learn

### ✅ Steps to Run the App

1. Clone or download this repository.
2. Place `svm_gold_model.pkl` in the same folder as `app.py`.
3. Run the app:

streamlit run app.py

---

## 📷 Sample UI

The app looks like this:

- Input section with number fields for Open, High, Low, Volume, Dividends
- “Predict” button to get the Close Price
- Output message showing predicted value

---

## ✨ Author

**Minha Mehmood**  
AI student at Superior University | Future Software Engineer  
Project goal: Understand ML deployment & predict financial data using real-world models.

---

## 📬 Feedback & Future Improvements

- Add visual graphs for price trends.
- Compare SVM with other models (like Random Forest, XGBoost).
- Deploy using Streamlit Cloud.

---
