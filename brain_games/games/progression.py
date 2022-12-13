import random


QUESTION = "What number is missing in the progression?"


def game():
    counter = int(random.choice('235'))
    quest_lst= list(range(2, 26, counter))
    lost_num = random.choice(quest_lst)
    lost_num_index = quest_lst.index(lost_num)
    quest_lst[lost_num_index] = ".."
    screen_question = str(quest_lst).translate(str(quest_lst).maketrans('','',",[]''"))
    screen_answer = str(lost_num)
    return screen_answer, screen_question

