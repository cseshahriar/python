""" Data Encapsulation in Python """

class Computer:

    def __init__(self):
        self.__maxprice = 900 # private attributes

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell() # 900 not change cause it's private, it's call  encapsulation

# using setter function
c.setMaxPrice(1000) # public method inside access private so it's work
c.sell()