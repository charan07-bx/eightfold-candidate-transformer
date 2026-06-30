# Eightfold AI – Multi-Source Candidate Data Transformer
### Technical Design

## Pipeline Overview

The solution follows a modular data pipeline:

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
Final JSON Output

---

## Canonical Candidate Model

The pipeline transforms all source data into a single canonical Candidate model.

Each field stores:

- Value
- Confidence Score
- Source Provenance

This enables traceability and conflict resolution across multiple data sources.

---

## Normalization Strategy

The normalization stage standardizes candidate information before merging.

Examples:

- Emails → lowercase
- Phone Numbers → E.164 format
- Names → Title Case
- Skills → duplicate removal and canonical formatting

---

## Merge Strategy

The merger combines structured and unstructured data into one candidate profile.

Rules:

- If both sources contain the same value:
    - Confidence = 1.0
    - Sources = CSV + Resume

- If values differ:
    - Resume value is preferred.
    - Confidence = 0.8
    - Provenance records both sources.

- If only one source contains a value:
    - Confidence = 0.7

---

## Validation

Before exporting:

- Required fields must exist.
- Email format is validated.
- Phone number format is validated.
- Empty skills are rejected.

---

## Configurable Output

The projector reads a runtime JSON configuration.

The configuration controls:

- Included fields
- Field names
- Confidence output
- Provenance output

No Python code changes are required.

---

## Edge Cases

The pipeline handles:

- Missing CSV
- Missing Resume
- Missing fields
- Duplicate skills
- Invalid phone numbers
- Empty values

---

## Assumptions

- Recruiter CSV follows expected column names.
- Resume is available as text.
- Phone numbers are normalized using the Indian region.