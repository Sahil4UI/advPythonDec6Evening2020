import io_data

class User:
    def __init__(self,role,name,id,pwd,grade):
        self.name=name
        self.role=role
        self.id=id
        self.pwd=pwd
        self.grade=grade
    
def registerUser(role,name,id,pwd,grade):
    obj = User(role,name,id,pwd,grade)
    io_data.storeUser(obj)


def fetchStudentData(id):
    data = io_data.fetchStudentData(id)
    return data

def loginUser(role,id,psw):
    user = io_data.loginUser(role,id,psw)
    return user

def insertTest(id,subject,grade):
    io_data.insertTest(id,subject,grade)

def getTest(id):
    test=io_data.getTest(id)
    return test

def insertQues(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans):
    io_data.insertQues(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans)
    
