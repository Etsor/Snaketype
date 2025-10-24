import datetime as dt
from typing import List, Tuple
from pytermcolors import colorize, Color
import requests


def evaluate(expected_words: List[str], typed_words: List[str]) -> Tuple[bool, int, List[str], List[str]]:
    """
    Compare generated words with the words typed by user.

    Args:
        expected_words: List of generated words.
        typed_words: List of words typed by user.

    Returns:
        Tuple:
        - count_mismatch (bool): True if the number of expected_words and typed_words differs.
        - mistakes_count (int): Number of word mismatches.
        - mistaken_expected_words (List[str]): Generated words that were mistyped.
        - typed_mistakes (List[str]): Corresponding typed words that were mistyped.
    """
    
    count_mismatch: bool = False
    mistakes_count: int = 0
    mistaken_expected_words: List[str] = []
    typed_mistakes: List[str] = []

    if len(expected_words) != len(typed_words):
        count_mismatch = True
        
    if not count_mismatch:
        for i in range(len(expected_words)):
            if expected_words[i] != typed_words[i]:
                mistakes_count += 1
                mistaken_expected_words.append(expected_words[i])
                typed_mistakes.append(typed_words[i])

    return count_mismatch, mistakes_count, mistaken_expected_words, typed_mistakes


def print_result(expected_words: List[str], typed_words: List[str]) -> None:
    """
    Print the evaluation result.

    Args:
        expected_words: List of generated words.
        typed_words: List of words provided by the user.
    """
    
    count_mismatch: bool
    mistakes_count: int
    mistaken_expected_words: List[str]
    typed_mistakes: List[str]
    
    count_mismatch, mistakes_count, mistaken_expected_words, typed_mistakes = evaluate(expected_words, typed_words)

    if count_mismatch:
        print('Word count mismatch!\n',
              f'Expected: {colorize(str(len(expected_words)), fg=Color.FG_GREEN)}\n',
              f'Got: {colorize(str(len(typed_words)), fg=Color.FG_RED)}')

        return

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

    print_borders(expected_words)
    accuracy = ((len(expected_words) - mistakes_count) / len(expected_words)) * 100
    print(f'Accuracy: {accuracy:.2f}%')


def print_words(words: List[str]) -> None:
    print(colorize(' '.join(words), fg=Color.DIM))


def print_borders(words: List[str]) -> None:
    """
    Print a horizontal border with length determined by length of words list.

    Args:
        words: List of words used to determine border length.
    """
    
    border_char = '-'    
    words_str: str = ' '.join(words)
    print(border_char * len(words_str))


def main() -> None:
    words_count: int = int(input('Enter words count: '))
    print()
    
    try:
        words: List[str] = requests.get(f'https://random-word-api.vercel.app/api?words={words_count}', timeout=5).json()
    except Exception:
        print(colorize('Failed to fetch words from API! :(', fg=Color.FG_RED))
        return
    
    print_words(words)

    start_time: dt.datetime = dt.datetime.now()

    user_input: str = input()
    typed_words: List[str] = user_input.strip().split(' ')

    finish_time: dt.datetime = dt.datetime.now()
    spent_time: float = (finish_time - start_time).total_seconds()

    print_borders(words)
    print(f'Time spent: {round(spent_time, 2)} sec')
    characters_typed: int = sum(len(word) for word in typed_words)
    wpm: float = (characters_typed / 5) / (spent_time / 60)
    print(f'WPM: {round(wpm, 2)}')
    print_borders(words)

    print_result(words, typed_words)

    print()


if __name__ == '__main__':
    main()
