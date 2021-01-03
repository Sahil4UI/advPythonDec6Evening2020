import controller,cgi

form = cgi.FieldStorage()

grade = form.getvalue("grade")
sub=form.getvalue('sub')
test = controller.getTestInfo(grade,sub)

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



    <h1>Start Test</h1>
    <hr>
    """)

if len(test)==0:
    print("<h2>No Test Available</h2>")
else:
    print("""
            <h2>Test Available</h2>
            <table width=100% border="2px"  cellpadding="12px">
                <tr>
                    <th>Test ID</th>
                    <th>Subject</th>
                    <th>Grade</th>
                    <th>Start Test</th>
                </tr>""")

    for i in range(len(test)):
        print(f"""
                <tr>
                    <td>{test[i][0]}</td>
                    <td>{test[i][1]}</td>
                    <td>{test[i][2]}</td>
                    <td><a href="startTest.py?t_id={test[i][0]}">Start Test</a></td>

                </tr>
        """ )

print("""    </table>
        """)

print("""</body>
</html>""")