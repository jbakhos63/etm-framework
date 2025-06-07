## 4. Elementary Timing Patterns

This chapter introduces the elementary timing patterns that serve as the building blocks for all ETM composites. A detailed outline is provided in `04_elementary_timing_patterns_outline.txt`.

### 4.1 Concept of Timing Patterns

The concept of a **timing pattern** generalizes the notion of a particle within Euclidean Timing Mechanics. In ETM each elementary entity is specified entirely by the deterministic evolution of a discrete phase value together with a structured record of interactions. A timing pattern is therefore defined as an ordered triple of (phase state, interaction history, configuration parameters) that evolves autonomously under the foundational rules of ETM. Timing patterns provide the foundation for constructing more complex composites that manifest as atoms, molecules, and macroscopic objects.

---

#### Definition 4.1: Timing Pattern

**Statement**: A timing pattern \(P\) is a discrete-time process defined by a phase variable \(\theta \in [0,1)\), an advancement rate \(\Delta \theta\), and a set of identity tags describing its classification. At each tick \(t\in\mathbb{N}\) the pattern updates its phase according to

```math
\theta(t+1) = (\theta(t) + \Delta \theta) \bmod 1.
```

The timing pattern also maintains a chronologically ordered list of interaction events \(H = [e_0, e_1, \ldots]\) where each event records the tick index, position, and resolution outcome. The pair \((\theta, H)\) constitutes the minimal state required for deterministic propagation.

**Mathematical Properties**:
- **Deterministic evolution**: Given \(\theta(t)\) and \(\Delta\theta\), the future phase state is uniquely determined.
- **Finite memory footprint**: Interaction history may be truncated or summarized without altering present dynamics.
- **Isolated autonomy**: In the absence of interactions, a timing pattern evolves independently from other patterns.

**Implementation Notes**:
- `Identity` objects in `etm/core.py` implement timing patterns by storing `theta`, `delta_theta`, and lists of mutation and interaction events.
- Update functions must apply modular arithmetic to guarantee \(\theta\in[0,1)\) after each tick.
- Tags such as `module_tag` and `ancestry` encode the classification of the pattern (electron-like, proton-like, etc.).

**Physical Interpretation**: Timing patterns represent the smallest indivisible building blocks of physical reality in ETM. Their deterministic phase evolution replaces the probabilistic wavefunction of quantum mechanics while still reproducing observable interference and interaction outcomes through structured echo and recruiter mechanisms.

---

#### Definition 4.2: Phase Configuration

**Statement**: The phase configuration of a timing pattern is the ordered pair \((\theta, \Delta\theta)\) specifying both the current phase and the advancement increment per tick. This pair determines the instantaneous dynamical state of the pattern.

**Formal Expression**:
```math
\text{PhaseConfig}(P) = (\theta, \Delta\theta).
```

**Properties**:
- **Periodicity**: If \(\Delta\theta = p/q\) for integers \(p,q\) with \(\gcd(p,q)=1\), then the pattern has an exact period of \(q\) ticks.
- **Stability scaling**: In `etm/config.py` the parameter `stability_scale_factor` couples \(\Delta\theta\) to energy and survivability metrics.
- **Phase distance**: Distinguishing two patterns at tick \(t\) uses the metric
```math
d_{\phi}(\theta_1,\theta_2)=\min(|\theta_1-\theta_2|,1-|\theta_1-\theta_2|).
```

**Implementation Notes**:
- All ETM modules requiring phase relationships should query the phase configuration rather than the raw phase value.
- Numerical precision of \(\Delta\theta\) should be preserved (e.g., double precision floats) to avoid cumulative drift.

---

#### Definition 4.3: Cycle Frequency

**Statement**: The cycle frequency \(f\) of a timing pattern is the reciprocal of its period measured in ticks, quantifying how many full phase cycles occur per tick interval.

**Formal Expression**:
```math
f = \frac{\Delta\theta}{1\ \text{tick}}.
```
For rational \(\Delta\theta=p/q\), the period is \(q\) ticks and \(f=p/q\) cycles per tick. For irrational \(\Delta\theta\), the phase never repeats exactly and \(f\) represents an incommensurable rotation number.

