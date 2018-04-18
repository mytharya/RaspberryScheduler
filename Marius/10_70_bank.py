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
known_accounts = {
    "Ziyad":("Current", 500),
    "Tom":("Savings",300),
    }
"""
print()
print(Z)
print(T)
print()
"""

while True:
    print()
    account_name = input("Select account you wish to operate : ").strip()
    if account_name not in known_accounts:
        new_account_q = input("Open new account? ").strip().capitalize()
        if new_account_q == "Y":
            print()
            print("1 for Current account")
            print("2 for Savings account")
            print()
            while True:
                account_type = int(input("Choose your account type : ").strip())
                if account_type == 1:
                    known_accounts[account_name] = ['Current', 0]
                    account_name[0] = ('Savings', 0)
                    break                    
                elif account_type == 2:
                    known_accounts[account_name] = ['Savings', 0]
                    account_name[0] = account_name,('Savings', 0)
                    break
                else:
                    print("Thats not a proper choice! Try again!")
        elif new_account_q == "N":
            continue
        else:
            print("Thats not a proper choice! Try again!")
            continue
    else:
        while True:
        #get menu options
        #print("\n"*50)
            print()
            print("1 for Current Statement")
            print("2 for Deposit")
            print("3 for Withdraw")
            print("4 to EXIT")
            print("any other choice returns you to account selection")
            print()
            

            menu_option = int(input("Please choose option : ").strip())
            
            if menu_option == 2:
                print()
                deposit_amount = int(input("Enter the ammount you wish to deposit : ").strip())
                print(known_accounts)
                print(account_name)
                print(deposit_amount)
                print(account_name)
                known_accounts[account_name].deposit(deposit_amount)
                #'account_name'.deposit(deposit_amount)
            elif menu_option == 3:
                print()
                withdraw_ammount = int(input("Enter the ammount you wish to withdraw : ").strip())
                new_account.withdraw(withdraw_ammount)
                print()
            elif menu_option == 1:
                print()
                #account_name.statement()
                print(known_accounts[account_name])
                #print()
                #print(known_accounts)
                print()
            elif menu_option == 4:
                print("doesent work for the moment ")
            else:
                break
