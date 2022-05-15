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

print(f'\nHi {name} at {age} years old this will be a piece of cake.\n')
print('Welcome to the te reo quiz')
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

    answer = input('Question 3: What is table in maori \n a.whanau \n b.papa \n c. tapu \n d. rapurangi\n')
    while answer.lower() != 'tapu':
        print('Wrong Answer :(')
        answer = input('Question 1: What is table in maori \n a.whanau \n b.papa \n c. tapu \n d. rapurangi\n')


    else:
        score += 1
        print('correct')

    print('Thankyou for Playing this small quiz game, you got', score, "questions correct!")
    mark = (score / total_questions) * 100
    print('your mark is:', mark)
    print('BYE!')
token_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]

print('Welcome to te reo numbers learning option')
answer = input('Are you ready to play the Quiz ? (yes/no) :')
if answer.lower() == 'yes' or 'y':
    print('what is', random.choice(token_list), 'in te reo maori')
