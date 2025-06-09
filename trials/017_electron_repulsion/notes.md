# Trial 017 – Electron Repulsion with Initial Approach

This experiment extends **Stage 3 – Long-Range Electric Interaction** of the *ETM Simulation Research Plan*. Two electrons start far apart and are given small initial velocities toward each other. After this initial displacement all motion obeys ETM return logic, demonstrating repulsion between like chiralities.

## Plan
- **Objective**: Observe whether two approaching electrons are repelled solely by echo-field gradients once their velocities are cleared.
- **Setup**: A `(21,21,21)` lattice with neutral recruiters at each node. Electron A begins at `(3,10,10)` with velocity `(1,0,0)`; Electron B starts at `(17,10,10)` with velocity `(-1,0,0)`. Each velocity is applied only on tick 1.
- **Method**:
  1. At tick 0 reinforce the echo field at both starting positions and advance the engine so the initial velocities shift each electron once.
  2. For subsequent ticks reinforce the echo at the electron locations, then move each electron to the neighbouring node with the **lowest** echo value—representing repulsion from the other electron's field.
  3. Record the trajectories for ten ticks in `electron_repulsion_results.json`.

## Results
Results appear below after running `run_trial.py`.

### Latest Results (2025 Run)
See notes_results.json for output.
