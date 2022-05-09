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
numbers = list(range(1,10))
number_set = set(numbers)
print(random.sample(number_set,1))
name = get_name()  # 1st function
age = get_age()  # 2nd function
print(f'\nHi {name} at {age} years old this will be a piece of cake.\n')
answer = str(input('Would you like to start with Learning Numbers in te reo or a Quiz?'))

if answer.lower() == 'learning numbers' or 'numbers':
    answer = str(input('Do you have experience with te reo maori'))
    if answer.lower() == 'yes':
        print("this will be a breeze then")
    else:
        print("thats okay ill make it easy")




if answer.lower() == 'quiz':
    print('Welcome to the te reo quiz')
    answer = str(input('Are you ready to play the Quiz ? (yes/no) :'))
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
