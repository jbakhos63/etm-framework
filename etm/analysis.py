"""Basic analysis utilities for ETM trial results."""

import os
import json
from typing import Dict, Any

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

RESULT_FILES = {
    "annihilation": os.path.join(
        ROOT_DIR,
        "trials",
        "001_electron_positron_annihilaton",
        "annihilation_results.json",
    ),
    "energy_calculation": os.path.join(
        ROOT_DIR,
        "trials",
        "002_energy_calculation",
        "energy_calculation_results.json",
    ),
    "photon_propagation": os.path.join(
        ROOT_DIR,
        "trials",
        "003_photon_propagation",
        "photon_propagation_results.json",
    ),
}


def load_results() -> Dict[str, Any]:
    """Load all available trial result files."""
    data = {}
    for name, path in RESULT_FILES.items():
        if os.path.exists(path):
            with open(path) as f:
                data[name] = json.load(f)
        else:
            data[name] = {}
    return data


def compute_metrics(results: Dict[str, Any]) -> Dict[str, float]:
    """Compute simple diagnostic metrics from trial data."""
    metrics = {}
    energy_data = results.get("energy_calculation", {})
    target = energy_data.get("target_ground_state")
    if target is not None:
        metrics["energy_error"] = abs(energy_data.get("energy_ev", 0.0) - abs(target))
    photon_path = results.get("photon_propagation", {})
    metrics["photon_steps"] = max(len(photon_path.get("positions", [])) - 1, 0)
    return metrics


def summarize() -> Dict[str, Any]:
    results = load_results()
    metrics = compute_metrics(results)
    summary = {"metrics": metrics, "results": results}
    print(json.dumps(summary, indent=2))
    return summary


if __name__ == "__main__":
    summarize()
