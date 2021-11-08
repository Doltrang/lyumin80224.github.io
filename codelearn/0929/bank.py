def account(name,number,balance):
    return {'name':name,'number':number,'balance':balance}

def deposit(acct,amount):
    acct['balance'] += amount

def withdraw(acct,amount):
    acct['balance'] -= amount

def desc(acct):
    return 'Account:'+str(acct)