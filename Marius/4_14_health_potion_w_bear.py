#4-14 health potion exercise

#difficulty level easy
difficulty_easy=1

#difficulty level medium
difficulty_medium=0.75

#difficulty level hard
difficulty_hard=0.50

#current difficulty
difficulty = difficulty_easy
print( "difficulty settings" , difficulty)



#initial player hp
initial_player_hp = 100
print ( "initial player hp" , initial_player_hp)
current_player_hp = (initial_player_hp * difficulty)
print ( "curent player hp" , current_player_hp)

#potion power
potion_power=40
print( "potion_power", potion_power)

#bear slap
initial_bear_slap = 20
bear_slap = initial_bear_slap + ( (initial_bear_slap * ( 1 - difficulty ))*2 )
print ( "bear slap power" , bear_slap)

#bear fight round 1
current_player_hp = current_player_hp - bear_slap
print ( "player gets slaped once" , current_player_hp)

#bear fight round 2
current_player_hp = current_player_hp - bear_slap
print ( "player gets slaped again" , current_player_hp)

#player dinks potion
current_player_hp = current_player_hp + potion_power * difficulty
print ( "curent player hp" , current_player_hp)
