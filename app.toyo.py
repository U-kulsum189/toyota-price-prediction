import numpy as np # type: ignore
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("mlr.pkl", "rb")
mlr = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_price_range(Age_08_04, KM, Weight):
    prediction = mlr.predict([[Age_08_04, KM, Weight]])
    return prediction

def main():
    st.title("Toyota Corolla Price Prediction")
    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Car Price ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # FIXED number inputs (numeric only)
    Age_08_04 = st.number_input("Age_08_04", min_value=0)
    KM = st.number_input("KM", min_value=0)
    Weight = st.number_input("Weight", min_value=0)

    result = ""
    if st.button("Predict"):
        result = predict_price_range(Age_08_04, KM, Weight)
        st.success(f"The output is {result}")

    if st.button("About"):
        st.text("Let's Learn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()
