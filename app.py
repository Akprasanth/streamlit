import streamlit as st
import pandas as pd
#For Excel File
df = pd.read_excel('Data_SDG_India_Index_2020-21.xlsx')
st.title('World Happiness Index 2021:')
st.write(df)
