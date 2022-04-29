import streamlit as st
from visual_analysis import *

SIDEBAR_OPTION_PROJECT_WIKI = "Project Wiki"
SIDEBAR_OPTION_ANALYSIS = "Data Analysis & Visualisation"
SIDEBAR_OPTION_TEAM = "Meet the Team"
SIDEBAR_OPTION_FORECAST = "Predict"

SIDEBAR_OPTIONS = [SIDEBAR_OPTION_PROJECT_WIKI, SIDEBAR_OPTION_ANALYSIS, SIDEBAR_OPTION_FORECAST, SIDEBAR_OPTION_TEAM]


def wiki_section():
    st.write( "*scope of project*")
    st.text("Broadband Systems Corporation has been at the forefront of" )
    st.text("ICT services in Rwanda with its mission of providing world-class broadband connectivity and solutions to empower citizens,") 
    st.text("communities, government, and businesses in Rwanda and the region, However, Bsc logistics and sales are not data-driven,")
    st.text("this can reduce the delivery services and increase the wastage.")
    st.text(" This project is designed with the capacity of making their business model more data-driven by  making the balance between Bsc’s demands and supply.")
    st.text("Project Goals")
    st.text("Trends")

def visual_analysis_section():

    #Defining SUB-SIDEBAR OPTIONS in the Visualisation section
    VIZ_SIDEBAR_OPTION_SALES = "SALES"
    VIZ_SIDEBAR_OPTION_CUSTOMERS = "CUSTOMERS"
    VIZ_SIDEBAR_OPTION_PRODUCTS = "PRODUCTS"
    VIZ_SIDEBAR_OPTION_SITE = "SITE"
    VIZ_SIDEBAR_OPTION_SALES_TEAM = "SALES TEAM"

    VIZ_SIDEBAR_OPTIONS = [VIZ_SIDEBAR_OPTION_SALES, VIZ_SIDEBAR_OPTION_CUSTOMERS, VIZ_SIDEBAR_OPTION_PRODUCTS, VIZ_SIDEBAR_OPTION_SITE, VIZ_SIDEBAR_OPTION_SALES_TEAM]

    VIZ_SIDEBAR_STATUS = st.sidebar.selectbox('Visualisation Section', VIZ_SIDEBAR_OPTIONS)

    if VIZ_SIDEBAR_STATUS == VIZ_SIDEBAR_OPTION_SALES:
        sales_section()
    elif VIZ_SIDEBAR_STATUS == VIZ_SIDEBAR_OPTION_CUSTOMERS:
        st.text("Customers")
    elif VIZ_SIDEBAR_STATUS == VIZ_SIDEBAR_OPTION_PRODUCTS:
        st.text("Product")
    elif VIZ_SIDEBAR_STATUS == VIZ_SIDEBAR_OPTION_SITE:
        st.text("Site Data")
    elif VIZ_SIDEBAR_STATUS == VIZ_SIDEBAR_OPTION_SALES_TEAM:
        st.text("Sales team")
    else:
        pass



def main():
    st.sidebar.success("Please choose an option bellow.")
    SIDEBAR_STATUS = st.sidebar.selectbox('Menu Option', SIDEBAR_OPTIONS)

    if SIDEBAR_STATUS == SIDEBAR_OPTION_PROJECT_WIKI:
        st.title("BCS Sales Forecasting Project")
        wiki_section()
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_ANALYSIS:
        visual_analysis_section()
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_FORECAST:
        st.text("Welcome to the model prediction")
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_TEAM:
        st.text("Meet the team")
    else:
        pass



main()