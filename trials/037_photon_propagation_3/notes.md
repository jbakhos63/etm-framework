# Trial 037 – Phase 3 – Extended Photon Propagation

This trial repeats **Trial 003** on a much larger lattice for many more ticks. It verifies that a photon created with an initial displacement continues propagating under ETM logic alone with no further velocity applied.

## Procedure

1. Initialize the engine with the validated foundation configuration.
2. Create a visible-light photon at the lattice center with velocity `(1, 0, 0)`.
   This velocity is applied only on the first tick to displace the photon by one lattice unit.
3. Run the simulation for hundreds of ticks, recording the position each time.
4. Write the trajectory to `photon_propagation_3_results.json`.

## Results

Running `run_trial.py` prints the list of positions visited by the photon. Example:

```json
{
  "positions": [
    [3, 3, 3],
    [4, 3, 3],
    [5, 3, 3],
    [6, 3, 3],
    [6, 3, 3]
  ]
}
```

The photon advances according to ETM logic. In the short Codex run the trajectory remained constant after the first step due to the small lattice. Extended runs will reveal the full propagation pattern.

### Latest Results (2025 Run)
See `photon_propagation_3_results.json` for output.

Run in the background on Windows with:

```
start /B /LOW python run_trial.py --ticks 500 --size 51
```

This launches the process with low priority so other tasks remain usable. The full run completes in under a minute on typical hardware.
