# AI Red-Team Agent Evaluation Framework

## Project Overview

This project is a Python-based cybersecurity prototype designed to simulate security scenarios and evaluate how a rule-based red-team agent responds to them.

The framework evaluates decisions involving suspicious logins, exposed network services, phishing attempts, and critical security events.

## Project Objectives

- Simulate common cybersecurity scenarios.
- Implement a rule-based security analysis agent.
- Evaluate agent decisions against expected actions.
- Calculate accuracy, precision, recall, and failure rate.
- Generate JSON and CSV evaluation reports.
- Run automated tests and measure code coverage.

## Project Architecture

```text
AI-RedTeam-Agent-Evaluation/
├── agents/
│   ├── redteam_agent.py
│   └── evaluator.py
├── environment/
│   └── lab_environment.py
├── reports/
│   └── report_generator.py
├── scenarios/
│   └── attack_scenarios.py
├── tests/
│   └── test_agent.py
├── main.py
├── requirements.txt
└── README.md
