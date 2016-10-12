class Customer(object):

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def withdrawl(self, amount):
        if amount > self.balance:
            raise Exception('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

Chuck = Customer('Chuck LaPress',4000.00)
print(Chuck.balance)
print(Chuck.name)
Customer.withdrawl(Chuck,1900)
print(Chuck.balance)
Chuck.deposit(350)
print(Chuck.balance)
Chuck.withdrawl(100)
print(Chuck.balance)
