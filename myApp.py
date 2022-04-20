import streamlit as st
import pandas as pd

@st.cache

st.image('Logo-KDT-JU.png')
st.write("My First Streamlit Web App")
df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)

#streamlit run sample.py
