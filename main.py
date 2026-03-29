#!/usr/bin/env python3
"""
Policy Exception Workbench - Main Application

A defensive cybersecurity governance tool for managing security policy exceptions.
"""

import os
import sys
from pathlib import Path
from typing import List, Dict, Any

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from src.loader import load_exceptions, load_control_library, load_compensating_controls
from src.translator import translate_exception
from src.control_designer import design_compensating_controls
from src.evidence import generate_evidence_checklist
from src.expiry import calculate_expiry_status
from src.reporter import generate_exception_report, generate_summary_report


def process_exceptions(data_dir: str, output_dir: str) -> List[Dict[str, Any]]:
    """
    Process all exceptions and generate reports.

    Args:
        data_dir: Directory containing CSV files
        output_dir: Directory for output reports

    Returns:
        List of processed exceptions
    """
    # Load data
    exceptions = load_exceptions(data_dir)
    compensating_controls = load_compensating_controls(data_dir)

    processed_exceptions = []

    for exception in exceptions:
        # Translate risks
        risk_summaries = translate_exception(exception)
        exception.update(risk_summaries)

        # Design compensating controls
        controls = design_compensating_controls(exception, compensating_controls)
        exception['compensating_controls'] = controls

        # Generate evidence checklist
        evidence = generate_evidence_checklist(controls)
        exception['evidence_checklist'] = evidence

        # Calculate expiry status
        expiry_info = calculate_expiry_status(exception)
        exception.update(expiry_info)

        # Generate individual report
        generate_exception_report(exception, output_dir)

        processed_exceptions.append(exception)

    # Generate summary report
    generate_summary_report(processed_exceptions, output_dir)

    return processed_exceptions


def print_terminal_summary(exceptions: List[Dict[str, Any]]) -> None:
    """Print a summary to the terminal."""
    total = len(exceptions)
    active = sum(1 for e in exceptions if e.get('status') == 'active')
    expired = sum(1 for e in exceptions if e.get('is_expired'))
    expiring_soon = sum(1 for e in exceptions if e.get('is_expiring_soon'))

    print("Policy Exception Workbench Summary")
    print("=" * 40)
    print(f"Total Exceptions: {total}")
    print(f"Active: {active}")
    print(f"Expired: {expired}")
    print(f"Expiring Soon (≤30 days): {expiring_soon}")
    print()
    print("Reports generated in output/ directory")


def main():
    """Main entry point."""
    # Determine directories
    script_dir = Path(__file__).parent
    data_dir = script_dir / 'data'
    output_dir = script_dir / 'output'

    # Ensure output directory exists
    output_dir.mkdir(exist_ok=True)

    try:
        # Process exceptions
        exceptions = process_exceptions(str(data_dir), str(output_dir))

        # Print summary
        print_terminal_summary(exceptions)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()