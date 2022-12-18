import random


QUESTION = 'Find the greatest common divisor of given numbers.'


def create_game():
    counter = int(random.choice('235'))
    num_first = random.randrange(0, 101, counter)
    num_second = random.randrange(0, 101, counter)
    screen_q = (f'{num_first} {num_second}')
    num_max = num_first
    if num_second > num_first:
        num_max = num_second
    for i in range(num_max, 0, -1):
        if ((num_first % i == 0) and (num_second % i == 0)):
            screen_ans = i
            return str(screen_ans), screen_q
