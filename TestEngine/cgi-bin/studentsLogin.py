import cgi 
import controller

form = cgi.FieldStorage()

id= form.getvalue("id")

my_data = controller.fetchStudentData(id)

print("Content-type:text/html\r\n\r\n")
print(f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h1>Student's Dashboard</h1>
    <h4>Name : {my_data[0][0]}</h4>
    <h4>Grade : {my_data[0][3]}</h4>
    <ul>
        <li>
            <a href="giveTest.py?id={my_data[0][1]}&grade={my_data[0][3]}">GIVE TEST</a>
        </li>
    </ul>
</body>
</html>
""")