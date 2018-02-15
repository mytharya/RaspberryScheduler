#7_43 dictionaries part 2

students = {
        "Alice":["ID0001",26,"A"],
        "Bob":["ID0002",27,"B"],
        "Claire":["ID0003",17,"C"],
        "Dan":["ID0004",21,"D"],
        "Emma":["ID0005",22,"E"],
        }
#
print(students)
#
print(students["Claire"][0])
print(students["Dan"][1:])
#
students_table = {
        "Alice":{"id":"ID0001","age":26,"grade":"A"},
        "Bob":{"id":"ID0002","age":27,"grade":"B"},
        "Claire":{"id":"ID0003","age":17,"grade":"C"},
        "Dan":{"id":"ID0004","age":21,"grade":"D"},
        "Emma":{"id":"ID0005","age":22,"grade":"E"},
        }
#
print(students_table["Dan"]["age"])
#
print(students_table["Emma"]["id"], students_table["Emma"]["grade"])
