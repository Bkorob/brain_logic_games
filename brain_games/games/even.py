import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = random.randint(0, 100)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = str(number)
    return correct_answer, question
