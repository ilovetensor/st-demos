import streamlit as st
import pandas as pd
st.title('Hello Streamlit!')


df = pd.read_csv('st-demos/data.csv')
st.line_chart(df, x='Date', y='Sales')
st.dataframe(df)