**Properties and Usage**:
- Timing patterns with similar cycle frequencies can resonate through recruiter echo reinforcement leading to composite formation.
- Energy estimates in `Identity.calculate_particle_energy` depend linearly on \(\Delta\theta\), linking cycle frequency to mass-like behavior.

**Implementation Notes**:
- Cycle frequency is an emergent quantity and need not be explicitly stored; it can be derived from `delta_theta` when required.
- Logging modules may track the number of completed cycles for diagnostics.

**Physical Interpretation**: Cycle frequency connects ETM timing patterns to observable energy scales. High-frequency patterns correspond to higher-mass particles, while low-frequency patterns manifest as neutrino-like or photon-like behaviors. Stable matter arises from patterns whose frequencies lock via recruiter networks into resilient composite structures.

---

### 4.2 Identity Attributes and Classification

Identities in ETM are distinguished not only by their phase dynamics but also by a finite set of attributes that encode charge-like, spin-like, and mass-like behavior. These attributes are realized symbolically using the ancestry and module tags within each `Identity` instance. They enable classification of timing patterns into categories analogous to elementary particle species.

#### Definition 4.4: Charge-Like Tag

**Statement**: A charge-like tag \(q\) is a symbolic marker appended to an identity's ancestry string indicating its interaction phase preference. Formally, let \(\Sigma_q\) be the set of allowable charge symbols. An identity with ancestry string \(a\) possesses charge \(q\in\Sigma_q\) if and only if
\[
  a = a_0 \oplus q,
\]
where \(\oplus\) denotes string concatenation.

**Properties**:
- **Conservation under propagation**: Charge-like tags persist through phase updates unless a detection-triggered mutation explicitly alters them.
- **Interaction mediation**: The echo field coupling strength is modulated by compatibility of charge-like tags between patterns.

**Implementation Notes**:
- In `etm/core.py` the ancestry string stores charge tags such as `"+"`, `"-"`, or neutral `"0"`.
- Detection events may invoke symbolic mutation to append or remove charge tags while preserving phase continuity.

---

#### Definition 4.5: Spin-Like Orientation

**Statement**: The spin-like orientation \(s\) of a timing pattern is a binary or integer label describing the orientation of its phase progression relative to the lattice. Let \(S=\{-1, +1\}\) represent two allowed orientations. A pattern has spin \(s\in S\) if its phase update rule obeys
\[
  \theta(t+1) = (\theta(t) + s\,\Delta\theta) \bmod 1.
\]

**Properties**:
- **Orientation reversal**: Interactions that flip spin correspond to multiplying \(s\) by \(-1\) while leaving \(\Delta\theta\) unchanged.
- **Composite coupling**: Stable bound states require net spin balance among constituent patterns.

**Implementation Notes**:
- The `Identity` class records spin using the field `orientation` with values `+1` or `-1`.
- Spin flipping during scattering is implemented in `ParticleFactory` helper functions.

---

#### Definition 4.6: Mass-Like Timing Inertia

**Statement**: Mass-like timing inertia \(m\) quantifies resistance of a timing pattern to phase perturbation. It is defined by the inverse of the allowed fractional change in \(\Delta\theta\) per detection event:
\[
  m = \Bigl(\frac{\delta\Delta\theta}{\Delta\theta}\Bigr)^{-1}.
\]
Here \(\delta\Delta\theta\) is the maximal change in advancement rate permitted by the current environment.

**Properties**:
- **Energy correspondence**: Greater mass-like inertia implies larger energy content as computed by `Identity.calculate_particle_energy`.
- **Stability indicator**: Patterns with high inertia resist timing disruptions and are more likely to survive in extreme echo environments.

**Implementation Notes**:
- Configuration parameters such as `kinetic_scale_factor` calibrate the numerical value of \(m\).
- Simulation scripts may adjust `delta_theta` within bounds derived from \(m\) when modeling interactions or composite formation.

