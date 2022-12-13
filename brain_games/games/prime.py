import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    sub_num = random.randint(3, 50)
    screen_question = sub_num
    for i in range(int(sub_num // 2), 0, -1):
        if sub_num % i == 0:
            screen_answer = 'no'
            return screen_answer, screen_question
        screen_answer = 'yes'
        return screen_answer, screen_question
