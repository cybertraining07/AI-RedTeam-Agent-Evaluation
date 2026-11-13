from agents.redteam_agent import RedTeamAgent
from agents.evaluator import AgentEvaluator
from scenarios.attack_scenarios import ATTACK_SCENARIOS
from reports.report_generator import save_reports


def main():
    print("=" * 50)
    print("AI RED-TEAM AGENT EVALUATION FRAMEWORK")
    print("=" * 50)

    agent = RedTeamAgent()
    evaluator = AgentEvaluator()

    print("\nRunning cybersecurity scenarios...\n")

    results = evaluator.evaluate(agent, ATTACK_SCENARIOS)

    for result in results:
        print(
            f"Scenario {result['scenario_id']}: "
            f"{result['scenario_type']} | "
            f"Decision: {result['agent_decision']} | "
            f"Result: {'PASS' if result['passed'] else 'FAIL'}"
        )

    print("\nGenerating reports...\n")

    save_reports(results)

    print("\nEvaluation completed.")


if __name__ == "__main__":
    main()
