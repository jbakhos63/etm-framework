import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.particles import ParticleFactory


def run_trial():
    electron = ParticleFactory.create_electron()
    photon = ParticleFactory.create_hydrogen_photon()

    interaction_strength = photon.calculate_orbital_interaction_strength(electron)
    can_emit = photon.can_be_emitted_by(electron)

    result = {
        "interaction_strength": round(interaction_strength, 3),
        "can_emit": bool(can_emit)
    }

    out_path = os.path.join(os.path.dirname(__file__), "photon_emission_3_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run_trial()
