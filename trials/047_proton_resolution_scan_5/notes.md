# Trial 047 – Phase 5 – Proton Resolution Scan

This trial begins the composite particle review phase. We vary the number of lattice nodes assigned to the proton pattern to determine the smallest stable configuration.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("proton_resolution")`
- **Lattice**: default `51×51×51` (override with `--size`)
- **Ticks**: default `200` (override with `--ticks`)
- **Scale**: multiplies the proton pattern offsets

Run with for example:
```bash
python run_trial.py --ticks 200 --size 51 --scale 2
```

## Results
Placeholder output from a short Codex run on a 21³ lattice with `scale=2`:
```json
{
  "scale": 2,
  "positions": [[10,10,10],[10,10,10],[10,10,10]]
}
```
See `proton_resolution_scan_5_results.json` for full data.
