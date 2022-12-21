import random


RULE = "What number is missing in the progression?"


def create_progression(end_prog, step_prog):
    question_lst = list(range(0, end_prog, step_prog))
    return question_lst


def generate_round():
    end_prog = random.randint(26, 50)
    step_prog = int(random.choice('235'))
    question_lst = create_progression(end_prog, step_prog)
    lost_num_index = random.randint(0, len(question_lst) - 1)
    lost_num = question_lst[lost_num_index]
    question_lst[lost_num_index] = ".."
    question = ' '.join(str(i) for i in question_lst)
    correct_answer = str(lost_num)
    return correct_answer, question
