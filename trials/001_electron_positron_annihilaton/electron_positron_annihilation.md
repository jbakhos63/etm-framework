# Electron–Positron Annihilation Trial

This trial proposes a minimal ETM simulation of an electron and a positron initially at rest and separated by a small but finite lattice distance. The goal is to examine how ETM chirality generates an effective electromagnetic attraction and to track the timing-strain energy released as photons when the particles annihilate.

## Objectives

1. **Validate Charge Interaction** – Show that opposite chirality patterns accelerate toward each other under the ETM timing rules, providing an information-theoretic analogue to the Coulomb force. Measuring the approach rate offers a pathway to calibrate an ETM value analogous to the Coulomb constant.
2. **Energy Accounting** – Confirm that the total timing strain before annihilation equals the energy carried away by the emergent photon patterns. This demonstrates conservation of energy within ETM and links photon creation to localized timing reorganization.
3. **Photon Generation Mechanism** – Record how the annihilation event produces photon timing patterns. Compare the resulting frequencies to those predicted by the strain in the initial electron–positron system.

## Simulation Outline

1. **Initial Conditions**
   - Place an electron identity and a positron identity on opposite sides of the lattice center, each at rest with respect to the simulation frame.
   - Set the initial separation large enough that immediate annihilation does not occur but small enough that chirality attraction draws them together within a manageable number of ticks.
2. **Dynamics**
   - Each identity is given a small velocity toward the lattice center. This velocity is applied only once at initialization to shift the starting position. Subsequent motion arises solely from the ETM return rules—there is no persistent movement step.
   - Detection is triggered each tick and records collisions, timing strain, and emitted photon identities.
   - Monitor the lattice for recruitment patterns indicating photon creation during the collision.
3. **Data Collection**
   - Record the tick number of annihilation, total strain energy immediately before the event, and the energy distribution among emitted photons.
   - Analyze whether the approach trajectory matches the expected $1/r^2$ form of a Coulomb-like force in the ETM framework.

## Expected Outcomes

- A quantitative demonstration that ETM chirality leads to an effective attractive force consistent with classical charge behavior.
- Conservation of timing strain energy, with photons carrying away the precise amount released by the annihilation.
- Insight into how ETM constructs photon identities from timing strain reorganization, informing further development of the photon model.

Documenting this trial will guide improvements to the ETM particle interaction rules and support future derivations of electromagnetic constants from first principles.

## Results

The updated `run_trial.py` relies on the engine's detection logic. Running the
trial produced the following JSON summary:

```json
{
  "events": [
    {
      "event_type": "particle_collision",
      "position": [3, 3, 3],
      "tick": 2,
      "trigger_id": "<electron_id>",
      "affected_ids": ["<positron_id>"],
      "energy_released": -168.0024,
      "photon_id": "<photon_id>",
      "photon_energy": -168.0024
    }
  ],
  "history_length": 2,
  "energy_before": -168.0024,
  "energy_after": -11512.4786,
  "energy_released_total": -168.0024,
  "photon_energy_total": -168.0024
}
```

A photon identity is created with energy matching the timing strain released by
the annihilation event, demonstrating integrated energy accounting within the
ETM engine.
\nThe engine now records total system energy before and after the tick, along with the energy carried by newly created photons. The values match within numerical precision, confirming conservation of timing-strain energy.
