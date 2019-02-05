# w3resources-30
# Write a Python program that will accept the base and height of a triangle and compute the area.

def ask4input(question, type):
    answer = input(question)
    while type(answer) != type:
        print(type(answer))
        print(answer)
        if type == 'int':
            try:
                answer = int(answer)
            except:
                print('ng')
        elif type == str:
            if answer.isalpha() == True:
                return answer
        else:
            print('none')

            
    # while type(answer) != type:
    #     answer = input(question)
    # else:
    #     return answer

def area(base, height):
    return (height * base) / 2

# main
base = ask4input('Base? ', int)
print(type(base))
while type(base) != int:
    base = ask4input('Base? ')
    while type(base) != int:
        base = ask4input('Base? ')

# try:
#     base = int(ask4input('Base? '))
# except:
#     print('u NEED a number')
# try:
#     height = int(ask4input('Height? '))
# except:
#     print('u NEED a number')

calculated_area = area(base, height)

print (calculated_area)