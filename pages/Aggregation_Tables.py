import streamlit as st
import pandas as pd

st.title('Aggregation Tables')
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

eng_df = pd.read_csv('engLocAccuracy1.csv')
span_df = pd.read_csv('spanLocAccuracy1.csv')
eng_adp = average_domain_pos(eng_df)
span_adp = average_domain_pos(span_df)

st.write('Each organic result has a position on the page, with a position of 1 meaning it is the ' \
        'very first result. In this table, the domains are sorted in descending order by number of appearances, ' \
        'with each domain having its average organic position')
lang_adp = st.selectbox("Choose Average Domain Position Dataset", ["English", "Spanish"])
if lang_adp == "English":
       st.dataframe(eng_adp.style.set_properties(color='#636363'))
elif lang_adp == "Spanish":
       st.dataframe(span_adp.style.set_properties(color='#636363'))