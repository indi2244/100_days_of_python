correct_number = 15
attempt = 1

while attempt <= 5:
    print("Guess a number between 1-20")
    number = int(input())

    if number < 10:
        print("Too low")
        attempt += 1
        continue
    elif number > 16:
        print("Too high")
        attempt += 1
        continue
    elif 10 <= number < 15:
        print("Almost there")
        attempt += 1
        continue
    elif number == correct_number:
        print("You are correct!")
        print(f"You guessed it in {attempt} attempt(s)")
        break
    else:
        print("That input is not acceptable")
        break
if attempt>5:
    print("no guesses left")