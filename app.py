import streamlit as st
import pandas as pd
import pickle

class GoldPricePredictorApp:
    def __init__(self):
        self.model = self.load_model("C:/Users/Lenovo L380 A&I//OneDrive/Desktop/project/svm_gold_model.pkl")

    def load_model(self, path):
        with open(path, 'rb') as file:
            model = pickle.load(file)
        return model

    def get_user_input(self):
        st.title("📊 Gold Price Prediction App")
        st.markdown("Enter values to predict the **Close Price**:")

        open_price = st.number_input("Open Price", min_value=0.0, format="%.2f")
        high_price = st.number_input("High Price", min_value=0.0, format="%.2f")
        low_price = st.number_input("Low Price", min_value=0.0, format="%.2f")
        volume = st.number_input("Volume", min_value=0.0, format="%.2f")
        dividends = st.number_input("Dividends", min_value=0.0, format="%.2f")

        user_data = pd.DataFrame({
            "Open": [open_price],
            "High": [high_price],
            "Low": [low_price],
            "Volume": [volume],
            "Dividends": [dividends]
        })
        return user_data

    def predict(self, input_data):
        input_data = input_data[['Open', 'High', 'Low', 'Volume', 'Dividends']]
        return self.model.predict(input_data)[0]

    def run(self):
        user_data = self.get_user_input()

        if st.button("Predict"):
            result = self.predict(user_data)
            st.success(f"✅ Predicted Close Price: **{result:.2f}**")

if __name__ == "__main__":
    app = GoldPricePredictorApp()
    app.run()
