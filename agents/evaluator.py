class AgentEvaluator:

    def evaluate(self, agent, scenarios):
        results = []

        for scenario in scenarios:
            decision = agent.analyze_scenario(scenario)
            expected = scenario["expected_action"]
            passed = decision == expected

            results.append({
                "scenario_id": scenario["id"],
                "scenario_type": scenario["type"],
                "agent_decision": decision,
                "expected_action": expected,
                "score": 100 if passed else 0,
                "passed": passed
            })

        return results

    def calculate_accuracy(self, results):
        if not results:
            return 0

        passed = sum(r["passed"] for r in results)
        return round((passed / len(results)) * 100, 2)

    def calculate_metrics(self, results):
        true_positive = sum(
            1 for r in results
            if r["agent_decision"] == "escalate_alert"
            and r["expected_action"] == "escalate_alert"
        )

        false_positive = sum(
            1 for r in results
            if r["agent_decision"] == "escalate_alert"
            and r["expected_action"] != "escalate_alert"
        )

        false_negative = sum(
            1 for r in results
            if r["agent_decision"] != "escalate_alert"
            and r["expected_action"] == "escalate_alert"
        )

        precision = (
            true_positive / (true_positive + false_positive)
            if true_positive + false_positive else 0
        )

        recall = (
            true_positive / (true_positive + false_negative)
            if true_positive + false_negative else 0
        )

        accuracy = self.calculate_accuracy(results)

        failure_rate = (
            100 - accuracy if results else 0
        )

        return {
            "accuracy": accuracy,
            "precision": round(precision * 100, 2),
            "recall": round(recall * 100, 2),
            "failure_rate": round(failure_rate, 2)
        }
