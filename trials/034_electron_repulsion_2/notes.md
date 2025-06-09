# Trial 034 – Extended Electron Repulsion

This trial mirrors **Trial 017** but on a larger lattice and for many more ticks.
Its purpose is to refine measurements of electron–electron repulsion and
confirm that energy remains conserved over long runs.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("electron_repulsion")`
- **Lattice**: Default `51×51×51` (override with `--size`)
- **Ticks**: Default `500` (override with `--ticks`)
- **Setup**: Two electrons start far apart with small opposing velocities so they
  move toward each other on the first tick only. Subsequent motion follows ETM
  return logic exclusively.
- **Output**: Trajectories are written to `electron_repulsion_2_results.json`.

Run in the background on Windows using:

```
start /B /LOW python run_trial.py --ticks 500 --size 51
```

Make sure to install dependencies first with `pip install -r requirements.txt`.
On a typical desktop the run finishes in well under a minute and prints a summary when complete.

## Results
The 2025 Codex test used a 21×21×21 lattice for two ticks to verify the script.
Both electrons moved one step toward each other on the first tick and again on
the second, demonstrating that the initial velocity is applied once and then
motion proceeds via return logic. Longer runs on a 51×51×51 lattice should yield
more precise repulsion curves.

```
{
  "electron_a": [[1,10,10],[2,10,10],[3,10,10]],
  "electron_b": [[19,10,10],[18,10,10],[17,10,10]]
}
```

### Latest Results (2025 Run)
See `electron_repulsion_2_results.json` for the full output.
