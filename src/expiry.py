"""
Expiry management module for Policy Exception Workbench.

Handles expiry calculations and status flagging.
"""

from datetime import datetime, date
from typing import Dict, Any, Tuple


def calculate_expiry_status(exception: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate expiry status for an exception.

    Args:
        exception: Exception dictionary with expiry_date

    Returns:
        Dictionary with expiry information
    """
    expiry_date_str = exception.get('expiry_date')
    if not expiry_date_str:
        return {
            'days_until_expiry': None,
            'is_expired': False,
            'is_expiring_soon': False,
            'expiry_status': 'Unknown',
            'recommended_action': 'Review expiry date'
        }

    try:
        expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d').date()
        today = date.today()

        if expiry_date < today:
            days_until = (today - expiry_date).days
            return {
                'days_until_expiry': -days_until,  # Negative for expired
                'is_expired': True,
                'is_expiring_soon': False,
                'expiry_status': 'Expired',
                'recommended_action': 'Immediate review and remediation required'
            }
        else:
            days_until = (expiry_date - today).days
            is_expiring_soon = days_until <= 30
            status = 'Expiring Soon' if is_expiring_soon else 'Active'
            action = 'Schedule review before expiry' if is_expiring_soon else 'Monitor expiry date'

            return {
                'days_until_expiry': days_until,
                'is_expired': False,
                'is_expiring_soon': is_expiring_soon,
                'expiry_status': status,
                'recommended_action': action
            }
    except ValueError:
        return {
            'days_until_expiry': None,
            'is_expired': False,
            'is_expiring_soon': False,
            'expiry_status': 'Invalid Date',
            'recommended_action': 'Correct expiry date format'
        }