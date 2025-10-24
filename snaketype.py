import datetime as dt
from typing import List
from pytermcolors import colorize, Color
import requests


def print_words(words: List[str]) -> None:
    print(colorize(" ". join(words), fg=Color.DIM))


def print_borders(words: List[str]) -> None:
    border_char = '-'    
    words_str: str = " ".join(words)
    print(border_char * len(words_str))


def evaluate(expected_words: List[str], typed_words: List[str]) -> None:
    mistakes_count: int = 0
    mistaken_expected_words: List[str] = []
    typed_mistakes: List[str] = []
    if len(expected_words) != len(typed_words):
        print('Word count mismatch!\n',
              f'Expected: {colorize(str(len(expected_words)), fg=Color.FG_GREEN)}\n',
              f'Got: {colorize(str(len(typed_words)), fg=Color.FG_RED)}')

        return

    for i in range(len(expected_words)):
        if expected_words[i] != typed_words[i]:
            mistakes_count += 1
            mistaken_expected_words.append(expected_words[i])
            typed_mistakes.append(typed_words[i])

    if mistakes_count != 0:
        mistake: str = 'mistake' if mistakes_count == 1 else 'mistakes'

        for i in range(len(mistaken_expected_words)):
            print('You made a mistake in word: ',
                   colorize(typed_mistakes[i], fg=Color.FG_RED),
                   '->',
                   colorize(mistaken_expected_words[i], fg=Color.FG_GREEN))

        print(colorize(f'You made {mistakes_count} {mistake}!', fg=Color.FG_YELLOW))

    else:
        print(colorize('You made zero mistakes!', fg=Color.FG_GREEN))


def main() -> None:
    words_count: int = int(input("Enter words count: "))
    words: List[str] = requests.get(f'https://random-word-api.vercel.app/api?words={words_count}').json()
    print_words(words)

    start_time: dt.datetime = dt.datetime.now()

    user_input: str = input()
    typed_words: List[str] = user_input.strip().split(" ")

    finish_time: dt.datetime = dt.datetime.now()
    spent_time: float = (finish_time - start_time).total_seconds()

    print_borders(words)
    print(f'Time spent: {round(spent_time, 2)} sec')
    print(f'WPM: {round(len(words) / spent_time * 60, 2)}')
    print_borders(words)

    evaluate(words, typed_words)


if __name__ == '__main__':
    main()
