# COSMOS-BH-01 — Analysis Plan v0.1

Status: PROPOSED

## Purpose
Define the relational feature calculations and evaluation order before inspecting held-out class labels.

## Inputs
For each system, retain only observations with explicit provenance, units, uncertainty/limit state, and measurement dependence. Missing values remain missing.

## Relational representation
Construct a bipartite constraint graph:
`observable -> constraint -> latent physical parameter`.
Edges carry source, method, uncertainty, dependence, transformation and timestamp.

## Features
F1 Constraint density = independent constraint edges / eligible latent targets.

F2 Cross-channel consistency = one minus normalized disagreement among independent estimates of the same latent target. The disagreement metric and normalization must be fixed from the training set only.

F3 State distinguishability = effective number of distinguishable latent configurations supported by independent constraints. The estimator must be fixed before held-out evaluation.

F4 Relational concentration = concentration of constraints over latent targets, reported with a predefined concentration statistic.

F5 Persistence = fraction of independent/temporal observations supporting the same latent configuration within uncertainty bounds.

F6 Degeneracy score = normalized residual ambiguity after applying the recorded constraints. Higher value means more unresolved alternatives. This feature is descriptive; it is not synonymous with physical collapse.

## Baselines
1. Conventional mass/dynamics features.
2. Conventional compactness features where radius is measured or bounded.
3. Class-specific physical-model likelihoods where available.
4. Random-label null.
5. Feature-shuffle null.
6. Observation-count/channel-matched null.

## Evaluation
Primary test: does the relational feature vector improve held-out discrimination or calibration beyond the conventional baseline?

Use nested cross-validation or a fixed train/held-out split. No class labels are used during relational feature construction. Report effect size, confidence/credible interval as appropriate, out-of-sample score, calibration, and null distribution.

## Required controls
- label permutation;
- feature permutation;
- leave-one-channel-out;
- uncertainty perturbation;
- observation-count matching;
- source/campaign separation where possible;
- independent or temporal validation where available.

## Interpretation gate
A relational signal is not evidence for a black hole by itself. Any physical interpretation requires comparison with established astrophysical models and independent observational constraints.

## Stop conditions
Stop and mark UNRESOLVED if the dataset is too small, labels leak into features, dependencies cannot be reconstructed, or the result is driven by observation count/source identity rather than physical information.

## Status rule
This file is a preregistered analysis plan. `PROPOSED != EXECUTED`.
