import json
import os
import sys
import time
import argparse

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity, Recruiter
from etm.particles import ParticleFactory

def run_trial(max_ticks: int = 500, lattice_size=(51, 51, 51), sleep_time: float = 0.01):
    config = ConfigurationFactory.validated_foundation_config("electron_repulsion")
    config.max_ticks = max_ticks
    config.lattice_size = lattice_size
    engine = ETMEngine(config)

    for pos in engine.echo_fields:
        engine.recruiters[pos] = Recruiter(theta_recruiter=0.0, ancestry_recruiter="neutral")

    center = engine.center
    offset = lattice_size[0] // 2 - 1
    electron_a = Identity(
        module_tag="ELECTRON_A",
        ancestry="neg",
        theta=0.0,
        delta_theta=0.05,
        position=(center[0] - offset, center[1], center[2]),
        velocity=(1, 0, 0),
    )
    electron_a.fundamental_particle = ParticleFactory.create_electron()

    electron_b = Identity(
        module_tag="ELECTRON_B",
        ancestry="neg",
        theta=0.0,
        delta_theta=0.05,
        position=(center[0] + offset, center[1], center[2]),
        velocity=(-1, 0, 0),
    )
    electron_b.fundamental_particle = ParticleFactory.create_electron()

    engine.identities.extend([electron_a, electron_b])

    data = {
        "electron_a": [list(electron_a.position)],
        "electron_b": [list(electron_b.position)],
    }

    for _ in range(config.max_ticks):
        engine.echo_fields[electron_a.position].add_reinforcement(1.0)
        engine.echo_fields[electron_b.position].add_reinforcement(1.0)

        if engine.tick > 0:
            neigh_a = engine.get_neighbors(*electron_a.position)
            next_a = min(neigh_a, key=lambda p: engine.echo_fields[p].rho_local)
            electron_a.position = next_a

            neigh_b = engine.get_neighbors(*electron_b.position)
            next_b = min(neigh_b, key=lambda p: engine.echo_fields[p].rho_local)
            electron_b.position = next_b

        engine.advance_tick()
        data["electron_a"].append(list(electron_a.position))
        data["electron_b"].append(list(electron_b.position))
        if engine.tick % 50 == 0:
            print(f"Tick {engine.tick}/{config.max_ticks}")
        time.sleep(sleep_time)


    result_path = os.path.join(os.path.dirname(__file__), "electron_repulsion_2_results.json")
    with open(result_path, "w") as f:
        json.dump(data, f, indent=2)

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extended electron repulsion trial")
    parser.add_argument("--ticks", type=int, default=500, help="Maximum ticks to run")
    parser.add_argument("--size", type=int, default=51, help="Cubic lattice dimension")
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.01,
        help="Seconds to pause between ticks so long runs remain responsive",
    )
    args = parser.parse_args()
    run_trial(
        max_ticks=args.ticks,
        lattice_size=(args.size, args.size, args.size),
        sleep_time=args.sleep,
    )

