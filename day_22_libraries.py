import random

my_number=random.randint(1,10)
print(my_number)


for i in range(10):
    new_number=random.randint(1,100)
    print(new_number)

#day22 challenge

import random


attempt=1
challenge_number=random.randint(1,20)
while attempt <= 5:
    print("Guess a number between 1-20")
    inp_number = int(input())
    
    if inp_number < challenge_number:
        print("low")
        attempt += 1
        continue
    elif inp_number > challenge_number:
        print("high")
        attempt += 1
        continue
    elif inp_number ==challenge_number:
        print("You are correct!")
        print(f"You guessed it in {attempt} attempt(s)")
        exit()
    else:
        print("That input is not acceptable")
        break
if attempt>5:
    print("no guesses left")





