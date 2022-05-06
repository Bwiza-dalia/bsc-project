from cProfile import label
from pyexpat import model
import pandas as pd
import streamlit as st
#import joblib 


#model = joblib.load('models/bsc_sales_model.pkl','wb')

from data import dataset
DataFrame= dataset()

def form_function():
    inputs = dict()

	
    st.title("sales prediction")

    with st.form("my_form"):
        _SalesAM_ID = st.text_input('enter salesAM ID')
        _CustomerID = st.text_input('enter Customer ID')
        _SiteID = st.text_input('enter _SiteID')
        Order_Quantity = st.text_input('enter Order Quantity')
        Discount_Applied = st.text_input('enter Discount Applied')
        Unit_Price = st.text_input('enter Unit Price')
        Unit_Cost = st.text_input('enter Unit Cost')
        Total_Amount = st.text_input('enter Total Amount')
        Month = st.text_input('enter Month')
        Bandwidth = st.text_input('enter Bandwidth')

        #submited form

        submitted = st.form_submit_button("submit")
        if submitted:
            inputs['_SalesAM_ID'] = _SalesAM_ID
            inputs['_CustomerID'] = _CustomerID
            inputs['_SiteID'] = _SiteID
            inputs['Order_Quantity'] =Order_Quantity
            inputs['Discount_Applied'] = Discount_Applied
            inputs['Unit_price'] = Unit_Price
            inputs['Unit_Cost'] = Unit_Cost
            inputs['Total_Amount'] = Total_Amount
            inputs['Month'] = Month
            inputs['Bandwidth'] = Bandwidth

            #prediction
            #prediction = model.predict([[inputs['_SalesAM_ID'],inputs['_CustomerID'],inputs['_SiteID'],inputs['Order_Quantity'],inputs['Discount_Applied'],inputs['Unit_price'],inputs['Total_Amount'],inputs['Month'],inputs['Bandwidth']]])
            #st.subheader(int(prediction[0]))

            


            





            


    

    
# form = st.form("my_form")
# form.slider("Inside the form")

# st.slider("Outside the form")

# # Now add a submit button to the form:
# form.form_submit_button("Submit")
