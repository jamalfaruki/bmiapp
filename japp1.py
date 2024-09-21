import streamlit as st
import pandas as pd
st.title("BMI CALCULATOR")
height=st.slider("Select your height in cm:",100,250,100)
weight=st.slider("Select your weight in kg:",40,300,40)
BMI=(weight/(height/100)**2)
st.write("Your BMI is:",BMI)
if BMI<=18.4:
    st.error("underweight")
elif( BMI<=24.9 and BMI>=18.5)  :
    st.success("Normal") 
elif(BMI<=29.9 and BMI>=25):
    st.warning("Overweight")  
elif(BMI<=34.9 and BMI>=30):
    st.warning("Obese")
elif(BMI<=39.9 and BMI>=35):
    st.warning(" Severely Obese")
elif( BMI>=40):
    st.warning("Morbidly Obese")
