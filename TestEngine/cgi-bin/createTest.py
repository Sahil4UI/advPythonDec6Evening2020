import cgi
import controller

form = cgi.FieldStorage()

id = form.getvalue('id')

if form.getvalue('test'):
    form_state = True
    subject = form.getvalue('sub')
    grade = form.getvalue('grade')
    controller.insertTest(id,subject,grade)
else:
    form_state=False


if form.getvalue("test_id"):
    test_id=form.getvalue("test_id")
    ques = form.getvalue("ques")
    opt_1 = form.getvalue("opt_1")
    opt_2 = form.getvalue("opt_2")
    opt_3 = form.getvalue("opt_3")
    opt_4 = form.getvalue("opt_4")
    ans = form.getvalue("ans")
    controller.insertQues(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans)

test = controller.getTest(id)
print("Content-type:text/html\r\n\r\n")

print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h1>Create Test</h1>
""")
if form_state==False:
    print(f"""
        <h2>Start Inserting Question</h2>
       <form action="createTest.py">
        <input type="hidden" value={id} name="id">
        <input type="hidden" value='create' name="test">

        <table>
            <tr>
                <td>
                    Choose Subjects
                </td>
                <td>
                    <select name="sub">
                        <option value="">Choose Subject</option>
                        <option value="Computer Science">Computer Science</option>
                        <option value="Maths">Maths</option>
                        <option value="General Knowledge">General Knowledge</option>
                        <option value="Science">Science</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td>Choose Grade</td>
                <td>
                    <select name="grade" id="">
                        <option>Select Grade</option>
                        <option value="1">1st</option>
                        <option value="2">2nd</option>
                        <option value="3">3rd</option>
                        <option value="4">4th</option>
                        <option value="5">5th</option>
                        <option value="6">6th</option>
                        <option value="7">7th</option>
                        <option value="8">8th</option>
                        <option value="9">9th</option>
                        <option value="10">10th</option>
                        <option value="11">11th</option>
                        <option value="12">12th</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td></td>
                <td><input type="submit" value="Submit"></td>
            </tr>
        </table>
    </form>
 """) 
print(f"""<form action="createTest.py">
        <input type="hidden" value={id} name="id">
            <table>
                <tr>
                    <td>Test ID</td>
                    <td>
                        <select name="test_id">""")
for i in range(len(test)):
    print(f"""
        <option value={test[i][0]}>{test[i][0]}</option>
    """)


print("""                        </select>
                    </td>
                </tr>
                <tr>
                <td>Enter Question</td>
                <td>
                    <textarea name="ques" id="" cols="30" rows="10"></textarea>
                </td>
            </tr>
            <tr>
                <td>Enter Option 1</td>
                <td>
                    <input type="text" name="opt_1" id="">
                </td>
            </tr>
            <tr>
                <td>Enter Option 2</td>
                <td>
                    <input type="text" name="opt_2" id="">
                </td>
            </tr>
            <tr>
                <td>Enter Option 3</td>
                <td>
                    <input type="text" name="opt_3" id="">
                </td>
            </tr>
            <tr>
                <td>Enter Option 4</td>
                <td>
                    <input type="text" name="opt_4" id="">
                </td>
            </tr>
            <tr>
                <td>Answer</td>
                <td>
                    <input type="text" name="ans" id="">
                </td>
            </tr>
            <tr>
                <td><input type="reset" value="Clear"></td>
                <td>
                    <input type="submit" value="Submit">
                </td>
            </tr>
        </table>
    </form>

 """)

print("""</body>
</html>
""")