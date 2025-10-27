import json
from typing import Dict, List
from datetime import datetime
from .core import EvaluationResult

def save_result(ev_res: EvaluationResult) -> None:
    if not ev_res.words_count_mismatch:
        timestamp_str: str = datetime.now().isoformat()
        data: Dict[str, str | float | int | List[str]] = {
            "timestamp": timestamp_str,
            "wpm": ev_res.wpm,
            "accuracy": ev_res.accuracy,
            "mistakes_count": ev_res.mistakes_count,
            "typed_mistakes": ev_res.typed_mistakes
        }
        
        with open(f"typing_test_{timestamp_str}.json", "a") as f:
            f.write(json.dumps(data, indent=4, ensure_ascii=False))