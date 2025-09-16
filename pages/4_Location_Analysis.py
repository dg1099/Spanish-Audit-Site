import streamlit as st
import plotly.express as px
import pandas as pd
import methods as m

eng_df = pd.read_csv('engLocAccuracy1.csv')
span_df = pd.read_csv('spanLocAccuracy1.csv')

st.title('Location Analysis')
st.header('Domestic Location Analysis')
st.write('After collecting our data, we wanted to determine how accurate results were to the location it was searched from. ' \
        'For example, if the search were from Los Angeles, California, all results from California would ' \
        'be given an accuracy score of 1. Otherwise, it would be given a score of 0. We only gave these ' \
        'scores to government websites that were not on the federal level (i.e. sites like usa.gov would ' \
        'be excluded). That means that the domestic location accuracy is based on municipal, local, district ' \
        'township, etc. sites that appeared.')
# should probably mention the database we used
st.write('We found that English searched generally performed well, with ' \
        'the lowest score of 0.45 given to Oklahoma, which could be explained by the fact that the sole ' \
        'locallity we observed was named Texas County. For Spanish, we found most scores close to 0, with ' \
        'the highest being California at 0.56. This indicates that Spanish searches were given an ' \
        'abundance of resources from other states, but many of these resources are state specific, such ' \
        'as when mail-in ballot deadlines are, where voting polls are located in a district, and who ' \
        'represents a county, meaning they would not be beneficial to a search user.')

eng_loc = m.domestic_location(eng_df)
span_loc = m.domestic_location(span_df)

lang_loc = st.selectbox('Choose Graph', ['English', 'Spanish'])
if lang_loc == 'English':
    st.plotly_chart(m.domestic_fig(eng_loc))
elif lang_loc == 'Spanish':
    st.plotly_chart(m.domestic_fig(span_loc))