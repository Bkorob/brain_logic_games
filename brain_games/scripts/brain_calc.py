#!/usr/bin/env python3
from brain_games.games import calc
import brain_games.engine


def main():
    brain_games.engine.run_game(calc)


if __name__ == '__main__':
    main()
