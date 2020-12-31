import cgi 
import controller

form = cgi.FieldStorage()

id= form.getvalue("id")


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
    <h1>Teachers's Dashboard</h1>
    <nav>
        <ul>
            <li>
                <a href='createTest.py?id={id}'>Create Test</a>
            </li>

            <li>
                <a href='viewTest.py?id={id}'>View Test</a>
            </li>
        </ul>
    </nav>
</body>
</html>
""")