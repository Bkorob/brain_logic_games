import random


QUESTION = "What is the result of the expression?"


def game():
    num_first = random.randint(0,100)
    num_second = random.randint(0,100)
    oper = random.choice('-','+','*')
    result = 0
    if oper == '-':
        result = num_first - num_second
    elif oper == '+':
        result = num_first + num_second
    elif oper == '*':
        result = num_first * num_second
    screen_answer = str(result)
    screen_question = f'{num_first} {oper} {num_second}'
    return screen_answer, screen_question


