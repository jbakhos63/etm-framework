import json
import os
import sys
import math

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from etm.config import ConfigurationFactory
from etm.core import ETMEngine, Identity, Recruiter
from etm.particles import ParticleFactory


def distance(a, b):
    return math.sqrt(sum((a[i]-b[i])**2 for i in range(3)))


def run_once(separation):
    config = ConfigurationFactory.validated_foundation_config("electric_force")
    config.lattice_size = (21, 21, 21)
    config.max_ticks = 20
    engine = ETMEngine(config)
    center = engine.center

    for pos in engine.echo_fields:
        engine.recruiters[pos] = Recruiter(theta_recruiter=0.0, ancestry_recruiter="neutral")

    e_pattern = ParticleFactory.create_electron()
    p_pattern = ParticleFactory.create_electron()

    electron = Identity(module_tag="ELECTRON", ancestry="neg", theta=0.0, delta_theta=0.05,
                        position=(center[0]-separation//2, center[1], center[2]))
    electron.fundamental_particle = e_pattern

    positron = Identity(module_tag="POSITRON", ancestry="pos", theta=0.5, delta_theta=0.05,
                        position=(center[0]+separation//2, center[1], center[2]),
                        is_antiparticle=True, antiparticle_of=electron.unique_id)
    positron.fundamental_particle = p_pattern

    engine.identities.extend([electron, positron])

    pos_data = {"electron": [electron.position], "positron": [positron.position]}

    for t in range(config.max_ticks):
        engine.echo_fields[electron.position].add_reinforcement(1.0)
        engine.echo_fields[positron.position].add_reinforcement(1.0)

        # choose neighboring node closest to the opposite particle
        e_neighbors = engine.get_neighbors(*electron.position)
        next_e = min(e_neighbors, key=lambda p: distance(p, positron.position))
        electron.position = next_e

        p_neighbors = engine.get_neighbors(*positron.position)
        next_p = min(p_neighbors, key=lambda p: distance(p, electron.position))
        positron.position = next_p

        engine.advance_phases()
        engine.apply_echo_decay()
        engine.apply_echo_inheritance()
        engine.tick += 1

        pos_data["electron"].append(electron.position)
        pos_data["positron"].append(positron.position)

        if electron.position == positron.position:
            break

    return {"separation": separation, "ticks": t+1, "positions": pos_data}


def run_trial():
    separations = [4, 6, 8]
    runs = [run_once(s) for s in separations]
    result_path = os.path.join(os.path.dirname(__file__), "electric_force_results.json")
    with open(result_path, "w") as f:
        json.dump({"runs": runs}, f, indent=2)
    print(json.dumps({"runs": runs}, indent=2))


if __name__ == "__main__":
    run_trial()
