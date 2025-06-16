import streamlit as st
import plotly.express as px
import pandas as pd

spanStates = ['AZ', 'CA', 'CO', 'CT', 'FL', 'GA', 'ID', 'IL', 'KS', 'MD', 'MA', 'MI', 'NE', 'NV', 'NJ', 'NM', 'NY', 'OH', 'OK', 'PA', 'RI', 'TX', 'UT', 'VA', 'WA', 'WI']
gov_types = ['government', 'government affiliated']

df = pd.read_csv('engLocAccuracy1.csv')
df = df[df['gov_type'].isin(gov_types)]
df = df[df['gov_state'] != 'DC']
df = df[df['gov_state'].isin(spanStates)]

df = df.groupby('state').mean('accuracy').reset_index()


fig = px.choropleth(df, locations=df['state'].tolist(),
                    locationmode="USA-states",
                    color="accuracy", # lifeExp is a column of gapminder
                    range_color=[0, 1],
                    hover_name="accuracy", # column to add to hover information
                    color_continuous_scale=px.colors.make_colorscale(["red", "orange", "yellow", "lightgreen", "green"]),
                    scope='usa')

st.plotly_chart(fig)