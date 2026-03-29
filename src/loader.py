"""
Data loader module for Policy Exception Workbench.

Loads CSV files, validates required columns, and normalizes data.
"""

import csv
from pathlib import Path
from typing import Dict, List, Any


def load_csv(file_path: str, required_columns: List[str]) -> List[Dict[str, Any]]:
    """
    Load a CSV file and return a list of dictionaries.

    Args:
        file_path: Path to the CSV file
        required_columns: List of column names that must be present

    Returns:
        List of dictionaries representing the CSV rows

    Raises:
        ValueError: If required columns are missing or file cannot be read
    """
    path = Path(file_path)
    if not path.exists():
        raise ValueError(f"File not found: {file_path}")

    with open(path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        if not reader.fieldnames:
            raise ValueError(f"No headers found in {file_path}")

        # Check required columns
        missing_columns = set(required_columns) - set(reader.fieldnames)
        if missing_columns:
            raise ValueError(f"Missing required columns in {file_path}: {missing_columns}")

        data = []
        for row in reader:
            normalized_row = {}
            for key, value in row.items():
                # Normalize: strip whitespace, treat empty as None
                normalized_value = value.strip() if value else None
                normalized_row[key] = normalized_value
            data.append(normalized_row)

    return data


def load_exceptions(data_dir: str) -> List[Dict[str, Any]]:
    """Load exceptions.csv"""
    required = [
        'exception_id', 'policy_id', 'exception_title', 'business_justification',
        'impacted_system', 'risk_type', 'requested_by', 'owner', 'existing_controls',
        'expiry_date', 'review_frequency_days', 'status'
    ]
    return load_csv(f"{data_dir}/exceptions.csv", required)


def load_control_library(data_dir: str) -> List[Dict[str, Any]]:
    """Load control_library.csv"""
    required = ['policy_id', 'control_title', 'compliance_objective', 'domain', 'risk_category']
    return load_csv(f"{data_dir}/control_library.csv", required)


def load_compensating_controls(data_dir: str) -> List[Dict[str, Any]]:
    """Load compensating_controls.csv"""
    required = [
        'control_name', 'applicable_risk_type', 'compliance_objective',
        'evidence_requirement', 'monitoring_dependency', 'implementation_guidance'
    ]
    return load_csv(f"{data_dir}/compensating_controls.csv", required)