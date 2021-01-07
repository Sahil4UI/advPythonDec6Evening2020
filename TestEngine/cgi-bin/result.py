import cgi
form=cgi.FieldStorage()
t_id=form.getvalue('t_d')
num_ques=form.getvalue('num_ques')
attempt =0
for i in range(int(num_ques)):
    if form.getvalue(f"ques_{i+1}"):
        attempt+=1


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
    <h1>Result</h1>
    <h4>No of Question : {num_ques}</h4>
    <h4>Question Attempted : {attempt}</h4>
    <h4>Question Unattempted : {int(num_ques)-attempt}</h4>


</body>
</html>
""")
