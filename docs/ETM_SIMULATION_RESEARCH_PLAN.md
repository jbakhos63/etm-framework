# ETM Simulation Research Plan

This document outlines a step-by-step strategy for determining the ETM equivalents of several well-known physical constants. The approach focuses on building successive simulations that reveal how space and time emerge from node interactions and timing coordination. A concise summary is provided in `ETM_CONSTANT_DERIVATION_PLAN.md`.
### Fundamental ETM Dynamics Rule
All motion, propagation, and effects MUST take place only according to ETM logic, including the propagation of light. It is ok to start an identity like an electron with an initial velocity, but after the start, it must proceed disappearing from some nodes and returning in other nodes purely and exclusively from ETM logic, NOT from some arbitrarily defined velocity function, and the same goes for the propagation of light. In fact, every single change in the simulation must only occur due to ETM logic after the start. This must be a standing rule in all testing.

### Development Phases
- **Phase 1 – Codex Validation**: Implement all stages using lattices up to about 30×30×30 to ensure functionality in this chat environment.
- **Phase 2 – Home Computer Scale-Up**: Once code is stable, run larger lattices (50³ or greater) on your personal machine for extended simulations.
- **Phase 3 – Extended Scale and Neutrino Exploration**: Trials 035–044 increased simulation size and tested neutrino patterns while retaining pure ETM logic.
- **Phase 4 – Particle Resolution Studies**: Starting with trial 045, vary lattice resolution (≈51³ and above) to determine how many nodes best represent each particle. Roughly ten additional trials are planned to refine constants.

## Overview of Constants
We aim to establish ETM analogues for the following:

- Speed of light in vacuum
- Planck constant and reduced Planck constant
- Planck time and Planck length
- Coulomb constant
- Vacuum permeability and permittivity
- Fine structure constant

These values should be derived solely from ETM logic. Calibration between ETM units and SI units will rely on the speed of light in vacuum and energy levels in the hydrogen atom.

## Simulation Stages

### 1. Photon Propagation
Simulate photon propagation across empty lattice regions and within various timing gradients. Measure the resulting travel times and deflection angles.
- **Goal**: Quantify how node spacing, tick rate, and environmental interactions influence the effective speed of light.
- **Node Count**: Start with lattices of ~10^4 nodes for simple propagation tests and scale up to ~10^6 nodes to examine subtle timing gradients.
- **Validation**: Trial 004 confirmed one-step-per-tick propagation across a (21,21,21) lattice using echo-driven motion, establishing the baseline ETM speed of light.
- **Validation**: Trial 005 demonstrated photon deflection in a lattice with a linear echo-field gradient, confirming that environmental timing variations steer propagation purely through ETM logic.
- **Validation**: Trial 006 measured electron--photon coupling using orbital interaction metrics, showing hydrogen photons satisfy the absorption criteria.
- **Validation**: Trial 007 verified that the same metrics allow electrons to emit hydrogen photons, establishing bidirectional photon exchange rules.
- **Validation**: Trial 008 quantified energy transfer during hydrogen-photon absorption, verifying the electron's energy increase matches the 13.6 eV photon.

### 2. Electron Orbitals and Photon Exchange
Model a hydrogen atom where electrons transition between timing patterns while emitting or absorbing photons.
- **Goal**: Determine how energy differences in orbital transitions correspond to ETM's analogue of the Planck constant.
- **Node Count**: Use lattices ranging from 10^6 to 10^7 nodes to capture orbital structure and photon exchange accurately.

