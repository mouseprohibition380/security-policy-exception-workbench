"""
Report generation module for Policy Exception Workbench.

Generates Markdown reports for exceptions and summaries.
"""

import os
from datetime import datetime
from typing import Dict, Any, List
from collections import Counter


def generate_exception_report(exception: Dict[str, Any], output_dir: str) -> str:
    """
    Generate a Markdown report for a single exception.

    Args:
        exception: Exception data with all processed information

    Returns:
        Path to the generated report file
    """
    exception_id = exception['exception_id']
    filename = f"{output_dir}/{exception_id}.md"

    content = f"""# Security Policy Exception Report

## Exception Details

**Exception ID:** {exception_id}
**Policy ID:** {exception.get('policy_id', 'N/A')}
**Title:** {exception.get('exception_title', 'N/A')}
**Status:** {exception.get('status', 'N/A')}

## Business Justification

{exception.get('business_justification', 'N/A')}

## Impact Assessment

**Impacted System:** {exception.get('impacted_system', 'N/A')}
**Risk Type:** {exception.get('risk_type', 'N/A')}
**Requested By:** {exception.get('requested_by', 'N/A')}
**Owner:** {exception.get('owner', 'N/A')}

## Risk Analysis

### Technical Risk Summary

{exception.get('technical_risk', 'N/A')}

### Business Risk Summary

{exception.get('business_risk', 'N/A')}

## Compensating Controls

"""

    compensating_controls = exception.get('compensating_controls', [])
    if compensating_controls:
        for i, control in enumerate(compensating_controls, 1):
            content += f"""### {i}. {control.get('control_name', 'N/A')}

**Compliance Objective:** {control.get('compliance_objective', 'N/A')}

**Implementation Guidance:** {control.get('implementation_guidance', 'N/A')}

"""
    else:
        content += "No compensating controls recommended.\n\n"

    content += "## Evidence Requirements\n\n"
    evidence_checklist = exception.get('evidence_checklist', [])
    if evidence_checklist:
        for item in evidence_checklist:
            content += f"- [ ] {item}\n"
    else:
        content += "No evidence requirements identified.\n"

    content += "\n## Monitoring Dependencies\n\n"
    monitoring_deps = []
    for control in compensating_controls:
        dep = control.get('monitoring_dependency')
        if dep:
            monitoring_deps.append(dep)

    if monitoring_deps:
        for dep in set(monitoring_deps):  # Unique
            content += f"- {dep}\n"
    else:
        content += "No monitoring dependencies identified.\n"

    content += f"""
## Expiry Information

**Expiry Date:** {exception.get('expiry_date', 'N/A')}
**Days Until Expiry:** {exception.get('days_until_expiry', 'N/A')}
**Status:** {exception.get('expiry_status', 'N/A')}

## Recommended Actions

{exception.get('recommended_action', 'N/A')}
"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    return filename


def generate_summary_report(exceptions: List[Dict[str, Any]], output_dir: str) -> str:
    """
    Generate a summary Markdown report.

    Args:
        exceptions: List of all processed exceptions

    Returns:
        Path to the generated summary report
    """
    filename = f"{output_dir}/exception_summary.md"

    total_exceptions = len(exceptions)
    active = sum(1 for e in exceptions if e.get('status') == 'active')
    expired = sum(1 for e in exceptions if e.get('is_expired'))
    expiring_soon = sum(1 for e in exceptions if e.get('is_expiring_soon'))

    risk_types = Counter(e.get('risk_type') for e in exceptions if e.get('risk_type'))

    content = f"""# Security Policy Exception Summary Report

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview

**Total Exceptions:** {total_exceptions}
**Active Exceptions:** {active}
**Expired Exceptions:** {expired}
**Expiring Within 30 Days:** {expiring_soon}

## Risk Type Distribution

"""

    for risk_type, count in risk_types.most_common():
        content += f"- {risk_type}: {count}\n"

    content += "\n## Review Priorities\n\n"

    # Sort by priority: expired first, then expiring soon, then others
    priorities = []
    for e in exceptions:
        if e.get('is_expired'):
            priorities.append((1, e['exception_id'], "EXPIRED - Immediate action required"))
        elif e.get('is_expiring_soon'):
            priorities.append((2, e['exception_id'], "Expiring soon - Schedule review"))
        else:
            priorities.append((3, e['exception_id'], "Active - Monitor expiry"))

    priorities.sort()
    for _, eid, desc in priorities:
        content += f"- {eid}: {desc}\n"

    content += "\n## Evidence Gaps\n\n"

    # Collect all evidence requirements
    all_evidence = []
    for e in exceptions:
        all_evidence.extend(e.get('evidence_checklist', []))

    evidence_counter = Counter(all_evidence)
    if evidence_counter:
        content += "Most common evidence requirements:\n\n"
        for req, count in evidence_counter.most_common(5):
            content += f"- {req} ({count} exceptions)\n"
    else:
        content += "No evidence requirements identified.\n"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    return filename