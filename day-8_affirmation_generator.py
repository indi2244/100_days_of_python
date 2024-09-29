name=input('what is your name?')
print("hi !", name )
okay=input("are you okay?")
if okay =="no":
    print("why what happened", name)
    scale =int(input("on the scale of 1-10 how are you feeling ?"))
    if scale <= 5:
        print("don't worry ", name ,"everything will be alright")
    else:
        print("that's great" , name)
else:
    print("have a good day")