import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity
from etm.particles import ParticleFactory
import argparse


def run_trial(max_ticks: int = 500, lattice_size=(51, 51, 51)):
    config = ConfigurationFactory.validated_foundation_config("photon_propagation")
    config.max_ticks = max_ticks
    config.lattice_size = lattice_size
    engine = ETMEngine(config)

    center = engine.center
    photon_pattern = ParticleFactory.create_visible_photon()
    photon = Identity(
        module_tag="PHOTON",
        ancestry="photon",
        theta=0.0,
        delta_theta=photon_pattern.core_timing_rate,
        position=center,
        velocity=(1, 0, 0),
    )
    photon.fundamental_particle = photon_pattern
    engine.identities.append(photon)

    positions = [list(photon.position)]
    for _ in range(config.max_ticks):
        engine.advance_tick()
        positions.append(list(photon.position))
        if engine.tick % 50 == 0:
            print(f"Tick {engine.tick}/{config.max_ticks}")

    result = {"positions": positions}
    out_path = os.path.join(os.path.dirname(__file__), "photon_propagation_3_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extended photon propagation trial")
    parser.add_argument("--ticks", type=int, default=500, help="Maximum ticks to run")
    parser.add_argument("--size", type=int, default=51, help="Cubic lattice dimension")
    args = parser.parse_args()
    run_trial(max_ticks=args.ticks, lattice_size=(args.size, args.size, args.size))
