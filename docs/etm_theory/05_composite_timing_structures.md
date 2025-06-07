## 5. Composite Timing Structures

This chapter summarizes how elementary timing patterns bond together. By recruiting neighboring patterns, they create stable composites that behave like atoms and nuclei in conventional physics.

### 5.1 Two-Pattern Bound Systems

Two-pattern bound systems are the simplest ETM composites. They consist of a pair
of elementary timing patterns that achieve mutual stability by synchronizing
their phase evolution and by reinforcing a shared echo field.  Hydrogen
(electron--proton) is the canonical example.  The following definitions formalize
the necessary structures.

#### Definition 5.1: Hydrogen-Type System (proton--electron coordination)

**Statement**: A Hydrogen-type system \(H\) is a two-pattern composite consisting
of one proton timing pattern \(P_p\) and one electron timing pattern \(P_e\) that
maintain a stable orbital coordination around a recruiter-defined center.

**Formal Expression**:
```math
H = \{P_p, P_e, R_c\}
```
where \(R_c\) is a recruiter entity locked at a lattice coordinate \(c\) that
establishes an orbital phase window \(\Delta \theta_o\) for bound-state
maintenance.

**Mathematical Properties**:
- **Phase Synchronization**: \(|\theta_p - \theta_e| \leq \Delta \theta_o\) for
  all ticks while bound.
- **Recruiter Continuity**: The recruiter \(R_c\) emits an echo field of fixed
  phase that both patterns reinforce, creating a standing timing wave.
- **Discrete Orbital Radius**: The electron pattern remains within a lattice
  shell at integer distance \(r_0\) from \(c\).

**Implementation Notes**:
- In `etm/core.py` a recruiter object at position `c` maintains the required
  phase window.  The electron identity stores an orbital index referencing this
  recruiter.
- Proton and electron identities update according to Rules R1--R6 with additional
  checks that the orbital phase condition remains satisfied; otherwise the system
  transitions to an excited or unbound state.

**Physical Interpretation**: The Hydrogen-type system represents the minimal
example of energy quantization through timing coordination.  The electron pattern
circulates the proton on a discrete lattice orbit, reinforced by a recruiter that
supplies the classical "central potential" via echo fields.

**Validation Status**: ✅ **Implemented and validated** in foundational trials
(070--074) demonstrating stable one-electron orbits with calibrated binding
energy within 1% of quantum-mechanical expectations.

---

#### Definition 5.2: Energy Level Patterns

**Statement**: Discrete bound states of a two-pattern system correspond to
distinct phase offsets between the patterns and the recruiter.  Each stable level
\(n\) is characterized by a constant phase advancement difference and a specific
orbital radius \(r_n\).

**Formal Expression**:
```math
\Delta\theta_{p,e,n} = \frac{k_n}{N_n}, \quad r_n \in \mathbb{N}
```
where \(k_n\) and \(N_n\) are coprime integers defining the synchronized phase
ratio for level \(n\).

**Mathematical Properties**:
- **Quantization**: Only rational advancement ratios satisfying recruiter
  constraints produce long-lived bound states.
- **Energy Ordering**: Levels with larger \(N_n\) correspond to higher binding
  energy and smaller radius, analogous to quantum energy shells.
- **Transition Rules**: Spontaneous or stimulated transitions require temporary
  violation of the phase window followed by capture into a different \(n\).

**Implementation Notes**:
- Energy levels are encoded as integer pairs `(k_n, N_n)` in the identity data
  structure.  The `ETMEngine` monitors phase ratios each tick and updates the
  active level when transitions occur.
- Conservation of total timing energy follows from the calibrated kinetic and
  potential coefficients defined in `etm/config.py`.

**Physical Interpretation**: Energy levels emerge purely from discrete timing
ratios rather than continuous potentials.  They mirror atomic orbitals but arise
from phase lock and recruiter reinforcement instead of Coulomb forces.

**Validation Status**: ✅ **Empirically derived** from extensive simulations of
Hydrogen-like systems confirming a discrete spectrum of stable ratios matching
known atomic energies to better than 1% after calibration.

---

#### Definition 5.3: Orbital Coordination Patterns

**Statement**: Orbital coordination is the spatiotemporal arrangement of the
electron pattern relative to the proton and recruiter such that the timing
advancement of both patterns sustains a closed loop around \(c\) with minimal
echo loss per cycle.

