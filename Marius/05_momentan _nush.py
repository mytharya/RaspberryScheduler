from random import randint

baza_de_date = {}

def clearScreen():
    print("\n"*20)

def unique_id():
    if len(baza_de_date.keys()) < 1000:
        while True:
            identificator_unic = randint(0,1000)
            if identificator_unic not in baza_de_date:
                return identificator_unic
    else:
        return None
class Magazin:
    def __init__(self, name):
        self.nume = name
        # self.listaClienti = {}
    
    def adaugaClient():
        if unique_id != None:
            baza_de_date[unique_id()] = client_nou
            # baza_de_date[unique_id()] = {'first_name':self.first_name, 'last_name':self.last_name}
        else:
            print("Prea multi clienti!")

    def listeazaClientii():
        for any_key in baza_de_date.keys():
            print("ID: {}, Nume: {}, Prenume: {}".format(any_key, baza_de_date[any_key].first_name, baza_de_date[any_key].last_name))

class Client:
    def __init__(self, nume, prenume):
        self.first_name = nume
        self.last_name = prenume
    
    # def listeazaClientii():
    #     for any_key in baza_de_date:
    #         print("ID: {}, Nume: {}, Prenume: {}".format(any_key, self.first_name, self.last_name))

    def askIntegerInput(intrebare, eroare):
            while True:
                int_input = input(intrebare).strip()
                try:
                    int_input = int(int_input)
                    return int_input
                except ValueError:
                    print(eroare)

    def adaugaProdus():
        Magazin.listeazaClientii()
        intrebare = "Introdu ID-ul clientului caruia doresti sa ii adaugi produsul: "
        eroare = "Valoarea introdusa nu e un ID!"
        while True:
            int_input = Client.askIntegerInput(intrebare, eroare)
            if int_input in baza_de_date:
                print("NR existent")
                # baza_de_date[int_input].append(produs_nou)
                
                break
            else:
                print("NR Inexistent")

class Produs(Client):
    def __init__(self, produs, greutate, defect):
        self.product = produs
        self.weight = greutate
        self.defekt = defect


# main prog
clearScreen()
client_nou = Client("Mike", "Wazowski")
Magazin.adaugaClient()
client_nou = Client("Rany","Dandy")
Magazin.adaugaClient()
client_nou = Client("James","Sullivan")
Magazin.adaugaClient()
produs_nou = Produs("Handy", 350, "ecran spart")
Client.adaugaProdus()

Magazin.listeazaClientii()