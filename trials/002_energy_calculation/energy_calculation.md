# Energy Calculation Validation

This trial isolates the energy calculation routine by placing a single electron near a recruiter.
It verifies that `Identity.calculate_particle_energy` returns a value close to the configured
target hydrogen ground state energy.

## Procedure

1. Initialize the ETM engine with the validated foundation configuration.
2. Create a recruiter at the lattice center and position an electron one step away.
3. Compute the electron's energy with `calculate_particle_energy`.
4. Store the resulting value in `energy_calculation_results.json`.

## Results

Running `run_trial.py` prints the calculated energy and writes a JSON summary.  An example output:

```json
{
  "electron_position": [3, 2, 2],
  "energy_ev": 38.3988,
  "target_ground_state": -13.6
}
```

The energy value can be compared against the theoretical target to evaluate calibration accuracy.
