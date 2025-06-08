import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity, Recruiter
from etm.particles import ParticleFactory


def run_trial():
    config = ConfigurationFactory.validated_foundation_config("moving_electron_echo")
    config.max_ticks = 10
    config.lattice_size = (21, 21, 21)
    engine = ETMEngine(config)

    # populate recruiters across lattice so inheritance works uniformly
    for pos in engine.echo_fields:
        engine.recruiters[pos] = Recruiter(theta_recruiter=0.0, ancestry_recruiter="neutral")

    center = engine.center
    electron_pattern = ParticleFactory.create_electron()
    electron = Identity(
        module_tag="ELECTRON",
        ancestry="neg",
        theta=0.0,
        delta_theta=0.05,
        position=(1, center[1], center[2]),
        velocity=(1, 0, 0),
    )
    electron.fundamental_particle = electron_pattern
    engine.identities.append(electron)

    data = {"positions": [], "echo_profile": []}

    for _ in range(config.max_ticks):
        # reinforce echo at electron position
        engine.echo_fields[electron.position].add_reinforcement(1.0)
        # advance the ETM engine (initial velocity applied only once)
        engine.advance_tick()

        pos = electron.position
        data["positions"].append(list(pos))
        above = (pos[0], min(pos[1] + 1, config.lattice_size[1] - 1), pos[2])
        below = (pos[0], max(pos[1] - 1, 0), pos[2])
        profile = {
            "tick": engine.tick,
            "above": engine.echo_fields[above].rho_local,
            "below": engine.echo_fields[below].rho_local,
        }
        data["echo_profile"].append(profile)

    result_path = os.path.join(os.path.dirname(__file__), "magnetic_field_results.json")
    with open(result_path, "w") as f:
        json.dump(data, f, indent=2)

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    run_trial()
