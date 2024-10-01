while True:
    print("choose right or left: ")
    direction=input()
    if direction =="right":
        print("you died")
        break
    elif direction=="left":
        print("correct")
        go_again=input("wanna go another")
        if go_again== "yes":
            continue
        else:
            exit()
    else:
        print("you're clever")





while True:
    print("choose a number between 1-6 : ")
    number=input()
    if number=="6" or number == "1":
        print("you survived")
        go_another=input("wanna go another round : ")
        if go_another=="yes":
            continue
        else:
            exit()
    elif number=="2" or number=="4":
        print("you barely survived")
        exit()
    else:
        print("you died !!")
        break