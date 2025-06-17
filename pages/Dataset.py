import streamlit as st
import pandas as pd

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
eng_df = pd.read_csv('engLocAccuracy1.csv')
span_df = pd.read_csv('spanLocAccuracy1.csv')
st.dataframe(eng_df.sample(n=10).style.set_properties(color='#636363'))
st.dataframe(span_df.sample(n=10).style.set_properties(color='#636363'))

st.header('Aggregation Tables')
st.write('To make the data meaningful, here are a few aggregated tables that show key differences ' \
        'in Google Search results')
st.subheader('Average Domain Position')
def average_domain_pos(data):
    df1 = data.groupby('domain')['domain'].value_counts()
    df1 = df1.to_frame().reset_index().sort_values(by='domain')
    df2 = data.groupby('domain')['org-position'].mean()
    df2 = df2.to_frame().reset_index().sort_values(by='domain').rename(columns={'count':'# of appearances', 'org-position': 'average org-position'})
    df3 = pd.merge(df1, df2, on='domain')
    df3 = df3.sort_values(by='count', ascending=False)
    return df3
eng_adp = average_domain_pos(eng_df)
span_adp = average_domain_pos(span_df)
st.write('Each organic result has a position on the page, with a position of 1 meaning it is the ' \
        'very first result. In this table, the domains are sorted in descending order by number of appearances, ' \
        'with each domain having its average organic position')
st.dataframe(eng_adp.style.set_properties(color='#636363'))
st.dataframe(span_adp.style.set_properties(color='#636363'))