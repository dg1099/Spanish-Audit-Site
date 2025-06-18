import streamlit as st
import plotly.express as px
import pandas as pd

spanStates = ['AZ', 'CA', 'CO', 'CT', 'FL', 'GA', 'ID', 'IL', 'KS', 'MD', 'MA', 'MI', 'NE', 'NV', 'NJ', 'NM', 'NY', 'OH', 'OK', 'PA', 'RI', 'TX', 'UT', 'VA', 'WA', 'WI']
gov_types = ['government', 'government affiliated']

eng_df = pd.read_csv('engLocAccuracy1.csv')
span_df = pd.read_csv('spanLocAccuracy1.csv')

def domestic_location_fig(data):
    df = data[data['gov_type'].isin(gov_types)]
    df = df[df['gov_state'] != 'DC']
    df = df[df['gov_state'].isin(spanStates)]
    df = df.groupby('state').mean('accuracy').reset_index()
    df['accuracy'] = df['accuracy'].round(decimals=3)
    fig = px.choropleth(df, locations=df['state'].tolist(),
                    locationmode="USA-states",
                    color="accuracy", 
                    range_color=[0, 1],
                    hover_name="accuracy", 
                    color_continuous_scale=px.colors.make_colorscale(["red", "orange", "yellow", "lightgreen", "green"]),
                    scope='usa')
    fig.update_layout(title='Domestic Location Accuracy of Local Government Search Results')
    return fig

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

eng_loc_fig = domestic_location_fig(eng_df)
span_loc_fig = domestic_location_fig(span_df)
lang_loc = st.selectbox('Choose Graph', ['English', 'Spanish'])
if lang_loc == 'English':
    st.plotly_chart(eng_loc_fig)
elif lang_loc == 'Spanish':
    st.plotly_chart(span_loc_fig)