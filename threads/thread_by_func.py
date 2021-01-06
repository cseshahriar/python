""" creating thread by function """
from threading import *


def displayNumbers():
    i = 0
    print(current_thread().getName())
    while(i <= 10):
        print(i)
        i += 1


print(current_thread().getName())
# creating thread
mythread = Thread(target=displayNumbers)
mythread.start()
