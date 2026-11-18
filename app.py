import streamlit as st
from groq import Groq
st.set_page_config(page_title = "interview assistent",page_icon='🫶',layout = 'centered')
st.title("AI Inteview Assistant")
st.caption("Pactice and Prepare for your Placements here")
st.caption("Launched by Akshata Ganesh")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except(KeyError,FileNotFound):
                st.error("API KEY is missing.Add it in Advanced settings")
                st.stop()
role=st.selectbox('Job title',['Machine Learning Engineer','Senior Software Engineer','Data Analyst','prompt Engineer','Other'])
if role == 'Other':
  st.text_input('Enter your Job Title','XXXXXXXXX')
model = st.selectbox('Model',['openai/gpt-oss-120b','openai/gpt-oss-20b'])
level=st.selectbox('Difficult Level',['Beginner','intermediate','Advanced'])
mode = st.radio('Activity',['Generate Questions','Generate Code Questions','Evaluate Answers','Improve Answer'])
if mode == 'Generate Questions':
  count = st.slider("Number of Questions",1,10,5)
elif mode == 'Generate Code Questions':
  topic = st.selectbox('Topics',['SQL','AIML','Python','DAS','DBMS'])
  count = st.slider("Number of Questions",1,10,5)
else:
  question = st.text_area('Enter Interview Questions here')
  answer = st.text_area('Enter your answer',height=160)

  
                
