import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity
from etm.particles import ParticleFactory


def run_trial():
    config = ConfigurationFactory.validated_foundation_config("photon_propagation")
    config.max_ticks = 4
    config.lattice_size = (7, 7, 7)
    engine = ETMEngine(config)

    center = engine.center
    photon_pattern = ParticleFactory.create_visible_photon()
    photon = Identity(
        module_tag="PHOTON",
        ancestry="photon",
        theta=0.0,
        delta_theta=photon_pattern.core_timing_rate,
        position=center,
        velocity=(1, 0, 0)
    )
    photon.fundamental_particle = photon_pattern
    engine.identities.append(photon)

    positions = [photon.position]
    for _ in range(config.max_ticks):
        engine.advance_tick()
        positions.append(photon.position)

    result = {"positions": positions}
    out_path = os.path.join(os.path.dirname(__file__), "photon_propagation_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run_trial()
