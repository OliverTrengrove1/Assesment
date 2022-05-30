"""
Oliver Trengroves assessment
this game allows users to learn basic te reo maori
"""

import random


def get_name():
    name_local = str(input("what is your name?:"))
    return name_local


def get_age():
    age_local = int(input("what is your age"))
    return age_local


# Main Routine
name = get_name()  # 1st function
age = get_age()  # 2nd function

print(f'\nHi {name} at {age} years old this will be a piece of cake.\n')
print('Welcome to the te reo quiz')
answer = input('Are you ready to play the Quiz ? (yes/no) :')


if answer.lower() == 'yes':
    answer = input('Question 1: What is one in maori \n a.rua \n b.seven \n c.tahi \n d. uno\n')

    while answer.lower() != 'tahi':
        print('Wrong Answer :(')
        answer = input('Question 1: What is one in maori \n a.rua \n b.seven \n c.tahi \n d.uno\n')


    else:

        print('correct')

    answer = input('Question 2:what is sunday in maori?\n a.ratapu\n b.raapa\n c.meircoles\n d.sunday\n ')
    while answer.lower() != 'ratapu':
        print('Wrong Answer :(')
        answer = input('Question 2:what is sunday in maori?\n a.ratapu\n b.raapa\n c.meircoles\n d.sunday\n')
    else:

        print('correct')

    answer = input('Question 3: What is table in maori \n a.whanau \n b.papa \n c.tapu \n d.rapurangi\n')
    while answer.lower() != 'tapu':
        print('Wrong Answer :(')
        answer = input('Question 3: What is table in maori \n a.whanau \n b.papa \n c.tapu \n d.rapurangi\n')
    else:

        print('correct')
    answer = input('Question 4: What is five in maori \n a.kiki \n b.drake \n c.5 \n d.rima\n')
    while answer.lower() != 'rima':
        print('Wrong Answer :(')
        answer = input('Question 4: What is table in maori \n a.kiki \n b.drake \n c.5 \n d.rima\n')
    else:

        print('correct')
    answer = input('Question 5: What is good morning in te reo \n a.morena \n b.whaka ora \n c.tangato \n d.morning\n')
    while answer.lower() != 'morena':
        print('Wrong Answer :(')
        answer = input('Question 5: What is table in maori \n a.morena \n b.whaka ora \n c.tangato \n d.morning\n')
    else:

        print('correct')
    answer = input('Question 6: What is tired in maori \n a.yawny \n b.ngenge \n c.abburido \n d.zzzzzz \n')
    while answer.lower() != 'ngenge':
        print('Wrong Answer :(')
        answer = input('Question 6: What is table in maori \n a.yawny \n b.ngenge \n c.abburido \n d.zzzzzz\n')

    else:

        print('correct')

print('Thankyou for Playing this small quiz game, you got' "questions correct!")

print('BYE!')
