
import unittest

from parser.csv_parser import CSVParser
from parser.resume_parser import ResumeParser

from transformer.normalizer import DataNormalizer
from transformer.merger import DataMerger
from transformer.validator import DataValidator


class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.csv_parser = CSVParser()
        self.resume_parser = ResumeParser()
        self.normalizer = DataNormalizer()
        self.merger = DataMerger()
        self.validator = DataValidator()

    def test_pipeline(self):

        csv_candidate = self.csv_parser.parse(
            "input/recruiter.csv"
        )[0]

        resume_candidate = self.resume_parser.parse(
            "input/resume.txt"
        )

        csv_candidate = self.normalizer.normalize(csv_candidate)
        resume_candidate = self.normalizer.normalize(resume_candidate)

        candidate = self.merger.merge(
            csv_candidate,
            resume_candidate
        )

        self.assertTrue(
            self.validator.validate(candidate)
        )

        self.assertEqual(
    candidate.name.value,
    "Darpalli Sai Charan Goud"
)

        self.assertEqual(
    candidate.email.value,
    "sc5357854@gmail.com"
)

        self.assertEqual(
            candidate.phone.value,
            "+919876543210"
        )

    def test_missing_resume(self):

        candidate = self.resume_parser.parse(
            "input/missing_resume.txt"
        )

        self.assertEqual(candidate, {})


if __name__ == "__main__":
    unittest.main()