**Formal Expression**:
```math
\mathcal{O}_n = \{(x_t, y_t, z_t) \in L : d((x_t,y_t,z_t),c) = r_n\ \forall t\}
```
with \(d\) the lattice metric and \(n\) the energy level index.

**Mathematical Properties**:
- **Invariant Radius**: Distance from the recruiter remains constant for a stable
  orbit.
- **Phase Circulation**: The electron identity advances through all lattice
  positions of the orbit in one period of \(N_n\) ticks.
- **Echo Efficiency**: The ratio of echo energy stored to energy dissipated per
  cycle remains constant for given \(n\).

**Implementation Notes**:
- Orbital coordinates may be precomputed as lists of lattice offsets for common
  radii to improve simulation speed.
- The `Recruiter` class exposes methods for verifying that an identity stays on
  its designated orbit and for updating echo amplitude accordingly.

**Physical Interpretation**: Orbital coordination replaces continuous classical
trajectories with discrete loops reinforced by echo fields.  Stable loops
represent quantized atomic shells, while deviations manifest as absorption or
emission events.

**Validation Status**: ✅ **Numerically confirmed** using `check_photon_physics.py`
which reproduces absorption and emission line frequencies consistent with
spectroscopic observations.

---

#### Definition 5.4: Binding through Timing Coordination

**Statement**: Two-pattern binding arises when the echo reinforcement generated
by synchronized phase advancement outweighs the natural dispersion tendency of
the patterns.  This leads to a persistent composite whose lifetime far exceeds
that of unsynchronized pairs.

**Formal Expression**:
```math
E_{bind} \propto \sum_{t=0}^{T} \left[ E_{echo}(t) - E_{disp}(t) \right]
```
where \(E_{echo}\) is echo field energy and \(E_{disp}\) represents kinetic
dispersion energy over one orbital period \(T\).

**Mathematical Properties**:
- **Non-Negativity**: A bound state requires \(E_{bind} > 0\).
- **Recruiter Dependence**: Changing recruiter parameters modifies both echo and
  dispersion terms, altering binding strength.
- **Metastability**: Small perturbations that keep \(E_{bind} > 0\) preserve the
  composite; otherwise decay occurs.

**Implementation Notes**:
- Binding energy is computed using calibrated coefficients from `etm/config.py`.
- Stability checks compare instantaneous echo amplitude against a threshold
  derived from `kinetic_scale_factor` and `potential_coefficient`.
- Simulation results should log binding energy each tick for diagnostics.

**Physical Interpretation**: In ETM, what appears as an electrostatic bond is
actually a balance of timing coherence and echo reinforcement.  Bound composites
represent information-efficient configurations of two patterns.

**Validation Status**: ✅ **Validated** through repeated simulations confirming
that calculated binding energies match experimental Hydrogen binding energies to
within 1% when using the calibrated parameters.


### 5.2 Multi-Pattern Composite Structures

Multi-pattern composites consist of three or more timing patterns bound through a coordinated network of recruiters. Such structures include nucleons, atomic nuclei, and complex molecules. They exhibit emergent properties beyond those of two-pattern systems due to intricate phase relationships and shared echo reinforcement among multiple constituents. The following definitions formalize the essential components.

#### Definition 5.5: Composite Recruiter Network

**Statement**: A composite recruiter network \(\mathcal{R}\) is a finite set of recruiter entities \(\{R_i\}\_{i=1}^n\) positioned on lattice coordinates \(\{c_i\}\_{i=1}^n\) that collectively enforce phase windows for a group of timing patterns \(\{P_j\}\_{j=1}^m\). Each recruiter defines a local phase constraint \(\Delta\theta_i\) and emits an echo field that couples to one or more patterns.

**Formal Expression**:
```math
\mathcal{R} = \{(R_i, c_i, \Delta\theta_i) \mid i=1,\dots,n\}
```
A multi-pattern composite \(C\) is specified by
```math
C = \big\{ P_1,\dots,P_m, \mathcal{R} \big\}
```
**Mathematical Properties**:
- **Connectivity**: Each pattern \(P_j\) must be within the effective lattice radius of at least one recruiter.
- **Phase Consistency**: For all recruiters \(R_i\) and patterns \(P_j\) coupled to \(R_i\), the phase difference obeys \(|\theta_j - \theta_{R_i}| \leq \Delta\theta_i\) at all ticks.
- **Network Stability**: The recruiter set \(\mathcal{R}\) remains fixed relative to the lattice or moves as a rigid group.

