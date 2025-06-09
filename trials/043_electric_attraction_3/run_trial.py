import json
import os
import sys
import argparse
import math

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity, Recruiter
from etm.particles import ParticleFactory


def distance(a, b):
    return math.sqrt(sum((a[i]-b[i])**2 for i in range(3)))


def run_trial(max_ticks: int = 500, lattice_size=(51, 51, 51)):
    config = ConfigurationFactory.validated_foundation_config("electric_attraction_3")
    config.max_ticks = max_ticks
    config.lattice_size = lattice_size
    engine = ETMEngine(config)

    for pos in engine.echo_fields:
        engine.recruiters[pos] = Recruiter(theta_recruiter=0.0, ancestry_recruiter="neutral")

    center = engine.center
    offset = lattice_size[0] // 4
    electron = Identity(
        module_tag="ELECTRON",
        ancestry="neg",
        theta=0.0,
        delta_theta=0.05,
        position=(center[0] - offset, center[1], center[2])
    )
    electron.fundamental_particle = ParticleFactory.create_electron()

    positron = Identity(
        module_tag="POSITRON",
        ancestry="pos",
        theta=0.5,
        delta_theta=0.05,
        position=(center[0] + offset, center[1], center[2]),
        is_antiparticle=True,
        antiparticle_of=electron.unique_id,
    )
    positron.fundamental_particle = ParticleFactory.create_electron()

    engine.identities.extend([electron, positron])

    positions = {
        "electron": [list(electron.position)],
        "positron": [list(positron.position)],
    }

    for _ in range(config.max_ticks):
        engine.echo_fields[electron.position].add_reinforcement(1.0)
        engine.echo_fields[positron.position].add_reinforcement(1.0)

        if engine.tick > 0:
            e_neighbors = engine.get_neighbors(*electron.position)
            next_e = min(e_neighbors, key=lambda p: distance(p, positron.position))
            electron.position = next_e

            p_neighbors = engine.get_neighbors(*positron.position)
            next_p = min(p_neighbors, key=lambda p: distance(p, electron.position))
            positron.position = next_p

        engine.advance_tick()
        positions["electron"].append(list(electron.position))
        positions["positron"].append(list(positron.position))
        if engine.tick % 50 == 0:
            print(f"Tick {engine.tick}/{config.max_ticks}")

    result = {"positions": positions, "ticks": config.max_ticks}
    out_path = os.path.join(os.path.dirname(__file__), "electric_attraction_3_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extended electron-positron attraction trial")
    parser.add_argument("--ticks", type=int, default=500, help="Maximum ticks to run")
    parser.add_argument("--size", type=int, default=51, help="Cubic lattice dimension")
    args = parser.parse_args()
    run_trial(max_ticks=args.ticks, lattice_size=(args.size, args.size, args.size))
