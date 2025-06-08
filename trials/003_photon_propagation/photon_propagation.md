# Photon Propagation Test

This trial verifies that photon identities created by the engine shift position once at initialization when a velocity is specified. Subsequent ticks obey ETM return logic without any persistent velocity.

## Procedure

1. Initialize the engine with the validated foundation configuration.
2. Create a visible-light photon at the lattice center with velocity `(1, 0, 0)`.
   This velocity is applied only on the first tick to displace the photon by one lattice unit.
3. Run the simulation for four ticks, recording the photon's position each tick.
4. Write the trajectory to `photon_propagation_results.json`.

## Results

Running `run_trial.py` prints the list of positions visited by the photon. Example:

```json
{
  "positions": [
    [3, 3, 3],
    [4, 3, 3],
    [5, 3, 3],
    [6, 3, 3],
    [6, 3, 3]
  ]
}
```

The photon advances one lattice unit each tick until reaching the boundary, where
it remains stationary due to lattice constraints.
\n### Latest Results (2025 Run)\nSee photon_propagation_results.json for output.
