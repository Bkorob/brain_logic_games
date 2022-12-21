import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0



def generate_round():
    number = random.randint(0, 100)
    result = is_even(number)
    if result == True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = number
    return str(correct_answer), question
