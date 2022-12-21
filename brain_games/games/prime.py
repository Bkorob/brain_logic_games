import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        correct_answer = 'no'
        return correct_answer
    for i in range(int(num / 2), 1, - 1):
        if num % i == 0:
            correct_answer = 'no'
            return correct_answer
    correct_answer = 'yes'
    return correct_answer


def generate_round():
    num = random.randint(0, 50)
    question = num
    correct_answer = is_prime(num)
    return correct_answer, question
