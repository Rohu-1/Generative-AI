


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
print(data)
for row in data:
    print(row)

connection.commit()
connection.close()