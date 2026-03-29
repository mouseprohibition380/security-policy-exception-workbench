"""
Risk translation module for Policy Exception Workbench.

Translates security policy exceptions into technical and business risk summaries.
"""

from typing import Dict, Any
from .rules import RISK_TYPE_SUMMARIES, DEFAULT_TECHNICAL_SUMMARY, DEFAULT_BUSINESS_SUMMARY


def translate_exception(exception: Dict[str, Any]) -> Dict[str, str]:
    """
    Translate an exception into risk summaries.

    Args:
        exception: Exception dictionary with risk_type

    Returns:
        Dictionary with 'technical_risk' and 'business_risk' keys
    """
    risk_type = exception.get('risk_type', '').lower()

    summaries = RISK_TYPE_SUMMARIES.get(risk_type, {})

    technical_risk = summaries.get('technical', DEFAULT_TECHNICAL_SUMMARY)
    business_risk = summaries.get('business', DEFAULT_BUSINESS_SUMMARY)

    return {
        'technical_risk': technical_risk,
        'business_risk': business_risk
    }