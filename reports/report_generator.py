import csv
import json
from pathlib import Path
from datetime import datetime, timezone

from agents.evaluator import AgentEvaluator


def save_reports(results, output_dir="reports"):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    total = len(results)
    passed = sum(1 for result in results if result["passed"])
    failed = total - passed

    evaluator = AgentEvaluator()
    metrics = evaluator.calculate_metrics(results)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_scenarios": total,
        "passed": passed,
        "failed": failed,
        "accuracy": metrics["accuracy"],
        "precision": metrics["precision"],
        "recall": metrics["recall"],
        "failure_rate": metrics["failure_rate"],
        "results": results
    }

    json_file = output_path / "evaluation_results.json"

    with json_file.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    csv_file = output_path / "evaluation_results.csv"

    fields = [
        "scenario_id",
        "scenario_type",
        "agent_decision",
        "expected_action",
        "score",
        "passed"
    ]

    with csv_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    print("Evaluation report generated successfully.")
    print(f"Total scenarios: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Accuracy: {metrics['accuracy']}%")
    print(f"Precision: {metrics['precision']}%")
    print(f"Recall: {metrics['recall']}%")
    print(f"Failure rate: {metrics['failure_rate']}%")
    print(f"JSON report: {json_file}")
    print(f"CSV report: {csv_file}")
