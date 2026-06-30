
import logging

from models.candidate import Candidate
from models.field import CandidateField


class DataMerger:
    

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def merge(self, csv_data: dict, resume_data: dict) -> Candidate:
        
        candidate = Candidate()

        candidate.name = self.merge_field(
            csv_data.get("name"),
            resume_data.get("name"),
            "csv",
            "resume",
        )

        candidate.email = self.merge_field(
            csv_data.get("email"),
            resume_data.get("email"),
            "csv",
            "resume",
        )

        candidate.phone = self.merge_field(
            csv_data.get("phone"),
            resume_data.get("phone"),
            "csv",
            "resume",
        )

        candidate.current_company = self.merge_field(
            csv_data.get("current_company"),
            resume_data.get("experience"),
            "csv",
            "resume",
        )

        candidate.title = self.merge_field(
            csv_data.get("title"),
            resume_data.get("experience"),
            "csv",
            "resume",
        )

        candidate.education = CandidateField(
            value=resume_data.get("education"),
            confidence=0.9,
            sources=["resume"],
        )

        candidate.github = CandidateField(
            value=resume_data.get("github"),
            confidence=0.9,
            sources=["resume"],
        )

        candidate.skills = self.merge_skills(
            csv_data.get("skills", []),
            resume_data.get("skills", []),
        )

        candidate.raw_text = resume_data.get("raw_text", "")

        return candidate

    def merge_field(
        self,
        csv_value,
        resume_value,
        csv_source,
        resume_source,
    ) -> CandidateField:

        if csv_value and resume_value:

            if csv_value == resume_value:

                return CandidateField(
                    value=csv_value,
                    confidence=1.0,
                    sources=[csv_source, resume_source],
                )

            return CandidateField(
                value=resume_value,
                confidence=0.8,
                sources=[csv_source, resume_source],
            )

        if csv_value:

            return CandidateField(
                value=csv_value,
                confidence=0.7,
                sources=[csv_source],
            )

        if resume_value:

            return CandidateField(
                value=resume_value,
                confidence=0.7,
                sources=[resume_source],
            )

        return CandidateField()

    def merge_skills(
        self,
        csv_skills,
        resume_skills,
    ):

        merged = {}

        for skill in csv_skills:

            merged[skill] = CandidateField(
                value=skill,
                confidence=0.8,
                sources=["csv"],
            )

        for skill in resume_skills:

            if skill in merged:

                merged[skill].confidence = 1.0

                merged[skill].sources.append("resume")

            else:

                merged[skill] = CandidateField(
                    value=skill,
                    confidence=0.8,
                    sources=["resume"],
                )

        return list(merged.values())