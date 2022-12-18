import random


def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    print(computer_choice)
    return computer_choice

def get_user_choice():
    user_choice = input('Please enter Rock, Paper or Scissors: ')
    print(user_choice)
    return user_choice

get_computer_choice()
get_user_choice()


# import random

# choices = ['rock', 'paper', 'scissors']

# def get_computer_choice():
#     computer_choice = random.choice(choices)
#     print(computer_choice)
#     return computer_choice

# def get_user_choice():
#     while True:
#         user_choice = input('Please enter rock, paper or scissors: ')
#         if user_choice.lower() not in choices:
#             print('Invalid entry. Please enter rock, paper, or scissors.')
#         else:
#             user_choice = user_choice.lower()
#             print(user_choice)
#             break    
#     return user_choice

# get_computer_choice()
# get_user_choice()
