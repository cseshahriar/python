# Threading:
import os
import time
from threading import Thread, Lock, current_thread
from queue import Queue # fifo


def worker(q, lock):
    while True:
        val = q.get()
        with lock:
            print(f'in {current_thread().name} got {val}')
        q.task_done()

if __name__ == '__main__':
    
    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        thread.daemon = True # daemon for while stop 
        thread.start()

    for i in range(1, 20):
        q.put(i)
    
    q.join()

    print('end main')
