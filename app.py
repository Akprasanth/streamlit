import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#For Excel File
df = pd.read_excel('Data_SDG_India_Index_2020-21.xlsx')

#Second Excel file
df2 = pd.read_excel('Test_file.xlsx')
countries = tuple(df2.COUNTRY.to_list())
cat_counts = {
    'CAT1': df2.CAT1.to_numpy(),
    'CAT2': df2.CAT2.to_numpy(),
    'CAT3': df2.CAT3.to_numpy(),
    'CAT4': df2.CAT4.to_numpy(),
}

##Filter Sidebars
state_list = df["State/UT"].to_list()
select = st.sidebar.selectbox('Filter the state/ut here:', state_list, key='1')
if select =="All":
    filtered_df = df
else:
    filtered_df = df[df["State/UT"]==select]
    
tab1, tab2 = st.tabs(["Page1", "Page2"])

with tab1:
    col1, col2 = st.columns([1, 1])
    col1.subheader('World Happiness Index 2021:')
    col1.write(filtered_df)

    width = 0.8  # the width of the bars: can also be len(x) sequence
    fig, ax = plt.subplots()
    bottom = np.zeros(6)
    for cat, cat_count in cat_counts.items():
        p = ax.bar(countries, cat_count, width, label=cat, bottom=bottom)
        bottom += cat_count

        ax.bar_label(p, label_type='center')
    ax.set_title('Countries and Status')
    ax.legend()
    col2.pyplot(fig)

    st.write(df)

with tab2:
    st.write(df) 
