"""
Evidence checklist generation module for Policy Exception Workbench.

Generates evidence checklists based on compensating controls.
"""

from typing import Dict, Any, List


def generate_evidence_checklist(compensating_controls: List[Dict[str, Any]]) -> List[str]:
    """
    Generate an evidence checklist from compensating controls.

    Args:
        compensating_controls: List of recommended compensating controls

    Returns:
        List of evidence requirements
    """
    checklist = []
    for control in compensating_controls:
        evidence = control.get('evidence_requirement')
        if evidence:
            checklist.append(evidence)

    # Remove duplicates while preserving order
    seen = set()
    unique_checklist = []
    for item in checklist:
        if item not in seen:
            seen.add(item)
            unique_checklist.append(item)

    return unique_checklist