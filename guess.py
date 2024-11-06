import random

random_number = random.randint(0,10)
print("enter a number between 0 and  10")

user_guess = int(input())

while user_guess != random_number:
    if user_guess > random_number:
        print("you are above the number")

    else:
        print("you are below the number")

    user_guess = int(input())

if user_guess == random_number:
    print("your guess is correct😊😊")