# ETM Framework – Euclidean Timing Mechanics

Euclidean Timing Mechanics (ETM) models physical reality as discrete timing relationships between nodes on a lattice. Particles are coherent timing patterns that propagate and interact purely through timing logic. This repository provides a modular Python implementation with validated test cases.

## Key Features
- **Model B detection-triggered conflict resolution**
- **Calibrated energy computation (<1% error)**
- **Enhanced proton timing patterns (>90% AGN survival)**
- **Photon–electron interaction framework**
- **Nucleon internal structure modeling**

## Repository Structure
```
etm-framework/
├── etm/                 # Core engine modules
│   ├── config.py        # Configuration classes and validated parameters
│   ├── core.py          # ETM engine implementation
│   └── particles.py     # Particle timing patterns
├── trials/              # Validation simulations
├── docs/                # Research documentation
├── test_modules.py      # Unit tests covering all modules
└── check_photon_physics.py
```

## Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/etm-framework.git
cd etm-framework
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Verify the installation
```bash
python test_modules.py
```
Expected output is `ALL TESTS PASSED!` confirming that the configuration, core engine, particles, and integration tests run correctly.

### Backward Compatibility
As ETM logic improves the particle timing patterns may be redefined. Earlier trials must still run successfully under the updated code. Backward compatibility therefore refers to preserving the **behavior** of validated experiments, not freezing the internal definitions of particles.

## Running Validation Trials
Each numbered folder in `trials/` contains scripts and documentation for a specific simulation.
To execute a trial run:
```bash
python trials/004_photon_speed/run_trial.py
```
Results are written as JSON and summarized in the accompanying `notes.md` file.
Recent trials include:
- **Trial 004** – baseline photon propagation across a 21×21×21 lattice
- **Trial 005** – photon deflection in an echo-field gradient
- **Trial 006** – orbital absorption strength of a hydrogen photon
- **Trial 007** – eligibility of hydrogen-photon emission
- **Trial 008** – electron energy gain from photon absorption
- **Trial 009** – electron–positron attraction via echo gradients
- **Trial 010** – convergence-time measurement for electric force
- **Trial 011** – moving electron echo profile
- **Trial 012** – magnetic deflection of a nearby electron
- **Trial 013** – attraction between parallel moving electrons
- **Trial 014** – preliminary fine structure constant estimate
- **Trial 015** – baseline Planck time analogue
- **Trial 016** – baseline Planck length analogue
- **Trial 017** – electron repulsion after an initial approach
- **Trial 018** – extended electron–positron annihilation baseline
- **Trial 019** – extended energy calculation on a larger lattice
- **Trial 020** – extended photon propagation baseline
- **Trial 021** – extended photon speed baseline
- **Trial 022** – extended photon gradient deflection
- **Trial 023** – extended photon absorption baseline
- **Trial 024** – extended photon emission baseline
- **Trial 025** – extended electron absorption energy
- **Trial 026** – extended electric attraction
- **Trial 027** – extended electric force measurement
- **Trial 028** – extended magnetic field measurement
- **Trial 029** – extended magnetic deflection
- **Trial 030** – extended parallel current attraction
- **Trial 031** – extended fine structure constant estimate
- **Trial 032** – extended Planck interval estimate
- **Trial 033** – extended Planck length estimate
- **Trial 034** – extended electron repulsion baseline (short test run confirmed
  approach and repulsion)

## Research Plan
The repository follows a staged development strategy:
1. **Codex Validation** – implement each simulation using lattices up to about 30×30×30 nodes to ensure code correctness in this environment.
2. **Home Computer Scale-Up** – run the same simulations on larger lattices (50³ or more) for extended durations to refine constants.
3. **Extended Scale and Neutrino Exploration** – explore lattices approaching 10⁸ nodes while testing neutrino timing patterns.
4. **Particle Resolution Studies** – vary lattice resolution and refine particle definitions to determine minimal stable node counts.
5. **Composite Particle Review** – beginning with trial 047, revisit protons and other composites to optimize their timing patterns and verify backward compatibility.

See `docs/ETM_SIMULATION_RESEARCH_PLAN.md` and `docs/ETM_CONSTANT_DERIVATION_PLAN.md` for details. Both documents emphasize that after initialization **all motion and interactions must arise exclusively from ETM logic**. Any velocity specified for an identity is used only once at creation to shift its starting position; further movement must result solely from ETM return rules.

## Development Guidelines
- Preserve validated parameters in `etm/config.py`
- Add new features in modular form with accompanying tests
- Document all simulation results in the `docs` and `trials` directories
- When particle definitions or rules change, rerun earlier successful trials to confirm backward compatibility.

The ETM framework is released under the MIT license. Researchers may reproduce and extend the work provided that the underlying timing logic is maintained.

### 2025 Trial Update
All thirty-three validation trials were rerun with the new single-use velocity logic. Results matched previous outputs, confirming ETM motion arises solely from timing returns.