---

### 4.3 Stable Individual Patterns

Stable individual timing patterns exhibit persistent phase configurations and interaction histories that remain self-consistent over arbitrarily long tick intervals. Such patterns correspond to the electron-, proton-, and neutrino-type identities in ETM. Their stability arises from internal timing coordination that resists echo disturbances and phase disruptions.

#### Definition 4.7: Electron-Type Pattern

**Statement**: An electron-type pattern is a metastable timing entity characterized by a central timing node of rate \(0.7\) and surrounding orbital interface nodes of rate \(0.5\). It includes outer cloud nodes with rate \(0.3\) that mediate recruiter echo exchange. Let \(E\) denote the set of timing nodes
\[
  E = \{n_0,(n_1,n_2,n_3,n_4),(n_5,n_6)\}
\]
with corresponding rates \((0.7,0.5,0.5,0.5,0.5,0.3,0.3)\). Phase coherence across these nodes yields an electron-type pattern when the ancestry tag contains the symbol `e` and mass-like inertia satisfies
\[
  m_e \approx 1.0.
\]

**Properties**:
- **Orbital compatibility**: The interface nodes enable phase locking with recruiter rings to form atomic orbitals.
- **Metastable behavior**: Stability metrics in `ElectronTimingPattern.stability_metrics` evaluate to values between 0.85 and 0.92, allowing long-lived yet reconfigurable states.

**Implementation Notes**:
- `ParticleFactory.create_electron()` instantiates this pattern using `ElectronTimingPattern` in `etm/particles.py`.
- Identity instances referencing an electron-type pattern set `fundamental_particle` accordingly and maintain the ancestry suffix `e`.

---

#### Definition 4.8: Proton-Type Pattern

**Statement**: A proton-type pattern employs a multi-shell arrangement of timing nodes to achieve high stability. The enhanced proton pattern uses a nuclear core node of rate \(1.0\), eight primary shell nodes of rate \(0.95\), an intermediate shell of rate \(0.85\), and outer edge connectors of rate \(0.75\). Denote the full node set by
\[
  P = \{c, s_i, i_j, e_k\mid i=1\dots8, j=1\dots8, k=1\dots6\}
\]
with timing rates \(r(c)=1.0\), \(r(s_i)=0.95\), \(r(i_j)=0.85\), and \(r(e_k)=0.75\). This configuration yields an AGN-survival probability exceeding 95%.

**Properties**:
- **High inertia**: The core and primary shell confer large mass-like timing inertia, producing a stable baryonic identity.
- **Cosmological viability**: `EnhancedProtonTimingPattern.calculate_agn_survival_probability` returns probabilities above 0.95 for strong echo environments.

**Implementation Notes**:
- `ParticleFactory.create_enhanced_proton()` constructs this pattern with stability metrics defined in `etm/particles.py`.
- Proton-type identities append the ancestry symbol `p` and set `fundamental_particle` to an `EnhancedProtonTimingPattern` instance.

---

#### Definition 4.9: Neutrino-Type Pattern

**Statement**: A neutrino-type pattern is a sparse timing entity with minimal interaction cross section. It contains a central node of rate \(0.1\) and two sparse interaction nodes of rate \(0.05\). Formally,
\[
  N = \{n_0,(n_1,n_2)\},\quad r(n_0)=0.1,\ r(n_1)=r(n_2)=0.05.
\]
Neutrino-type patterns carry the ancestry tag `ν` and propagate efficiently through recruiter networks without disrupting other identities.

**Properties**:
- **Matter transparency**: Stability metrics in `NeutrinoTimingPattern.stability_metrics` emphasize propagation efficiency and minimal echo disturbance.
- **Interaction mediation**: Neutrinos participate in weak interactions only when `enable_weak_interactions` is true in the configuration.

**Implementation Notes**:
- `ParticleFactory.create_neutrino()` provides a default neutrino-type pattern.
- Detection and interaction modules consult the ancestry tag `ν` to apply weak scattering rules.

