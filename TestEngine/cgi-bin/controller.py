import model

def registerUser(role,name,id,pwd,grade):
    model.registerUser(role,name,id,pwd,grade)


def fetchStudentData(id):
    data = model.fetchStudentData(id)
    return data

def  loginUser(role,id,psw):
    user = model.loginUser(role,id,psw)
    return user

def insertTest(id,subject,grade):
    model.insertTest(id,subject,grade)

def getTest(id):
    test=model.getTest(id)
    return test

def insertQues(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans):
    model.insertQues(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans)

def getSubjects(grade):
    sub=model.getSubjects(grade)
    return sub

def getTestInfo(grade,sub):
    test_info = model.getTestInfo(grade,sub)
    return test_info
    
def getQuestions(t_id):
    ques = model.getQuestions(t_id)
    return ques