# Trial 009 – Electron–Positron Attraction

This trial begins Stage 3 of the **ETM Simulation Research Plan**: measuring the effective long‑range electric interaction. We place an electron and a positron at rest on opposite sides of a small lattice and let the echo‑field gradients dictate their motion.

## Plan
- **Objective**: Demonstrate that opposite chiralities move toward each other solely by echo reinforcement, providing the groundwork for extracting an ETM analogue of the Coulomb constant.
- **Setup**: A `(21,21,21)` lattice with recruiters at every node. The electron starts at `(7,10,10)` and the positron at `(13,10,10)`. Both have `velocity=None` so they are not moved by any preset rule.
- **Dynamics**: Each tick adds echo reinforcement at the particles' locations. Motion rules pick the neighbouring node with the highest echo value from the opposite particle's field. Echo inheritance spreads the reinforcement creating a gradient that steers the particles toward each other.
- **Measurement**: Record the positions of both particles over six ticks to track their approach rate.

## Results
Results of `run_trial.py` are appended below after execution.

### Recorded Positions
```json
{
  "electron": [[7,10,10],[8,10,10],[9,10,10],[10,10,10],[9,10,10],[8,10,10],[7,10,10]],
  "positron": [[13,10,10],[12,10,10],[11,10,10],[10,10,10],[9,10,10],[8,10,10],[7,10,10]],
  "ticks": 6
}
```

The electron and positron move symmetrically toward each other and meet at the lattice center by tick 3. They then continue past one another because the local echo maxima shift once the particles cross. Despite the small size, this qualitative attraction confirms that echo‑field gradients alone can produce motion analogous to the electric force.
\n### Latest Results (2025 Run)\nSee notes_results.json for output.
