import random


QUESTION = "What number is missing in the progression?"


def create_game():
    counter = int(random.choice('235'))
    q_lst = list(range(2, 26, counter))
    lost_num = random.choice(q_lst)
    lost_num_index = q_lst.index(lost_num)
    q_lst[lost_num_index] = ".."
    screen_q = str(q_lst).translate(str(q_lst).maketrans('', '', ",[]''"))
    screen_ans = str(lost_num)
    return screen_ans, screen_q
