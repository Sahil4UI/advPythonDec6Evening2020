import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    username="root",
    password = "root1234"
)
cursor = connection.cursor()
