from typing import List
from pytermcolors import colorize, Color
import sys
from .core import EvaluationResult

def print_result(ev_res: EvaluationResult) -> None:   
    if ev_res.words_count_mismatch:
        print("Word count mismatch!\n",
              f"Expected: {colorize(str(len(ev_res.expected_words)), fg=Color.FG_GREEN)}\n",
              f"Got: {colorize(str(len(ev_res.typed_words)), fg=Color.FG_RED)}")

        sys.exit(0)

    _print_borders(ev_res.expected_words)   
    print(f"Spent time: {ev_res.spent_time:.2f}")
    print(f"WPM: {ev_res.wpm:.2f}")
    print(f"Accuracy: {ev_res.accuracy:.2f}%")
    _print_borders(ev_res.expected_words)

    if ev_res.mistakes_count != 0:
        mistake_word: str = "mistake" if ev_res.mistakes_count == 1 else "mistakes"
        for i in range(len(ev_res.mistaken_expected_words)):
            print("You made a mistake in word: ",
                   colorize(ev_res.typed_mistakes[i], fg=Color.FG_RED),
                   "->",
                   colorize(ev_res.mistaken_expected_words[i], fg=Color.FG_GREEN))
        print(colorize(f"You made {ev_res.mistakes_count} {mistake_word}!", fg=Color.FG_YELLOW))

    else:
        print(colorize("You made zero mistakes!", fg=Color.FG_GREEN))
    _print_borders(ev_res.expected_words)


def print_words(words: List[str]) -> None:
    print(colorize(" ".join(words), fg=Color.DIM))


def _print_borders(words: List[str]) -> None:
    border_char = "-"    
    words_str: str = " ".join(words)
    print(border_char * len(words_str))
