# Trial 048 – Phase 5 – Proton Resolution Scan (Scale 2)

This trial continues the composite proton study by examining stability when the proton pattern is expanded by a factor of two.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("proton_resolution")`
- **Lattice**: default `51×51×51` (override with `--size`)
- **Ticks**: default `200` (override with `--ticks`)
- **Scale**: fixed at `2` by default

Run with for example:
```bash
python run_trial.py --ticks 200 --size 51
```

## Results
Placeholder output from a short Codex run on a 21³ lattice:
```json
{
  "scale": 2,
  "positions": [[10,10,10],[10,10,10],[10,10,10]]
}
```
See `proton_resolution_scan_6_results.json` for full data.
