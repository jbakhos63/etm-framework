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
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3)))


def run_once(separation, engine):
    center = engine.center

    e_pattern = ParticleFactory.create_electron()
    p_pattern = ParticleFactory.create_electron()

    electron = Identity(
        module_tag="ELECTRON",
        ancestry="neg",
        theta=0.0,
        delta_theta=0.05,
        position=(center[0] - separation // 2, center[1], center[2]),
    )
    electron.fundamental_particle = e_pattern

    positron = Identity(
        module_tag="POSITRON",
        ancestry="pos",
        theta=0.5,
        delta_theta=0.05,
        position=(center[0] + separation // 2, center[1], center[2]),
        is_antiparticle=True,
        antiparticle_of=electron.unique_id,
    )
    positron.fundamental_particle = p_pattern

    engine.identities.extend([electron, positron])

    pos_data = {"electron": [list(electron.position)], "positron": [list(positron.position)]}

    for _ in range(engine.config.max_ticks):
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
        pos_data["electron"].append(list(electron.position))
        pos_data["positron"].append(list(positron.position))
        if engine.tick % 50 == 0:
            print(f"Tick {engine.tick}/{engine.config.max_ticks}")
        if electron.position == positron.position:
            break

    return {"separation": separation, "ticks": engine.tick, "positions": pos_data}


def run_trial(max_ticks: int = 500, lattice_size=(51, 51, 51)):
    results = []
    # choose separations that fit comfortably inside the lattice
    max_sep = lattice_size[0] // 2
    separations = [max_sep // 3, max_sep // 2, max_sep]
    for sep in separations:
        config = ConfigurationFactory.validated_foundation_config("electric_force_2")
        config.max_ticks = max_ticks
        config.lattice_size = lattice_size
        engine = ETMEngine(config)
        for pos in engine.echo_fields:
            engine.recruiters[pos] = Recruiter(theta_recruiter=0.0, ancestry_recruiter="neutral")
        results.append(run_once(sep, engine))

    out_path = os.path.join(os.path.dirname(__file__), "electric_force_measurement_2_results.json")
    with open(out_path, "w") as f:
        json.dump({"runs": results}, f, indent=2)

    print(json.dumps({"runs": results}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extended electric force measurement")
    parser.add_argument("--ticks", type=int, default=500, help="Maximum ticks to run")
    parser.add_argument("--size", type=int, default=51, help="Cubic lattice dimension")
    args = parser.parse_args()
    run_trial(max_ticks=args.ticks, lattice_size=(args.size, args.size, args.size))
