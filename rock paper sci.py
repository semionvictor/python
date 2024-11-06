# generate a random number (coputer _chioce)
# accept users choice
# make a chioce



import random

choices = ["rock","paper","scissors"]


computer_choice = ""
def generate_computer_choice():
    randomInt = random.randint(0,2)
    computer_choice = choices[(randomInt)]
    return computer_choice

user_choice = ""

def accept_user_choice():
    print("enter your choices rock,paper,scissors")
    user_choice = input().lower()
    while user_choice not in choices:
        print("enter a valid choice")
        user_choice = input()
    return user_choice

computer_choice = generate_computer_choice()
user_choice = accept_user_choice()

def user_win(user_choice,computer_choice):
    if user_choice == 'rock' and computer_choice == 'scissors':
        
        return True
    elif user_choice == 'scissors' and computer_choice == 'paper':
        
        return True
    elif user_choice == 'paper' and computer_choice == 'rock':
        
        return True
    else:
        return False
    
trial_count = 2

while trial_count > 0 and not user_win(user_choice,computer_choice):
    user_choice = accept_user_choice()
    computer_choice= generate_computer_choice()
    trial_count = trial_count -1

if user_win(user_choice,computer_choice):
        print("you win😁😁😁")
else:
        print("you lose😒😒😒")
    
