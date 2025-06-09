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
    config = ConfigurationFactory.validated_foundation_config("electron_positron_annihilation_2")
    config.max_ticks = max_ticks
    config.lattice_size = lattice_size
    engine = ETMEngine(config)

    # populate recruiters across lattice
    for pos in engine.echo_fields:
        engine.recruiters[pos] = Recruiter(theta_recruiter=0.0, ancestry_recruiter="neutral")

    center = engine.center
    electron = Identity(
        module_tag="ELECTRON",
        ancestry="neg",
        theta=0.0,
        delta_theta=0.05,
        position=(center[0] - 10, center[1], center[2]),
        velocity=(1, 0, 0),
    )
    electron.fundamental_particle = ParticleFactory.create_electron()

    positron = Identity(
        module_tag="POSITRON",
        ancestry="pos",
        theta=0.5,
        delta_theta=0.05,
        position=(center[0] + 10, center[1], center[2]),
        velocity=(-1, 0, 0),
        is_antiparticle=True,
        antiparticle_of=electron.unique_id,
    )
    positron.fundamental_particle = ParticleFactory.create_electron()

    engine.identities.extend([electron, positron])

    events = []
    for _ in range(config.max_ticks):
        engine.advance_tick()
        for event in engine.results_history[-1]["detection_events"]:
            if event["event_type"] == "particle_collision":
                events.append(event)
                break
        if events:
            break

    tick_data = engine.results_history[-1] if engine.results_history else {}
    summary = {
        "events": events,
        "history_length": len(engine.results_history),
        "energy_before": tick_data.get("energy_before"),
        "energy_after": tick_data.get("energy_after"),
        "energy_released_total": tick_data.get("energy_released_total"),
        "photon_energy_total": tick_data.get("photon_energy_total"),
    }

    result_path = os.path.join(os.path.dirname(__file__), "annihilation_2_results.json")
    with open(result_path, "w") as f:
        json.dump(summary, f, indent=2)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extended electron–positron annihilation trial")
    parser.add_argument("--ticks", type=int, default=500, help="Maximum ticks to run")
    parser.add_argument("--size", type=int, default=51, help="Cubic lattice dimension")
    args = parser.parse_args()
    run_trial(max_ticks=args.ticks, lattice_size=(args.size, args.size, args.size))
