import cgi,controller
form = cgi.FieldStorage()
t_id = form.getvalue('t_id')
ques = controller.getQuestions(t_id)

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
    <form action="submitTest.py">""")
for i in range(len(ques)):
    print(f"""<h4>{ques[i][1]}</h4>
              """)
    for j in range(2,6):
        print(f""" <ul>
        <li>
                            <input type="radio" name="ques_{i+1}">
                            <label>{ques[i][j]}</label>
                    </li>
                    </ul>    
    """)
print("""
</form>
</body>
</html>""")