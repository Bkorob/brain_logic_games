import random


QUESTION = 'Find the greatest common divisor of given numbers.'


def game():
    counter = random.choice('235')
    if counter == '2':
        num_first = random.randrange(0, 101, 2)
        num_second = random.randrange(0, 101, 2)
    elif counter == '3':
        num_first = random.randrange(0, 101, 3)
        num_second = random.randrange(0, 101, 3)
    else:
        num_first = random.randrange(0, 101, 5)
        num_second = random.randrange(0, 101, 5)
    screen_question = (f'{num_first} {num_second}')
    print(screen_question)
    if num_first > num_second:
        num_max = num_first
    else:
        num_max = num_second
    for i in range(num_max + 1, 0, -1):
        if ((num_first % i == 0) and (num_second % i == 0)):
            screen_answer = i
            return str(screen_answer), screen_question
