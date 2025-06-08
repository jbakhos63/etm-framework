import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
    electric_path = os.path.join(base_dir, "010_electric_force_measurement", "electric_force_results.json")
    coulomb_constant = estimate_coulomb_constant(electric_path)

    # Photon speed from Trial 004 is one lattice step per tick
    c_etm = 1.0

    # Planck constant analogue from Trial 008: photon energy 13.6 for frequency 1/tick
    hbar_etm = 13.6

    alpha_etm = coulomb_constant / (hbar_etm * c_etm)

    result = {
        "coulomb_constant": coulomb_constant,
        "hbar_etm": hbar_etm,
        "c_etm": c_etm,
        "alpha_etm": alpha_etm
    }

    out_path = os.path.join(os.path.dirname(__file__), "fine_structure_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run_trial()
