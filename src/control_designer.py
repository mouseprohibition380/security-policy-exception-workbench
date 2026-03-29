"""
Compensating control design module for Policy Exception Workbench.

Recommends compensating controls based on exception risk types.
"""

from typing import Dict, Any, List


def design_compensating_controls(exception: Dict[str, Any], compensating_controls: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Recommend compensating controls for an exception.

    Args:
        exception: Exception dictionary
        compensating_controls: List of available compensating controls

    Returns:
        List of recommended compensating controls
    """
    risk_type = exception.get('risk_type', '').lower()

    recommendations = []
    for control in compensating_controls:
        if control.get('applicable_risk_type', '').lower() == risk_type:
            recommendations.append({
                'control_name': control.get('control_name'),
                'compliance_objective': control.get('compliance_objective'),
                'evidence_requirement': control.get('evidence_requirement'),
                'monitoring_dependency': control.get('monitoring_dependency'),
                'implementation_guidance': control.get('implementation_guidance')
            })

    return recommendations