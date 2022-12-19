import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def create_game():
    num = random.randint(0, 50)
    screen_q = num
    if num <= 2:
        screen_ans = 'no'
        return screen_ans, screen_q
    for i in range(int(num / 2), 0, - 1):
        if num % i == 0:
            screen_ans = 'no'
            return screen_ans, screen_q
    screen_ans = 'yes'
    return screen_ans, screen_q
