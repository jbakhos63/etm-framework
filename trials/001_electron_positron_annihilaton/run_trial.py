import json
import os
import sys

# Ensure repository root is on the path when executed from this folder
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity, Recruiter
from etm.particles import ParticleFactory


def run_trial():
    # Configure engine
    config = ConfigurationFactory.validated_foundation_config("electron_positron_annihilation")
    config.max_ticks = 6
    config.lattice_size = (7, 7, 7)
    engine = ETMEngine(config)

    # Create recruiters across lattice so evaluation functions work
    for pos in engine.echo_fields:
        engine.recruiters[pos] = Recruiter(theta_recruiter=0.0, ancestry_recruiter="neutral")

    center = engine.center
    electron = Identity(
        module_tag="ELECTRON",
        ancestry="neg",
        theta=0.0,
        delta_theta=0.05,
        position=(center[0]-2, center[1], center[2]),
        velocity=(1, 0, 0)
    )
    electron.fundamental_particle = ParticleFactory.create_electron()
    positron = Identity(
        module_tag="POSITRON",
        ancestry="pos",
        theta=0.5,
        delta_theta=0.05,
        position=(center[0]+2, center[1], center[2]),
        velocity=(-1, 0, 0),
        is_antiparticle=True,
        antiparticle_of=electron.unique_id
    )
    positron.fundamental_particle = ParticleFactory.create_electron()
    engine.identities.extend([electron, positron])

    events = []
    for _ in range(config.max_ticks):
        engine.advance_tick()

        # Check detection events for annihilation
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

    results_path = os.path.join(os.path.dirname(__file__), "annihilation_results.json")
    with open(results_path, "w") as f:
        json.dump(summary, f, indent=2)

    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    run_trial()
