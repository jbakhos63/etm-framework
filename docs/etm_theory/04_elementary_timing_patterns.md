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

=======
