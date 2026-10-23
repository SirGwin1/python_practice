##Procedural_Programing
#Working with Dictionaries

account = {
    'name':'John Mark',
    'account_number':1234567890,
    'balance': 5000
}

def deposit(account, amount):
    if amount <= 0:
        raise ValueError('oops! you cant deposit a negative amount')
    account['balance'] += amount

def withdrawal(account, amount):
    if amount <= 0:
        raise ValueError('withdrawal amount must be positive')

    if amount > balance:
        raise ValueError('insufficient funds')
        
    account['balance'] -= amount

##Object_Oriented_Programing
#Working with Classes

class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('oops! you cant deposit this amount please check the amount and try again')
        self.balance += amount

    def withdrawal(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient Funds')
        if amount <= 0:
            raise ValueError('oops you cant deposit this amount please check the amount and try again')
        self.balance -= amount
    


