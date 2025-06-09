import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)


def estimate_coulomb_constant(results_path):
    with open(results_path) as f:
        data = json.load(f)
    vals = []
    for run in data["runs"]:
        s = run["separation"]
        t = run["ticks"]
        vals.append(s / (t ** 2))
    return sum(vals) / len(vals)


def run_trial():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    electric_path = os.path.join(base_dir, "027_electric_force_measurement_2", "electric_force_measurement_2_results.json")
    coulomb_constant = estimate_coulomb_constant(electric_path)

    c_etm = 1.0  # photon moves one step per tick
    hbar_etm = 13.6  # from electron absorption energy

    alpha_etm = coulomb_constant / (hbar_etm * c_etm)

    result = {
        "coulomb_constant": round(coulomb_constant, 3),
        "hbar_etm": hbar_etm,
        "c_etm": c_etm,
        "alpha_etm": round(alpha_etm, 4),
    }

    out_path = os.path.join(os.path.dirname(__file__), "fine_structure_estimate_2_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run_trial()
