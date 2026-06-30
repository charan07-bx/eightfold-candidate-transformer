

import logging
import re
from pathlib import Path
from typing import Dict


class ResumeParser:
    

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def parse(self, file_path: str) -> Dict:
        
        path = Path(file_path)

        if not path.exists():
            self.logger.warning(f"Resume file not found: {file_path}")
            return {}

        try:
            with open(path, "r", encoding="utf-8") as file:
                text = file.read()

        except Exception as e:
            self.logger.exception(f"Unable to read resume: {e}")
            return {}

        candidate = {
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "skills": self.extract_skills(text),
            "experience": self.extract_experience(text),
            "education": self.extract_education(text),
            "github": self.extract_github(text),
            "raw_text": text,
        }

        return candidate

    def extract_name(self, text: str) -> str:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return lines[0] if lines else ""

    def extract_email(self, text: str) -> str:
        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )
        return match.group() if match else ""

    def extract_phone(self, text: str) -> str:
        match = re.search(
            r"(\+?\d[\d\s\-]{8,}\d)",
            text,
        )
        return match.group().strip() if match else ""

    def extract_skills(self, text: str):
        known_skills = {
            "Python",
            "Java",
            "SQL",
            "Machine Learning",
            "C++",
            "JavaScript",
            "React",
            "Node.js",
            "Git",
            "Docker",
        }

        found = []

        lower_text = text.lower()

        for skill in known_skills:
            if skill.lower() in lower_text:
                found.append(skill)

        return sorted(found)

    def extract_experience(self, text: str) -> str:
        match = re.search(
            r"Experience\s*(.*?)\s*Education",
            text,
            re.DOTALL | re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return ""

    def extract_education(self, text: str) -> str:
        match = re.search(
            r"Education\s*(.*?)\s*(GitHub|$)",
            text,
            re.DOTALL | re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return ""

    def extract_github(self, text: str) -> str:
        match = re.search(
            r"https?://github\.com/[^\s]+",
            text,
        )

        return match.group() if match else ""