import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
#For Excel File
df = pd.read_excel('Data_SDG_India_Index_2020-21.xlsx')

##Filter Sidebars
state_list = df["State/UT"].to_list()
select = st.sidebar.selectbox('Filter the state/ut here:', state_list, key='1')
if select =="All":
    filtered_df = df
else:
    filtered_df = df[df["State/UT"]==select]
    
col1, col2 = st.columns([2, 1])
    
col1.subheader('World Happiness Index 2021:')
col1.write(filtered_df)

fig1 = plt.figure()
ax = sns.countplot(x='SDG 2', data=filtered_df, palette = 'hls')
col2.subheader('Plot-2')
col2.pyplot(fig1)

