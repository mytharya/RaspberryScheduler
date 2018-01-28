#difficulty
#0 = easy
#1 = medium
#2 = hard
difficulty = 2

#initial player hp
initial_player_hp = 100
print("inital player hp value = ", initial_player_hp)
#player hp modifier
player_hp_modifier = 30
#player hp
current_player_hp = initial_player_hp - (difficulty * player_hp_modifier)
print("actual player hp", current_player_hp)

#initial bear slapping power
initial_bear_slap = 20
print("initial bear slap power = ", initial_bear_slap)
#bear slap modifier
bear_slap_modifier = 10
#actual bear slap
bear_slap = initial_bear_slap + difficulty * bear_slap_modifier
print("actual bear slap power", bear_slap)

#initial potion power
initial_potion_hp_value = 40
#poition difficulty modifier
potion_difficulty_modifier = 10
#actual potion power
potion_hp_value = initial_potion_hp_value - (difficulty * potion_difficulty_modifier)
print("actual potion power", potion_hp_value)

#player gets slapped
print("player gets slapped..")
current_player_hp = current_player_hp - bear_slap
print("player hp =", current_player_hp)

#player gets slapped again
print("player gets slapped..")
current_player_hp = current_player_hp - bear_slap
print("player hp =", current_player_hp)

#player drinks potion
print("player drinks potion..")
current_player_hp = current_player_hp + potion_hp_value
print("player hp =", current_player_hp)
