import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        screen_answer = 'no'
        return screen_answer
    for i in range(int(num / 2), 1, - 1):
        if num % i == 0:
            screen_answer = 'no'
            return screen_answer
    screen_answer = 'yes'
    return screen_answer 


def create_game():
    num = random.randint(0, 50)
    screen_question = num
    screen_answer = is_prime(num)
    return screen_answer, screen_question
print(create_game())