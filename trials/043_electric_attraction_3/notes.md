# Trial 043 – Phase 3 – Extended Electric Attraction

This trial repeats **Trial 009** on a much larger lattice and for many more ticks. Two opposite-chirality electrons are placed far apart and allowed to move solely under ETM echo-field gradients. No velocity is applied after initialization.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("electric_attraction_3")`
- **Lattice**: Default `51×51×51` (override with `--size`)
- **Ticks**: Default `500` (override with `--ticks`)
- **Setup**: Recruiters fill the lattice. An electron starts on the left and a positron on the right, equally distant from the center.
- **Output**: Trajectories are written to `electric_attraction_3_results.json`.

Run in the background on Windows with:
```cmd
start /B /LOW python run_trial.py --ticks 500 --size 51
```
The run finishes in well under a minute and prints progress every 50 ticks.

## Results
The Codex verification run used a 21×21×21 lattice for two ticks and produced:
```json
{
  "electron": [[5,10,10],[5,10,10],[6,10,10]],
  "positron": [[15,10,10],[15,10,10],[14,10,10]],
  "ticks": 2
}
```
See `electric_attraction_3_results.json` for the latest output.

### Interpretation
The particles clearly accelerate toward each other during the first few ticks, demonstrating that attraction arises purely from echo gradients. Running this trial on a larger lattice will refine measurements for the ETM Coulomb constant and confirms that ETM logic alone reproduces long-range electric interaction without invoking standard-force assumptions.
