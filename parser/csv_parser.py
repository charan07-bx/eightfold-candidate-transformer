import csv
import logging
from pathlib import Path
from typing import Dict, List


class CSVParser:

    REQUIRED_COLUMNS = {
        "name",
        "email",
        "phone",
        "current_company",
        "title",
        "skills",
    }

    def __init__(self):
        
        self.logger = logging.getLogger(__name__)

    def parse(self, file_path: str) -> List[Dict]:
        
        path = Path(file_path)

        if not path.exists():
            self.logger.warning(f"CSV file not found: {file_path}")
            return []

        candidates = []

        try:

            with open(path, "r", encoding="utf-8") as csv_file:

                reader = csv.DictReader(csv_file)

                if reader.fieldnames is None:
                    self.logger.error("CSV has no header row.")
                    return []

                missing_columns = self.REQUIRED_COLUMNS - set(reader.fieldnames)

                if missing_columns:
                    self.logger.error(
                        f"Missing required columns: {missing_columns}"
                    )
                    return []

                for row in reader:

                    candidate = {
                        "name": row.get("name", "").strip(),
                        "email": row.get("email", "").strip(),
                        "phone": row.get("phone", "").strip(),
                        "current_company": row.get(
                            "current_company", ""
                        ).strip(),
                        "title": row.get("title", "").strip(),
                        "skills": [
                            skill.strip()
                            for skill in row.get("skills", "").split(",")
                            if skill.strip()
                        ],
                    }

                    candidates.append(candidate)

        except Exception as e:
            self.logger.exception(f"Error while reading CSV: {e}")
            return []

        return candidates