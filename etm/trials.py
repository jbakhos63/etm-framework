"""Utilities to run ETM validation trials.

This module provides a convenience wrapper for executing the published
validation trials contained in the top-level `trials` directory.
"""

import os
import sys
import subprocess
import json
from typing import Dict

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

TRIAL_SCRIPTS = {
    "annihilation": "trials/001_electron_positron_annihilaton/run_trial.py",
    "energy_calculation": "trials/002_energy_calculation/run_trial.py",
    "photon_propagation": "trials/003_photon_propagation/run_trial.py",
}


def _run_script(rel_path: str) -> Dict:
    """Execute a trial script and return its JSON output."""
    path = os.path.join(ROOT_DIR, rel_path)
    proc = subprocess.run([sys.executable, path], capture_output=True, text=True)
    output = proc.stdout.strip()
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return {}


def run_all() -> Dict[str, Dict]:
    """Run all validation trials and return a dictionary of results."""
    return {name: _run_script(script) for name, script in TRIAL_SCRIPTS.items()}


if __name__ == "__main__":
    results = run_all()
    print(json.dumps(results, indent=2))
