#7_42 dictionaries

#define empty dictionary
students = {}
print(type(students))
#
students = {"Alice":25,"Bob":27,"Claire":17,"Dan":21,"Emma":22}
#print all (doesent work)
print(students)
#print a certain key
print("print a key from dictionary, in this case: Dan = ",students["Dan"])
#add a new student
students["Fred"] = 25
#print Fred data
print("print new key data, in this case: Fred = ",students["Fred"])
#change Alice bday
print("Alice is = ",students["Alice"])
students["Alice"]=26
print("Alice is = ",students["Alice"])
#delete items
del students["Fred"]
#print student fred wich in no more and print gives error
#print(students["Fred"])
#print all keys in students
print(students.keys())
#save students.keys() as list
a = list(students.keys())
#print list
print(a)
print(a[0])
print(a[1])
print(a[2])
#
print(students.values())
#
print(list(students.values())[2:])
#
print(students)
#
print(students["Dan"])
#this doesent work and it should not
#print(students[0])
#
students["Alice"] = 1026
#
print(students.items())
