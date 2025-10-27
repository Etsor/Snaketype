from datetime import datetime
from typing import List
from pytermcolors import colorize, Color
import requests
import sys
from .ui import print_result, print_words
from .fallback import get_fallback_words
from .core import EvaluationResult, evaluate


def main() -> None:
    words_count: int = int(input("Enter words count (1-30): "))
    if words_count < 1 or words_count > 30:
        print("Invalid count of words")
        sys.exit(0)
    print()

    words: List[str] = []

    try:
        words = requests.get(f"https://random-word-api.vercel.app/api?words={words_count}", timeout=3).json()
    except Exception:
        print(colorize("Looks like you are offline!\nUsing fallback list..", fg=Color.FG_YELLOW))
        words = get_fallback_words(words_count)
        
    print_words(words)

    start_time: datetime = datetime.now()
    user_input: str = input()
    finish_time: datetime = datetime.now()
    typed_words: List[str] = user_input.strip().split(" ")
    spent_time: float = (finish_time - start_time).total_seconds()

    ev_res: EvaluationResult = evaluate(words, typed_words, spent_time)
    print_result(ev_res)
    print()


if __name__ == "__main__":
    main()
