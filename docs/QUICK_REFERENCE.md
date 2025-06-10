# ETM Framework – Quick Reference

This card summarizes the essential commands and rules for working with the ETM simulation library.

## Setup
```bash
pip install -r requirements.txt
python test_modules.py
```
All tests must pass before running simulations.

## Critical Configuration
```python
from etm.config import ConfigurationFactory
config = ConfigurationFactory.validated_foundation_config("example")
```
Do **not** modify the validated constants in `etm/config.py` unless performing new validation.

## Running a Trial
```bash
python trials/004_photon_speed/run_trial.py
```
Results are stored in JSON format within the trial folder and explained in `notes.md`.

## Recent Trials
- 004 Photon speed baseline
- 005 Photon deflection in an echo gradient
- 006 Hydrogen-photon absorption strength
- 007 Photon emission from an electron
- 008 Electron energy change from absorption
- 018 Extended electron–positron annihilation
- 019 Extended energy calculation
- 020 Extended photon propagation
- 021 Extended photon speed
- 022 Extended photon gradient
- 023 Extended photon absorption
- 024 Extended photon emission
- 025 Extended electron absorption energy
- 026 Extended electric attraction
- 027 Extended electric force measurement
- 028 Extended magnetic field measurement
- 029 Extended magnetic deflection
- 030 Extended parallel current attraction
- 031 Extended fine structure constant estimate
- 032 Extended Planck interval estimate
- 033 Extended Planck length estimate
- 034 Extended electron repulsion (500 ticks on 51³ lattice)
- 035 Extended electron–positron annihilation (phase 3)
- 036 Extended energy calculation (phase 3)
- 037 Extended photon propagation (phase 3)
- 038 Extended photon speed (phase 3)
- 039 Extended photon gradient (phase 3)
- 040 Extended photon absorption (phase 3)
- 041 Extended photon emission (phase 3)
- 042 Extended electron absorption energy (phase 3)
- 043 Extended electric attraction (phase 3)
## Fundamental Rule
All motion, propagation, and effects after initialization must emerge only from ETM logic—no explicit velocity functions or external forces are allowed. Any `velocity` set on an identity is applied only at the first tick to establish an initial displacement and is then cleared.

For detailed guidance see `docs/AI_DEVELOPER_GUIDE.md`, the full `ETM_SIMULATION_RESEARCH_PLAN.md`, and `docs/ETM_CONSTANT_DERIVATION_PLAN.md`.
Use the optional `--sleep` argument in any trial's run script to slow down each tick if a background run needs to stay responsive.

### Development Phases
1. **Codex Validation** – use lattices up to about 30×30×30 nodes.
2. **Home Computer Scale-Up** – rerun on larger lattices (≥50³) for higher precision.
