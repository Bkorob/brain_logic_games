from brain_games.cli import welcome_user


WIN_COUNTER = 3


def counting(selected_game):
    name = welcome_user()
    print(selected_game.QUESTION)
    counter = 0
    while counter < WIN_COUNTER:
        screen_answer, screen_question = selected_game.create_game()
        print(f'Question: {screen_question}')
        user_answer = input('Your answer: ')
        if screen_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{screen_answer}'")
            print(f"Let's try again, {name}!")
            return
        else:
            counter += 1
            print('Correct!')
    print(f'Congratulations, {name}!')
