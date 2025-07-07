import streamlit as st
import pandas as pd
import methods as m

eng_df = m.load_data('engLocAccuracy1.csv')
span_df = m.load_data('spanLocAccuracy1.csv')

rand_eng = m.sample(eng_df)
rand_span = m.sample(span_df)

st.title('Data Collection')
st.header('Methodology')
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

st.header('Raw Data')
st.write("This is a random sample of what our raw data looked like!")

lang = st.selectbox("Choose Raw Dataset", ["English", "Spanish"])

if lang == "English":
        st.dataframe(rand_eng.style.set_properties(color='#636363'))
elif lang == "Spanish":
       st.dataframe(rand_span.style.set_properties(color='#636363'))