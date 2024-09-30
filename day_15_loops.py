count=0
while count<=10 :
    print(count)
    count+=1
from getpass import getpass as input


exit="no"
while exit.lower() == "no":  # Added .lower() to handle "No", "NO", etc.
    print("Select your move (R, P or S)")
    player1Move = input("Player 1 > ")
    player2Move = input("Player 2 > ")

    if player1Move=="R":
        if player2Move=="R":
            print("draw")
        elif player2Move=="P":
            print("player2 wins")
        elif player2Move=="S":
            print("player1 wins")
        else:
            print("invalid input player2")
    elif player1Move=="P":
        if player2Move=="P":
            print("draw")
        elif player2Move=="R":
            print("player1 wins")
        elif player2Move=="S":
            print("player2 wins")
        else:
            print("invalid input player2")
    elif player1Move=="S":
        if player2Move=="S":
            print("draw")
        elif player2Move=="P":
            print("player1 wins")
        elif player2Move=="R":
            print("player2 wins")
        else:
            ("invalid input player2")
    else:
        print("invalid input player1")
    exit = input("Do you want to exit?: ")    