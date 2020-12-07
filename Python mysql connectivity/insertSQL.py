import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    username="root",
    password = "root1234",
    database = "COLLEGE"
)
cursor = connection.cursor()


s_id = int(input("Enter Student id : "))
s_name= input("Enter Student Name : ")
s_marks = int(input("Enter Student marks "))

query = "INSERT INTO COLLEGE_STUDENT VALUES(%s,%s,%s)"
value = (s_id,s_name,s_marks)
cursor.execute(query,value)
connection.commit()