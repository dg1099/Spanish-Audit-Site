import streamlit as st
import pandas as pd
import plotly.express as px
from trafilatura import fetch_url, extract_metadata
import csv
from htmldate import find_date

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

@st.cache_data
def domestic_location(data):
    spanStates = ['AZ', 'CA', 'CO', 'CT', 'FL', 'GA', 'ID', 'IL', 'KS', 'MD', 'MA', 'MI', 'NE', 'NV', 'NJ', 'NM', 'NY', 'OH', 'OK', 'PA', 'RI', 'TX', 'UT', 'VA', 'WA', 'WI']
    gov_types = ['government', 'government affiliated']

    df = data[data['gov_type'].isin(gov_types)]
    df = df[df['gov_state'] != 'DC']
    df = df[df['gov_state'].isin(spanStates)]
    df = df.groupby('state').mean('accuracy').reset_index()
    df['accuracy'] = df['accuracy'].round(decimals=3)
    return df

@st.cache_data
def domestic_fig(df):
    fig = px.choropleth(df, locations=df['state'].tolist(),
                    locationmode="USA-states",
                    color="accuracy", 
                    range_color=[0, 1],
                    hover_name="accuracy", 
                    color_continuous_scale=px.colors.make_colorscale(["red", "orange", "yellow", "lightgreen", "green"]),
                    scope='usa')
    fig.update_layout(title='Domestic Location Accuracy of Local Government Search Results')
    return fig

# def get_date(url):
#     download = fetch_url(url)
#     metadata = extract_metadata(download)
#     return metadata.date

# if __name__ == "__main__":
#     with open('spanLocAccuracy1.csv', 'r', encoding = 'utf-8') as inFile:
#         with open('last-updated.csv', 'w', encoding='utf-8', newline='') as outFile:
#             writer = csv.writer(outFile)
#             fieldnames = ['domain', 'title', 'link', 'gov_type', 'last_update']
#             writer.writerow(fieldnames)
#             reader = csv.DictReader(inFile)
#             for row in reader:
#                 new = [row['domain'], row['title'], row['link'], row['gov_type']]
#                 try:
#                     date = get_date(row['link'])
#                     # print(f'{row['title']}: {date}')
#                 # except:
#                 #     date = find_date(row['link'])
#                 except:
#                     print(f'Failed: {row['link']}')
#                     date = 'Unknown'
#                 new.append(date)
#                 writer.writerow(new)