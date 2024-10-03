
def rollDice():
    import random
    dice=random.randint(1,6)
    print("you rolled",dice)

rollDice()#once
rollDice()#twice
for i in range(10):
    rollDice() #roll 10 times



#day23 challenge
def login():
    while True:
        name=input("what is your username : ")
        password=input("what is your password : ")
        if name=="indira" and password=="indii":
            print("welcome !!")
            break
        else:
            print("you are not indira")
            continue
login()


