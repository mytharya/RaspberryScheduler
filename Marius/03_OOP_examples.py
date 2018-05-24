print("\n"*20)

#super class
class Animal:
    
    #constructor function
    def __init__(self, name):
        self.name = name

#subclass
#class name-of-new-class(inherited-class)
class Cat(Animal):
    
    #constructor function
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
    
    #normal function
    def purr(self):
        print("Purr...")

#subclass
#class name-of-new-class(inherited-class)
class Dog(Animal):
    legs = 4
    
    #constructor function
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    #normal function
    def bark(self):
        print("Woof!")

felix = Cat("Kitty", 4)
#print(felix.color) #cat does not have "color" attribute
print(felix.legs,"\n")
print(felix.name)

fido = Dog("Fido", "brown")
print(fido.name)
print(fido.color)
fido.bark()

print(fido.legs) #fidos (who is a dog) legs = 4
print(Dog.legs) #default no of legs for any dog