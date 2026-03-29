"""
Rules and constants for Policy Exception Workbench.
"""

from typing import Dict


# Risk type mappings for translation
RISK_TYPE_SUMMARIES: Dict[str, Dict[str, str]] = {
    'mfa': {
        'technical': 'Weakens authentication mechanisms, increasing risk of account takeover through credential theft or brute force attacks. Reduces visibility into authentication failures and successful unauthorized access.',
        'business': 'Exposes sensitive business data and systems to unauthorized access, potentially leading to data breaches, compliance violations, and reputational damage.'
    },
    'privileged access': {
        'technical': 'Elevates risk of unauthorized system modifications, data exfiltration, and lateral movement within the network. Challenges governance and auditability of administrative actions.',
        'business': 'Increases potential for insider threats, operational disruptions, and regulatory non-compliance due to uncontrolled privileged operations.'
    },
    'logging': {
        'technical': 'Reduces ability to detect security incidents, investigate breaches, and maintain audit trails. Impacts incident response effectiveness and forensic analysis capabilities.',
        'business': 'Heightens risk of undetected security incidents, delayed breach discovery, and inadequate compliance evidence for audits and regulatory requirements.'
    },
    'network segmentation': {
        'technical': 'Compromises network isolation, enabling potential lateral movement and unauthorized access between network segments. Weakens defense-in-depth security posture.',
        'business': 'Increases exposure to network-based attacks, data exfiltration risks, and potential for widespread system compromise affecting multiple business units.'
    },
    'vendor access': {
        'technical': 'Introduces third-party access vectors that may bypass internal security controls. Creates dependencies on vendor security practices and monitoring capabilities.',
        'business': 'Exposes business operations to vendor-related security incidents, supply chain attacks, and potential data leakage through third-party systems.'
    }
}


# Default summaries for unknown risk types
DEFAULT_TECHNICAL_SUMMARY = 'Introduces security control gaps that may enable unauthorized access, data exposure, or system compromise.'
DEFAULT_BUSINESS_SUMMARY = 'Creates operational and compliance risks that could impact business continuity, regulatory compliance, and stakeholder trust.'