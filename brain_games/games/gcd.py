import random


RULE = 'Find the greatest common divisor of given numbers.'


def generate_round():
    counter = int(random.choice('235'))
    num_first = random.randrange(1, 101, counter)
    num_second = random.randrange(1, 101, counter)
    question = (f'{num_first} {num_second}')
    num_min = min(num_first, num_second)
    for i in range(num_min, 0, - 1):
        if ((num_first % i == 0) and (num_second % i == 0)):
            correct_answer = i
            return str(correct_answer), question
        else:
            generate_round()
