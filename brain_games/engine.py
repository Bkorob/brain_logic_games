from brain_games.cli import welcome_user


def game_engine(selected_game):
    name = welcome_user()
    print(selected_game.QUESTION)
    result = 0
    while result < 3:
        screen_answer, screen_question = selected_game.game()
        print(f'Question: {screen_question}')
        user_answer = input('Your answer: ')
        if screen_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{screen_answer}'")
            print(f"Let's try again, {name}!")
            return
        if screen_answer == user_answer:
            result += 1
            print('Correct!')
    print(f'Congratulations, {name}!')
    return
