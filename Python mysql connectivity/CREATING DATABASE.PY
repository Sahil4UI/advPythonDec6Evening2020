import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    username="root",
    password = "root1234"
)
cursor = connection.cursor()

#cursor.execute("CREATE DATABASE COLLEGE")
cursor.execute("SHOW DATABASES")
for database in cursor:
    print(database)