from typing import List
from dataclasses import dataclass, field
import os
import json


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


@dataclass
class ResultsDifference:
    wpm_diff: float = 0.0
    accuracy_diff: float = 0.0
    mistakes_diff: float = 0.0
        

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


def compare_results(ev_res_1: EvaluationResult, 
                    ev_res_2: EvaluationResult) -> ResultsDifference:
    
    return ResultsDifference(ev_res_1.wpm - ev_res_2.wpm,
                             ev_res_1.accuracy - ev_res_2.accuracy,
                             ev_res_1.mistakes_count - ev_res_2.mistakes_count)


def find_prev_result() -> str:
    from .io.filemanager import RESULTS_DIR, PREFIX
    
    prev_res_fn: str = ""
    prev_res_f_mod_time: float = 0.0

    if not os.path.exists(RESULTS_DIR):
        return ""

    for root, _, files in os.walk(RESULTS_DIR):
        for name in files:
            if name.startswith(PREFIX) and name.endswith(".json"):
                full_path = os.path.join(root, name)
                mod_time = os.path.getmtime(full_path)
                if mod_time > prev_res_f_mod_time:
                    prev_res_f_mod_time = mod_time
                    prev_res_fn = full_path

    return prev_res_fn


def analyze_prev_result(prev_res_fn: str) -> EvaluationResult:
    prev_res = ""

    with open(prev_res_fn, "r") as f:
        prev_res = json.load(f)

    return EvaluationResult(wpm=prev_res["wpm"],
                            accuracy=prev_res["accuracy"],
                            mistakes_count=prev_res["mistakes_count"])        
