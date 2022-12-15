import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    num = random.randint(2, 50)
    screen_question = num
    for i in range(int(num / 2), 1, - 1):
        if num % i == 0:
            screen_answer = 'no'
            return screen_answer, screen_question
    screen_answer = 'yes'
    return screen_answer, screen_question
