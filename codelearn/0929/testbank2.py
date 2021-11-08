from bank2 import Account as acc

acct1=acc('羅小貴','00123-4560000',1000) #物件(acct1) = 類別(account)產生的
acct2=acc('羅小睿','00123-4560001',500)

acct1.deposit(100)
acct2.withdraw(400)
print(acct1)
print(acct2)