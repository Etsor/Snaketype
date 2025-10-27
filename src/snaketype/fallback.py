from typing import List
from random import sample


WORDS: List[str] = [
    "apple", "river", "sunlight", "dream", "forest", "shadow", "whisper",
    "crystal", "mountain", "storm", "ocean", "flame", "memory", "planet",
    "mirror", "thunder", "breeze", "garden", "wolf", "echo"
]


def get_fallback_words(count: int) -> List[str]:
    return sample(WORDS, count)
