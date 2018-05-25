from random import randint

baza_de_date = {}

def unique_id():
    identificator_unic = randint(0,1000)
    return identificator_unic

class Client:
    def __init__(self, nume, prenume):
        self.first_name = nume
        self.last_name = prenume
    
    def adaugaClient(self, nume, prenume):
        baza_de_date[unique_id()] = {}
    
    def listeazaClientii(self):
        for any_key in baza_de_date:
            print("ID: {}, Nume: {}, Prenume: {}".format(any_key, self.first_name, self.last_name))

class Produs(Client):
    def __init__(self, produs, greutate, defect):
        self.product = produs
        self.weight = greutate
        self.defekt = defect

# main prog
client_nou = Client("Mike", "Kowalsky")
produs_nou = Produs("Handy", 350, "ecran spart")

# baza_de_date.listeazaClientii()
# baza_de_date.adaugaClient()
baza_de_date.adaugaClient("a","b")
client_nou.listeazaClientii()
print(baza_de_date)