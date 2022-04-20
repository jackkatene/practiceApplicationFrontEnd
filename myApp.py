import streamlit as st
import pandas as pd

st.write ("Hello Kiet")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

