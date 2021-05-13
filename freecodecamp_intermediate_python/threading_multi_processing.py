# Multi Processing vs Multi Threading. 
""" 
Process: an instance pf a program(e.g a python interpreter)

+ takes advantage of multple CPUs and cores
+ Separate memory space -> memory is not shared between processes
+ Great for CPU-bound processing
+ New proces is stated independently from other processes
+ Process are interruptible/killable 
+ One GIL each process -> avoids GIL limitation

- Heavyweight
- Starting a process is lower than starting a thread.
- More memory
- IPC (inter-process communication) is more complicated 
"""

"""
Threads: An entity within a process that can be scheduled (also know as lghtweight process)
A process can spaw multiple thread

+ All thread within a process share the same memory
+ Lightweight
+ Starting a thread is lower than process
+ Great for I/O-bound tasks

- Thread is limited by GIL: Only one thread at a time 
- No effect for CPU-bound tasks
- Not interruptable/killable
- Careful with race conditions
"""

""" 
GIL: Global interpreter lock
- A lock that allows onle one thread at a time to execute in Python
- Needed in Cpython because memory management is not thread-safe

-Avoid:
    - se multiprocessing
    - Use a different, free-threaded Python implementation (Jython, IronPython)
    - Use Python as a wrapper for third-party libraries (C/C++) -> numpy, script


"""

# Multiprocessing
import os
from multiprocessing import Process
import time

def square_numbers():
    for i in range(100):
        sqrt = i * i
        # print(sqrt)
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()
print('num_processes', num_processes) # 8

# create processes
for i in range(num_processes):
    p = Process(target=square_numbers) # args=(,)
    processes.append(p)

# start
for p in processes:
    p.start()

# joins
for p in processes:
    p.join() # wait

print('end main')

# multi-threading
from threading import Thread

threads = []
num_threads = 10 # 10 diff thread

for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# start 
for t in threads:
    t.start()

# join 
for t in threads:
    t.join()

print('end main')