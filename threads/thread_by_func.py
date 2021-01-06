""" creating thread by function """
from threading import Thread


def displayNumbers():
    i = 0
    while(i <= 100):
        print(i)
        i += 1


# creating thread
mythread = Thread(target=displayNumbers)
mythread.start()
