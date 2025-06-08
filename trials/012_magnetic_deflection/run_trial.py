import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity, Recruiter
from etm.particles import ParticleFactory


def run_trial():
    config = ConfigurationFactory.validated_foundation_config("magnetic_deflection")
    config.max_ticks = 10
    config.lattice_size = (21, 21, 21)
    engine = ETMEngine(config)

    # populate recruiters across lattice
    for pos in engine.echo_fields:
        engine.recruiters[pos] = Recruiter(theta_recruiter=0.0, ancestry_recruiter="neutral")

    center = engine.center
    e_pattern = ParticleFactory.create_electron()

    electron_a = Identity(
        module_tag="ELECTRON_A",
        ancestry="neg",
        theta=0.0,
        delta_theta=0.05,
        position=(1, center[1], center[2]),
        velocity=(1, 0, 0),
    )
    electron_a.fundamental_particle = e_pattern

    electron_b = Identity(
        module_tag="ELECTRON_B",
        ancestry="neg",
        theta=0.0,
        delta_theta=0.05,
        position=(1, center[1] + 2, center[2]),
    )
    electron_b.fundamental_particle = ParticleFactory.create_electron()

    engine.identities.extend([electron_a, electron_b])

    data = {"electron_a": [list(electron_a.position)], "electron_b": [list(electron_b.position)]}

    for _ in range(config.max_ticks):
        engine.echo_fields[electron_a.position].add_reinforcement(1.0)
        engine.echo_fields[electron_b.position].add_reinforcement(1.0)

        # move electron_b toward neighbour with strongest echo from electron_a
        neighbors = engine.get_neighbors(*electron_b.position)
        next_b = max(neighbors, key=lambda p: engine.echo_fields[p].rho_local)
        electron_b.position = next_b

        engine.advance_tick()

        data["electron_a"].append(list(electron_a.position))
        data["electron_b"].append(list(electron_b.position))

    result_path = os.path.join(os.path.dirname(__file__), "magnetic_deflection_results.json")
    with open(result_path, "w") as f:
        json.dump(data, f, indent=2)

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    run_trial()
