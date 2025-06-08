# ETM Constant Derivation Plan

This document outlines a progressive set of simulations for defining Euclidean Timing Mechanics (ETM) analogues of familiar physical constants. Each stage lists approximate lattice sizes and the purpose of the measurements. Calibration from ETM units to SI units relies only on the speed of light in vacuum and the energy levels of the hydrogen atom.

## 1. Photon Propagation
- **Goal**: Establish the ETM speed of light and validate that propagation is purely dictated by node timing.
- **Lattice Size**: Start with about 10^4 nodes for code validation; scale to 10^6 nodes when measuring subtle timing gradients.

## 2. Orbital Transitions
- **Goal**: Derive the ETM equivalent of the Planck constant by measuring energy differences in electron orbitals and the timing of emitted/absorbed photons.
- **Lattice Size**: 10^6–10^7 nodes to capture orbital structure.

## 3. Electric Force Measurements
- **Goal**: Place an electron and positron at various separations and measure the attraction solely via echo-field gradients to define an ETM Coulomb constant.
- **Lattice Size**: At least 10^7 nodes to minimize boundary effects.

## 4. Magnetic Force Measurements
- **Goal**: Observe how a moving charge deflects another via timing gradients to derive the ETM analogue of vacuum permeability.
- **Lattice Size**: Similar to electric force studies, ~10^7 nodes.

## 5. Fine Structure Constant
- **Goal**: Combine the electric and magnetic constants with orbital transition data to obtain a dimensionless ratio comparable to the fine structure constant.
- **Lattice Size**: ~10^7 nodes.
- **Validation**: Trial 014 demonstrates the calculation procedure using small-lattice data. Future runs on larger grids will refine the estimate.

## 6. Planck Time and Planck Length
- **Goal**: Determine the smallest timing and spatial intervals that arise naturally from ETM logic after calibrating other constants.
- **Lattice Size**: Explore 10^8 nodes if resources allow.

## Development Phases
1. **Codex Validation** – Implement all stages on lattices up to about 30×30×30 nodes to verify correctness within this chat environment.
2. **Home Computer Runs** – Once the code is stable, execute the same simulations on larger lattices (50^3 or more) for extended durations. Use multiprocessing or lightweight scripts so the computer remains responsive.

Each stage refines the constants' precision. Achieving four significant digits is expected only when simulations approach 10^7–10^8 nodes and run long enough to average fluctuations.
