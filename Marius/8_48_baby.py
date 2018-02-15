#8_48 baby
from random import choice

questions = ["Why the sky is so hih? : ",
             "Why u such a fatty? : ",
             "HAha!! : ",
             "waddap homoboy? no homo",
             "Where ma bitches at? : "]

question = choice(questions)
answer1 = input(question).strip().lower()

while answer1 != "cuz":
    
    answer1 = input ("but why? : ").strip().lower()

print()
print("oh,k,l8er")
    

#another vatiant of loop
print("\n"*20)
print("second variant of a loop",)
answers = []
answer = []
answer = input ("Why does the sky is so high? : ").strip().lower()

while answer != "cuz":
    
    answer = input ("but why? : ").strip().lower()
    answers.append(answer)

print()
print("oh,k,l8er \n")

print(answers)
