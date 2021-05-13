# Threading:
import os
import time
from threading import Thread, Lock
from queue import Queue # fifo

database_value = 0

def increase(lock):
    global database_value

    with lock:
        local_copy = database_value
        # processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy

if __name__ == '__main__':
    
    lock = Lock()
    print('Start value', database_value)

    # creating Threads
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    
    # start 
    thread1.start()
    thread2.start()

    # wait for threads to complete
    thread1.join()
    thread2.join()

    print('End value', database_value)
