import cgi
import controller

form = cgi.FieldStorage()

id=form.getvalue("id")
grade=form.getvalue("grade")
subjects = controller.getSubjects(grade)

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
    <form action="showTest.py">
        <input type='hidden' value={grade} name="grade">
        <table>
            <tr>
                <td>Choose Subjects</td>
                <td>
                    <select name="sub">
                        <option>Choose Subject</option>""")
for i in subjects:
    print(f"<option value={i[0]}>{i[0]}</option>")
print("""                   </select>
                </td>
            </tr>
            <tr>
                <td></td>
                <td>
                    <input type="submit">
                </td>
            </tr>
        </table>
    </form>
</body>
</html>
""")