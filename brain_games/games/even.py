import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def create_game():
    number = random.randint(0, 100)
    result = is_even(number)
    screen_q = number
    screen_ans = str(result)
    return screen_ans, screen_q
