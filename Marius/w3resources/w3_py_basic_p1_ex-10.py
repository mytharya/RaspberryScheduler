# w3resources-10
# Write a Python program that accepts an integer (n) and computes the value of (n+nn+nnn)

# my variant
while True:
    try:
        value = int(input('Enter a number in order to calculate value of ( x + xx + xxx ) : '))
        break
    except:
        print("That's not a number!")

number = value + int(str(value) + str(value)) + int(str(value) + str(value) + str(value))
print(number)

# official variant
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)