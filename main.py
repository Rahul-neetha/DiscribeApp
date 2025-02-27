
import os
from langchain.llms import OpenAI
import streamlit as st


openai_key = st.secrets["OPENAI_API_KEY"] 
# initialize st framework
os.environ["OPENAI_API_KEY"]=openai_key

st.title('Celebrity App')
input_text=st.text_input("search the celebrity u want")

llm=OpenAI(temperature=0.6)

if input_text:
    st.write(llm(input_text))


