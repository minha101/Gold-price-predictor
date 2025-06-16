import streamlit as st
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

st.set_page_config(page_title="Gold Price Bivariate Analysis", layout="centered")

# ====== Visualization Class =======
class BivariateAnalysis:
    def __init__(self, data):
        self.data = data

    def scatter_plot(self, x, y):
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(x=self.data[x], y=self.data[y], ax=ax)
        ax.set_title(f'{x} vs {y}')
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        st.pyplot(fig)

    def box_plot(self, x, y):
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x=self.data[x], y=self.data[y], ax=ax)
        ax.set_title(f'{y} by {x}')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        st.pyplot(fig)

    def correlation_heatmap(self):
        fig, ax = plt.subplots(figsize=(8, 6))
        corr = self.data.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        ax.set_title('Correlation Heatmap')
        st.pyplot(fig)

# ====== Main Prediction App =======
class GoldPricePredictorApp:
    def __init__(self):
        self.model = self.load_model("svm_gold_model.pkl")
        self.data = self.load_data()
        self.analyzer = BivariateAnalysis(self.data)

    def load_model(self, path):
        with open(path, 'rb') as file:
            model = pickle.load(file)
        return model

    def load_data(self):
        df = pd.read_csv("Gold  Prices.csv")
        df = df.drop(columns=['Date', 'Stock Splits', 'Capital Gains'], errors='ignore')
        imputer = SimpleImputer(strategy='mean')
        df[df.columns] = imputer.fit_transform(df)
        df['High_Category'] = pd.qcut(df['High'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])
        return df

    def get_user_input(self):
        st.subheader("🔍 Enter values to predict the **Close Price**:")

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
        st.title("🏆 Gold Price Prediction & Analysis App")

        # Sidebar: select mode
        mode = st.sidebar.radio("Choose Mode", ["📈 Predict Close Price", "📊 Data Visualization"])

        if mode == "📈 Predict Close Price":
            user_data = self.get_user_input()

            if st.button("Predict"):
                result = self.predict(user_data)
                st.success(f"✅ Predicted Close Price: **{result:.2f}**")

        elif mode == "📊 Data Visualization":
            st.subheader("Bivariate Analysis")

            chart_type = st.selectbox("Select chart type:", ["Scatter Plot", "Box Plot", "Correlation Heatmap"])

            if chart_type == "Scatter Plot":
                numeric_cols = self.data.select_dtypes(include='number').columns.tolist()
                x = st.selectbox("X-axis:", numeric_cols, index=0)
                y = st.selectbox("Y-axis:", numeric_cols, index=1)
                self.analyzer.scatter_plot(x, y)

            elif chart_type == "Box Plot":
                y = st.selectbox("Select Numeric Column:", self.data.select_dtypes(include='number').columns.tolist())
                self.analyzer.box_plot("High_Category", y)

            elif chart_type == "Correlation Heatmap":
                self.analyzer.correlation_heatmap()

# ====== Run App =======
if __name__ == "__main__":
    app = GoldPricePredictorApp()
    app.run()
