import json
from typing import Dict, List
from datetime import datetime
from .core import EvaluationResult
from pytermcolors import colorize, Color
import os
import sys


RESULTS_DIR: str = "./results"


def save_result(ev_res: EvaluationResult) -> None:
    if ev_res.words_count_mismatch:
        sys.exit(0)
        
    timestamp_str: str = datetime.now().isoformat()
    data: Dict[str, str | float | int | List[str]] = {
        "timestamp": timestamp_str,
        "wpm": ev_res.wpm,
        "accuracy": ev_res.accuracy,
        "mistakes_count": ev_res.mistakes_count,
        "typed_mistakes": ev_res.typed_mistakes
    }

    try:
        os.makedirs(f"{RESULTS_DIR}")
    except OSError:
        print(colorize("Error occured while creating" + 
                       f"\"{RESULTS_DIR}\" directory...\n" +
                       "Try to run app with \"-ws\" flag", 
                       fg=Color.FG_RED))
        sys.exit(0)
    
    with open(f"{RESULTS_DIR}/typing_test_{timestamp_str}.json", "a") as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))
