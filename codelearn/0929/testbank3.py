from bank2 import Account
acct=Account('王中明','00123-4560002',500)
acct.balance = 5 
# acct._Account__balance=5
acct.x = 100
acct.y = 200
acct.z = 300
print(acct)
print(acct.balance)
print(acct.x,acct.y,acct.z) #黏
print(dir(acct))