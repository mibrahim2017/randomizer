import random

print("welcome to the randomizer guessing game, here you will try to guess the correct number between 1-50")
secret_number=random.randint(1,50)
attempts=0 
while True:
    guess=int(input("enter a number between 1-50: "))
    attempts=attempts+1

    if guess==secret_number:
        print("you just guessed the secret number!")
        print(f"the number was {secret_number}")
        print(f"you have done {attempts} attempts")
        break
    elif guess>secret_number:
        print("too high, enter a lower number")
    elif guess<secret_number:
        print("too low, enter a higher number")
    else:
        print("invalid number")
