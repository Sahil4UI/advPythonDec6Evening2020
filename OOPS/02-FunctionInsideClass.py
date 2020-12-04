class Bank:
    """This is my bank class"""
    acc_no = None
    bal = 0
    pin = None
    branch = "Rohini"
    ifsc = 4232200

    def showDetails(self):
        # self = this (refers to the current object)
        print("Details")
        print("Acc No : ",self.acc_no)
        print("Balance : ",self.bal)

cust_1 = Bank()
cust_1.acc_no = 45454545789
cust_1.bal += 5000
cust_1.pin = 1234
cust_1.showDetails()

cust_2 = Bank()
cust_2.acc_no = 45454545121
cust_2.bal += 8000
cust_2.pin = 1134
cust_2.showDetails()