
import json
import logging

from models.candidate import Candidate


class DataProjector:
    

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def project(
        self,
        candidate: Candidate,
        config_path: str,
    ) -> dict:
        

        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)

        output = {}

        for field in config["fields"]:

            path = field["path"]

            if path == "full_name":
                output[path] = candidate.name.value

            elif path == "primary_email":
                output[path] = candidate.email.value

            elif path == "skills":
                output[path] = [
                    skill.value
                    for skill in candidate.skills
                ]

        if config.get("include_confidence", False):

            output["confidence"] = {
                "name": candidate.name.confidence,
                "email": candidate.email.confidence,
                "phone": candidate.phone.confidence,
            }

        if config.get("include_provenance", False):

            output["provenance"] = {
                "name": candidate.name.sources,
                "email": candidate.email.sources,
                "phone": candidate.phone.sources,
            }

        return output