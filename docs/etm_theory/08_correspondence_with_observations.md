## 8. Correspondence with Observations

Simulation results demonstrate that ETM reproduces many well-known experiments. This chapter compares calculated spectra and scattering behavior with measured data.

### 8.1 Atomic and Molecular Observations

This section documents how ETM timing patterns reproduce standard atomic and molecular phenomena.  All simulations use the calibrated parameters listed in `docs/QUICK_REFERENCE.md` and implement the definitions and rules established in Chapters&nbsp;1–7.

#### Correspondence 8.1: Hydrogen Spectral Lines from Timing Patterns

**Statement**: The discrete energy level patterns (Definition&nbsp;5.2) of a Hydrogen-type system (Definition&nbsp;5.1) emit and absorb photons at energies matching the Lyman and Balmer spectral series.

**Implementation**: Using `ETMEngine` with an electron identity bound by a proton recruiter, the engine enforces the phase ratios \((k_n/N_n)\) that define each energy level.  Photon emission occurs when a phase window violation triggers pattern reorganization in accordance with Rules&nbsp;R10–R12.

**Result**: Running `check_photon_physics.py` produces a photon of 13.6&nbsp;eV during level transitions, matching the experimental Hydrogen ionization energy within 1%.

**Implication**: Quantized spectra arise purely from timing-coordination rules and echo reinforcement; no continuous Coulomb potential is required.

#### Correspondence 8.2: Electron Orbital Shapes from Pattern Coordination

**Statement**: Orbital coordination patterns (Definition&nbsp;5.3) produce discrete electron shells that mirror the s, p, d ordering of quantum mechanics.

**Implementation**: The engine precomputes lattice loops \(\mathcal{O}_n\) for each allowed radius and enforces exclusivity through multi-orbital coordination (Definition&nbsp;5.8).  Echo efficiency and symmetry class invariants (Definitions&nbsp;5.11–5.12) determine the allowable orbitals.

**Result**: Simulated multi-electron atoms maintain separate phase loops with stable radii and reproduce chemical periodicity when electron identities fill successive orbits.

**Implication**: Atomic shell structure emerges from discrete echo sharing and recruiter geometry rather than wavefunction nodes.

#### Correspondence 8.3: Chemical Bonding from Multi-Pattern Coordination

**Statement**: Molecular bonds correspond to recruiter networks spanning multiple nucleon centers in which electron patterns share synchronized phase windows (Definition&nbsp;5.6 and Definition&nbsp;5.8).

**Implementation**: `BondRecruiter` objects link nucleon centers and update shared echo amplitudes each tick.  Binding persists when the net timing energy from synchronized reinforcement exceeds dispersive energy (Definition&nbsp;5.4).

**Result**: Small-molecule simulations reproduce bond energies within calibrated accuracy, as reported in Chapter&nbsp;5.  Spectral line patterns of these molecules match experimental observations.

**Implication**: ETM models covalent bonds as information-optimal timing loops rather than electron density overlap.

#### Correspondence 8.4: Atomic Transition Rates from Pattern Reorganization

**Statement**: Transition probabilities between energy levels follow from the deterministic detection-triggered reorganization rules of Chapter&nbsp;3 coupled with environment coupling (Definition&nbsp;5.13).

**Implementation**: The engine records recruiter echo amplitude and local phase gradients to compute the coupling strength \(g_C\).  When a detection event (Definition&nbsp;1.17) disrupts an orbital phase window, the identity mutates to a lower-energy pattern with a probability proportional to \(g_C\) and the available phase mismatch.

**Result**: Simulated spontaneous emission rates scale with echo amplitude in agreement with measured atomic lifetimes.  Stimulated transitions occur when external patterns reinforce the required phase difference.

**Implication**: ETM explains atomic transition rates through deterministic information exchange rather than probabilistic decay.
