# Trial 018 – Extended Electron–Positron Annihilation

This experiment repeats Trial 001 on a much larger lattice for hundreds of ticks. The goal is to gather long‑duration data useful for deriving ETM analogues of the Coulomb constant and verifying energy conservation under extended conditions.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("electron_positron_annihilation_2")`
- **Lattice**: Default `51×51×51` (adjustable via `--size` argument)
- **Ticks**: Default `500` (adjustable via `--ticks` argument)
- **Setup**: Electron and positron start far apart with a small initial velocity toward each other. That velocity is applied only on the first tick; all subsequent motion is governed solely by ETM return logic.
- **Output**: Energy metrics and any collision events are written to `annihilation_2_results.json`.

To run the simulation in the background on Windows while keeping the system responsive, execute:

```
start /B /LOW python run_trial.py --ticks 500 --size 51
```

This command launches the Python process with low priority so other tasks remain usable.

## Results
Run the script and place the JSON output here.

### Latest Results (2025 Run)
See annihilation_2_results.json for output.
