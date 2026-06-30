# Eightfold AI – Multi-Source Candidate Data Transformer

## Overview

This project implements a multi-source candidate data transformation pipeline for the Eightfold AI Engineering Intern assignment.

The pipeline ingests candidate information from multiple sources, normalizes the data, merges it into a canonical candidate profile, validates the result, and generates configurable JSON output.

---

## Features

- Parse structured recruiter CSV data
- Parse unstructured resume text
- Normalize emails, phone numbers, names, and skills
- Merge candidate information from multiple sources
- Track confidence and provenance
- Validate the final candidate profile
- Generate configurable JSON output
- Unit tests for the pipeline

---

## Project Structure

```
eightfold_candidate_transformer/

├── config/
│   ├── default_config.json
│   └── custom_config.json
│
├── input/
│   ├── recruiter.csv
│   └── resume.txt
│
├── models/
│   ├── candidate.py
│   └── field.py
│
├── output/
│   └── candidate.json
│
├── parser/
│   ├── csv_parser.py
│   └── resume_parser.py
│
├── schemas/
│   └── candidate_schema.json
│
├── transformer/
│   ├── merger.py
│   ├── normalizer.py
│   ├── projector.py
│   └── validator.py
│
├── tests/
│   └── test_pipeline.py
│
├── utils/
│   ├── date_utils.py
│   ├── phone_utils.py
│   └── skill_utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python main.py
```

The generated output will be saved in:

```
output/candidate.json
```

---

## Run the Tests

```bash
python -m unittest tests.test_pipeline
```

---

## Pipeline

```
Recruiter CSV
        │
        ▼
CSV Parser

Resume TXT
        │
        ▼
Resume Parser
        │
        ▼
Data Normalizer
        │
        ▼
Data Merger
        │
        ▼
Data Validator
        │
        ▼
Data Projector
        │
        ▼
candidate.json
```

---

## Technologies Used

- Python
- JSON
- Regular Expressions
- phonenumbers
- unittest

---

## Assumptions

- Recruiter CSV follows the expected column names.
- Resume is provided as a text file.
- Phone numbers are assumed to be Indian numbers during normalization.
- Missing sources should not crash the pipeline.

---

## Future Improvements

- Support PDF and DOCX resumes.
- Add LinkedIn profile parser.
- Add GitHub API integration.
- Improve skill canonicalization.
- Support additional output schemas.

---

## Author

Darpalli Sai Charan Goud