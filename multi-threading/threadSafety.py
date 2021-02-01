import threading
import time

class ThreadSafety():
    def __init__(self,bal):
        self.bal = bal
    
    def Balance(self,amount):
        lock.acquire()
        try:
            print(f"hello , {threading.current_thread().getName()}")
            time.sleep(2)
            if self.bal >amount :
                self.bal=self.bal-amount
                print(f"{threading.current_thread().getName()}, Your Remaining Balance:{self.bal}")
            else:
                print(f" Canot withdraw for {threading.current_thread().getName()}")
        except Exception as ex:
            print(ex)
            
        print(f"{threading.current_thread().getName()}, Your Balance after transaction:{self.bal}")
        lock.release()
        print(f"Lock released by {threading.current_thread().getName()}")
    
obj=ThreadSafety(10000)
obj1=ThreadSafety(10000)

lock = threading.Lock()
t1 = threading.Thread(target=obj.Balance ,args=(2000,),name="Ram")
t2 = threading.Thread(target=obj1.Balance ,args=(5000,),name="Shyam")
t1.start()
t2.start()
        
                
                