def PinPicker(number):
    import random
    pin=""
    for i in range(number):
        pin+=str(random.randint(0,9))
    return pin
my_pin=PinPicker(4)
print(my_pin)


def Area_of_triangle(base, height):
    area=base * height
    return area
area=Area_of_triangle(10,20)
print(area)

#day25 challenge
import random
def roll_dice(sides):
    result=random.randint(1,sides)
    return result
def roll_6_and_8():
    roll_6=roll_dice(6)
    roll_8=roll_dice(8)
    health=roll_6*roll_8
    return health

character="yes"

while character=="yes" :
    char=input("Enter the name of character")
    health=str(roll_6_and_8())
    print("their health is ",health,"hp")
    character=input("want another character")


