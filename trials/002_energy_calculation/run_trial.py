import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity, Recruiter
from etm.particles import ParticleFactory


def run_trial():
    config = ConfigurationFactory.validated_foundation_config("energy_calculation")
    config.max_ticks = 1
    config.lattice_size = (5, 5, 5)
    engine = ETMEngine(config)

    # Place recruiter at center
    center = engine.center
    engine.recruiters[center] = Recruiter(theta_recruiter=0.0, ancestry_recruiter="neg")

    # Place electron one step from center
    electron = Identity(
        module_tag="ELECTRON",
        ancestry="neg",
        theta=0.0,
        delta_theta=0.05,
        position=(center[0] + 1, center[1], center[2])
    )
    electron.fundamental_particle = ParticleFactory.create_electron()
    engine.identities.append(electron)

    # Calculate energy directly
    energy = electron.calculate_particle_energy(center, engine.echo_fields, config)

    result = {
        "electron_position": electron.position,
        "energy_ev": round(energy, 4),
        "target_ground_state": config.target_hydrogen_ground_state,
    }

    out_path = os.path.join(os.path.dirname(__file__), "energy_calculation_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run_trial()
