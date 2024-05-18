from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import sqlite3

import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#conn=sqlite3.connect("student.db")
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows



## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]




## Streamlit App


st.set_page_config(page_title="I can Retrieve Any SQL query")


# Embed custom CSS to style the title
st.markdown(
    """
    <style>
    .title {
        color: purple;
        font-size: 2em;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use the custom class for the title
st.markdown('<h1 class="title">SQL GENIUS</h1>', unsafe_allow_html=True)
# Embed custom CSS to style the title
st.markdown(
    """
    <style>
    .header {
        color: orange;
        font-size: 2em;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use the custom class for the title
st.markdown('<h1 class="header">Gemini App To Retrieve SQL Data</h1>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stTextInput > div > div > input {
        border: 2px solid #4CAF50;
        padding: 10px;
        font-size: 16px;
        border-radius: 5px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stMarkdown h2 {
        color: #4CAF50;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)


question=st.text_input("Input",key="input")
submit=st.button("Ask question")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The response is")
    for row in response:
        print(row)
        st.header(row)

