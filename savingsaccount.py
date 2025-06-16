import streamlit as st

from account import Account


balance = 100000
limit = 10000

class Savingsaccount(Account):
    def __init__(self,balance):
        Account.__init__(self,balance)

    def withdraw(self, amount, limit = 10000):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient Funds")
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount