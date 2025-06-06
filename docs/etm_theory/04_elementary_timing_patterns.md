## 4. Elementary Timing Patterns

Elementary timing patterns specify the fundamental rhythmic structures that serve as building blocks for all higher ETM constructs. Each pattern is characterized by its phase advancement rate, spatial node configuration, stability metrics, and interaction properties. The patterns presented in this chapter have been validated through simulation and serve as canonical references for particle‑level modeling.

### 4.1 Electron‑Type Timing Pattern

#### Definition 4.1: Electron‑Type Timing Pattern

**Statement**: The electron-type pattern is a metastable lepton timing configuration characterized by a uniform phase advancement rate  
\(\Delta \theta_{\mathrm{e}} = 0.05\) (yielding a 20‑tick period). Its node arrangement and stability metrics are optimized for compatibility with proton-type patterns, enabling the formation of atomic orbitals.

**Formal Expression**:
\[
\theta_{\mathrm{e}}(t+1) = \bigl(\theta_{\mathrm{e}}(t) + 0.05\bigr) \bmod 1
\]

**Node Configuration**:

| Relative Position | Timing Rate | Role                |
|------------------:|------------:|-------------------- |
| (0, 0, 0)         | 0.7         | electron_core       |
| (±1, 0, 0)        | 0.5         | orbital_interface   |
| (0, ±1, 0)        | 0.5         | orbital_interface   |
| (±2, 0, 0)        | 0.3         | orbital_cloud       |

This configuration reflects the distributed nature of the electron timing pattern: a coherent core surrounded by an interface shell and a sparse orbital cloud, facilitating interaction with proton fields.

**Stability Metrics** (empirically derived):

- Core coherence: 0.85
- Orbital compatibility: 0.90
- Interaction flexibility: 0.88
- Binding capability: 0.92

**Implementation Requirements**:

1. Initialize the identity with phase \(\theta_{\mathrm{e}} \in [0,1)\) and advancement rate \(\Delta \theta_{\mathrm{e}} = 0.05\).
2. Construct the node list as specified above.  
   In code, this corresponds to `ElectronTimingPattern()` in `etm/particles.py`.
3. Ensure phase advancement occurs once per tick according to the global update protocol (see Rule R1).
4. Validate stability metrics during initialization; reject configurations with metrics below established thresholds.
5. Track phase evolution and node interactions to detect possible transitions or decay events.

**Physical Interpretation**:  
The electron-type timing pattern models the discrete temporal rhythm associated with an electron in ETM. The 20‑tick period and node arrangement provide a spatially extended yet coherent pattern capable of coupling to proton-type recruiters, resulting in atomic orbital formation. The metastable nature of the pattern allows transitions via photon absorption or emission while preserving lepton number.

**Validation Status**: ✅ **Experimentally confirmed** through hydrogen-atom simulations demonstrating stable electron–proton timing coherence for more than 100 ticks with coherence strength exceeding 0.95.

---

When extending this subsection or refining the stability metrics, it may be helpful to rerun the existing electron orbital simulations (`ETMEngine` with `ElectronTimingPattern`) and share updated statistics such as coherence strength and binding energy. These results can then be incorporated into the documentation to strengthen the empirical foundation of the pattern.

