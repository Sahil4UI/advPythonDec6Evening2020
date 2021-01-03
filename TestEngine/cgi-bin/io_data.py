import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="myTestEngine"
)

cursor = connection.cursor()

def storeUser(obj):
    if obj.role=='teacher':
        table="teacher"
    else:
        table = "student"
    query=f"insert into {table} values (%s,%s,%s,%s)"
    cursor.execute(query,(obj.name,obj.id,obj.pwd,obj.grade))
    connection.commit()


def loginUser(role,id,pwd):
    if role=='teacher':
        table="teacher"
    else:
        table = "student"
    query=f"select * from  {table} where id=%s and psw=%s"
    cursor.execute(query,(id,pwd))
    data=cursor.fetchall()
    return data


def fetchStudentData(id):
    query=f"select * from student where id={id}"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def insertTest(id,subject,grade):
    query = "insert into test values (%s,%s,%s)"
    values = (id,subject,grade)
    cursor.execute(query,values)
    connection.commit()

def getTest(id):
    query=f"select * from test where teacher_id={id}"
    cursor.execute(query)
    test=cursor.fetchall()
    return test

def insertQues(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans):
    query = "insert into questions values(%s,%s,%s,%s,%s,%s,%s)";
    values=(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans)
    cursor.execute(query,values)
    connection.commit()


def getSubjects(grade):
    query= f"select subject from test where grade = {grade}"
    cursor.execute(query)
    sub  =cursor.fetchall()
    return sub

def getTestInfo(grade,sub):
    query = "select * from test where grade=%s and subject=%s"
    value=(grade,sub)
    cursor.execute(query,value)
    test_info = cursor.fetchall()
    return test_info