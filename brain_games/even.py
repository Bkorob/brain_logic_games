#!/usr/bin/env python3


from random import randint


def has_even():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        i = randint(1, 101)
        print(f'Question: {i}')
        answer = input('Your answer: ')
        if i % 2 == 0 and answer == 'yes':
            print('Correct!')
        elif i % 2 != 0 and answer == 'no':
            print('Correct!')
        else:
            if i % 2 == 0:
                ans = 'yes'
            elif i % 2 != 0:
                ans = 'no'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{ans}'.")
            print(f"Let's try again, {name}")
            return
    print(f'Congradulations, {name}!')
    return


def main():
    has_even()


if __name__ == '__main__':
    main()
