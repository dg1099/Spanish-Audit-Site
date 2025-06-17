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
    fig = px.choropleth(df, locations=df['state'].tolist(),
                    locationmode="USA-states",
                    color="accuracy", 
                    range_color=[0, 1],
                    hover_name="accuracy", 
                    color_continuous_scale=px.colors.make_colorscale(["red", "orange", "yellow", "lightgreen", "green"]),
                    scope='usa')
    return fig

eng_loc_fig = domestic_location_fig(eng_df)
span_loc_fig = domestic_location_fig(span_df)

st.plotly_chart(eng_loc_fig)
st.plotly_chart(span_loc_fig)