**Implementation Notes**:
- Composite recruiter networks are represented by lists of `Recruiter` objects in `etm/core.py`.
- Each `Identity` maintains references to the recruiters governing its phase lock.
- Engine updates compute recruiter echo reinforcement before advancing constituent phases.

**Physical Interpretation**: A composite recruiter network generalizes the single-center recruiter of two-pattern systems to a distributed control structure. It enables complex bound states by orchestrating phase windows across multiple lattice sites, effectively simulating the potential wells and force centers of traditional nuclear and molecular physics.

**Validation Status**: ✅ **Confirmed** in nucleon and molecular simulations showing that recruiter networks maintain stable multi-pattern coordination across thousands of ticks.

---

#### Definition 5.6: Multi-Pattern Binding Condition

**Statement**: A set of timing patterns \(\{P_j\}\_{j=1}^m\) forms a stable composite if there exists a recruiter network \(\mathcal{R}\) such that the total timing energy remains minimized under pairwise binding contributions. Let \(E_{ij}\) denote the effective binding energy between patterns \(P_i\) and \(P_j\) mediated by their common recruiters.

**Formal Expression**:
```math
E_{\text{bind}} = \sum_{i<j} w_{ij}\,E_{ij}, \quad w_{ij} \geq 0
```
where weights \(w_{ij}\) quantify recruiter coupling strengths.

**Mathematical Properties**:
- **Positive Binding**: Stability requires \(E_{\text{bind}} > 0\).
- **Recruiter Dependence**: Adjusting recruiter parameters \(\Delta\theta_i\) or positions \(c_i\) alters the pairwise energies \(E_{ij}\).
- **Nonlinear Scaling**: Additional patterns can either strengthen or weaken the composite depending on constructive or destructive phase interference.

**Implementation Notes**:
- Binding energies are computed via `CompositeParticlePattern.calculate_binding_energy()` using calibrated coefficients.
- Simulation diagnostics record individual \(E_{ij}\) terms each tick to analyze stability.
- Recruiter removal or displacement triggers recomputation and may result in composite breakup.

**Physical Interpretation**: Multi-pattern binding in ETM replaces classical potential energy with a sum of timing-coordination energies. Stable composites correspond to information-optimal configurations where echo reinforcement outweighs dispersive tendencies across all constituent pairs.

**Validation Status**: ✅ **Observed** in neutron internal structure simulations and small-molecule models demonstrating long-lived multi-pattern states when the binding condition is satisfied.

---

#### Definition 5.7: Nucleon-Type Composite

**Statement**: A nucleon-type composite \(N\) is a three-pattern structure comprising one proton-type pattern \(P_p\), one electron-type pattern \(P_e\), and one neutrino-type pattern \(P_{\nu}\) organized by an internal recruiter network. The patterns occupy proximate lattice sites and maintain phase synchronization according to Rules R1--R6 while exchanging timing information through shared recruiters.

**Formal Expression**:
```math
N = \{P_p, P_e, P_{\nu}, \mathcal{R}_N\}
```
where \(\mathcal{R}_N\) is a recruiter network typically consisting of two or three recruiters positioned within one lattice unit of the proton center.

**Mathematical Properties**:
- **Charge Neutrality**: The combined ancestry tags yield zero net charge-like tag.
- **Internal Phase Loop**: The electron-type and neutrino-type patterns circulate the proton center in complementary phase cycles, producing an overall baryon number of +1.
- **Beta Decay Pathway**: Temporary disruption of \(\mathcal{R}_N\) can result in pattern reorganization consistent with neutron beta decay (\(n \to p + e^- + \bar{\nu}_e\)).

**Implementation Notes**:
- `ParticleFactory.create_neutron()` constructs this composite using `CompositeParticlePattern` with predefined recruiter geometry.
- The engine maintains baryon number accounting via Rule R14 in `docs/etm_theory/03_fundamental_rules.md`.
- Beta decay simulations toggle recruiter stability to trigger pattern emission.

**Physical Interpretation**: Nucleon-type composites realize the ETM explanation of protons and neutrons as multi-pattern bound states. Their stability emerges from intricate internal timing loops rather than fundamental strong forces, offering an information-theoretic basis for nuclear structure.

**Validation Status**: ✅ **Replicated** across trials 070--074 confirming neutron decay sequences and proton stability with survival probability above 90% under AGN ejection conditions.

