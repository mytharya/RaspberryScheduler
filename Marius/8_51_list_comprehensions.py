#8_51 list comprehensions

even_numbers = [x for x in range(1,101) if x % 2 == 0]
print (even_numbers)

odd_numbers = [x for x in range(1,101) if x % 2 != 0]
print (odd_numbers)

#other
print()
words = ["the","quick","brown","fox","jumps","over","the","lazy","dog"]
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)
numbers = [3,6,4,8,7,9,1]

class Client:
    def __init__(self,nume):
        self.name = nume

client_nou = Client("Ana-Maria")

lista_clienti = []

lista_clienti.append(Client("Ion"))
lista_clienti.append(client_nou)
