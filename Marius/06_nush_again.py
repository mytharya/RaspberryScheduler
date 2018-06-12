# se da un magazin, trebuie mentinuta o lista de clienti in care fiecare are nume, prenume.
# baza_de_date = {0:{"a","b"},1:{"c","d"}}

def clearScreen():
    print("\n"*20)

class Client:
    def __init__(self, nume, prenume):
        self.first_name = prenume
        self.last_name = nume
        self.objects = []

    def adaugaObiect(self, obiect):
        self.objects.append(obiect)
    
    def printInfo(self):
        print("{}, {}, {}.".format(self.first_name, self.last_name, self.objects))

class Magazin:
    def __init__(self, nume):
        self.name = nume
        self.lista_clienti = []

    def adaugaClient(self, nume, prenume):
        # ambele procedee sunt corecte
        # client_nou = Client(nume, prenume)
        # self.lista_clienti.append(client_nou)
        # vs
        self.lista_clienti.append(Client(nume, prenume))

    def printListaClienti(self):
        for client in self.lista_clienti:
            if isinstance(client, Client):
                Client.printInfo(client)
    
    def alegeClient(self, nume, prenume):
        for client in self.lista_clienti:
            if isinstance(client, Client):
                if nume == client.last_name and prenume == client.first_name:
                    return client

class Perie:
    def __init__(self, lungime):
        self.lenght = lungime

# main prog
clearScreen()

shop = Magazin("ButiQ")
# shop.adaugaClient("e","f")
Magazin("ButiQ").adaugaClient("e","f")
# shop.adaugaClient("a","b")
# shop.adaugaClient("c","d")
shop.lista_clienti.append(Perie("7 cm"))
client_ales = shop.alegeClient("e","f")
print(client_ales)
piaptan = Perie
client_ales.adaugaObiect(piaptan)
# Magazin("ButiQ").alegeClient("e","f").adaugaObiect(piaptan)
shop.printListaClienti()
