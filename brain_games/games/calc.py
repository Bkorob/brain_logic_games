import random


RULE = "What is the result of the expression?"


def give_operation(num1, num2, operator):
    if operator == '-':
        operation_result = num1 - num2
    elif operator == '+':
        operation_result = num1 + num2
    elif operator == '*':
        operation_result = num1 * num2
    return operation_result


def create_game():
    num_first = random.randint(0, 10)
    num_second = random.randint(0, 10)
    operator = random.choice('-+*')
    operation_result = give_operation(num_first, num_second, operator)
    correct_answer = str(operation_result)
    question = f'{num_first} {operator} {num_second}'
    return correct_answer, question
