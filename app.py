import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def codebot(input_prompt,question):
    model=genai.GenerativeModel('gemini-pro')
    return model.generate_content([input_prompt,question]).text
st.set_page_config(page_title="CodeBOT",page_icon="🤖")
st.title("CODEBOT🤖")
select=st.selectbox("Programming Language:",['C','C++','Python','Java','JavaScript'])
question=st.text_input("Enter your Question:")
input_prompt="""
you are a pro coder with extensive knowledge in {select} programming Language and you know how to make hard coding question to simple ones by explaining them clearly with 
test cases and also explain the codes Time Complexity and space complexity
and also explain the code Clearly. Make sure that you provide the correct code before giving output.
"""
b=st.button("Generate With CodeBot🤖")
if b and select and question:
    result=codebot(input_prompt,question)
    st.write(result)

    