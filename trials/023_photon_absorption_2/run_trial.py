import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.particles import ParticleFactory


def run_trial():
    # Create electron pattern and hydrogen photon pattern
    electron = ParticleFactory.create_electron()
    photon = ParticleFactory.create_hydrogen_photon()

    interaction_strength = photon.calculate_orbital_interaction_strength(electron)
    can_absorb = photon.can_be_absorbed_by(electron)

    result = {
        "interaction_strength": round(interaction_strength, 3),
        "can_absorb": bool(can_absorb)
    }

    out_path = os.path.join(os.path.dirname(__file__), "photon_absorption_2_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run_trial()
