# COSMOS-BH-01 — Computational Preflight Test v0.1

Status: TESTED (preflight only)

## Purpose
Verify that the planned evaluation machinery can distinguish a synthetic signal from shuffled-label null data before applying it to astronomical observations.

## Synthetic setup
- N = 240 systems.
- Two balanced synthetic classes.
- Six relational-style features.
- Five-fold stratified cross-validation.
- Logistic regression used only as a simple evaluation harness.
- Random seed: 20260907.

## Observed preflight values
- Synthetic planted-signal mean 5-fold ROC-AUC: **0.770**.
- 200 label-permutation runs: mean ROC-AUC **0.504**, SD **0.056**, central 95% empirical interval **0.379–0.599**.
- Permuting one informative feature reduced mean 5-fold ROC-AUC to **0.698**.

## Interpretation
The computational harness behaves as expected on synthetic data: planted signal is recoverable and label permutation removes the intended class relationship. This validates only the mechanics of the preflight test.

It does **not** validate any COSMOS physical hypothesis, black-hole interpretation, relational ontology, or astronomical classifier. The synthetic signal was deliberately constructed and contains no observational data.

## Next gate
Do not promote this to an experiment result. The next valid step is real-data acquisition with provenance, independent channels, held-out labels, and the preregistered null controls.

`TESTED` here means only the computational preflight was executed. `PROPOSED != EXECUTED` remains true for COSMOS-BH-01 as an astronomical experiment.
