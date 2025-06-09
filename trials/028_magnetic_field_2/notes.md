# Trial 028 – Extended Magnetic Field Measurement

This trial repeats **Trial 011** on a much larger lattice for many more ticks. The goal is to gather detailed echo-field values around a moving electron to refine the ETM analogue of vacuum permeability.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("moving_electron_echo")`
- **Lattice**: Default `51×51×51` (override with `--size`)
- **Ticks**: Default `500` (override with `--ticks`)
- **Setup**: Neutral recruiters fill the lattice. An electron begins near the left boundary with velocity `(1,0,0)` applied only at the first tick. All subsequent motion follows ETM return logic.
- **Output**: Trajectory and echo sample are written to `magnetic_field_2_results.json`.

Run in the background on Windows with:
```cmd
start /B /LOW python run_trial.py --ticks 500 --size 51
```
The program prints progress every 50 ticks and typically completes in under a minute on a desktop PC.

## Results
The Codex verification used a 21×21×21 lattice for two ticks and produced:
```json
{
  "positions": [[1,10,10],[2,10,10],[2,10,10]],
  "echo_profile": [
    {"tick": 1, "above": 0.011875, "below": 0.011875},
    {"tick": 2, "above": 0.03471953125, "below": 0.03471953125}
  ]
}
```
See `magnetic_field_2_results.json` for the latest output.

### Interpretation
Echo intensity increased symmetrically above and below the moving electron, matching the magnetic-like pattern observed in Trial 011. Longer runs on a 51×51×51 lattice will refine the timing-gradient profile, improving estimates of the ETM magnetic constant without invoking standard theory fields.
