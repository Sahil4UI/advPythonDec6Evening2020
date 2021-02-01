import threading

def job_1():
    print("job_1 started")
    for i in range(10000):
        for j in range(10000):
            k = i+j
    print("Job_1 Done.....")


def job_2():
    print("job_2 started")
    print("Job_2 Done.....")

def job_3():
    print("job_3 started")
    for i in range(10):
        for j in range(5):
            k = i+j
    print("Job_3 Done.....")

task1 = threading.Thread(target = job_1)
task2 = threading.Thread(target = job_2)
task3 = threading.Thread(target = job_3)

task1.start()
task2.start()
task3.start()
