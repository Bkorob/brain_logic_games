from brain_games.cli import welcome_user


WIN_COUNTER = 3


def counting(selected_game):
    name = welcome_user()
    print(selected_game.QUESTION)
    counter = 0
    while counter < WIN_COUNTER:
        screen_ans, screen_q = selected_game.game()
        print(f'Question: {screen_q}')
        user_ans = input('Your answer: ')
        if screen_ans != user_ans:
            print(f"'{user_ans}' is wrong answer ;(. "
                  f"Correct answer was '{screen_ans}'")
            print(f"Let's try again, {name}!")
            return
        if screen_ans == user_ans:
            counter += 1
            print('Correct!')
    print(f'Congratulations, {name}!')
    return
