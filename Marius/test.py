#test cu mita

class Account:
    def __init__(self,namex,balancex,min_balancex):
        self.name = namex
        self.balance = balancex
        self.min_balance = min_balancex

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

    def printName(self):
        print("Account name: {}".format(self.name))
        
#A = Account ("Ana", 500, 0)
#B = Account ("baba", 1000, -100)
#A.statement()
account_list = [Account("Gama", 0, -1)]
#for account in account_list:
#    account.printName()

while True:
    print()
    account_name = input("Select account you wish to operate : ").strip().capitalize()

    cond = True
    for cont in account_list:
        if cont.name == account_name:
            cond = False
            print("The account {} exists.".format(account_name))
            break

    if cond == True:
        new_account = Account(account_name, 0 , 0)
        print(len(account_list))
        account_list.append(new_account)
        print(len(account_list))
        for cont in account_list:
            cont.printName()
