import sys
sys.path.append('..')

from model import model

def createAcc(name,email):
    user = model.createAccount(name,email)
    return user

def balEnquiry():
    pass

def amtWithdraw():
    pass