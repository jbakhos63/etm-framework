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
=======
=======
