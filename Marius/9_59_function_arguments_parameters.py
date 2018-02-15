#9_59_funtion arguments and parameters

#likes is defaulted to python and ALWAYS are AT END
def about (name, age, likes="Python"):
        sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
        return sentence

#v1
print(about("Jack",23,"Python"))
#v2
print(about(age= 23, name= "Jack", likes= "Python"))
