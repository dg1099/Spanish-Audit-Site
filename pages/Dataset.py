import streamlit as st
import pandas as pd

st.write("This is a random sample of what our raw data looked like!")
df = pd.read_csv('engLocAccuracy1.csv')
st.write(df.sample(n=10).style.set_properties(color='#636363'))

count = df.groupby('domain')['domain'].value_counts()
count = count.to_frame().reset_index().sort_values(by='domain')
df3 = df.groupby('domain')['org-position'].mean()
df3 = df3.to_frame().reset_index().sort_values(by='domain').rename(columns={'org-position': 'average org-position'})
df4 = pd.merge(count, df3, on='domain')
df4 = df4.sort_values(by='count', ascending=False)

st.write('Here is an aggregated table')
st.dataframe(df4.style.set_properties(color='#636363'))