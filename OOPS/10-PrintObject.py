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

    def __str__(self):
        return self.name

    def __del__(self):
        print("Object of {} destroyed".format(self.name))

cust_1 = Bank('Ram',45040544504,5000,1234)
cust_1.showDetails()

print(cust_1)