import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    for i in range(int(num / 2), 1, - 1):
        if num % i == 0:
            return False
    return True


def generate_round():
    num = random.randint(0, 50)
    question = num
    if is_prime(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
