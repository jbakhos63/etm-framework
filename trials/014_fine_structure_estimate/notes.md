# Trial 014 – Preliminary Fine Structure Constant

This trial inaugurates **Stage 5 – Fine Structure Constant** of the *ETM Simulation Research Plan*. Our goal is to combine prior electric, magnetic, and photon measurements to form a first estimate of the dimensionless fine structure constant in ETM units.

## Plan
1. Extract an effective ETM Coulomb constant from the convergence times of electron–positron pairs in Trial 010.
2. Use the baseline photon speed from Trial 004 and the hydrogen photon energy from Trial 008 to define provisional ETM analogues of `c` and `ħ`.
3. Combine these values to compute
   \[ \alpha_{\mathrm{ETM}} = \frac{k_e}{\hbar_{\mathrm{ETM}} c_{\mathrm{ETM}}}. \]

Because our lattices remain small (21×21×21), the numerical result will serve only as a proof of methodology.

## Execution
Running `run_trial.py` loads prior JSON results and performs the calculation. The script also stores the outcome in `fine_structure_results.json`.

## Results
The script computed a preliminary value (see `fine_structure_results.json`) of `alpha_etm` = 0.0531.
