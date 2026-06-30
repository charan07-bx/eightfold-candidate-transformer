

import logging
import re

from models.candidate import Candidate


class DataValidator:
    

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def validate(self, candidate: Candidate) -> bool:
        
        if not candidate.name.value:
            self.logger.error("Candidate name is missing.")
            return False

        if not self.validate_email(candidate.email.value):
            self.logger.error("Invalid email.")
            return False

        if not self.validate_phone(candidate.phone.value):
            self.logger.error("Invalid phone number.")
            return False

        for skill in candidate.skills:
            if not skill.value:
                self.logger.error("Empty skill found.")
                return False

        return True

    def validate_email(self, email: str) -> bool:
        
        if not email:
            return False

        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        return re.match(pattern, email) is not None

    def validate_phone(self, phone: str) -> bool:
        

        if not phone:
            return False

        return phone.startswith("+") and len(phone) >= 10