# log -record
import logging,time,threading
logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)s) %(message)s ')

def delayed():
    logging.debug("Running....")
    
t1 = threading.Timer(3,delayed)
t1.setName("Thread-1")

t2 = threading.Timer(5,delayed)
t2.setName("Thread-2")

logging.debug("Starting Timer Thread...")
t1.start()
t2.start()

logging.debug("DOne")