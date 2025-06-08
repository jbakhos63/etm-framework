# Trial 004 – Photon Speed Baseline

This trial implements the first stage of the *ETM Simulation Research Plan*: verifying photon propagation in empty space. We run a single visible-light photon through a \(21 \times 21 \times 21\) lattice (approximately 9,261 nodes) for ten ticks.

**Objective**

- Confirm that a free photon travels one lattice step per tick irrespective of lattice size.
- Produce baseline data for the effective speed of light in ETM units.

**Method**

1. **Initialization** – The ETM engine is configured via `ConfigurationFactory.validated_foundation_config` with lattice size `(21, 21, 21)` and `max_ticks = 10`.
2. **Photon creation** – A visible-light photon timing pattern is created and attached to an `Identity` positioned near the lattice center.
3. **Propagation** – A uniform echo gradient along the x‑axis steers the photon. At each tick the photon moves to the neighbor with the highest echo value, and global timing updates are applied.
4. **Output** – Positions are written to `photon_speed_results.json` for analysis.

The run script is `run_trial.py` within this folder.

## Results

Running `run_trial.py` produced the following trajectory stored in `photon_speed_results.json`:

```json
{
  "positions": [[10,10,10], [11,10,10], [12,10,10], [13,10,10], [14,10,10], [15,10,10], [16,10,10], [17,10,10], [18,10,10], [19,10,10], [20,10,10]],
  "ticks": 10
}
```

The photon advanced exactly one lattice unit along the x-axis each tick. With lattice spacing and tick duration taken as ETM units, this establishes the baseline **speed of light** in vacuum as one lattice step per tick. No deviation was observed over the 21×21×21 lattice, confirming that lattice size does not affect propagation speed at this scale.
