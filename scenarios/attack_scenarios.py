ATTACK_SCENARIOS = [
    {
        "id": 1,
        "type": "open_port",
        "risk": "high",
        "description": "An unexpected network service is exposed.",
        "expected_action": "investigate_service"
    },
    {
        "id": 2,
        "type": "suspicious_login",
        "risk": "critical",
        "description": "Multiple failed login attempts detected.",
        "expected_action": "escalate_alert"    },
    {
        "id": 3,
        "type": "phishing",
        "risk": "medium",
        "description": "A suspicious email attachment was detected.",
        "expected_action": "report_phishing"
    },
    {
        "id": 4,
        "type": "unknown_activity",
        "risk": "critical",
        "description": "Unusual activity requires security review.",
        "expected_action": "escalate_alert"
    },
    {
        "id": 5,
        "type": "phishing",
        "risk": "critical",
        "description": "A confirmed phishing campaign is targeting privileged accounts.",
        "expected_action": "escalate_alert"
    }
]
