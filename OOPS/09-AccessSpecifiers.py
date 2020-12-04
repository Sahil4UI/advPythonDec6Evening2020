class Bank:
    """This is my bank class"""
    branch = "Rohini"
    ifsc = 4232200
    # Parametrized Constructor
    def __init__(self, name, acc_no, bal, pin):
        print("Constructor called...")
        self.name = name    # public
        self._acc_no = acc_no  # protected
        self._bal = bal   # protected
        self.__pin = pin    # private
        self.details = []

    def showDetails(self):
        print("Details")
        self.details.append([self._acc_no, self._bal, self.__pin, self.branch, self.ifsc])
        print(self.details)

    def __del__(self):
        print("Object of {} destroyed".format(self.name))

cust_1 = Bank('Ram',45040544504,5000,1234)
cust_1.showDetails()

# cust_1.__pin = 9999
# print("Pin changed successfully...",cust_1.showDetails())