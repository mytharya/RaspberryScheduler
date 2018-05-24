class Student:
    def __init__(self, nume, prenume, age):
        self.nume = nume
        self.prenume = prenume
        self.age = age

    def adauga(self):
        conditia = False
        for numar in studenti.keys():
            if student_nou.nume in studenti[numar]["nume"] and student_nou.prenume in studenti[numar]["prenume"] and student_nou.age == studenti[numar]["age"]:
                print("Acesta persoana exista deja!")
                conditia = True
                break

        if conditia == False:
            studenti[numar+1] = {"nume":student_nou.nume, "prenume":student_nou.prenume, "age":student_nou.age}

    def sterge(self):
        conditia = False
        for numar in studenti.keys():
            if student_nou.nume in studenti[numar]["nume"] and student_nou.prenume in studenti[numar]["prenume"] and student_nou.age == studenti[numar]["age"]:
                conditia = True
                break
        
        if conditia == True:
            del studenti[numar]

    def listeaza():
        print("\nExista urmatorii studenti in lista noastra:")
        for numar in studenti.keys():
            print("Numar: {}, Nume: {}, Prenume: {}, Varsta: {}".format(numar, studenti[numar]["nume"], studenti[numar]["prenume"], studenti[numar]["age"]))

class Cursuri(Student):
    def __init__(self, materie, note):
        self.materie = materie
        self.note = note

    def adauga(self):
        # print(cursuri_noi.materie)
        # print(cursuri_noi.note)
        Student.listeaza()
        numar = input("Carui student vrei sa ii adaugi noi cursuri si/sau noi note?").strip()
        numar = int(numar)
        print(studenti[numar]["materii"])
        if cursuri_noi.materie not in studenti[numar]["materii"]:
            studenti[numar]["materii"][cursuri_noi.materie] = []
        if cursuri_noi.note not in studenti[numar]["materii"][cursuri_noi.materie]:
            studenti[numar]["materii"][cursuri_noi.materie] = cursuri_noi.note

    def sterge():
        print("aici o sa sterg.... candva...... :)")

    def listeaza():
        for numar in studenti.keys():
            if "materii" in studenti[numar]:
                for materii in studenti[numar]["materii"].keys():
                    #print(materii)
                    print("Student-ul/a {} {} are note la urmatoarele cursuri: {} ".format(studenti[numar]["nume"], studenti[numar]["prenume"], materii))

#main program
studenti = {0:{"nume":"Marius", "prenume":"POPA", "age":15, "materii":{"matematica":[5,7]}},
            1:{"nume":"Oana", "prenume":"POPA", "age":8, "materii":{"romana":[1,2], "germana":[7,8]}},
            2:{"nume":"Madalina", "prenume":"POPA", "age":7, "materii":{"arte":[10, 10]}},
            3:{"nume":"Nicoleta", "prenume":"POPA", "age":10},
            4:{"nume":"Madalina", "prenume":"POPA", "age":8},
            5:{"nume":"Mike", "prenume":"POPA", "age":16, "materii":{"karate":[8, 9]}},
            }

print("\n"*20)

student_nou = Student("Madalina", "POPA", 8)
Student.listeaza()
student_nou.adauga()
Student.listeaza()
#student_nou = Student("Nicoleta", "POPA", 10)
#student_nou.sterge()
student_nou = Student("Madalina", "POPA", 8)
student_nou.adauga()
Cursuri.listeaza()
student_nou = Student("Oana", "POPA", 8)
cursuri_noi = Cursuri("germana", 2)
cursuri_noi.adauga()
Cursuri.listeaza()