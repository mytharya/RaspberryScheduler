#9_57 variabile scope

#global scope
a = 250
x=[1,2,3]

def f1():
    #local scope !!!
    b = a - 25
    print("print a:",a)
    print("print b:",b)
    # c non existent yet
    #print("print c:",c)
    x[0] = 5

def f2():
    a = 50 #this is local does not overwright global
    c = 25
    print("print a:",a)
    #b is local scope of f1, cannot be seen outside of f1
    #print("print b",b)
    print("print c:",c)

def f3():
    global a #this means i'll overwrite a global value
    a = 100 # this is the overwriting
    print(a)

print("\nf1 local scope")
f1()
print("\nf2, local scope")
f2()
print("\nglobal scope")
#global scope
print("print a",a)
#local scopt of f1
#print("print b",b)
#local scope of f2
#print("print c",c)
