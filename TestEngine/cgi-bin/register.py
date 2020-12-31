import cgi,controller

form = cgi.FieldStorage()
role=form.getvalue('role')
name = form.getvalue('u_name')
id = form.getvalue('u_id')
pwd = form.getvalue('u_pwd')
grade = form.getvalue('grade')

controller.registerUser(role,name,id,pwd,grade)

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
    <h1>Registration Successfull</h1>
    <h2>Welcome {name}</h2>""")
if role =="teacher":
    print(f"<a href='teachersLogin.py?id={id}'>Go to Teachers Page</a>")
else:
    print(f"<a href='studentsLogin.py?id={id}'>Go to Students Page</a>")
("""
</body>
</html>
""")