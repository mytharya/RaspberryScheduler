from random import randint

def unique_id(self):
    identificator_unic = randint(0,1000)
    return identificator_unic

class Client:
    def __init__(self, nume, prenume):
        self.first_name = nume
        self.last_name = prenume
        #self.baza_de_date = {}
    
    def adaugaClient(self, nume, prenume):
        self.baza_de_date[unique_id] = Client(nume, prenume)
    
    def listeazaClientii(self):
        for unique_id in self.baza_de_date:
            print(unique_id)
            print("ID: {}, Nume: {}, Prenume: {}".format(unique_id, self.first_name, self.last_name))

class Produs(Client):
    def __init__(self, produs, greutate, defect):
        self.product = produs
        self.weight = greutate
        self.defekt = defect

baza_de_date = {}

# main prog
client_nou = Client("Mike", "Kowalsky")
produs_nou = Produs("Handy", 350, "ecran spart")

# baza_de_date.listeazaClientii()
baza_de_date.adaugaClient(client_nou)
baza_de_date.listeazaClientii()