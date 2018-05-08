#this is a school management system for children and grades

kiddosInSchool = {"Mike":{"Mathematic":[5, 7]}}

#def addKiddo(name):

#def editKiddo(name):

#def removeKiddo(name):

def addKiddosGrade(name, subject, grade):
    if name not in kiddosInSchool.keys():
        kiddosInSchool[name] = {}

    if subject not in kiddosInSchool[name].keys():
        kiddosInSchool[name][subject] = []

    kiddosInSchool[name][subject].append(grade)
    

#def editKiddosGrade(name,grade):
    
def removeKiddosGrade(name, subject, grade):
    if name in kiddosInSchool.keys():
        if subject in kiddosInSchool[name].keys():
            if grade in kiddosInSchool[name][subject]:
                kiddosInSchool[name][subject].remove(grade)

                #now check if the student has any subjects with grades
                if (len(kiddosInSchool[name][subject]) == 0):
                    #kiddosInSchool[name].keys().remove(subject)
                    del kiddosInSchool[name][subject]
                    if (len(kiddosInSchool[name].keys()) == 0):
                        #kiddosInSchool.keys().remove(name)
                        del kiddosInSchool[name]

def printKiddosGrades():
    print("\n")
    for student in kiddosInSchool.keys():
        for subject in kiddosInSchool[student].keys():
            grades = kiddosInSchool[student][subject]
            print("Student {} has these grade(s) {} in {}".format(student, str(grades), subject))
    
#main program
print("\n"*20)
printKiddosGrades()
addKiddosGrade('Mike', 'Mathematic', 1)
printKiddosGrades()
addKiddosGrade('Mike', 'Algebra', 10)
printKiddosGrades()
addKiddosGrade('Tom', 'Geography', 1)
printKiddosGrades()
removeKiddosGrade('Tom', 'Geography', 1)
printKiddosGrades()
removeKiddosGrade('Mike', 'Algebra', 10)
printKiddosGrades()
