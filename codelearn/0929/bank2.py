class Account:
    #self:這個物件的
    #__init__ 建構子Constructor
    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.__balance=balance
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        self.__balance -= amount
    def __str__(self):
        return 'Account<{},{},{}>'.format(self.name,self.number,self.__balance)