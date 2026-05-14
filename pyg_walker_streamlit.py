import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

# Importing data

df = pd.read_excel('E-commerce1/cleaned_data_ecommerce.xlsx')

# Adjust the width of the streamlit page
st.set_page_config(
    page_title="use pygwalker in streamlit", 
    layout="wide"
    
)

# Add title
st.title("use pygwalker in streamlit")

# Generate the HTML using pygwalker
pyg_html = pyg.walk(df, return_html=True)

# Embed the HTML into the streamlit app
components.html(pyg_html, height=1000, scrolling=True)