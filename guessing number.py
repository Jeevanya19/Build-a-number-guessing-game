import random

secret = random.randint(0,29)
attempts = 0

while True:
    guess = int(input("Enter the guess number: "))
    attempts += 1

    if guess == secret:
        print("Yay! You guessed it correct!")
        print("Number of attempts:", attempts)
        break

    elif guess < secret:
        print("Too low")

    else:
        print("Too high")
