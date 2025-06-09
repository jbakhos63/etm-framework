import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity
from etm.particles import ParticleFactory


def run_trial():
    config = ConfigurationFactory.validated_foundation_config("electron_absorption_energy_3")
    config.max_ticks = 1
    config.lattice_size = (51, 51, 51)
    engine = ETMEngine(config)

    center = engine.center
    electron_pattern = ParticleFactory.create_electron()
    electron = Identity(
        module_tag="ELECTRON",
        ancestry="electron",
        theta=0.0,
        delta_theta=0.1,
        position=center,
    )
    electron.fundamental_particle = electron_pattern

    initial_energy = electron.calculate_particle_energy(center, engine.echo_fields, config)

    photon = ParticleFactory.create_hydrogen_photon()
    assert photon.can_be_absorbed_by(electron_pattern)

    electron.delta_theta += photon.energy_content / config.kinetic_scale_factor
    final_energy = electron.calculate_particle_energy(center, engine.echo_fields, config)
    energy_change = final_energy - initial_energy

    result = {
        "initial_energy": round(initial_energy, 3),
        "final_energy": round(final_energy, 3),
        "energy_change": round(energy_change, 3),
        "photon_energy": photon.energy_content,
    }

    out_path = os.path.join(os.path.dirname(__file__), "electron_absorption_energy_3_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run_trial()
