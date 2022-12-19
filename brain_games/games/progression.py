import random


QUESTION = "What number is missing in the progression?"


def create_progression():
    counter = int(random.choice('235'))
    question_lst = list(range(2, 26, counter))
    return question_lst


def create_game():
    question_lst = create_progression()
    lost_num_index = random.randint(0, len(question_lst) - 1)
    lost_num = question_lst[lost_num_index]
    question_lst[lost_num_index] = ".."
    screen_q = ' '.join(str(i) for i in question_lst)
    screen_ans = str(lost_num)
    return screen_ans, screen_q
