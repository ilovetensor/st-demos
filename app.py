import streamlit as st
import pandas as pd
st.title('Hello Streamlit!')


df = pd.read_csv('data.csv')
st.line_chart(df, x='Date', y='Sales')
st.dataframe(df)