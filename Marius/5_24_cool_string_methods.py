#cool string methods
print("=")
x="happy birthday"
#find location of birthday position
print(x.index("birthday"))
print("=")
#find location of whatever (wich does not exist)
#print (x.index("krgogkjhsdfhjsfhjgfsv"))
#disabled due to fact it crashes the app
#find start position of word
print(x.find("birthday"))
#find start position of .........
print(x.find("diuhwjhbviudbfngr"))
#-1 result is normal as it didnt find any result (but at least no crash)
#this one works
print(x.index("birthday"))
#this one does not because of case matching
#print(x.index("Birthday"))
#this one works
print(x.find("birthday"))
#this one does not because of case of matching
print(x.find("Birthday"))
#

# new variable
y="00000000happybirthday0000000000"
#strips any "0" from all text
print(y.strip("0"))
#strips "0"'s from the left side of text
print(y.lstrip("0"))
#strips "0"'s from the right part of text
print(y.rstrip("0"))
#this strips just the !!!spaces!!!
print(y.rstrip())

#input name with some spaces and then strip the spaces
name = input("what is you name?: ").strip()
print (name)
#lenght of variable
len (name)
