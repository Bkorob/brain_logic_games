import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def create_game():
    number = random.randint(0, 100)
    result = is_even(number)
    question = number
    correct_answer = str(result)
    return correct_answer, question
