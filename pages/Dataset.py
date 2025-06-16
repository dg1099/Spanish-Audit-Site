import streamlit as st
import pandas as pd

st.title('Data Collection')
st.subheader('Methodology')
st.write('''Section 203 of the Voting Rights Act dictates that political subdivisions 
         with more than 10,000 people or over 5 percent of the population speaking a language 
         minority must provide voting materials in that language. We gathered a list of these 
         subdivisions (using the U.S. Census API) where Spanish voting materials were 
         required by law. In total, we had 231 localities.''')
st.write('''With these localities, we followed methods used in "Algorithmic Misjudgement
         in Google Search Results: Evidence from Auditing the US Online Electoral Information
         Environment" (Perrault et al., 2024) to search 131 political queries in each location, 
         once in English and once in Spanish (232 in total) on Google. We collected the search
         result pages to note any differences in searching in each language.''')

st.subheader('Raw Data')
st.write("This is a random sample of what our raw data looked like!")
df = pd.read_csv('engLocAccuracy1.csv')
st.write(df.sample(n=10).style.set_properties(color='#636363'))

st.subheader('Aggregation Tables')
st.write('To make the data meaningful, here are a few aggregated tables that show key differences' \
'in Google Search results')
count = df.groupby('domain')['domain'].value_counts()
count = count.to_frame().reset_index().sort_values(by='domain')
df3 = df.groupby('domain')['org-position'].mean()
df3 = df3.to_frame().reset_index().sort_values(by='domain').rename(columns={'org-position': 'average org-position'})
df4 = pd.merge(count, df3, on='domain')
df4 = df4.sort_values(by='count', ascending=False)

st.write('Here is an aggregated table')
st.dataframe(df4.style.set_properties(color='#636363'))