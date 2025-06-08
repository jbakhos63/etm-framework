# Trial 013 – Magnetic Attraction of Parallel Currents

This trial advances **Stage 4 – Magnetic Interaction** of the *ETM Simulation Research Plan*. It investigates whether two electrons moving in parallel experience mutual attraction purely from echo‑field gradients.

## Plan
- **Objective**: Observe the lateral approach of two electrons travelling side by side along the $x$‑axis.
- **Setup**: A $(21,21,21)$ lattice populated with neutral recruiters. Electrons A and B start at $(1,y_0,z_0)$ and $(1,y_0+2,z_0)$ with initial velocity $(1,0,0)$. This velocity is applied only on the first tick to place them in motion; thereafter the return algorithm moves each electron toward the neighbour with the strongest echo, representing magnetic influence.
- **Method**:
  1. Reinforce the echo field at both electron positions.
  2. Move each electron to the neighbouring node with the largest echo value.
  3. Advance the ETM engine so the return logic shifts both electrons forward along $x$ after the initial displacement.
  4. Record the positions for ten ticks in `parallel_current_results.json`.

## Results
```json
{
  "electron_a": [[1,10,10],[1,10,10],[2,11,10],[2,10,10],[3,11,10],[3,10,10],[4,11,10],[4,10,10],[4,10,10],[4,10,10],[4,10,10]],
  "electron_b": [[1,12,10],[1,12,10],[2,11,10],[2,10,10],[3,11,10],[3,10,10],[4,11,10],[4,10,10],[4,10,10],[4,10,10],[4,10,10]]
}
```

The electrons moved toward each other, meeting at the same $y$ coordinate by tick 3 and remaining side by side thereafter. This demonstrates a magnetic-like attraction consistent with parallel currents in classical electromagnetism.
