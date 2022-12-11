#!/usr/bin/env python3


from brain_games.games import gcd
import brain_games.engine


def main():
    brain_games.engine.game_engine(gcd)


if __name__ == '__main__':
    main()
