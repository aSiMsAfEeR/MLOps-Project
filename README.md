# MLOps Project

Structured machine-learning project template with data ingestion, configuration management, artifacts, logging, and notebook exploration.

## Highlights

- Data ingestion pipeline under `src/data_ingestion.py`.
- Centralized YAML configuration in `config/config.yaml`.
- Reusable path constants and common utility helpers.
- Raw/train/test artifacts for reproducible experimentation.
- Notebook workspace for exploration and model iteration.

## Stack

- Python
- pandas
- NumPy
- scikit-learn
- PyYAML
- Google Cloud Storage client

## Getting Started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the pipeline modules from the repository root so relative paths resolve correctly.

```bash
python src/data_ingestion.py
```

## Project Layout

```text
config/      Configuration and path constants
src/         Pipeline code, logging, and custom exceptions
utils/       Shared helper functions
artifacts/   Raw and split data artifacts
notebook/    Exploratory notebook work
```

## Repository Status

This repo is a support showcase for Python/MLOps capability. Keep notebooks reproducible, avoid committing secrets, and prefer small pipeline modules that can later be covered with tests.

