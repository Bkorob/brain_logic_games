import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def create_game():
    number = random.randint(0, 100)
    result = ''
    screen_q = str(number)
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    screen_ans = str(result)
    return screen_ans, screen_q
