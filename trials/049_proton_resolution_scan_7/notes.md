# Trial 049 – Phase 5 – Proton Resolution Scan (Scale 3)

This trial extends the composite proton study by expanding the pattern by a factor of three.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("proton_resolution")`
- **Lattice**: default `51×51×51` (override with `--size`)
- **Ticks**: default `200` (override with `--ticks`)
- **Scale**: fixed at `3` by default

Run with for example:
```bash
python run_trial.py --ticks 200 --size 51
```

## Results
A ten‑tick run on a 21³ lattice produced no displacement when the scale was set to
three. The proton remained centered for all ticks, confirming stability at this
larger pattern size. See `proton_resolution_scan_7_results.json` for the recorded
positions.
