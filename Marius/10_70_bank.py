#10_70 bank

#Global classes
class Account:
    #Class constructor(functia care se apeleaza cand se instantiaza clasa)
    def __init__(self,name,balance,min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    #Class Function (seen within class and childs)
    def deposit(self,amount):
        self.balance = self.balance + amount
        #or
        #self.balance += amount
        print("\n Ammount has been succefully deposited. ")

    def withdraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance = self.balance - amount
            #or
            #self.balance -= amount
            print("\n Ammount has been succefully subtracted!. ")
        else:
            print("\n Sorry, not enough funds! ")

    def statement(self):
        print("\n Accout Balance: {} Pounds. ".format(self.balance))

    def printInfo(self):
        print("\n Account name: {} and has balance of {} Pound(s). ".format(self.name, self.balance))

    def select(self):
        print("\n You have selected {}s Account. ".format(self.name))

#Child class with its own constructor
class Current(Account):

    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)

    #Print function override (print(Current) normally returns pointer addres, this overwrites that function)
    def __str__(self):
        return"{}'s Current Account Balance: {} Pound(s). ".format(self.name, self.balance)

#Child class with its own constructor
class Savings(Account):

    #Class constructor(functia care se apeleaza cand se instantiaza clasa)
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance = 0)
        print("\n Instancing class Savings: {} {}".format(name, balance))

    def __str__(self):
        return"{}'s Savings Account Balance: {} Pound(s) ".format(self.name, self.balance)

'''
#Exemplu instantiere de clase cu constructor calls
print("c1")
Z = Savings ("abc", 100)
print("c2")
X = Savings ("bcd", 200)
print("c3")
'''

#Global functions
def printAllAccounts():
    for person in known_accounts:
        print(person)

def printAccountInfoByName(name):
    for person in known_accounts:
        if person.name == name:
            person.printInfo()
            break
def getAccountByName(name):
    for person in known_accounts:
        if person.name == name:
            return person
    return None

#Global variables
known_accounts = [Savings("Alfa", 300),Current("Gama", 500)]

print("\n"*20)

while True:
    selection = input("\n 1. Open new account\n 2. Manage existing account\n 3. Delete existing account\n 4. EXIT \n\n Your selection?: ")
    try:
        selection = int(selection)
    except ValueError:
        print("\n That's not an int! ")
        continue
    if selection == 1:      #1. Open new account
        accountFound = False
        new_account_name = str(input("\n Select account name you wish to operate: ")).strip().capitalize()
        for person in known_accounts:
            if person.name == new_account_name:
                accountFound = True
                break
        if accountFound == True:
            print("\n Account exists. ")
        else:
            print("\n Account does not exist! ")
            while True:
                new_account_q = str(input("\n Open new account? ")).strip().capitalize()
                if new_account_q == "Y":
                    while True:
                        new_account_type = int(input("\n 1 for Current\n 2 for Savings\n 3 for Exit: "))
                        if new_account_type == 1:       #1 for Current
                            new_account_sum = int(input("\n Add a sum you wish to deposit: "))
                            new_account = Current (new_account_name, new_account_sum)
                            known_accounts.append(new_account)

                           # known_accounts.append(Current (new_account_name, int(input("\n Sum?:")) ))

                            break
                        
                        elif new_account_type == 2:     #2 for Savings
                            new_account_sum = int(input("\n Add a sum you wish to deposit: "))
                            new_account = Savings (new_account_name, new_account_sum)
                            known_accounts.append(new_account)
                            break
                        
                        elif new_account_type == 3:     #3 for EXIT
                            break
                    break
                elif new_account_q == "N":
                    print("\n Exit din new account ")
                    break
    elif selection == 2:    #2. Manage existing account
        while True:
            #print all acounts
            print("\n")
            printAllAccounts()

            #ask new account name
            print("\n")
            account_name = str(input("\n Input account name: ")).strip().capitalize()
            accountFound = False
            #break when person is found within known accounts
            for person in known_accounts:
                if person.name == account_name:
                    accountFound = True
                    break

            #if account isnt found
            if accountFound == False:
                print("\n Only existing accounts please! ")
            
            #if account is found do the rest
            else:
                
                #menu
                while True:
                    
                    #prints account info
                    print("\n")
                    printAccountInfoByName(account_name)

                    #selection menu
                    selection = input("\n 1. Deposit \n 2. Withdraw \n 3. EXIT \n Your selection is: ")

                    #re-try until input is int and save it as int
                    #try/exept block for exceptions
                    try:
                        selection = int(selection)
                    except:
                        print("\n Incorect value ")
                        continue
                    
                    if selection == 1:      #1. Deposit
                        #asks for ammount
                        ammount = input("\n Ammount you wish to deposit: ")
                        try:
                            ammount = int(ammount)
                        except:
                            print("\n Invalid ammount ")
                            continue                        
                        person = getAccountByName(account_name)
                        person.deposit(ammount)

                    if selection == 2:      #2. Withdraw
                        ammount = input("\n Ammount you wish to withdraw: ")
                        try:
                            ammount = int(ammount)
                        except:
                            print("\n Invalid ammount ")
                            continue
                        person = getAccountByName(account_name)
                        person.withdraw(ammount)

                    if selection == 3:      #3. EXIT
                        break
                break
    elif selection == 3:    #3. Delete Account
        print("\n")
        printAllAccounts()
        if len(known_accounts) >= 1:
            account_name = input("\n Select a account name from list: ").strip().capitalize()
            accountFound = False
            for person in known_accounts:
                if person.name == account_name:
                    accountFound = True
                    break

            if accountFound == True:
                person = getAccountByName(account_name) #variabila globala sau locala?
                known_accounts.remove(person)
                print("\n {}s account has been deleted! ".format(account_name))
                del person
                del account_name
            else:
                print("\n Only accounts within the list! ")
                continue
        else:
            print("Account list is empty! ")

    elif selection == 4:    #4. EXIT
        print("==3")
        break