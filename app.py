import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
#For Excel File
df = pd.read_excel('C://Users//anprasanth//Downloads//Data_SDG_India_Index_2020-21.xlsx')
st.title('World Happiness Index 2021:')
st.write(df)

##Filter Sidebars
state_list = df["State/UT"].to_list()
select = st.sidebar.selectbox('Filter the state/ut here:', state_list, key='1')
if select =="All":
    filtered_df = df
else:
    filtered_df = df[df["Stat/UT"]==select]


fig1 = plt.figure()
ax = sns.countplot(x='SDG 2', data= df, palette = 'hls')
st.pyplot(fig1)

