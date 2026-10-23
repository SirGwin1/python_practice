account = {
    'name':'John Mark',
    'account_number':1234567890,
    'balance': 5000
}

def deposit(account, amount):
    if amount <= 0:
        raise ValueError(oops! you cant deposit a negative amount)
    account['balance'] += amount

def withdrawal(account, amount):
    if amount <= 0:
        raise ValueError('withdrawal amount must be positive')

    if amount > balance:
        raise ValueError(insufficient funds)
        
    account['balance'] -= amount
    
    


