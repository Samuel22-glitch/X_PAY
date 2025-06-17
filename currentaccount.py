from account import Account

class currentAccount(Account):
    def __init__(self, balance,):
        Account.__init__(self, balance)

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient Funds")
        self.balance -= amount

    def deposit(self, amount):

       if amount >= 0:
           self.balance += amount
