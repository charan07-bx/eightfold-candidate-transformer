"""
main.py

Entry point for the Candidate Data Transformer.
"""

import json
import logging

from parser.csv_parser import CSVParser
from parser.resume_parser import ResumeParser

from transformer.normalizer import DataNormalizer
from transformer.merger import DataMerger
from transformer.validator import DataValidator
from transformer.projector import DataProjector


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def main():

    logging.info("Reading recruiter CSV...")

    csv_parser = CSVParser()

    csv_candidates = csv_parser.parse(
        "input/recruiter.csv"
    )

    if not csv_candidates:
        logging.error("No recruiter data found.")
        return

    logging.info("Reading resume...")

    resume_parser = ResumeParser()

    resume_candidate = resume_parser.parse(
        "input/resume.txt"
    )

    logging.info("Normalizing data...")

    normalizer = DataNormalizer()

    csv_candidate = normalizer.normalize(
        csv_candidates[0]
    )

    resume_candidate = normalizer.normalize(
        resume_candidate
    )

    logging.info("Merging sources...")

    merger = DataMerger()

    candidate = merger.merge(
        csv_candidate,
        resume_candidate,
    )

    logging.info("Validating candidate...")

    validator = DataValidator()

    if not validator.validate(candidate):
        logging.error("Validation failed.")
        return

    logging.info("Projecting output...")

    projector = DataProjector()

    output = projector.project(
        candidate,
        "config/custom_config.json",
    )

    with open(
        "output/candidate.json",
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            output,
            file,
            indent=4,
        )

    logging.info(
        "Transformation completed successfully."
    )

    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    main()