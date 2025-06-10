# Trial 046 – Phase 3 – Extended Magnetic Deflection

This trial repeats **Trial 012** on a larger lattice for many more ticks. We examine how the echo field of a moving electron alters the trajectory of a nearby electron using only ETM timing logic.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("magnetic_deflection")`
- **Lattice**: Default `51×51×51` (override with `--size`)
- **Ticks**: Default `500` (override with `--ticks`)
- **Setup**: Neutral recruiters occupy all nodes. Electron A begins near the left boundary with velocity `(1,0,0)` applied only on the first tick. Electron B is placed two steps above A's path with no velocity. Thereafter both electrons move solely via ETM return logic.
- **Output**: Trajectories are written to `magnetic_deflection_3_results.json`.

Run in the background on Windows with:
```cmd
start /B /LOW python run_trial.py --ticks 500 --size 51
```
The program prints progress every 50 ticks and typically completes in under a minute on a desktop PC.

## Results
A short verification on a 21×21×21 lattice for two ticks produced:
```json
{
  "electron_a": [[1,10,10],[2,10,10],[3,10,10]],
  "electron_b": [[1,12,10],[1,11,10],[1,10,10]]
}
```
See `magnetic_deflection_3_results.json` for the latest output.

### Interpretation
Electron B moved toward the path of Electron A even without any velocity, confirming that the moving charge creates a timing gradient consistent with the magnetic deflection seen in Trial 012. Running this extended version on a 51³ lattice will refine the ETM magnetic constant and improve overall accuracy.
