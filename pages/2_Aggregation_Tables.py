import streamlit as st
import methods as m

eng_df = m.load_data('engLocAccuracy1.csv')
span_df = m.load_data('spanLocAccuracy1.csv')
eng_adp = m.average_domain_pos(eng_df)
span_adp = m.average_domain_pos(span_df)
dom_freq = m.domain_freq(eng_adp, span_adp)
test = m.gov_perc(span_df, 'Clark County')

st.title('Aggregation Tables')
st.write('To make the data meaningful, here are a few aggregated tables that show key differences ' \
        'in Google Search results.')
st.subheader('Average Domain Position')

st.write('Each organic result has a position on the page, with a position of 1 meaning it is the ' \
        'very first result. In this table, the domains are sorted in descending order by number of appearances, ' \
        'with each domain having its average organic position')
lang_adp = st.selectbox("Choose Average Domain Position Dataset", ["English", "Spanish"])
if lang_adp == "English":
       st.dataframe(eng_adp.style.set_properties(color='#636363'))
elif lang_adp == "Spanish":
       st.dataframe(span_adp.style.set_properties(color='#636363'))

st.subheader('Domain Frequency By Language')
st.dataframe(dom_freq)

st.write(test)