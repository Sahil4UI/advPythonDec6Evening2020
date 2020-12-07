import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    username="root",
    password = "root1234",
    database = "COLLEGE"
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM COLLEGE_STUDENT")
# data = cursor.fetchall()
# for i in data:
#     print(i)

data = cursor.fetchone()
print(data)
