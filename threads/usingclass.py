from threading import *


class MyThread:

    def displayNumbers(self):
        i = 0
        while(i <= 10):
            print(i)
            i += 1


obj = MyThread()
thread = Thread(target=obj.displayNumbers)
thread.start()
