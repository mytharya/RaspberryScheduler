#10_70 bank

class Account:
    def __init__(self,name,balance,min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        #or
        #self.balance += amount

    def withdraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance = self.balance - amount
            #or
            #self.balance -= amount
        else:
            print(" Sorry, not enough funds! ")

    def statement(self):
        print("Accout Balance: {} Pounds".format(self.balance))

class Current(Account):

    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)

    def __str__(self):
        return"{}'s Current Account Balance: {} Pound(s) ".format(self.name, self.balance)

class Savings(Account):

    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance = 0)

    def __str__(self):
        return"{}'s Savings Account Balance: {} Pound(s) ".format(self.name, self.balance)

Z = Current ("Ziyad", 500)
T = Savings ("Tom",300)
print()
print(Z)
print(T)
print()
