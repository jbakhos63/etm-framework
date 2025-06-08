# Trial 007 – Photon Emission Eligibility

This trial continues Stage 2 of the *ETM Simulation Research Plan* by
verifying that a hydrogen-energy photon can be emitted from an
electron timing pattern purely according to orbital compatibility rules.

## Objective
- Compute the coupling strength between a hydrogen photon and an electron.
- Determine whether the electron is capable of emitting the photon using ETM
  emission criteria.

## Method
1. **Particle Initialization** – Create a standard electron timing pattern and a
   hydrogen-energy photon via `ParticleFactory` utilities. No lattice is
   required for this coupling test.
2. **Emission Calculation** – Invoke
   `PhotonTimingPattern.calculate_orbital_interaction_strength` and
   `can_be_emitted_by` to evaluate emission eligibility.
3. **Output** – The resulting interaction strength and emission boolean are
   stored in `photon_emission_results.json`.

Run the procedure with `run_trial.py` in this directory.


## Results
Running `run_trial.py` produced the following output:

```json
{
  "interaction_strength": 0.405,
  "can_emit": true
}
```

The interaction strength exceeds the 0.2 emission threshold, indicating that a
hydrogen-energy photon can indeed be emitted by the electron timing pattern.
This confirms that ETM orbital compatibility metrics allow photon emission
without invoking external potential functions.
