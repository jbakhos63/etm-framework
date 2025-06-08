# AI Developer Guide – ETM Framework

This guide explains how to work with the Euclidean Timing Mechanics simulation library. It summarizes the module architecture, describes validated parameters, and outlines recommended workflows for extending the code base.

## 1. Framework Overview
ETM represents particles as timing patterns across a discrete lattice. Node interactions alter local tick rates, and all propagation arises from this timing logic. After initialization no velocity or force is imposed externally; motion results solely from the ETM update rules.

Development proceeds in two phases:
1. **Codex Validation** – use lattices up to about 30×30×30 nodes to verify each simulation in this repository.
2. **Home Computer Scale-Up** – once stable, rerun the simulations on larger lattices (50³ or more) for extended periods to refine constant measurements.

The file `docs/ETM_CONSTANT_DERIVATION_PLAN.md` details how these simulations map to fundamental constants.

## 2. Directory Layout
```
etm/
  config.py      # Configuration classes and constants
  core.py        # Engine controlling timing updates
  particles.py   # Particle timing patterns
trials/          # Validation trials with notes and results
```
Additional research documents are stored in the `docs/` directory.

## 3. Installation
Follow the steps in the main `README.md`:
```bash
pip install -r requirements.txt
python test_modules.py
```
Use Python 3.10 or later.

## 4. Validated Parameters
The configuration module contains calibrated constants that must remain unchanged unless new validations are performed.
```python
connectivity = 8
kinetic_scale_factor = 1000.0
potential_coefficient = 0.003723
enable_passive_coexistence = True
default_conflict_resolution = SYMBOLIC_MUTATION
```
Altering these values invalidates previous scientific achievements.

## 5. Running Trials
Each trial folder contains:
- `run_trial.py` – script to execute the simulation
- `notes.md` – description of goals and results
- `*_results.json` – data output

Run a trial with
```bash
python trials/005_photon_gradient/run_trial.py
```
Examine the JSON output and accompanying notes for interpretation.

Recent trials illustrate core functionality:
- **004** Photon speed baseline
- **005** Photon deflection by echo gradients
- **006** Photon absorption strength
- **007** Photon emission eligibility
- **008** Electron energy gain after absorption

## 6. Adding New Features
1. Create a branch for your changes.
2. Add new modules or extend existing ones in the `etm/` package.
3. Provide unit tests in `test_modules.py` or a new file.
4. Document new logic thoroughly in `docs/` and update the research plan.
5. Ensure `python test_modules.py` passes before committing.

## 7. Research Guidelines
- Conform to the ETM Simulation Research Plan (`docs/ETM_SIMULATION_RESEARCH_PLAN.md`).
 - Maintain the rule that **all dynamics after initialization arise from ETM logic alone**.
   Any `velocity` attribute is applied once at creation to set an initial displacement
   and is then cleared so that subsequent movement results only from ETM return rules.
- Record simulation environments and parameters so results can be reproduced.

By following these practices, researchers can build upon the ETM framework while preserving prior validations.
