class RedTeamAgent:

    def __init__(self, name="RedTeam-Agent"):
        self.name = name

    def analyze_scenario(self, scenario):
        scenario_type = scenario.get("type", "").lower()
        risk = scenario.get("risk", "").lower()

        # Always prioritize critical security events
        if risk == "critical":
            return "escalate_alert"

        if scenario_type == "open_port":
            return "investigate_service"

        elif scenario_type == "suspicious_login":
            return "investigate_login"

        elif scenario_type == "phishing":
            return "report_phishing"

        return "request_more_information"
