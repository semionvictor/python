import random
import sched
import time

def guess_game():
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
        print("you got the correct answer😊😊")


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(20, 1, guess_game)
scheduler.run()
