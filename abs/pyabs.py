# abstract base class
from abc import ABC, abstractmethod


class Payment(ABC):
    """ Abstract Class """

    def print_slip(self, amount):
        print('Purchase of amount- ', amount)

    @abstractmethod
    def payment(self, amount):
        pass


class CreditCardPayment(Payment):

    def payment(self, amount): # override
        print('Credit card payment of- ', amount)


class MobileWalletPayment(Payment):

    def payment(self, amount): # override
        print('Mobile wallet payment of- ', amount)


obj = CreditCardPayment()
obj.payment(100)
obj.print_slip(100)

print(isinstance(obj, Payment))
obj = MobileWalletPayment()
obj.payment(200)
obj.print_slip(200)
print(isinstance(obj, Payment))
