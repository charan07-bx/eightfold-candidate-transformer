from dataclasses import dataclass, field
from typing import List


@dataclass
class CandidateField:
    
    value: object = None

    confidence: float = 0.0

    sources: List[str] = field(default_factory=list)