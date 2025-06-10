# Trial 045 – Phase 4 – Magnetic Field Measurement with Resolution Scaling

This trial restarts the magnetic-field study from **Trial 028** but kicks off phase 4. The focus is on how particle resolution affects measured timing disturbances.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("moving_electron_echo")`
- **Lattice**: Default `51×51×51` (override with `--size` to test different resolutions)
- **Ticks**: Default `500` (override with `--ticks`)
- **Setup**: Neutral recruiters fill the lattice. An electron begins near the left boundary with velocity `(1,0,0)` applied only at tick 0. All subsequent motion is pure ETM logic.
- **Output**: Trajectory and echo samples written to `magnetic_field_4_results.json`.

Run in the background with:
```cmd
start /B /LOW python run_trial.py --ticks 500 --size 51
```

## Results
A Codex check on a `21×21×21` lattice for two ticks produced placeholder data:
```json
{
  "positions": [[1,10,10],[2,10,10]],
  "echo_profile": []
}
```
See `magnetic_field_4_results.json` for full results.
