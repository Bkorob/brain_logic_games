import random


QUESTION = "What is the result of the expression?"


def is_operation(num1, num2, oper):
    if oper == '-':
        operation_result = num1 - num2
    elif oper == '+':
        operation_result = num1 + num2
    elif oper == '*':
        operation_result = num1 * num2
    return operation_result


def create_game():
    num_first = random.randint(0, 10)
    num_second = random.randint(0, 10)
    oper = random.choice('-+*')
    operation_result = is_operation(num_first, num_second, oper)
    # Не понял насчёт "такое определение переменных". А такое?
    screen_ans = str(operation_result)
    screen_q = f'{num_first} {oper} {num_second}'
    return screen_ans, screen_q
