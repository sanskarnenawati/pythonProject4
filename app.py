import streamlit as st
from predict_cost import predict
import numpy as np
import pandas as pd
df  = pd.read_csv("rent.csv")
st.title('Home price prediction')

st.write('---')

# area of the house
area = st.slider('Area of the house', 1000, 5000, 1500)

# no. of bedrooms in the house
bedrooms = st.number_input('No. of bedrooms', min_value=0, step=1)

# no. of balconies in the house
status = st.radio('No. of balconies', ('furnished',"unfurnished","semifurnished"))

location = df['location'].drop_duplicates()
sel_location = st.sidebar.selectbox('Select your location:', location)
if st.button('Predict House Price'):
    cost = predict(np.array([[area, bedrooms, status, location]]))
    st.text(cost[0])