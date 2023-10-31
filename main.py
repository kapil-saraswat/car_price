import pandas as pd
import datetime
import xgboost as xgb
import streamlit as st

def main():
    html_temp = """
        <h1>Car Price Prediction</h1>
    """
    model = xgb.XGBRegressor()
    model.load_model("xgb_model.json")
    
    st.markdown(html_temp,unsafe_allow_html=True)
st.markdown("This app will help you to prdict your car price")
p1 = st.number_input("Enter car showroom price",2.5,25.5,step=1.0)
p2 = st.number_input("Enter car driven in  KM",100,50000,step=100)
s1 = st.selectbox("Select the fuel_type",("Petrol","Diesel","CNG"))

if s1== "Petrol":
    p3=0
elif s1== "Diesel":
    p3=1
elif s1 == "CNG":
    p3=2

s2 = st.selectbox("Select the Seller_Type",("Dealer","INdividual"))

if s2== "Dealer":
    p4=0 
elif s2 == "INdividual":
    p4=1

s3= st.selectbox("Select the Transmission_type",("Manual","Automatic"))

if s3== "Manual":
    p5=0 
elif s3 == "Automatic":
    p5=1
p6 = st.slider("NO. of owners",0,3)

date_time = datetime.datetime.now()
year= st.number_input('Car purchase year',1990,date_time.year,step=1)
    
p7 = date_time.year - year

data_new = pd.DataFrame({
    'Present_Price':5.59,
    'Kms_Driven':27000,
    'Fuel_Type':0,
    'Seller_Type':0,
    'Transmission':0,
    'Owner':0,
    'Age':8},index=[0])


if __name__== '__main__':
    main()
    
    
           