import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.particles import ParticleFactory

EV_TO_J = 1.60218e-19
PLANCK_CONSTANT = 6.62607015e-34
SPEED_OF_LIGHT = 299_792_458.0


def run_trial():
    config = ConfigurationFactory.validated_foundation_config("planck_length_2")
    photon = ParticleFactory.create_hydrogen_photon()

    energy_j = photon.energy_content * EV_TO_J
    frequency_hz = energy_j / PLANCK_CONSTANT
    period_s = 1.0 / frequency_hz
    tick_duration_s = period_s / photon.core_timing_rate

    # Step length derived from one lattice step per tick
    step_length_m = SPEED_OF_LIGHT * tick_duration_s

    result = {
        "photon_frequency_hz": frequency_hz,
        "tick_duration_s": tick_duration_s,
        "step_length_m": step_length_m,
    }

    out_path = os.path.join(os.path.dirname(__file__), "planck_length_2_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run_trial()
