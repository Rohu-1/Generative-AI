# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st
# import os 
# import sqlite3

# import google.generativeai as genai


# genai.configure(api_key=os.getenv("AIzaSyDcTSDS66eSGzr4tXQfnP8T7uxOWB8f5SU"))
# conn=sqlite3.connect("student.db")
# def get_gemini_response(question,prompt):
#     model=genai.GenerativeModel('gemini-pro')
#     response=model.generate_content([prompt[0],question])
#     return response.text

# def read_sql_query(sql,db):
#     conn-sqlite3.connect(db)
#     cur=conn.cursor()
#     cur.execute(sql)
#     rows=cur.fetchall()
#     conn.commit()
#     conn.close()
#     for row in rows:
#         print(row)
#     return rows



# ## Define Your Prompt
# prompt=[
#     """
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
#     SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
#     the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
#     \nExample 2 - Tell me all the students studying in Data Science class?, 
#     the SQL command will be something like this SELECT * FROM STUDENT 
#     where CLASS="Data Science"; 
#     also the sql code should not have ``` in beginning or end and sql word in output

#     """


# ]




# ## Streamlit App


# st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("Gemini App To Retrieve SQL Data")

# question=st.text_input("Input",key="input")
# submit=st.button("Ask question")

# if submit:
#     response=get_gemini_response(question,prompt)
#     print(response)
#     response=read_sql_query(response,"student.db")
#     st.subheader("The response is")
#     for row in response:
#         print(row)
#         st.header(row)




import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()


table_info ="""
Create table STUDENT(NAME VARCHAR(25),CLass varchar(25),section varchar(25),Marks INT)
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')


print("The inserted records are")

data=cursor.execute('''select * from student''')

for row in data:
    print(row)

connection.commit()
connection.close()