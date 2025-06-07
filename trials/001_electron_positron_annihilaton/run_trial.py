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
        position=(center[0]-2, center[1], center[2])
    )
    electron.fundamental_particle = ParticleFactory.create_electron()

    positron = Identity(
        module_tag="POSITRON",
        ancestry="pos",
        theta=0.5,
        delta_theta=0.05,
        position=(center[0]+2, center[1], center[2]),
        is_antiparticle=True,
        antiparticle_of=electron.unique_id
    )
    positron.fundamental_particle = ParticleFactory.create_electron()

    engine.identities.extend([electron, positron])

    events = []
    for _ in range(config.max_ticks):
        # Move both identities one step toward each other along x-axis before advancing
        if electron.position and positron.position and electron.position[0] < positron.position[0]:
            electron.position = (electron.position[0] + 1, electron.position[1], electron.position[2])
            positron.position = (positron.position[0] - 1, positron.position[1], positron.position[2])

        engine.advance_tick()

        # Check detection events for annihilation
        for event in engine.results_history[-1]["detection_events"]:
            if event["event_type"] == "particle_collision":
                events.append(event)
                break
        if events:
            break

    with open("annihilation_results.json", "w") as f:
        json.dump({"events": events, "history_length": len(engine.results_history)}, f, indent=2)

    print(json.dumps({"events": events, "history_length": len(engine.results_history)}, indent=2))

if __name__ == "__main__":
    run_trial()
