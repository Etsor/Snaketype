import requests
from datetime import datetime
from typing import List
from sys import exit
from pytermcolors import colorize, Color

from .io.ui import print_result, print_words
from .fallback import get_fallback_words
from .core import EvaluationResult, evaluate, find_prev_result
from .io.filemanager import save_result
from .utils import has_arg


def main() -> None:
    try:
        save_res: bool = True
        if has_arg("-ws") or has_arg("--without-saving"):
            save_res = False

        try:
            words_count = int(input("Enter words count (1-20): "))
            if words_count < 1 or words_count > 20:
                print(colorize("Invalid count of words", fg=Color.FG_RED))
                return

        except ValueError:
            print(colorize("Invalid input! Please enter a number", fg=Color.FG_RED))
            return

        print()

        words: List[str] = []

        try:
            words = requests.get("https://random-word-api.vercel.app/api?words="
                                 f"{words_count}", timeout=3).json()

        except Exception:
            print(colorize("Looks like you are offline!\nUsing fallback list..",
                           fg=Color.FG_YELLOW))

            words = get_fallback_words(words_count)

        print_words(words)

        start_time: datetime = datetime.now()
        user_input: str = input()
        finish_time: datetime = datetime.now()
        typed_words: List[str] = user_input.strip().split(" ")
        spent_time: float = (finish_time - start_time).total_seconds()

        ev_res: EvaluationResult = evaluate(words, typed_words, spent_time)
        print_result(ev_res, find_prev_result())
        print()

        if save_res:
            save_result(ev_res)

    except KeyboardInterrupt:
        print(colorize("\nExiting... Bye!", fg=Color.FG_GREEN, bold=True))
        exit(130)


if __name__ == "__main__":
    main()