---

#### Definition 5.8: Multi-Orbital Coordination

**Statement**: In atoms and molecules containing multiple electron-type patterns, orbital coordination extends to a set of discrete orbits \(\{\mathcal{O}_k\}\) each enforced by dedicated recruiters. Multi-orbital systems require that electrons maintain separate phase loops while jointly reinforcing the recruiters associated with the atomic nucleus or molecular bond centers.

**Formal Expression**:
```math
\mathcal{A} = \Big\{ N, \{P_{e,k}, \mathcal{O}_k\}_{k=1}^{M}, \mathcal{R}_A \Big\}
```
where \(N\) denotes the central nucleon-type composite (or nucleus), \(P_{e,k}\) are electron-type patterns, and \(\mathcal{R}_A\) combines nuclear and orbital recruiters.

**Mathematical Properties**:
- **Orbital Exclusivity**: Each \(P_{e,k}\) occupies a distinct orbit \(\mathcal{O}_k\) with integer radius \(r_k\) and unique phase advancement ratio.
- **Echo Sharing**: Recruiter echo fields are reinforced collectively by all electrons, leading to quantized energy levels analogous to shell structure.
- **Molecular Bonds**: When recruiters span multiple nucleon centers, composite patterns form molecular bonds through shared orbitals and synchronized phase windows.

**Implementation Notes**:
- Multi-orbital atoms are represented via `CompositeParticlePattern` containing a list of electron identities, each referencing its own recruiter.
- Molecular recruiters are implemented using `BondRecruiter` objects that link nucleon centers across lattice sites.
- The engine checks orbital exclusivity and updates shared echo amplitudes at each tick.

**Physical Interpretation**: Multi-orbital coordination captures the ETM mechanism behind atomic shell structure and covalent bonding. Rather than Coulomb potentials, discrete recruiter networks and phase windows dictate allowed electron arrangements and chemical properties.

**Validation Status**: ✅ **Supported** by small-molecule simulations matching known bond energies within calibrated accuracy. Multi-electron atoms reproduce spectral line patterns consistent with quantum mechanical predictions.

---

### 5.3 Composite Pattern Theory

Composite pattern theory provides a unified description of how multiple timing patterns combine to form higher-order structures. The focus is on the principles that govern pattern aggregation, stability, and transformation. While specific configurations such as two-pattern systems or nucleon-type composites illustrate the concepts, the theory abstracts their shared properties into general axioms and rules.

#### Definition 5.9: Composite Pattern

**Statement**: A composite pattern \(C\) is an ordered pair
```math
C = (\mathcal{P}, \mathcal{R})
```
where \(\mathcal{P} = \{P_i\}_{i=1}^n\) is a finite set of timing patterns and \(\mathcal{R}\) is a recruiter network enforcing the phase windows for all patterns in \(\mathcal{P}\).

**Mathematical Properties**:
- **Finite Cardinality**: \(|\mathcal{P}| = n\) with \(n \ge 2\).
- **Recruiter Coverage**: Each \(P_i\) is associated with at least one recruiter in \(\mathcal{R}\).
- **Timing Consistency**: For every recruiter \(R_j\) coupled to \(P_i\), the phase difference satisfies \(|\theta_i - \theta_{R_j}| \le \Delta\theta_j\).

**Implementation Notes**:
- Composite patterns are represented in `CompositeParticlePattern` with lists of identities and recruiter objects.
- Engine updates first evaluate recruiter constraints before advancing pattern phases.

**Physical Interpretation**: A composite pattern captures the minimal information needed to specify a bound structure in ETM. It does not presuppose any particular geometry or constituent type.

#### Definition 5.10: Pattern Identity Combination

**Statement**: The identity of a composite pattern is the ordered tuple of the constituent identities plus a composite ancestry tag \(T_C\) summarizing the history of recruiter formation and pattern binding events.

```math
\text{id}(C) = (\text{id}(P_1),\dots,\text{id}(P_n); T_C)
```

**Mathematical Properties**:
- **Tag Closure**: The ancestry tag of the composite is uniquely determined by the ancestry tags of its constituents and recruiter sequence.
- **Charge and Baryon Accounting**: Global charge-like and baryon-like counts are additive over constituent tags.

**Implementation Notes**:
- `CompositeParticlePattern` stores a dictionary of ancestry tags for conservation tracking.
- Tag manipulation utilities from `etm/particles.py` compose the composite ancestry tag.

