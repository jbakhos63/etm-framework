# Trial 021 – Extended Photon Speed

This trial repeats **Trial 004** on a larger lattice for many more ticks. It verifies that a photon continues to advance exactly one lattice step per tick when propagation arises solely from ETM logic.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("photon_speed_2")`
- **Lattice**: Default `51×51×51` (override with `--size`)
- **Ticks**: Default `500` (override with `--ticks`)
- **Setup**: Establish a constant echo gradient along the x‑axis by assigning recruiter values equal to each node's x‑coordinate. Create a visible‑light photon one step from the lattice boundary with no persistent velocity. After initialization the photon moves purely according to ETM return logic.
- **Output**: Positions are stored in `photon_speed_2_results.json`.

Run in the background on Windows using:
```
start /B /LOW python run_trial.py --ticks 500 --size 51
```
A full run finishes in under a minute on typical hardware and prints a JSON summary.

## Results
The short Codex verification used a 21×21×21 lattice for two ticks and produced the following output:

```json
{
  "positions": [[1,10,10],[2,10,10],[3,10,10]],
  "ticks": 2
}
```

### Latest Results (2025 Run)
See `photon_speed_2_results.json` for data from the extended run.
