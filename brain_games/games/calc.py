import random


QUESTION = "What is the result of the expression?"


def create_game():
    num_first = random.randint(0, 10)
    num_second = random.randint(0, 10)
    oper = random.choice('-+*')
    result = 0
    if oper == '-':
        result = num_first - num_second
    elif oper == '+':
        result = num_first + num_second
    else:
        result = num_first * num_second
    screen_ans = str(result)
    screen_q = f'{num_first} {oper} {num_second}'
    return screen_ans, screen_q
