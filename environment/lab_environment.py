class CybersecurityEnvironment:

    def __init__(self):
        self.scenarios = [
            {
                "id": 1,
                "type": "open_port",
                "risk": "high",
                "description": "An unexpected network service is exposed."
            },
            {
                "id": 2,
                "type": "suspicious_login",
                "risk": "critical",
                "description": "Multiple failed login attempts detected."
            },
            {
                "id": 3,
                "type": "phishing",
                "risk": "medium",
                "description": "A suspicious email attachment was detected."
            }
        ]

    def get_scenarios(self):
        return self.scenarios
