from typing import List
from pytermcolors import colorize, Color
from ..core import (
    EvaluationResult,
    ResultsDifference,
    analyze_prev_result,
    compare_results
)


def print_result(ev_res: EvaluationResult, prev_res_fn: str) -> None:
    if ev_res.words_count_mismatch:
        print("\nWord count mismatch!"
              f"\nExpected: {colorize(str(len(ev_res.expected_words)), fg=Color.FG_GREEN)}"
              f"\nGot: {colorize(str(len(ev_res.typed_words)), fg=Color.FG_RED)}")
        return

    _print_borders(ev_res.expected_words)
    print(f"Spent time: {ev_res.spent_time:.2f}")
    print(f"WPM: {ev_res.wpm:.2f}")
    print(f"Accuracy: {ev_res.accuracy:.2f}%")
    _print_borders(ev_res.expected_words)

    if ev_res.mistakes_count != 0:
        mistake: str = "mistake" if ev_res.mistakes_count == 1 else "mistakes"
        for i in range(len(ev_res.mistaken_expected_words)):
            print("You made a mistake in word:",
                  colorize(ev_res.typed_mistakes[i],
                           fg=Color.FG_RED),
                  "->",
                  colorize(ev_res.mistaken_expected_words[i],
                           fg=Color.FG_GREEN))

        print(colorize(f"You made {ev_res.mistakes_count} {mistake}!",
                       fg=Color.FG_YELLOW))

    else:
        print(colorize("You made zero mistakes!", fg=Color.FG_GREEN))
    _print_borders(ev_res.expected_words)

    if prev_res_fn != "":
        prev_ev_res: EvaluationResult = analyze_prev_result(prev_res_fn)
        res_diff: ResultsDifference = compare_results(ev_res, prev_ev_res)

        if res_diff.wpm_diff > 0:
            print("Your WPM improved by "
                  f"{res_diff.wpm_diff:.2f} points!",
                  colorize(f"\n{prev_ev_res.wpm:.2f}", Color.FG_RED),
                  "->",
                  colorize(f"{ev_res.wpm:.2f}", Color.FG_GREEN))

        elif res_diff.wpm_diff < 0:
            print("Your previous WPM was better by "
                  f"{abs(res_diff.wpm_diff):.2f} points:",
                  colorize(f"\n{prev_ev_res.wpm:.2f}", Color.FG_GREEN),
                  "->",
                  colorize(f"{ev_res.wpm:.2f}", Color.FG_RED))

        if res_diff.accuracy_diff > 0:
            print("Your accuracy improved by "
                  f"{res_diff.accuracy_diff:.2f}%!",
                  colorize(f"\n{prev_ev_res.accuracy:.2f}", Color.FG_RED),
                  "->",
                  colorize(f"{ev_res.accuracy:.2f}", Color.FG_GREEN))

        elif res_diff.accuracy_diff < 0:
            print("Your previous accuracy was better by "
                  f"{abs(res_diff.accuracy_diff):.2f}%",
                  colorize(f"\n{prev_ev_res.accuracy:.2f}", Color.FG_GREEN),
                  "->",
                  colorize(f"{ev_res.accuracy:.2f}", Color.FG_RED))

        if res_diff.mistakes_diff < 0:
            print("You made "
                  f"{abs(res_diff.mistakes_diff)} fewer mistakes than before!",
                  colorize(f"\n{prev_ev_res.mistakes_count}", Color.FG_RED),
                  "->",
                  colorize(f"{ev_res.mistakes_count}", Color.FG_GREEN))

        elif res_diff.mistakes_diff > 0:
            print("You made "
                  f"{res_diff.mistakes_diff} more mistakes than before",
                  colorize(f"\n{prev_ev_res.mistakes_count}", Color.FG_GREEN),
                  "->",
                  colorize(f"{ev_res.mistakes_count}", Color.FG_RED))
        _print_borders(ev_res.expected_words)


def print_words(words: List[str]) -> None:
    print(colorize(" ".join(words), fg=Color.DIM))


def _print_borders(words: List[str]) -> None:
    DEFAULT_BORDER_LEN: int = 48
    border_char = "-"
    words_str: str = " ".join(words)
    if len(words_str) > DEFAULT_BORDER_LEN:
        print(border_char * len(words_str))
    else:
        print(border_char * DEFAULT_BORDER_LEN)
