from random import randint

class Student:
    def __init__(self, nume, prenume):
        self.name = prenume #variabila interna a clasei
        self.lastname = nume
        self.age = None
        self.subjects = {}
    
    def setAge(self, age):
        self.age = age
    
    def addMark(self, subiect, nota):
        if subiect in self.subjects:
            self.subjects[subiect].append(nota)
        else:
            self.subjects[subiect] = nota

    def removeMark(self, subiect, note):
        if subiect in self.subjects:
            if type(note) == list:
                for nota in note:
                    if nota in self.subjects[subiect]:
                        self.subjects[subiect].remove(nota)
                        if len(self.subjects[subiect]) == 0:
                            del self.subjects[subiect]
                    else:
                        print("Nota inexistenta: {}".format(str(nota)))
            else:
                print("Nota sau notele sub forma unei liste eg:[1,2]")
        else:
            print("Nu exista subiectul: {}".format(subiect))

    def printInfo(self):
        print("{}, {}, {}, {}.".format(self.name, self.lastname,self.age, self.subjects))

class Classroom:
    def __init__(self, nume_profesor):
        self.professor_name = nume_profesor
        self.students = {}

    def addStudent(self, nume, prenume):
        identifier = self.getNewIdentifier()
        if identifier != None:
            studentul = Student(nume, prenume)
            self.students[identifier] = studentul
        else:
            print("Too many students already.")

    def removeStudent(self, identifier):
        if identifier in self.students:
            del self.students[identifier]

    def printInfo(self):
        for student_key in self.students:
            print(student_key)
            self.students[student_key].printInfo()

    def getNewIdentifier(self):
        if len(self.students) < 1000:
            while True:
                rand_num = randint(1,1000)
                print(self.students)
                if rand_num not in self.students:
                    return rand_num
        else:
            return None

    def getStudent(self, identifier):
        identifier = int(identifier)
        if identifier in self.students:
            return self.students[identifier]
        else:
            return None
        

clasa = Classroom("Troscolescu")
clasa.addStudent("a","b")
clasa.printInfo()
identificator = input("da ceva si tu: ").strip()
student = clasa.getStudent(identificator)
if student != None:
    student.addMark("Desen", 1)
clasa.printInfo()

# student_nou = Student("Mike", "Ala-YO")
# student_nou.setAge(99)
# student_nou.addMark("Matematica", 1)
# student_nou.addMark("Geografie", [3,5,7])
# student_nou.printInfo()
# student_nou.removeMark("Geografie", [3,5,7])
# student_nou.printInfo()

# dictionar_nou = {}
# nume = "Marius"

# dictionar_nou[nume] = [1,2]
# print(dictionar_nou[nume])
# dictionar_nou[nume].append(3)
# print(dictionar_nou[nume])
