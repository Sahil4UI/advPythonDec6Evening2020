import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    username="root",
    password = "root1234",
    database = "COLLEGE"
)
cursor = connection.cursor()
# cursor.execute("USE COLLEGE")
query = "CREATE TABLE COLLEGE_STUDENT(S_ID INT PRIMARY KEY,S_NAME VARCHAR(20),S_MARKS INT)"
cursor.execute(query)

