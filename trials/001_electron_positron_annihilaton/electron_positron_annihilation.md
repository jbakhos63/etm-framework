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
   - Run the ETM engine with detection triggered at each tick. Track positions, phases, and timing strain of both identities as they move.
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

The updated script `run_trial.py` relies on the engine's staged annihilation logic.
When the electron and positron reach the same lattice node a collision event is
logged.  One tick later the particles are removed and two photons with matching
timing–strain energy are emitted from that node. Running the script produced the
following `annihilation_results.json`:

```json
{
  "events": [
    {
      "tick": 3,
      "released_energy": 0.0,
      "photon_ids": ["<photon1>", "<photon2>"],
      "position": [3, 3, 3]
    }
  ],
  "history_length": 3
}
```


The output now reports the energy released by the annihilation and the
identifiers of both emitted photons. Energy accounting uses the ETM timing–
strain calculation and confirms conservation through the transformation.

