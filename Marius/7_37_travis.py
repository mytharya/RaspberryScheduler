#7_37 travis

#known_users
known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Giorgie","Harry"]
#lenght?
print(len(known_users))
print("\n"*20)
print("=============================================")
print("Hello! My name is WAY-2-GAY","\n")
#while loop
while True:
    name = input("Available commands: name input, Clear, Print or Exit :").strip().capitalize()
    print()

    if name == "Clear":
        #print clear
        #print clear
        #print clear
        print("\n"*45)

    elif name == "Print":
        #print list
        #print list
        #print list
        print(known_users,"\n")

    elif name == "Exit" or name == "":
        #loop exit
        #loop exit
        #loop exit
        print("k, bb, cya")
        break
        #exit()
    
    elif name not in known_users:
        #add to system?
        #add to system?
        #add to system?
        print("I dont think i've met you {} \n".format(name))
        add_me = input("Would you like to be added to the system (y/n)?").strip().lower()

        if add_me == "y" or add_me == "Y":
            #added to system
            #added to system
            #added to system
            print()
            known_users.append(name)
            print("Is your name '{}' in the list? ".format(name), name in known_users,"\n")
            
        else:
            #not added to system
            #not added to system
            #not added to system
            print()
            print("You were not added to the system {}!".format(name),"\n")
            print("Is your name '{}' in the list? ".format(name), name in known_users,"\n")

    elif name in known_users:
        #remove from system?
        #remove from system?
        #remove from system?
        print("Hello {}!".format(name),"\n")
        remove = input("Would you like to be removed from the system (y/n)?").strip().lower()
        print()
        
        if remove == "y" or remove == "Y":
            #removing you
            #removing you
            #removing you
            print()
            known_users.remove(name)
            print("Is your name '{}' in the list? ".format(name), name in known_users,"\n")

        else:
            #not removed
            #not removed
            #not removed
            print()
            print("You were not deleted! \n")
            print("Is your name '{}' in the list? ".format(name), name in known_users,"\n")
