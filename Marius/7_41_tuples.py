#7_41_tuples

our_tuple = (1,2,3,"A","B","C")
#print
print(our_tuple)
#print type
print(type(our_tuple))
#print the 1 to 3 variabiles of our tuple
print(our_tuple[0:3])
#new list
our_list = [1,2,3,4,5,6,7]
#print our list
print(type(our_list))
#replace 2nd variable number xx
our_list[2] = 100
#print
print(our_list)
#tuple and string are imutable, but lists are mutable
#tuple are read only

#list to tuple
A = [1,2,3]
#print & type
print(A)
#change to tuple
print(tuple(A))
#modifiy A as tuple
A = tuple(A)
#print A
print(A)
#print type of A
print(type(A))
#define multiple variabiles
(A,B,C) = 1,2,3
#
print(A)
print(B)
print(C)
#
D,E,F = [1,2,3]
print(D)
print(E)
print(F)
#
G,H,I = "789"
print(G)
print(H)
print(I)
