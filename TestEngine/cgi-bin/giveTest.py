import cgi
import model

form = cgi.FieldStorage()

id=form.getvalue("id")
grade=form.getvalue("grade")
subjects = controller.getSubjects(grade)