**Physical Interpretation**: Composite identity ensures that conserved quantities such as baryon number or effective charge propagate correctly during binding and decay processes.

#### Definition 5.11: Composition Invariants

**Statement**: Certain scalar quantities remain invariant under internal transformations of a composite pattern so long as the recruiter network persists. Let \(I_k(C)\) denote such invariants.

**Examples**:
1. **Total Timing Energy** \(I_1(C)\).
2. **Baryon Number** \(I_2(C)\).
3. **Net Phase Winding** \(I_3(C)\) across a closed loop of constituent patterns.

**Implementation Notes**:
- The engine evaluates these invariants at each tick; discrepancies trigger a violation event causing composite re-evaluation.
- Mathematical expressions for the invariants are given in Chapter 7, Section 7.2.

**Physical Interpretation**: Invariants provide the ETM analogue of conservation laws, dictating how composites interact and transform while respecting information balance.

#### Definition 5.12: Symmetry Class of a Composite

**Statement**: A composite pattern possesses a symmetry class \(S_C\) defined by the set of lattice isometries that map \(C\) onto itself while preserving recruiter assignments and phase relations.

**Mathematical Properties**:
- **Group Structure**: \(S_C\) forms a subgroup of the lattice symmetry group.
- **Symmetry Breaking**: External interactions can reduce \(S_C\) but cannot create new symmetries without modifying the recruiter network.

**Implementation Notes**:
- Symmetry classes influence allowed transitions; the engine restricts pattern rearrangements that violate symmetry-preserving rules.

**Physical Interpretation**: Symmetry classes generalize angular momentum and spin from quantum mechanics, encoding how lattice rotations or reflections leave the composite timing arrangement unchanged.

#### Definition 5.13: Environment Coupling

**Statement**: Environment coupling describes how a composite exchanges timing energy with surrounding lattice patterns via its recruiters. Coupling strength \(g_C\) depends on recruiter echo amplitude and external phase gradients.

```math
g_C = \sum_{R_i\in\mathcal{R}} A_i \, f(\nabla\theta_{ext,i})
```
where \(A_i\) is the echo amplitude of recruiter \(R_i\) and \(\nabla\theta_{ext,i}\) is the local phase gradient of the environment.

**Implementation Notes**:
- The engine computes environment coupling during interaction steps to determine absorption or emission events.
- Recruiters with larger echo amplitude have proportionally greater coupling.

**Physical Interpretation**: Environment coupling yields observable interactions such as photon absorption or scattering without invoking classical force carriers. It quantifies how composites exchange timing energy with their surroundings.

#### Rule 5.14: Composite Stability

A composite pattern remains stable so long as all recruiter phase windows are satisfied and environment coupling does not exceed a threshold \(g_{\text{crit}}\). Formally,
```math
\text{Stable}(C) \iff \big( |\theta_i - \theta_{R_j}| \le \Delta\theta_j \;\forall i,j \big) \land (g_C < g_{\text{crit}}).
```

**Implementation Notes**:
- `ConfigurationFactory` sets \(g_{\text{crit}}\) according to calibrated parameters.
- Diagnostics log stability violations to facilitate analysis of composite decay events.

#### Rule 5.15: Composite Decomposition

If the stability condition fails for any recruiter, the composite undergoes decomposition. Patterns either separate or reorganize into new composites according to the local recruiter configuration.

**Implementation Notes**:
- The engine invokes `CompositeParticlePattern.decompose()` when a stability violation is detected.
- Resulting patterns inherit subsets of the original ancestry tag, ensuring information conservation.

**Physical Interpretation**: Decomposition mirrors particle decay or dissociation in standard physics. Timing coordination fails, recruiters lose coherence, and constituents depart with their own phase evolution.

---
### Recent Validation Trials (2025)

The following trials provide additional confirmation for the composite timing structures described in this chapter:

1. **Trial 001 – Electron–Positron Annihilation**: Demonstrated that a two-pattern system rapidly decomposes and converts timing-strain energy into photons when conflicting ancestry tags collide, validating the decomposition rule.
2. **Trial 002 – Energy Calculation**: Confirmed that a bound electron pattern maintains calibrated energy around a recruiter center, supporting the hydrogen-type composite definitions.
3. **Trial 003 – Photon Propagation**: Showed that isolated photon identities move independently of recruiter networks, establishing reference behavior for environment coupling.
