import streamlit as st
import pandas as pd

st.write("This is a random sample of what our raw data looked like!")
df = pd.read_csv('engLocAccuracy1.csv')
st.write(df.sample(n=10).style.set_properties(color='#636363'))