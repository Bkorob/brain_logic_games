import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    if question <= 1:
        return False
    for i in range(int(question / 2), 1, - 1):
        if question % i == 0:
            return False
    return True


def generate_round():
    question = random.randint(0, 50)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(correct_answer), question
