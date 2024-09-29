'''x=input("enter a number")
if x  >= 1000:
    print ("winner")#this wont run because '>=' not supported between instances of 'str' and 'int'
else:
    print("try again") '''

x=int(input("enter a number"))# int is used to change the string into and integer
if x  >= 1000:
    print ("winner")
else:
    print("try again")




pi=float(input("enter value of pi"))# float is used to change the string into and integer
if pi == 3.14 :
    print ("winner")
else:
    print("try again")
