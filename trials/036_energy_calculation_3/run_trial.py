import json
import os
import sys
import argparse

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity, Recruiter
from etm.particles import ParticleFactory


def run_trial(max_ticks: int = 500, lattice_size=(51, 51, 51)):
    config = ConfigurationFactory.validated_foundation_config("energy_calculation_3")
    config.max_ticks = max_ticks
    config.lattice_size = lattice_size
    engine = ETMEngine(config)

    center = engine.center
    engine.recruiters[center] = Recruiter(theta_recruiter=0.0, ancestry_recruiter="neg")

    electron = Identity(
        module_tag="ELECTRON",
        ancestry="neg",
        theta=0.0,
        delta_theta=0.05,
        position=(center[0] + 1, center[1], center[2])
    )
    electron.fundamental_particle = ParticleFactory.create_electron()
    engine.identities.append(electron)

    energies = []
    positions = [list(electron.position)]
    for _ in range(config.max_ticks):
        energy = electron.calculate_particle_energy(center, engine.echo_fields, config)
        energies.append(round(energy, 4))
        engine.advance_tick()
        positions.append(list(electron.position))
        if engine.tick % 50 == 0:
            print(f"Tick {engine.tick}/{config.max_ticks}")

    result = {
        "energies_ev": energies,
        "positions": positions,
        "target_ground_state": config.target_hydrogen_ground_state,
    }

    out_path = os.path.join(os.path.dirname(__file__), "energy_calculation_3_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extended energy calculation trial")
    parser.add_argument("--ticks", type=int, default=500, help="Maximum ticks to run")
    parser.add_argument("--size", type=int, default=51, help="Cubic lattice dimension")
    args = parser.parse_args()
    run_trial(max_ticks=args.ticks, lattice_size=(args.size, args.size, args.size))
