import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity, Recruiter
from etm.particles import ParticleFactory


def run_trial():
    config = ConfigurationFactory.validated_foundation_config("photon_speed_baseline")
    config.max_ticks = 10
    config.lattice_size = (21, 21, 21)
    engine = ETMEngine(config)

    center = engine.center
    # Establish a constant echo gradient along the x-axis so motion arises from ETM timing logic
    for pos in engine.echo_fields:
        engine.recruiters[pos] = Recruiter(theta_recruiter=0.0, ancestry_recruiter="neutral")
        engine.echo_fields[pos].rho_local = pos[0]

    photon_pattern = ParticleFactory.create_visible_photon()
    photon = Identity(
        module_tag="PHOTON",
        ancestry="photon",
        theta=0.0,
        delta_theta=photon_pattern.core_timing_rate,
        position=(1, center[1], center[2])
    )
    photon.fundamental_particle = photon_pattern
    engine.identities.append(photon)

    positions = [photon.position]
    for _ in range(config.max_ticks):
        neighbors = engine.get_neighbors(*photon.position)
        next_pos = max(neighbors, key=lambda p: engine.echo_fields[p].rho_local)
        photon.position = next_pos

        engine.advance_phases()
        engine.apply_echo_decay()
        engine.apply_echo_inheritance()
        engine.tick += 1
        positions.append(photon.position)

    result = {
        "positions": positions,
        "ticks": config.max_ticks
    }
    out_path = os.path.join(os.path.dirname(__file__), "photon_speed_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run_trial()
