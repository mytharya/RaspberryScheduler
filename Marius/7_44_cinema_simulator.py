#7_44 cinema simulator

#films
films = {
    "Finding Dory":[3,5],
    "Boure":[18,0],
    "Tarzan":[15,1],
    "Ghost Busters":[12,5]
    }

while True:
    print (films,"\n")
    choice = input("What movie do you want to watch? ").strip().title()
    print()
    
    if choice in films:
        age = int(input("How old are you? ").strip())
        print()
        #check user age
        if age >= films[choice][0]:
            #check number of seats
            if films[choice][1] > 0:
                print ("We have {} seat(s). \n".format(films[choice][1]))
                seats = int(input("How many seats you need? :".strip()))
                print()
                if seats > films[choice][1]:
                    print ("You selected too many seats. Select again. \n")
                elif seats <= films[choice][1]:
                    print ("Here are your {} seat(s). \n".format(seats))
                    print ("Enjoy the MOVIE! \n")
                    films[choice][1] = films[choice][1] - seats
                elif seats == 1:
                    print ("The last seat avaliable is yours. \n")
                    films[choice][1] = films[choice][1] - seats
            elif films[choice][1] == 0:
                print("NO tickets avaliable \n")
        else:
            print ("You are too young to watch that!!! \n")
    else:
        print("We dont have that film.... \n")
