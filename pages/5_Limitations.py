import streamlit as st
import methods as m

st.title('Limitations')
st.header('reCAPTCHA')
st.write('''While running our program, Google's reCAPTCHA measures would stop our scraping, 
         leading to incomplete data. At the time, we could not fix the issue before the end
         of the presidential election, but CredLab has since developed a solution.''')
st.header('Translation')
st.write('''All members who worked on the project had proficiency in Spanish, but we acknowledge 
         that we are not professional translators nor fully knew what a Spansih-speaker would 
         realistacally search on Google. In the future, we would like to collect real Spanish 
         queries instead of relying on translations.''')
st.header('Chrome Settings')
st.write('''All of the lab computers where we ran the scripts had the language set to English 
         in Chrome, even if we were searching Spanish queries. In the future, we would like to take
         this into account and observe any differences in data results.''')