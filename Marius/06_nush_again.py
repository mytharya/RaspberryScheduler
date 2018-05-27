baza_de_date = {0:{"a","b"},1:{"c","d"}}

def clearScreen():
    print("\n"*20)

class Client:
    def __init__(self, nume, prenume):
        self.first_name = nume
        self.last_name = prenume
    
    def adaugaClient(nume, prenume):
        lk = Client.lastKey()
        print(lk)
        baza_de_date[lk] = {nume, prenume}
    
    def lastKey():
        lastKey = len(baza_de_date.keys())
        return lastKey
        
    
    def printListaClienti():
        for key in baza_de_date.keys:
            print("{},{},{}".format(key, self.first_name, self.last_name))

# main prog
clearScreen()

Client.adaugaClient("e","f")