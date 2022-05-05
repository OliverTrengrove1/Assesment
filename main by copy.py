'''
Oliver Trengroves assessment
this game allows users to learn basic te reo maori
'''

import random


def get_name():
    name_local = input("what is your name?:")
    return name_local


def get_age():
    age_local = int(input("what is your age"))
    return age_local


# Main Routine
name = get_name()  # 1st function
age = get_age()  # 2nd function
print('\nHi {name} at {age} years old this will be a piece of cake.\n'')
answer = input('Would you like to start with Learning Numbers in te reo or a Quiz?')
print('Welcome to the te reo quiz')
if answer.lower() == 'learning numbers':

answer = input('Are you ready to play the Quiz ? (yes/no) :')
score = 0
total_questions = 3

if answer.lower() == 'yes':
    answer = input('Question 1: What is one in maori \n a.rua \n b.seven \n c. tahi \n d. uno\n')

    while answer.lower() != 'tahi':
        print('Wrong Answer :(')
        answer = input('Question 1: What is one in maori \n a.rua \n b.seven \n c.tahi \n d.uno\n')


    else:
        score += 1
        print('correct')

    answer = input('Question 2:what is sunday in maori?\n a.ratapu\n b.raapa\n c.meircoles\n d.sunday\n ')
    while answer.lower() != 'ratapu':
        print('Wrong Answer :(')
        answer = input('Question 2:what is sunday in maori?\n a.ratapu\n b.raapa\n c.meircoles\n d.sunday\n')
    else:
        score += 1
        print('correct')

print('Thankyou for Playing this small quiz game, you got', score, "questions correctly!")
mark = (score / total_questions) * 100
print('your mark is:', mark)
print('BYE!')
