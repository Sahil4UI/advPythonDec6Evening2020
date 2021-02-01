# log -record
import logging,time,threading
logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)s) %(message)s ')

class MyThread(threading.Thread):
    def run(self):
        logging.debug("running....")

for i in range(5):
    obj=MyThread()
    obj.start()