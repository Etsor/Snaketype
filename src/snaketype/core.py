from typing import List
from dataclasses import dataclass, field
import json
from filemanager import RESULTS_DIR


@dataclass
class EvaluationResult:
    expected_words: List[str] = field(default_factory=list[str])
    typed_words: List[str] = field(default_factory=list[str])
    spent_time: float = 0.0
    words_count_mismatch: bool = False
    mistakes_count: int = 0
    accuracy: float = 0.0
    mistaken_expected_words: List[str] = field(default_factory=list[str])
    typed_mistakes: List[str] = field(default_factory=list[str])
    wpm: float = 0.0


def evaluate(expected_words: List[str], 
             typed_words: List[str], 
             spent_time: float) -> EvaluationResult:
    
    ev_res: EvaluationResult = EvaluationResult(expected_words=expected_words, 
                                                typed_words=typed_words, 
                                                spent_time=spent_time)

    if len(expected_words) != len(typed_words):
        ev_res.words_count_mismatch = True

    if not ev_res.words_count_mismatch:
        for i in range(len(ev_res.expected_words)):
            if ev_res.expected_words[i] != ev_res.typed_words[i]:
                ev_res.mistakes_count += 1
                ev_res.mistaken_expected_words.append(expected_words[i])
                ev_res.typed_mistakes.append(typed_words[i])

        characters_typed: int = sum(len(word) for word in ev_res.typed_words)
        ev_res.wpm = (characters_typed / 5) / (spent_time / 60)
        ev_res.accuracy = ((len(ev_res.expected_words) - ev_res.mistakes_count) 
                           / len(ev_res.expected_words)) * 100

    return ev_res


def _analyze_previous_result() -> EvaluationResult:
    pass


def compare_results(ev_res_prev: EvaluationResult, 
                    ev_res_curr: EvaluationResult) -> EvaluationResult:
    pass
