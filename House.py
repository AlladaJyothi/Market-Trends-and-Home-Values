import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  sklearn.linear_model import LinearRegression
from sklearn.metrics  import mean_squared_error,r2_score
import pickle
import os

image_path = r"C:\Users\DELL\Pictures\inno_image.webp"
st.write(f"Image path: {image_path}")
st.write(f"File exists: {os.path.exists(image_path)}")

if os.path.exists(image_path):
    st.image(image_path)
else:
    st.error("Image file not found.")

    
name=st.title('Market Trends and Home Values')
st.header('Enter below details')
model = pickle.load(open(r"C:\Users\DELL\Downloads\lr.pkl","rb"))

SquareFeet = st.number_input("Enter the size of the house",min_value = 600, max_value = 20000, step = 50)
Bedrooms = st.number_input("Enter the number of bedrooms",min_value = 0, max_value = 5, step = 1)	
Bathrooms = st.number_input("Enter the number of bathrooms",min_value = 0, max_value = 5, step = 1)	
Neighborhood = st.radio("Enter the neighbourhood",['Rural','Urban','Suburb'])
neighbor = 1 if Neighborhood=="Rural" else 2 if Neighborhood=="Urban" else 3
YearBuilt = st.number_input("Enter the number of year of construction",min_value = 1900, max_value = 2030, step = 1)

if st.button("Submit"):
    price=model.predict([[SquareFeet,Bedrooms,Bathrooms,neighbor,YearBuilt]])
    st.write(f'The price of the flat with given details is Rs.{price}')
    #except Exception as e:
        #st.error(f'Error making prediction:{e}')
        

    
