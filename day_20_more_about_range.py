for i in range(100 ,110): # starting and ending . the ending 110 wont appear cause it prints less than that
    print(i)

for days in range(1,8):
    print("day", days)

#15 times table
print("15 table")
for i in range(1,11):
    print(i,"* 15 =", i*15)


for i in range(0,1000,50):#starting ending and then distance or range or differences
    print(i)

for i in range(10,0,-1):# print 10-0 backwards
    print(i)

#day20 challange
x=int(input("enter the starting point: "))
y=int(input("enter the ending point: "))
z=int(input("enter the differences: "))

for i in range(x,y,z):
    print(i)