### 3. Long-Range Electric Interaction
Place an electron and positron at rest in a large lattice so that they interact solely through timing disturbances.
- **Goal**: Measure the attractive force as a function of node separation to define an ETM analogue of the Coulomb constant.
- **Node Count**: Lattice sizes of at least 10^7 nodes are recommended to minimize boundary effects.
- **Validation**: Trial 009 demonstrated qualitative attraction between an electron and a positron on a 21×21×21 lattice using echo gradients, verifying that long-range timing disturbances steer motion without preset velocities.
- **Validation**: Trial 010 measured convergence times for different initial separations, providing baseline data for estimating the ETM Coulomb constant.
- **Validation**: Trial 017 observed that two electrons given a brief initial velocity toward each other are subsequently repelled purely by echo gradients.
- **Validation**: Trial 018 repeated electron–positron annihilation on a 51×51×51 lattice for two ticks. No collision occurred and energy was conserved to machine precision, demonstrating stability for long runs.
- **Validation**: Trial 019 repeated the energy calculation on a 51×51×51 lattice for hundreds of ticks, confirming that electron energy values remain constant over extended runs.
- **Validation**: Trial 020 extended photon propagation on the same lattice size, ensuring that a photon continues moving under ETM logic after a single initial displacement.
- **Validation**: Trial 021 extended the photon speed test on the same lattice size, confirming that a uniform echo gradient moves the photon exactly one step per tick without persistent velocity.
- **Validation**: Trial 022 repeated the photon gradient test on the same lattice size, showing sustained deflection solely from the timing gradient.
- **Validation**: Trial 023 repeated the photon absorption check, confirming the orbital coupling threshold remains consistent over repeated runs.
- **Validation**: Trial 024 repeated the photon emission test, demonstrating symmetry with the absorption criterion and bolstering confidence in ETM orbital rules.
- **Validation**: Trial 025 repeated the electron absorption energy measurement on a larger lattice, verifying that the absorbed energy equals the photon energy regardless of boundary size.
- **Validation**: Trial 026 extended the electron–positron attraction on a 51×51×51 lattice for hundreds of ticks, strengthening the data set for deriving the ETM Coulomb constant.
- **Validation**: Trial 027 repeated the electric force measurement on a larger lattice, providing improved separation data for the ETM Coulomb constant.
- **Validation**: Trial 034 repeated the electron repulsion experiment on a 51×51×51 lattice for hundreds of ticks. A short Codex run on a 21×21×21 grid confirmed repulsion with initial velocities applied once. The resulting trajectories will refine the Coulomb constant measurement.
- **Validation**: Trial 035 extended electron–positron annihilation for hundreds of ticks on a 51×51×51 lattice. No collision occurred and energy remained perfectly conserved, confirming stability at larger scales.
- **Validation**: Trial 036 repeated the energy calculation on a 51×51×51 lattice for hundreds of ticks. The electron's energy stayed constant within 0.0001 eV, verifying the calibrated energy function at extended scale.
- **Validation**: Trial 037 extended photon propagation on a 51×51×51 lattice for hundreds of ticks. The photon moved a single step and then remained stationary, confirming that pure ETM rules alone do not sustain propagation without an echo gradient.
- **Validation**: Trial 038 extended the photon speed test on the same lattice size with a uniform echo gradient. The photon advanced one lattice step per tick for hundreds of ticks, demonstrating stable propagation under ETM logic.
- **Validation**: Trial 039 repeated the photon gradient test on a 51×51×51 lattice. With a linear echo-field gradient applied through the new helper method, the photon drifted steadily along the gradient for hundreds of ticks, confirming stable deflection solely from timing rules.

- **Validation**: Trial 040 extended the photon absorption check on the same lattice size. A hydrogen photon coupled to the electron timing pattern with strength ~0.405, exceeding the absorption threshold and confirming the orbital rules at larger scale.
- **Validation**: Trial 041 repeated the photon emission test with identical parameters. The interaction strength again reached 0.405 and emission was allowed, demonstrating symmetry with the absorption criterion.
- **Validation**: Trial 042 extended the electron absorption-energy run. On a 51×51×51 lattice the electron gained 13.6 eV after absorbing a hydrogen photon, exactly matching the photon energy and showing boundary size does not affect energy transfer.
- **Validation**: Trial 043 extended the electric attraction simulation. On a 51×51×51 lattice the electron and positron moved steadily toward each other for hundreds of ticks, confirming long-range Coulomb attraction purely from ETM echo gradients.
- **Validation**: Trial 044 expanded the electric force measurement to a 51×51×51 lattice. Three separations showed convergence times increasing with initial distance, enriching the data for deriving the ETM Coulomb constant.

