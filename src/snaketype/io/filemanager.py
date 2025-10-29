import json
from typing import Dict
from datetime import datetime
from ..core import EvaluationResult
import os


RESULTS_DIR: str = "./results"
PREFIX: str = "typing_test_"

def save_result(ev_res: EvaluationResult) -> None:
    if ev_res.words_count_mismatch:
        return
            
    timestamp: str = datetime.now().isoformat()
    data: Dict[str, float | int] = {
        "wpm": ev_res.wpm,
        "accuracy": ev_res.accuracy,
        "mistakes_count": ev_res.mistakes_count,
    }

    os.makedirs(f"{RESULTS_DIR}", exist_ok=True)
    
    with open(f"{RESULTS_DIR}/{PREFIX}_{timestamp}.json", "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
