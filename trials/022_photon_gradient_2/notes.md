# Trial 022 – Extended Photon Gradient

This trial repeats **Trial 005** on a larger lattice for many more ticks. It verifies that a photon drifts along an echo-field gradient purely under ETM logic with no persistent velocity.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("photon_gradient_2")`
- **Lattice**: Default `51×51×51` (override with `--size`)
- **Ticks**: Default `500` (override with `--ticks`)
- **Setup**: Assign a neutral recruiter to every node and set `rho_local = y - y_center` so echo strength increases along the $y$‑axis. Create a visible-light photon at `(1, y_center, z_center)`.
- **Output**: Positions are stored in `photon_gradient_2_results.json`.

Run in the background on Windows using:
```
start /B /LOW python run_trial.py --ticks 500 --size 51
```
A full run typically finishes in under a minute and prints a JSON summary.

## Results
The short Codex verification used a 21×21×21 lattice for two ticks and produced:
```json
{
  "positions": [[1,10,10],[1,11,10],[1,12,10]],
  "ticks": 2
}
```

### Latest Results (2025 Run)
See `photon_gradient_2_results.json` for extended output.
