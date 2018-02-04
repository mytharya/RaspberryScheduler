#6_32 logical opterators
#<>== comparison operators
#not,and,or    logical operators

#NOT operators
print(not True)
print(not False)

print(not 2 < 3)
print(not 3 > 1)
print(not 4 == 3)

x = 10
y = 20

if not y < x:
    print("it worked 1")

#Logical OPERATORS

#Variabile
c = 10
d = 5

#AND operator
if c >= 10 and d > 1:
    print("it worked 2")

#NAND   --- NOT and AND (combined)---
if not (c > 10 and d > 1):
    print("it worked 3")

#OR operator
if c > 1 or d > 1:
    print("it worked 4")

#NOR --- NOT and OR (combined)--- operator
if not (c > 100 or d > 100):
    print("it worked 5")

#v1
print("v1")
if (c>5 and d>5) or (c>1 and d>1):
    print("it worked 6")
#v2
print("v2")
if print(print("c>5",c>5) and print("d>5",d>5)) or print(print("c>1",c>1) and print("d>1",d>1)):
    print("it worked 7")
#v3
print("v3")
print("c>5",c>5)
print("d>5",d>5)
print("c>1",c>1)
print("d>1",d>1)
