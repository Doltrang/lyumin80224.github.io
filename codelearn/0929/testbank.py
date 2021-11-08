import bank
acct = bank.account('羅小貴','00123-4560000',1000)
bank.deposit(acct,100)
print(bank.desc(acct))
bank.withdraw(acct,500)
print(bank.desc(acct))