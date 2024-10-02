multiple=int(input("Enter a number: "))
attempts=0
for i in range(1,11):
    correct_ans=i*multiple
    print(i,"*",multiple)
    answer=int(input(""))
    if answer==correct_ans:
        print("correct")
        attempts+=1
    else:
        print("you are wrong !!!")
    
if attempts==10:
    print("perfect score")
else:
    print(f"better luck next time, you got{attempts} out of 10")


