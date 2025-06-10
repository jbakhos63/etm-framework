# Trial 046 – Phase 4 – Electron Resolution Scan

This trial examines how the number of lattice nodes used to define an electron affects its stability. The `scale` parameter multiplies the electron's pattern offsets.

## Plan
- **Engine**: `ConfigurationFactory.validated_foundation_config("electron_resolution")`
- **Lattice**: Default `51×51×51` (override with `--size`)
- **Ticks**: Default `200` (override with `--ticks`)
- **Scale**: Adjusts how many nodes form the electron pattern

Run with for example:
```
python run_trial.py --ticks 200 --size 51 --scale 2
```

## Results
Initial Codex run on a 21³ lattice with `scale=2` for two ticks produced placeholder data:
```json
{
  "scale": 2,
  "positions": [[10,10,10],[10,10,10],[10,10,10]]
}
```
See `electron_resolution_scan_4_results.json` for full data.
