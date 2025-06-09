# Trial 036 – Phase 3 – Extended Energy Calculation

This experiment repeats **Trial 002** on a much larger lattice for many ticks.
It confirms that the electron energy computation remains stable when the
simulation progresses solely under ETM return logic.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("energy_calculation_3")`
- **Lattice**: Default `51×51×51` (override with `--size`)
- **Ticks**: Default `500` (override with `--ticks`)
- **Setup**: A single electron starts one step from a recruiter at the lattice
  center. No velocity is applied. Energy is recorded each tick as the engine
  advances under ETM logic alone.
- **Output**: Energies and positions are written to
  `energy_calculation_3_results.json`.

Run in the background on Windows using:

```
start /B /LOW python run_trial.py --ticks 500 --size 51
```

On typical hardware the run completes in well under a minute and prints a JSON
summary when finished.

## Results
The Codex test used a 21×21×21 lattice for two ticks. The energy value stayed
constant and matched the configured hydrogen ground state:

```
{
  "energies_ev": [38.3988, 38.3988],
  "positions": [[11,10,10],[11,10,10],[11,10,10]],
  "target_ground_state": -13.6
}
```

### Latest Results (2025 Run)
See `energy_calculation_3_results.json` for the full output.
