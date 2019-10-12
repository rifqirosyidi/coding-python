
secret_number = 7

while True:
    guess = int(input("Guess a number between 1 to 10 : "))

    if guess == secret_number:
        print("You guessed it right")
        break