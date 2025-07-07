import streamlit as st
import pandas as pd

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

@st.cache_data
def sample(df):
    return df.sample(n=10)

@st.cache_data
def average_domain_pos(data):
    df1 = data.groupby('domain')['domain'].value_counts()
    df1 = df1.to_frame().sort_values(by='domain').rename(columns={'count': '# of appearances'})
    df2 = data.groupby('domain')['org-position'].mean()
    df2 = df2.to_frame().sort_values(by='domain').rename(columns={'count': '# of appearances', 'org-position': 'average org-position'})
    df3 = pd.merge(df1, df2, on='domain')
    df3 = df3.sort_values(by='# of appearances', ascending=False)
    return df3.reset_index()[:100]

@st.cache_data
def domain_freq(df1, df2):
    col1 = df1[['domain', '# of appearances']]
    col2 = df2[['domain', '# of appearances']]
    tempdf = pd.merge(col1, col2, on='domain', how='outer')
    tempdf = tempdf.fillna(0)
    tempdf = tempdf.rename(columns={'# of appearances_x': 'english appearances', '# of appearances_y': 'spanish appearances'})
    tempdf['difference'] = tempdf['english appearances'] - tempdf['spanish appearances']
    return tempdf.sort_values(by='difference').reset_index().drop('index', axis=1)[:100]

@st.cache_data
def gov_perc(data, county):
      df = data[data['location'] == county]
      col1 = df.groupby('query')['query'].value_counts()
      col2 = df.groupby('query')['gov_type'].agg('sum')
      df = pd.merge(col1, col2, on='query')
      df['gov_type'] = df['gov_type'].apply(lambda x: x.count('g') if type(x) != int else 0)
      df['percent'] = df['gov_type']/df['count']
      return df.reset_index()