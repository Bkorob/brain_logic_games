import random


QUESTION = 'Find the greatest common divisor of given numbers.'


def names():
    counter = int(random.choice('235'))
    num_first = random.randrange(0, 101, counter)
    num_second = random.randrange(0, 101, counter)
    screen_question = (f'{num_first} {num_second}')
    return screen_question
def game():
    if num_first > num_second:
        num_max = num_first
    else:
        num_max = num_second
    for i in range(num_max + 1, 0, -1):
        if ((num_first % i == 0) and (num_second % i == 0)):
            screen_answer = i
            return str(screen_answer), screen_question
