# COSMOS-BH-01 — Multi-Channel Benchmark v0.1

**Status:** PROPOSED  
**Date:** 2026-09-07

## Objective

Construct the first real observational benchmark capable of testing the strongest COSMOS-BH-01 hypothesis:

> Does a label-blind relational representation of independently measured constraints add reproducible discriminative information beyond conventional astrophysical observables when distinguishing black-hole-compatible systems from alternative compact-object interpretations?

This benchmark is a **test design**, not a result.

## Why this benchmark is necessary

The first real benchmark was dominated by gravitational-wave-only events. That test established an important limitation: mass/orbital information from one observational channel can reproduce conventional classifications, but it cannot test whether relational structure across independent constraints contributes additional information.

The present benchmark therefore requires genuine cross-channel observations.

## Primary candidate set

### 1. Gaia BH1 — primary positive control

Use the Gaia BH1 system as a high-value multi-channel benchmark because its dark companion was constrained through Gaia astrometric orbital motion and follow-up spectroscopic radial velocities. The joint analysis places the companion near 10 solar masses, while the spectroscopic mass function provides a strong lower bound that rules out an ordinary luminous companion.

Allowed inputs must preserve the distinction between:

- astrometric position/motion/orbital constraints;
- spectroscopic radial-velocity constraints;
- parallax/distance information;
- photometric constraints on luminous contribution.

Do not convert all of these into one duplicated "mass" feature before constructing the relation graph.

### 2. OGLE-2011-BLG-0462 / MOA-2011-BLG-191 — ambiguity control

Use the isolated microlensing compact-object event as a controlled ambiguity case. HST astrometry and ground-based microlensing photometry provide different observational modalities, but they are linked by the same lensing event and common model assumptions.

The benchmark must therefore encode their dependency explicitly. Published analyses allow materially different mass ranges, including a roughly 7-solar-mass black-hole interpretation and a 1.6–4.4-solar-mass range compatible with either a neutron star or low-mass black hole.

This object is valuable precisely because the architecture must preserve unresolved interpretation rather than force a binary label.

### 3. GW170817 — multi-messenger control

Use GW170817 as a cross-physics control containing gravitational-wave and electromagnetic observations.

The purpose is to test whether the relation representation can preserve consistency and disagreement across genuinely distinct channels. The remnant must not be hard-coded as a black hole or neutron star ground truth when the underlying interpretation remains model-dependent.

### 4. GW-only events — negative/control set

Retain GW150914, GW190425, GW200105, GW200115, GW190814 and GW230529 as controls where appropriate.

They are useful for testing:

- whether the relational representation collapses to conventional mass/orbital information when only one channel exists;
- whether channel count is being artificially inflated by derived features;
- whether ambiguous mass-gap events remain ambiguous;
- whether adding labels can leak information into feature construction.

They are not substitutes for the multi-channel benchmark.

## Feature protocol

The relational feature set remains frozen as defined in `PROTOCOL_v0.1.md`:

- F1 — constraint density
- F2 — cross-channel consistency
- F3 — state distinguishability
- F4 — relational concentration
- F5 — persistence
- F6 — degeneracy score

No new feature may be introduced after inspection of held-out class labels.

## Data representation

Each observation must retain:

- object/system identifier;
- source identifier and version/date;
- observing instrument or survey;
- measurement method;
- value and unit;
- uncertainty or posterior representation;
- limit/censoring flag;
- dependency class;
- transformation history.

The graph should represent:

`observation → constraint → physical parameter`

and must not collapse independent observations into one node before dependency information has been recorded.

## Dependency controls

For every pair of constraints, assign:

- I0 — same underlying observation;
- I1 — partially dependent;
- I2 — substantially independent;
- I3 — independent multi-messenger / multi-physics.

Primary relational analysis uses I2/I3. I1 is sensitivity analysis. I0 does not increase independent-channel count.

## Evaluation design

### Primary comparison

Compare:

1. conventional physical baseline;
2. conventional baseline + relational features;
3. relational-only representation;
4. null relational representation;
5. label-permutation control;
6. feature-shuffle control;
7. missing-channel control.

Use held-out evaluation or nested cross-validation. Do not select features using the held-out labels.

### Required reporting

Report:

- effect size;
- out-of-sample discrimination;
- uncertainty interval;
- calibration;
- label-permutation null distribution;
- feature-shuffle null distribution;
- leave-one-channel-out sensitivity;
- uncertainty perturbation sensitivity;
- dependency-model sensitivity;
- comparison with conventional astrophysical baselines.

## Minimum success condition

A positive result requires all of the following:

1. relational features improve out-of-sample performance beyond the predefined conventional baseline;
2. the improvement survives label permutation and feature-shuffle controls;
3. the effect survives reasonable uncertainty and dependency perturbations;
4. the effect is not attributable to one post-hoc selected system or one channel;
5. the effect replicates on held-out systems.

A conventional baseline winning is a valid scientific result.

## Minimum falsification conditions

The relational hypothesis is weakened or rejected if:

- relational improvement disappears after dependency correction;
- improvement is explained by ordinary mass/orbital variables;
- label-shuffled data produce comparable performance;
- feature-shuffled graphs retain the signal;
- the result depends on one ambiguous object;
- the result disappears under realistic uncertainty perturbation;
- independent systems fail to reproduce the effect.

## Current status

**PROPOSED — not executed.**

No astrophysical AUC or classification result is claimed by this document.

The next computational step is to build the provenance table for the primary candidate systems, freeze the dependency graph, and only then run the held-out benchmark.

## Provenance

Primary external references include ESA's Gaia BH1 discovery material and the Gaia BH1 discovery paper, NASA's Hubble isolated black-hole analysis, NASA NTRS documentation for OB110462, and established GW170817 multi-messenger literature.
