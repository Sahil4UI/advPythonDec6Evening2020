# log -record
import logging,time,threading
logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)s) %(message)s ')

def job():
    logging.debug("Starting....")
    time.sleep(2)
    logging.debug("Exiting...")    
print("main->",threading.current_thread().getName())


for i in range(5):
    t= threading.Thread(target=job)
    t.start()