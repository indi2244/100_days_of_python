subject=input("Enter the subject : ")
full_marks=int(input("Enter the full marks" ))
obt_marks=int(input("Enter the obtained marks "))

percentage=obt_marks/full_marks

grade= percentage*4

if grade >=3.6 and grade<=4 :
    print("A+")

elif grade>=3.2 and grade<3.6 :
    print("A")

elif grade>=2.8  and grade<3.2 :
    print("B+")
elif grade>= 2.4 and grade<2.8:
    print("B")
elif grade<2.4 :
    print("NG")
else:
    print("invalid input")

print ("you got",grade, "in",subject)