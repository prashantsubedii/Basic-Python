print("Welcome to Number Guessing Game!")
import random
num = random.randint(1,50)
guess =0
attemps=0
while guess!=num:
    print("Type a number between 1 to 50")
    guess=int(input())
    attemps+=1

    if guess<num:
        print("Too low!")
    elif guess>num:
        print("Too high!")  
    else:
        print("You guessed it right!")
        print(f"You guessed the number in {attemps} attemps")