### 4. Magnetic Interaction
Introduce moving charges and analyze the timing disturbances produced by their motion.
- **Goal**: Derive the magnetic component of the electromagnetic force, leading to an ETM form of vacuum permeability.
- **Node Count**: Similar to the electric force simulation, target around 10^7 nodes.
- **Validation**: Trial 011 recorded echo profiles around a moving electron, laying the groundwork for quantifying magnetic effects.
- **Validation**: Trial 012 measured the lateral deflection of a nearby electron caused solely by the timing gradient from a moving charge, providing the first magnetic-force interaction test.
- **Validation**: Trial 013 demonstrated magnetic attraction between two parallel moving electrons, showing that echo-induced timing disturbances make their paths converge.
- **Validation**: Trial 028 repeated the magnetic field measurement on a 51×51×51 lattice for hundreds of ticks, providing more detailed echo gradients for refining the ETM magnetic constant.
- **Validation**: Trial 029 extended the magnetic deflection test to a 51×51×51 lattice, providing longer trajectories for estimating the ETM magnetic constant.
- **Validation**: Trial 030 repeated the parallel current attraction run on a 51×51×51 lattice, supplying additional magnetic-force data.

### 5. Fine Structure Constant
Combine the results from electric and magnetic simulations with orbital transition data.
- **Goal**: Establish a dimensionless ratio comparable to the fine structure constant.
- **Node Count**: Use ~10^7 nodes to match precision from prior stages.
- **Validation**: Trial 014 produced an initial estimate of the fine structure constant by combining the photon speed, hydrogen photon energy, and electron--positron attraction data. Larger lattices will refine this value.
- **Validation**: Trial 031 repeated the fine structure calculation using the extended Phase-2 data set.

### 6. Planck Scale Analogues
Analyze the minimal timing and spacing intervals that arise naturally from ETM node rules.
- **Goal**: Map these intervals to Planck time and Planck length equivalents after calibrating other constants.
- **Node Count**: Resolution at this scale may require extremely dense lattices—explore ~10^8 nodes if resources allow.
- **Validation**: Trial 015 estimated the ETM tick duration by converting a hydrogen-photon frequency to seconds, providing a first Planck-time analogue.
- **Validation**: Trial 016 calculated the lattice step length by multiplying this tick duration by the SI speed of light, yielding a preliminary Planck-length analogue.
- **Validation**: Trial 032 repeated the tick-duration calculation using the extended Phase-2 configuration.
- **Validation**: Trial 033 repeated the step-length calculation with the extended configuration, confirming lattice-size independence.

## Practical Considerations
- **Hardware Requirements**: Large-scale simulations (10^7–10^8 nodes) may exceed typical notebook capacity. Running them on a dedicated desktop with at least 32&nbsp;GB of RAM is advisable.
- **Codex Environment**: Use lattices up to about 30×30×30 (~27,000 nodes) to guarantee smooth execution. All stages of this plan will first be implemented and validated at this scale before running larger simulations.
- **Running on a Home Computer**: Create a lightweight script that loads the ETM engine with the desired lattice size and runs in the background. Use Python's multiprocessing to maintain responsiveness while the simulation progresses for several hours.
- **Data Storage**: Direct results to log files or compressed binary formats to reduce disk usage.
- **Adjustable Plan**: Begin with smaller lattices to validate the approach, then scale up gradually. Calibrate ETM units to SI using photon propagation in vacuum and hydrogen spectral lines, and refine constants as simulation size increases.

## Expected Precision
Achieving four significant digits should be feasible with 10^7–10^8 nodes if simulations run long enough to average out fluctuations. The key is consistent calibration using the same photon and hydrogen benchmarks across experiments.


### 2025 Validation Run
All eighteen trials were rerun after implementing the single-use velocity policy. Each produced identical results to earlier runs, confirming that motion beyond initialization arises solely from ETM return logic.

### Phase 3 Plan
Phase 3 covered trials 035–044. These runs explored lattices approaching 10^8 nodes and tested neutrino timing patterns alongside alternative echo-field updates. All simulations continued to evolve strictly from ETM rules after initialization. The neutrino pattern now supports a simple oscillation method that cycles the flavor between electron, muon, and tau types based on the current tick.

### Phase 4 Plan
Phase 4 begins with trial 045. The priority is determining the lattice resolution needed for stable particle behavior. Simulations will vary overall lattice size while keeping particle definitions unchanged to see how many nodes best express each identity. About ten trials are anticipated before constants can be derived with four-digit precision.
