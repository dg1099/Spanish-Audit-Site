import pandas as pd
import plotly.express as px
import streamlit as st
import methods as m

soc_domains = [
                'youtube.com', 
                'instagram.com',
                'twitter.com',
                'x.com',
                'meta.com',
                'facebook.com',
                'pinterest.com',
                'reddit.com',
                'tiktok.com',
                ]

eng_df = m.load_data('engLocAccuracy1.csv')
span_df = m.load_data('spanLocAccuracy1.csv')

eng_soc = eng_df[eng_df['domain'].isin(soc_domains)].sort_values(by='domain')
eng_soc['count'] = 1#.to_frame().sort_values(by='count').reset_index()
eng_soc['lang'] = 'english'
eng_soc = eng_soc[['domain', 'query', 'lang', 'count']]

span_soc = span_df[span_df['domain'].isin(soc_domains)]
span_soc['count'] = 1#.to_frame().sort_values(by='count').reset_index()
span_soc['lang'] = 'spanish'
span_soc = span_soc[['domain', 'query', 'lang', 'count']]
soc = pd.concat([eng_soc, span_soc])
#soc['total'] = soc['count_x'] + soc['count_y']

fig = px.bar(soc, x='domain', y='count', color='lang', barmode='group', hover_data='query')

st.plotly_chart(fig)

eng_soc['count'] = eng_soc.groupby('query')['query'].transform('count')
eng_soc = eng_soc.drop_duplicates()
span_soc['count'] = span_soc.groupby('query')['query'].transform('count')
span_soc = span_soc.drop_duplicates()
soc = pd.concat([eng_soc, span_soc]).sort_values(by='count')
st.dataframe(eng_soc)
gif = px.bar(soc, x='domain', y='count', color='lang', barmode='group', hover_data='query')
st.plotly_chart(gif)

# suggests misunderstanding in queries