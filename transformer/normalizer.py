
import logging
from typing import Dict, List

import phonenumbers


class DataNormalizer:
    

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def normalize(self, candidate: Dict) -> Dict:
        

        normalized = candidate.copy()

        normalized["email"] = self.normalize_email(
            candidate.get("email", "")
        )

        normalized["phone"] = self.normalize_phone(
            candidate.get("phone", "")
        )

        normalized["skills"] = self.normalize_skills(
            candidate.get("skills", [])
        )

        normalized["name"] = self.normalize_name(
            candidate.get("name", "")
        )

        return normalized

    def normalize_email(self, email: str) -> str:

        return email.strip().lower()

    def normalize_name(self, name: str) -> str:

        return " ".join(word.capitalize() for word in name.split())

    def normalize_phone(self, phone: str) -> str:

        try:

            parsed = phonenumbers.parse(phone, "IN")

            if phonenumbers.is_valid_number(parsed):

                return phonenumbers.format_number(
                    parsed,
                    phonenumbers.PhoneNumberFormat.E164,
                )

        except Exception:
            pass

        return phone

    def normalize_skills(
        self,
        skills: List[str],
    ) -> List[str]:

        cleaned = []

        seen = set()

        for skill in skills:

            skill = skill.strip().title()

            if skill and skill not in seen:

                cleaned.append(skill)

                seen.add(skill)

        return sorted(cleaned)