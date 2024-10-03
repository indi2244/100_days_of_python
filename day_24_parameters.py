def whichCake(ingredient):# one arguments
    if ingredient=="chocolate":
        print("yum")
    elif ingredient=="carrot":
        print("sweet")
    elif ingredient=="broccoli":
        print("no wayyy")
    else:
        print("oh !! might taste good")
whichCake(ingredient="chocolate")


def Cake(ingredient,base,icing):#more arguments
    if ingredient=="chocolate":
        print("yum")
    elif ingredient=="carrot":
        print("sweet")
    elif ingredient=="broccoli":
        print("no wayyy")
    else:
        print("oh !! might taste good")
        print("so you want a ",ingredient,"with a base", base,"and icing", icing)
Cake("peppa","biscuit","chocolate chip")



#user input
def Cake(ingredient,base,icing):#more arguments
    if ingredient=="chocolate":
        print("yum")
    elif ingredient=="carrot":
        print("sweet")
    elif ingredient=="broccoli":
        print("no wayyy")
    else:
        print("oh !! might taste good")
    print("so you want a ",ingredient,"with a base", base,"and icing", icing)

ingredient1=input("enter ingredient: ")
base1=input("enter a base foe cake : ")
icing1=input("enter an icing : ")
Cake(ingredient1,base1,icing1)


#fixing this
'''def pizza_order(topping1 topping2):
  if topping1 = "pepperoni":
    print(topping1, "is a great choice")
  else:
    print(topping1, "is kinda lame on pizza")
  print(topping2, "sounds delicious, much better than" topping1)
  
topping1 =  input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")
  pizza_order(topping1, topping2)'''

def pizza_order(topping1 ,topping2):
  if topping1 == "pepperoni":
    print(topping1, "is a great choice")
  else:
    print(topping1, "is kinda lame on pizza")
  print(topping2, "sounds delicious, much better than" ,topping1)
  
topping1 =  input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")
pizza_order(topping1, topping2)

''

import random
sides=int(input("How many sides : "))
playGame="yes"

def rollDice(sides):
    number=random.randint(1,sides)
    print("you rolled", number)

while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll again?")

