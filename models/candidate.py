from dataclasses import dataclass, field
from typing import List

from models.field import CandidateField


@dataclass
class Candidate:

    name: CandidateField = field(default_factory=CandidateField)

    email: CandidateField = field(default_factory=CandidateField)

    phone: CandidateField = field(default_factory=CandidateField)

    current_company: CandidateField = field(default_factory=CandidateField)

    title: CandidateField = field(default_factory=CandidateField)

    experience: CandidateField = field(default_factory=CandidateField)

    education: CandidateField = field(default_factory=CandidateField)

    github: CandidateField = field(default_factory=CandidateField)

    skills: List[CandidateField] = field(default_factory=list)

    raw_text: str = ""