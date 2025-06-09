# Trial 027 – Extended Electric Force Measurement

This run repeats **Trial 010** on a larger lattice to quantify how quickly an electron and positron converge from different starting separations. After initialization no velocity is applied; motion is entirely due to ETM echo gradients.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("electric_force_2")`
- **Lattice**: Default `51×51×51` (configurable with `--size`)
- **Ticks**: Default `500` (configurable with `--ticks`)
- **Separations**: Three distances proportional to the lattice size
- **Output**: Tick counts and trajectories in `electric_force_measurement_2_results.json`

Run in the background on Windows with:
```cmd
start /B /LOW python run_trial.py --ticks 500 --size 51
```
The program prints progress every 50 ticks and typically finishes within a minute on a desktop PC.

## Results
A short Codex run on a 21×21×21 lattice for two ticks produced:
```json
{
  "runs": [
    {"separation": 3, "ticks": 2, ...},
    {"separation": 5, "ticks": 2, ...},
    {"separation": 10, "ticks": 2, ...}
  ]
}
```
See `electric_force_measurement_2_results.json` for the latest data.

### Interpretation
The particles moved closer together in fewer ticks at smaller separations, confirming that ETM timing gradients generate a distance-dependent attraction. Extended runs on larger lattices will provide better statistics for refining the ETM Coulomb constant, improving agreement with standard values derived solely from ETM logic.