---

### 4.4 Propagating Patterns

Propagating timing patterns transmit energy and information across the ETM lattice. Their dynamics are characterized by coordinated phase advancement and spatial translation. This section formalizes the photon-type pattern as the canonical propagating identity and defines the mechanics of wave packet propagation and detection-triggering events.

#### Definition 4.10: Photon-Type Pattern

**Statement**: A photon-type pattern is an electromagnetic timing disturbance that propagates through space via an expanding front of high-rate nodes. Let $C$ denote the core node with timing rate $1.5$ and $F(t)$ the set of propagation-front nodes at tick $t$. Initially
$$F(0)=\{f_i\mid r(f_i)=1.2\}.$$
Propagation proceeds by shifting each $f_i$ one lattice step per tick along the 8-connected directions while preserving relative phase. Edge nodes $E(t)$ with rate $1.0$ and extended nodes $X(t)$ with rate $0.8$ maintain coherence at larger radius. The ancestry tag contains the symbol `ph`.

**Properties**:
- **Electromagnetic coherence**: `PhotonTimingPattern.stability_metrics` report values near $0.99$ for electromagnetic coherence and propagation efficiency.
- **Space traversal**: Photons are cosmologically viable and traverse the lattice without mass-like inertia.
- **Orbital coupling**: The metric `orbital_coupling` describes interaction strength with electron orbitals.

**Implementation Notes**:
- `ParticleFactory.create_photon()` instantiates this pattern and calls `set_photon_energy` to adjust frequency and wavelength.
- The pattern nodes and timing rates are defined in `etm/particles.py` under `PhotonTimingPattern`.
- Photon identities use `ParticleType.PHOTON` and remain `STABLE` under normal conditions.

---

#### Definition 4.11: Wave Packet Propagation

**Statement**: Wave packet propagation is the coordinated translation of a set of timing nodes $\{n_k(t)\}$ such that for each tick
$$n_k(t+1)=n_k(t)+\delta p_k,$$
where $\delta p_k$ is a lattice displacement chosen from the engine's 8-connected neighbor set. The phase state at each node advances according to its $\Delta\theta$ while maintaining the ordering of phases across the packet.

**Formal Algorithm**:
1. For each node $n_k$ with position $p_k(t)$ compute neighbor positions via `ETMEngine.get_neighbors`.
2. Select $\delta p_k$ that maximizes echo reinforcement in the direction of propagation.
3. Update $p_k(t+1)=p_k(t)+\delta p_k$ and apply the phase update rule
$$\theta_k(t+1) = (\theta_k(t) + \Delta\theta_k) \bmod 1.$$
4. Repeat for all nodes in the packet.

**Implementation Notes**:
- Photon propagation uses this mechanism with front nodes moving outward every tick.
- Composite patterns may propagate by coupling multiple wave packets.
- The engine stores positions in `Identity.position` and updates them during `advance_tick`.

---

#### Definition 4.12: Detection-Triggering Event

**Statement**: A detection-triggering event occurs when a propagating pattern interacts with another identity or a boundary such that conflict resolution must be invoked. Formally a `DetectionEvent` instance $(e,\,p,\,t)$ is recorded with event type $e$ (e.g., `PHOTON_INTERACTION`), position $p$, and tick $t$. The event references the triggering particle and the affected identities.

**Properties**:
- **Model B behavior**: Detection events activate resolution methods specified by `ConflictResolutionMethod`, such as `SYMBOLIC_MUTATION`.
- **State mutation**: Affected identities may alter ancestry, phase, or spin based on the selected resolution.
- **Information recording**: Events are appended to `ETMEngine.detection_events` for later analysis.

**Implementation Notes**:
- The configuration flag `enable_detection_events` in `ETMConfig` controls whether events are logged.
- Photon absorption by an electron triggers a `PHOTON_INTERACTION` event resulting in phase reconfiguration.
- Detection events are essential for reproducing measurement-dependent phenomena while maintaining deterministic propagation prior to detection.

---
