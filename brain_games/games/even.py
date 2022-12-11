from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    number = randint(0, 100)
    result = ''
    screen_question = str(number)
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    screen_answer = str(result)
    return screen_answer, screen_question
