import weakref

class Bank:
    """This is my bank class"""
    branch = "Rohini"
    ifsc = 4232200
    # Parametrized Constructor
    def __init__(self, name, acc_no, bal, pin):
        print("Constructor called...")
        self.name = name
        self.acc_no = acc_no
        self.bal = bal
        self.pin = pin
        self.details = []

    def showDetails(self):
        print("Details")
        self.details.append([self.acc_no, self.bal, self.pin, self.branch, self.ifsc])
        print(self.details)

    def __del__(self):
        print("Object of {} destroyed".format(self.name))

def callback(ref):
    print("Callback Reference :",ref)


cust_1 = Bank('Ram',45040544504,5000,1234)
# making a copy of object 1
obj_copy = cust_1

ref = weakref.ref(cust_1,callback)

print("Object :",cust_1)
print("Ref :",ref)
print("Calling ref :",ref())

print("Deleting Reference now...")
del cust_1
del obj_copy
print("Calling ref :",ref())

