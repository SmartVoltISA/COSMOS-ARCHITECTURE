# COSMOS-BH-01 — Null Control v0.1

Status: PROPOSED

## Objective
Determine whether any apparent relational classification signal is caused by label leakage, source identity, observation density, or arbitrary graph structure rather than compact-object physics.

## Controls

### N1 — Label permutation
Randomly permute BH/NS/other labels while preserving every observation. Repeat across a predefined number of permutations. Performance must collapse toward the null distribution.

### N2 — Feature permutation
Break the relation between systems and one or more relational feature columns while preserving marginal distributions.

### N3 — Observation-count matching
Match or weight systems so that class differences in number of measurements/channels cannot explain the result.

### N4 — Source/campaign control
Where possible, prevent the model from learning source, telescope, survey, catalog, or publication identity.

### N5 — Channel ablation
Repeat after removing astrometry, timing, EM, GW, orbital, and other channels individually where present.

### N6 — Uncertainty perturbation
Perturb measurements within their stated uncertainty model and repeat the evaluation. A claimed signal must not depend on one arbitrary central-value realization.

### N7 — Conventional-baseline control
Compare relational features against conventional physical observables. A relational model that adds no out-of-sample information is a valid negative result.

## Leakage rule
Class labels, object names whose names encode class, post-publication classification text, and any derived quantity calculated using the target label are forbidden from model-development features.

## Interpretation
Passing a null control only establishes that a computational signal is not trivially caused by that control. It does not establish a new physical mechanism.

## Status rule
`PROPOSED != EXECUTED`. No control is marked passed until an actual reproducible run is completed and recorded.
