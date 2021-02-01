import threading
import time
def job():
    print(f"job_started by {threading.current_thread().getName()}")
    time.sleep(2)
    for i in range(1000):
        for j in range(1000):
            k = i+j
    print(f"Job Ended by {threading.current_thread().getName()}.....")
    
print("main->",threading.current_thread().getName())


for i in range(5):
    t= threading.Thread(target=job,name=f'Thread_{i}')
    t.start()