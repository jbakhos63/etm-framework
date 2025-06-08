# Trial 008 – Electron Energy Change from Photon Absorption

This trial extends the *Electron Orbitals and Photon Exchange* stage by quantifying the energy transferred to an electron when it absorbs a hydrogen photon. The aim is to demonstrate that the ETM energy computation matches the photon's energy content, providing a basis for defining the ETM analogue of the Planck constant.

## Objective
- Create a ground-state electron in the center of a small lattice.
- Simulate absorption of a hydrogen photon by increasing the electron's `delta_theta` according to the photon's energy.
- Verify that the electron's energy increase equals the photon energy when calculated with ETM's calibrated formula.

## Method
1. **Initialization** – Use `ConfigurationFactory.validated_foundation_config` with lattice size `(21,21,21)` and `max_ticks=1`.
2. **Electron Setup** – Instantiate an electron identity at the lattice center with `delta_theta=0.1` and attach the standard electron timing pattern.
3. **Energy Calculation** – Compute the electron's initial energy using `calculate_particle_energy`.
4. **Photon Setup** – Create a hydrogen photon timing pattern. Confirm that it can be absorbed by the electron pattern via `can_be_absorbed_by`.
5. **Absorption** – Increase the electron's `delta_theta` by `photon.energy_content / config.kinetic_scale_factor` to represent photon energy transfer.
6. **Post-Absorption Energy** – Recalculate the electron energy and record the difference.
7. **Output** – Save initial energy, final energy, and energy change to `absorption_energy_results.json`.

All motion and effects after initialization obey ETM logic. The electron's increased kinetic timing rate represents absorbed energy without any arbitrary velocity function.

## Results
Results are recorded in `absorption_energy_results.json` and summarized below.

```json
{
  "initial_energy": -34.001,
  "final_energy": -20.401,
  "energy_change": 13.6,
  "photon_energy": 13.6
}
```

The electron's energy increased by exactly the photon's 13.6&nbsp;eV. This matches ETM's calibrated energy formula and confirms that photon absorption is quantized according to timing-rate increments. This result supports defining the ETM analogue of Planck's constant by equating discrete changes in `delta_theta` with photon energies.
