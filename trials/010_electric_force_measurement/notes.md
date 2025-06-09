# Trial 010 – Quantifying Electron–Positron Attraction

This trial continues **Stage 3 – Long-Range Electric Interaction** of the *ETM Simulation Research Plan*.  Trial 009 demonstrated qualitative attraction between an electron and a positron in a small lattice.  Here we measure how quickly the pair converges from different initial separations to begin estimating an ETM analogue of the Coulomb constant.

## Objective
- Run multiple simulations with the electron and positron separated by various distances.
- Record the number of ticks required for the pair to meet under echo-field-driven motion.
- Provide baseline data for modelling the effective electric force in ETM units.

## Method
1. **Initialization** – For each separation distance $d$, create a `(21,21,21)` lattice using `ConfigurationFactory.validated_foundation_config` with `max_ticks=20`.
2. **Recruiters** – Populate every node with a neutral `Recruiter` so that echo inheritance functions uniformly across the lattice.
3. **Particle Placement** – Place an electron at `(center_x - d/2, center_y, center_z)` and a positron at `(center_x + d/2, center_y, center_z)`.  Both start with `velocity=None`.
4. **Echo Dynamics** – At each tick:
    - Reinforce the echo field at each particle's location.
    - Advance phases, apply echo decay, and apply echo inheritance.
    - Move each particle to the neighbouring node with the highest echo value, ensuring that motion is entirely driven by the echo gradient from the opposite charge.
5. **Data Collection** – Track the positions each tick.  Stop early if the particles occupy the same node.
6. **Output** – Store tick counts and trajectories for all tested separations in `electric_force_results.json`.

## Results
Results will be appended below after running `run_trial.py`.

### Recorded Positions and Tick Counts
The simulation results show convergence times increasing with initial separation:

```
Separation 4: 2 ticks
Separation 6: 3 ticks
Separation 8: 4 ticks
```

The trajectories for each run are saved in `electric_force_results.json`. This monotonic relationship between starting distance and meeting time is consistent with an attractive interaction derived from timing-gradients. Quantitative force extraction will require larger lattices, but these baseline results confirm that the ETM framework produces distance-dependent attraction without preset velocities.
\n### Latest Results (2025 Run)\nSee notes_results.json for output.
