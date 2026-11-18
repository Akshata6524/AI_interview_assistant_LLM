import streamlit as st
from groq import Groq
st.set_page_config(page_title = "interview assistent",page_icon='🫶',layout = 'centered')
st.title("AI Inteview Assistant")
st.caption("Pactice and Prepare for your Placements here")

try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except(KeyError,FileNotFound):
                st.error("API KEY is missing.Add it in Advanced settings")
                st.stop()
role=st.selectbox('Job title',['Machine Learning Engineer','Senior Software Engineer','Data Analyst','prompt Engineer','Other'])
if role == 'Other';
st.text_input('Enter your Job Title','XXXXXXXXX')
                
