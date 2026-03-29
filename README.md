# Policy Exception Workbench

A defensive cybersecurity governance tool that transforms security policy exceptions into actionable risk insights, compensating controls, and compliance evidence requirements.

## Overview

The Policy Exception Workbench helps security teams and business stakeholders understand and manage the risks associated with security policy exceptions. By translating technical exceptions into business impact assessments and recommending specific compensating controls, the tool bridges the gap between security requirements and operational needs.

## Features

- **Risk Translation**: Converts policy exceptions into technical and business risk summaries
- **Compensating Control Design**: Recommends specific controls based on exception risk types
- **Evidence Requirements**: Generates checklists for compliance evidence collection
- **Expiry Management**: Tracks exception lifecycles with automated expiry alerts
- **Executive Reporting**: Provides both detailed exception reports and executive summaries
- **Markdown Output**: Generates professional reports suitable for documentation and audits

## Example Exception Workflow

1. **Input**: Security team identifies need for MFA bypass on legacy system
2. **Translation**: Tool generates technical risk (authentication weakening) and business risk (data breach exposure)
3. **Controls**: Recommends enhanced monitoring, session timeouts, and access reviews
4. **Evidence**: Creates checklist for SIEM logs, configuration proofs, and review reports
5. **Monitoring**: Identifies dependencies on real-time alerting and session monitoring
6. **Expiry**: Sets review reminders and tracks exception lifecycle

## Sample Data Structure

### Exceptions CSV
```csv
exception_id,policy_id,exception_title,business_justification,impacted_system,risk_type,requested_by,owner,existing_controls,expiry_date,review_frequency_days,status
EX001,POL-SEC-001,Temporary MFA Bypass,Legacy system compatibility,CRM System,MFA,John Doe,Jane Smith,Password auth,2026-06-15,90,active
```

### Compensating Controls CSV
```csv
control_name,applicable_risk_type,compliance_objective,evidence_requirement,monitoring_dependency,implementation_guidance
Enhanced Monitoring,MFA,Increase authentication visibility,SIEM logs of login attempts,Real-time alerting,Implement additional authentication logging
```

## How to Run

### Prerequisites
- Python 3.6+
- No external dependencies required

### Execution
```bash
python main.py
```

The tool will:
1. Load exception data from `data/exceptions.csv`
2. Process each exception through risk translation and control design
3. Generate individual Markdown reports in `output/`
4. Create a summary report at `output/exception_summary.md`
5. Display terminal summary of exception status

## Sample Output

### Terminal Summary
```
Policy Exception Workbench Summary
========================================
Total Exceptions: 6
Active: 5
Expired: 1
Expiring Soon (≤30 days): 1

Reports generated in output/ directory
```

### Individual Exception Report (EX001.md)
```markdown
# Security Policy Exception Report

## Exception Details
**Exception ID:** EX001
**Policy ID:** POL-SEC-001
**Title:** Temporary MFA Bypass for Legacy System

## Risk Analysis
### Technical Risk Summary
Weakens authentication mechanisms, increasing risk of account takeover...

### Business Risk Summary
Exposes sensitive business data and systems to unauthorized access...

## Compensating Controls
### 1. Enhanced Monitoring
**Compliance Objective:** Increase visibility into authentication attempts
**Implementation Guidance:** Implement additional logging for all authentication events...

## Evidence Requirements
- [ ] SIEM logs of failed login attempts
- [ ] Configuration showing max session time of 30 minutes
```

## Roadmap

- [ ] Web-based interface for exception management
- [ ] Integration with SIEM systems for automated evidence collection
- [ ] Risk scoring algorithms for exception prioritization
- [ ] Automated compliance report generation
- [ ] Integration with ticketing systems for workflow management

## Ethical and Operational Use Note

This tool is designed to enhance security governance by providing transparency into policy exceptions and ensuring appropriate compensating controls are implemented. It should be used as part of a comprehensive security program that includes:

- Regular security training and awareness
- Independent security reviews and audits
- Incident response planning
- Continuous monitoring and improvement

The tool does not replace human judgment or regulatory requirements. All exceptions should be approved through appropriate governance processes and regularly reviewed for continued necessity and effectiveness.

## License

[Add appropriate license information]