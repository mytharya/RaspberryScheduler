import random

health = 50
diff=3
#low=int(25*diff)
#high=int(50*diff)
potion_health = int(random.randint(25, 50)/diff)
print("health",health)
print("diff",diff)
#print("low",low)
#print("high",high)
print("potion_health",potion_health)

health = health + potion_health
print ("health value", health)
