from brain_games.cli import welcome_user


ROUNDS_TO_WIN = 3


def run_game(selected_game):
    name = welcome_user()
    print(selected_game.RULE)
    counter = 0
    while counter < ROUNDS_TO_WIN:
        correct_answer, question = selected_game.generate_round()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if correct_answer == user_answer:
            counter += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
