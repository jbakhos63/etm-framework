# Trial 015 – Planck Interval Baseline

This trial inaugurates **Stage 6 – Planck Scale Analogues** of the *ETM Simulation Research Plan*. Its purpose is to estimate the minimal temporal interval ("Planck time" analogue) implied by current ETM calibration.

## Plan
1. Create a hydrogen-energy photon using `ParticleFactory.create_hydrogen_photon()`.
2. Compute its frequency in SI units using the relation $E=h\nu$.
3. Determine the ETM tick duration by dividing the photon's oscillation period by its core timing rate.
4. Record this tick duration as a preliminary ETM Planck time.

## Method
- The calculation is purely numerical; no lattice propagation is required.
- Energy is converted from electronvolts to joules with $1\,\text{eV}=1.60218\times10^{-19}\,\text{J}$.
- The Planck constant is $h=6.62607015\times10^{-34}\,\text{J·s}$.

## Expected Outcome
A JSON file reporting the photon frequency and the derived tick duration in seconds. This value provides a first estimate of the smallest time step represented by one ETM tick.

## Results

The script computed a photon frequency of approximately $3.29\times10^{15}\,\text{Hz}$ and an ETM tick duration of $1.52\times10^{-16}\,\text{s}$. These values provide a baseline mapping between ETM ticks and SI seconds.
