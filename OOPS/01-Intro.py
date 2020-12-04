class Bank:
    """This is my bank class"""
    acc_no = None
    bal = 0
    pin = None
    branch = "Rohini"
    ifsc = 4232200

cust_1 = Bank()
cust_1.acc_no = 45454545789
cust_1.bal += 5000
cust_1.pin = 1234

print(cust_1.__dict__)