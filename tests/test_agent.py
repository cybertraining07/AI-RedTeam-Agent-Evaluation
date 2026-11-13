import json
from reports.report_generator import save_reports
from agents.redteam_agent import RedTeamAgent
from agents.evaluator import AgentEvaluator
from scenarios.attack_scenarios import ATTACK_SCENARIOS


def test_open_port_decision():
    agent = RedTeamAgent()
    result = agent.analyze_scenario({"type": "open_port", "risk": "high"})
    assert result == "investigate_service"


def test_suspicious_login_decision():
    agent = RedTeamAgent()
    result = agent.analyze_scenario(
        {"type": "suspicious_login", "risk": "critical"}
    )
    assert result == "escalate_alert"

def test_phishing_decision():
    agent = RedTeamAgent()
    result = agent.analyze_scenario({"type": "phishing", "risk": "medium"})
    assert result == "report_phishing"


def test_critical_unknown_activity():
    agent = RedTeamAgent()
    result = agent.analyze_scenario(
        {"type": "unknown_activity", "risk": "critical"}
    )
    assert result == "escalate_alert"


def test_evaluator_accuracy():
    agent = RedTeamAgent()
    evaluator = AgentEvaluator()

    results = evaluator.evaluate(agent, ATTACK_SCENARIOS)

    assert len(results) == 5
    assert evaluator.calculate_accuracy(results) == 100.0
def test_evaluator_detects_incorrect_decision():

    class IncorrectAgent:
        def analyze_scenario(self, scenario):
            return "ignore_security_alert"

    evaluator = AgentEvaluator()

    test_scenario = [
        {
            "id": 6,
            "type": "suspicious_login",
            "risk": "critical",
            "description": "Suspicious login activity detected.",
            "expected_action": "escalate_alert"
        }
    ]

    results = evaluator.evaluate(IncorrectAgent(), test_scenario)

    assert results[0]["passed"] is False
    assert results[0]["score"] == 0
    assert evaluator.calculate_accuracy(results) == 0.0
def test_evaluator_metrics_detect_false_positive():

    evaluator = AgentEvaluator()

    results = [
        {
            "scenario_id": 7,
            "scenario_type": "open_port",
            "agent_decision": "escalate_alert",
            "expected_action": "investigate_service",
            "score": 0,
            "passed": False
        }
    ]

    metrics = evaluator.calculate_metrics(results)

    assert metrics["accuracy"] == 0.0
    assert metrics["precision"] == 0.0
    assert metrics["recall"] == 0.0
    assert metrics["failure_rate"] == 100.0
def test_evaluator_metrics_detect_false_negative():

    evaluator = AgentEvaluator()

    results = [
        {
            "scenario_id": 8,
            "scenario_type": "suspicious_login",
            "agent_decision": "investigate_login",
            "expected_action": "escalate_alert",
            "score": 0,
            "passed": False
        }
    ]

    metrics = evaluator.calculate_metrics(results)

    assert metrics["accuracy"] == 0.0
    assert metrics["precision"] == 0.0
    assert metrics["recall"] == 0.0
    assert metrics["failure_rate"] == 100.0
def test_report_generator_creates_json_and_csv(tmp_path):

    results = [
        {
            "scenario_id": 1,
            "scenario_type": "open_port",
            "agent_decision": "investigate_service",
            "expected_action": "investigate_service",
            "score": 100,
            "passed": True
        }
    ]

    save_reports(results, output_dir=tmp_path)

    json_file = tmp_path / "evaluation_results.json"
    csv_file = tmp_path / "evaluation_results.csv"

    assert json_file.exists()
    assert csv_file.exists()

    with json_file.open(encoding="utf-8") as file:
        report = json.load(file)

    assert report["total_scenarios"] == 1
    assert report["accuracy"] == 100.0
def test_non_critical_suspicious_login():
    agent = RedTeamAgent()

    result = agent.analyze_scenario({
        "type": "suspicious_login",
        "risk": "high"
    })

    assert result == "investigate_login"


def test_unknown_scenario():
    agent = RedTeamAgent()

    result = agent.analyze_scenario({
        "type": "unknown_activity",
        "risk": "low"
    })

    assert result == "request_more_information"
def test_evaluator_handles_empty_results():
    evaluator = AgentEvaluator()

    assert evaluator.calculate_accuracy([]) == 0
