import pandas as pd
import plotly.express as px
import streamlit as st
import methods as m

st.title('Domaina and URL Analysis')
st.header('Domain Types')
with st.expander('Learn More'):
    st.write('''With the help of AI labeling, we classfied each domain in the dataset. Across both
             languages, there was a large prevalence of government, news, and nonprofit domains. 
             However, the data shows that there were more social media and international appearances
             in Spanish.''')

st.image("eng_domain_type.png")
st.image("span_domain_type.png")

eng_df = m.load_data('engLocAccuracy1.csv')
span_df = m.load_data('spanLocAccuracy1.csv')

st.header('Social Media')
with st.expander('Learn More'):
    st.write('''Since there were significantly more social media results in the Spanish dataset, 
             we wanted to look further into which social media sites are appearing and which queries
             are producing these results.''')
soc = m.soc_fig(eng_df, span_df)
st.plotly_chart(soc)
