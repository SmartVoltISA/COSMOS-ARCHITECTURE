# COSMOS-BH-01 — Results Precheck v0.1

Status: TESTED / PRECHECK ONLY
Date: 2026-09-07

## Scope

This document records the completed precheck of the full experimental control structure. It is not the observational result of COSMOS-BH-01.

## Variants tested

1. Synthetic positive-control signal.
2. Label permutation null control.
3. Feature permutation control.
4. Observation-count / quality control.
5. Channel-removal sensitivity.
6. Conventional-feature baseline.
7. Relational-feature model.
8. Held-out evaluation logic.

## Precheck result

The synthetic positive control produced AUC ≈ 0.770. The label-permutation control produced mean AUC ≈ 0.504 over 200 permutations. This is consistent with the expected separation between an intentionally injected signal and a null label relationship.

The precheck therefore verifies that the analysis pipeline can distinguish a constructed signal from shuffled labels without treating random agreement as physical evidence.

## Interpretation

SUPPORTED: the control architecture is capable of detecting a predefined synthetic relational signal and rejects the corresponding label-shuffle null at the precheck level.

NOT TESTED: whether real astronomical compact-object observations contain such a signal.

NOT CLAIMED: black-hole detection, neutron-star detection, new gravity, event horizon, singularity, or evidence for the Ω relational model.

## Real-data benchmark candidates

### OB110462

NASA/NTRS reports an inferred mass of 1.6–4.4 solar masses and describes the object as most likely either a neutron star or a low-mass black hole. The same source reports tension between photometric and astrometric models and states that additional observations/modeling are needed. This makes it a high-value ambiguity/control case rather than a ground-truth BH label.

### GW170817

NASA/NTRS reports that gravitational-wave data alone did not rule out low-mass black-hole possibilities for the binary components and that the merger-remnant outcome was model-dependent. Therefore this event must not be hard-coded as an unquestionable BH ground truth in the label-blind development stage.

## Decision

PROCEED to real-data extraction only after freezing the feature definitions and null-control rules. Ambiguous systems remain ambiguous. Ground-truth labels, where used, enter only in held-out evaluation.

## Provenance

External anchors:
- NASA NTRS: https://ntrs.nasa.gov/citations/20230003522
- NASA NTRS: https://ntrs.nasa.gov/citations/20210014674

Internal experiment:
- COSMOS-BH-01/README.md
- COSMOS-BH-01/PROTOCOL_v0.1.md
- COSMOS-BH-01/DATA_SCHEMA_v0.1.md
- COSMOS-BH-01/ANALYSIS_PLAN_v0.1.md
- COSMOS-BH-01/NULL_CONTROL_v0.1.md

PROPOSED ≠ EXECUTED.
PRECHECK ≠ PHYSICAL RESULT.
UNKNOWN ≠ TRUE.
