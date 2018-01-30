#health potion
import random
import math

#initial.health
initial_health = 50

#difficulty
difficulty_level = 2

#smtg
#low=int(25*diff)
#high=int(50*diff)

#random number generator
random_number = random.randint(25, 50)
#potion heath
potion_health = int ( random_number / difficulty_level )

#print suff
print ("health =",initial_health)
print ("difficulty level =",difficulty_level)
#print ("low",low)
#print ("high",high)
print ("random number generator =", random_number)
print ("potion health =",potion_health)

current_health = initial_health + potion_health
print ("curent health value =", current_health)

#unknown
#print(math.floor())
