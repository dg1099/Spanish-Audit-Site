import streamlit as st
import pandas as pd

st.title('Aggregation Tables')
st.write('To make the data meaningful, here are a few aggregated tables that show key differences ' \
        'in Google Search results.')
st.subheader('Average Domain Position')
def average_domain_pos(data):
    df1 = data.groupby('domain')['domain'].value_counts()
    df1 = df1.to_frame().sort_values(by='domain').rename(columns={'count': '# of appearances'})
    df2 = data.groupby('domain')['org-position'].mean()
    df2 = df2.to_frame().sort_values(by='domain').rename(columns={'count': '# of appearances', 'org-position': 'average org-position'})
    df3 = pd.merge(df1, df2, on='domain')
    df3 = df3.sort_values(by='# of appearances', ascending=False)
    return df3.reset_index()

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

st.subheader('Domain Frequency By Language')
col1 = eng_adp[['domain', '# of appearances']]
col2 = span_adp[['domain', '# of appearances']]
tempdf = pd.merge(col1, col2, on='domain', how='outer')
tempdf = tempdf.fillna(0)
tempdf = tempdf.rename(columns={'# of appearances_x': 'english appearances', '# of appearances_y': 'spanish appearances'})
tempdf['difference'] = tempdf['english appearances'] - tempdf['spanish appearances']
st.dataframe(tempdf.sort_values(by='difference').reset_index().drop('index', axis=1))

# what percentage of results were government for each query?
# test1 = eng_df[eng_df['location'] == 'Yuma County']
# gov_types = ['government', 'government affiliated']
# test11 = test1['gov_type'].isin(gov_types)
# um = test1[test11]
# test2 = span_df[span_df['location'] == 'Yuma County']

# st.dataframe(um)

def gov_perc(county):
      df = span_df[span_df['location'] == county]
      col1 = df.groupby('query')['query'].value_counts()
      st.write(col1.reset_index())
      col2 = df.groupby('query')['gov_type'].agg('sum')
      st.write(col2)
      df = pd.merge(col1, col2, on='query')
      st.write(df)
      df['gov_type'] = df['gov_type'].apply(lambda x: x.count('g') if type(x) != int else 0)
      df['percent'] = df['gov_type']/df['count']
      return df.reset_index()
test = gov_perc('Clark County')
st.write(test)