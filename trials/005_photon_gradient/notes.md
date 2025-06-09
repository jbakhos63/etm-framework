# Trial 005 – Photon Deflection in an Echo Gradient

This trial extends the photon propagation study by introducing an environment with a steady echo-field gradient. The goal is to confirm that photon motion is influenced solely by ETM logic when spatial echo strength varies.

## Objective
- Observe the trajectory of a photon travelling through a lattice where echo strength increases along the $y$‑axis.
- Quantify the resulting deflection to verify that timing‐gradient environments modify the ETM speed of light and direction of propagation.

## Method
1. **Initialization** – The ETM engine is created with lattice size $(21,21,21)$ and `max_ticks = 10` using `ConfigurationFactory.validated_foundation_config`.
2. **Environment Setup** – Every lattice node receives a `Recruiter` with neutral ancestry. Echo fields are initialized so that $\rho_{(x,y,z)} = y - y_\text{center}$, generating a linear gradient upward.
3. **Photon creation** – A visible-light photon timing pattern is instantiated at position $(1,y_\text{center},z_\text{center})` with no preset velocity. Its movement will be determined each tick by choosing the neighbouring node with the highest echo-field value.
4. **Propagation** – For ten ticks the simulation advances phases and echo dynamics. At each tick the photon is relocated to the neighbour with maximal echo strength—this implements motion strictly through ETM echo logic without a persistent velocity attribute.
5. **Output** – The list of visited positions is saved in `photon_gradient_results.json`.


## Results
The photon trajectory recorded in `photon_gradient_results.json` shows a clear drift toward increasing $y$ values:

```
{
  "positions": [[1,10,10],[1,11,10],[1,12,10],[1,13,10],[1,14,10],[1,15,10],[0,16,10],[0,17,10],[0,18,10],[0,19,10],[0,20,10]],
  "ticks": 10
}
```

The photon initially moves vertically upward while remaining near its starting $x$ coordinate until hitting the lattice boundary at $x=0$. It then continues upward along the boundary. This confirms that the echo gradient alone dictates its motion, satisfying the rule that all propagation arises solely from ETM logic after initialization.
\n### Latest Results (2025 Run)\nSee notes_results.json for output.
