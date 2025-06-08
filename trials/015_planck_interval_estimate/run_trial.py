import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.particles import ParticleFactory


EV_TO_J = 1.60218e-19
PLANCK_CONSTANT = 6.62607015e-34


def run_trial():
    config = ConfigurationFactory.validated_foundation_config("planck_interval")
    photon = ParticleFactory.create_hydrogen_photon()

    energy_j = photon.energy_content * EV_TO_J
    frequency_hz = energy_j / PLANCK_CONSTANT
    period_s = 1.0 / frequency_hz

    tick_duration_s = period_s / photon.core_timing_rate

    result = {
        "photon_energy_eV": photon.energy_content,
        "photon_frequency_hz": frequency_hz,
        "tick_duration_s": tick_duration_s,
    }

    out_path = os.path.join(os.path.dirname(__file__), "planck_interval_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run_trial()
