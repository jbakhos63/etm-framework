import json
import os
import sys
import argparse

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity
from etm.particles import ParticleFactory


def run_trial(max_ticks: int = 200, lattice_size=(51, 51, 51), scale: int = 1):
    config = ConfigurationFactory.validated_foundation_config("proton_resolution")
    config.max_ticks = max_ticks
    config.lattice_size = lattice_size
    engine = ETMEngine(config)

    center = engine.center
    # Use the validated enhanced proton pattern. There is currently no
    # generic ``create_proton`` helper, so we call ``create_enhanced_proton``
    # directly.
    p_pattern = ParticleFactory.create_enhanced_proton(scale=scale)
    proton = Identity(
        module_tag="PROTON",
        ancestry="pos",
        theta=0.0,
        delta_theta=0.05,
        position=center,
    )
    proton.fundamental_particle = p_pattern
    engine.identities.append(proton)

    data = {"scale": scale, "positions": [list(proton.position)]}
    for _ in range(config.max_ticks):
        engine.advance_tick()
        data["positions"].append(list(proton.position))
        if engine.tick % 50 == 0:
            print(f"Tick {engine.tick}/{config.max_ticks}")

    result_path = os.path.join(os.path.dirname(__file__), "proton_resolution_scan_5_results.json")
    with open(result_path, "w") as f:
        json.dump(data, f, indent=2)

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Proton resolution scan")
    parser.add_argument("--ticks", type=int, default=200, help="Maximum ticks to run")
    parser.add_argument("--size", type=int, default=51, help="Cubic lattice dimension")
    parser.add_argument("--scale", type=int, default=1, help="Proton pattern scale factor")
    args = parser.parse_args()
    run_trial(max_ticks=args.ticks, lattice_size=(args.size, args.size, args.size), scale=args.scale)
