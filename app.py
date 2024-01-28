import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('crop_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app
st.title('Crop Type Prediction App')

# Input fields
temperature = st.number_input('Temperature (Celsius)', min_value=0.0, max_value=50.0, value=25.0)
humidity = st.number_input('Humidity (%)', min_value=0.0, max_value=100.0, value=50.0)
ph = st.number_input('pH', min_value=0.0, max_value=14.0, value=7.0)
rainfall = st.number_input('Rainfall (mm)', min_value=0.0, max_value=400.0, value=100.0)
N = st.number_input('Nitrogen Content', min_value=0, max_value=200, value=50)
P = st.number_input('Phosphorus Content', min_value=0, max_value=200, value=50)
K = st.number_input('Potassium Content', min_value=0, max_value=200, value=50)

# Predict button
if st.button('Predict Crop Type'):
    input_data = pd.DataFrame([[temperature, humidity, ph, rainfall, N, P, K]],
                              columns=['temperature', 'humidity', 'ph', 'rainfall', 'N', 'P', 'K'])
    prediction = model.predict(input_data)
    st.subheader(f'The recommended crop type is: {prediction[0]}')
