import cgi
import controller

form = cgi.FieldStorage()
role = form.getvalue('role')
id=form.getvalue('u_id')
psw = form.getvalue('u_pwd')

user = controller.loginUser(role,id,psw)
name = user[0][0]

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
    <h1>Login Successfull</h1>
    <h2>Welcome {name}</h2>""")
if role == "teacher":
    print(f"<a href='teachersLogin.py?id={id}'>Go to Teachers Page</a>")
else:
    print(f"<a href='studentsLogin.py?id={id}'>Go to Students Page</a>")

print("""   
</body>
</html>""")