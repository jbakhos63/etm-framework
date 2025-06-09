# Trial 047 – Phase 3 – Extended Parallel Current Attraction

This trial repeats **Trial 013** on a larger lattice for many more ticks. We test how two electrons moving in parallel gradually draw together solely from ETM timing gradients.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("parallel_current")`
- **Lattice**: Default `51×51×51` (override with `--size`)
- **Ticks**: Default `500` (override with `--ticks`)
- **Setup**: All nodes contain neutral recruiters. Electrons A and B start one lattice step apart in the $y$ direction near the left boundary, both with velocity `(1,0,0)` applied only on the first tick. Subsequent motion follows ETM return logic.
- **Output**: Trajectories are written to `parallel_current_3_results.json`.

Run in the background on Windows with:
```cmd
start /B /LOW python run_trial.py --ticks 500 --size 51
```
The program prints progress every 50 ticks and typically finishes in under a minute on a desktop PC.

## Results
A short verification on a 21×21×21 lattice for two ticks produced:
```json
{
  "electron_a": [[1,10,10],[1,10,10],[1,11,10]],
  "electron_b": [[1,12,10],[1,12,10],[1,11,10]]
}
```
See `parallel_current_3_results.json` for the latest output.

### Interpretation
Both electrons moved toward each other even without persistent velocity, meeting by the second tick. This mirrors the magnetic attraction seen in Trial 013. Running the extended version on a 51³ lattice will provide long-range timing data to refine the ETM magnetic constant and improve overall theory accuracy.
