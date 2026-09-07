# COSMOS-BH-01 — Protocol v0.1

## Status

`PROPOSED`

## 1. Research question

Can a label-blind relational representation of independently measured compact-object observables distinguish black-hole-compatible systems from neutron-star and other compact-object alternatives more reliably than predefined conventional baselines?

## 2. Preregistered separation of layers

### Observation layer

Only measured or source-derived quantities with preserved provenance enter the raw dataset.

### Physical baseline layer

Established dynamical, relativistic, neutron-star, black-hole and measurement-error models are evaluated independently of the Ω-derived feature set.

### Relational layer

Candidate graph features are computed from observational relations only.

### Evaluation layer

Target labels are revealed only for held-out evaluation.

## 3. Primary observables

Retain where available:

- object/system identifier;
- mass and asymmetric uncertainty;
- distance and uncertainty;
- orbital period, semi-major axis and eccentricity;
- radial-velocity constraints;
- astrometric constraints;
- lensing observables;
- X-ray/optical/radio observables;
- timing/pulsation observables;
- gravitational-wave mass/spin/tidal constraints;
- radius or radius limits;
- independent observing campaign identifiers;
- measurement provenance and publication/version identifiers.

Missing observables remain missing. They are not silently imputed into the primary evidence layer.

## 4. Relational representation

For each target construct a typed graph:

`observable → constraint → latent physical parameter`

Edges must record:

- source;
- measurement method;
- uncertainty;
- dependence/independence status where known;
- transformation used;
- timestamp or observation epoch where relevant.

No edge may encode the target class during model construction.

## 5. Candidate features

### F1 — Constraint density

Number of independent observational constraints normalized by the predefined observation-set size.

### F2 — Cross-channel consistency

Agreement among independently measured channels under the same physical parameterization.

### F3 — State distinguishability

Distance between posterior predictive distributions of competing physical states after uncertainty propagation.

### F4 — Relational concentration

Concentration of independently derived constraints around a common state.

### F5 — Persistence

Stability of the inferred state under leave-one-channel-out and predefined uncertainty perturbation tests.

### F6 — Degeneracy score

A predeclared scalar measuring whether observationally distinct descriptions collapse into an observationally indistinguishable state. The exact estimator must be fixed before seeing held-out labels.

## 6. Baseline comparison

At minimum compare against:

- conventional dynamical features;
- conventional compactness/mass features where valid;
- source-class-specific physical models;
- a random-label control;
- a feature-shuffled relational control;
- a missing-channel control.

## 7. Data split

The primary evaluation must use a held-out set defined before final model fitting.

If the sample is small, use nested cross-validation with all preprocessing performed inside the training folds.

No candidate may be moved between train and test after inspecting its label.

## 8. Statistical requirements

Report:

- effect size;
- confidence/credible interval;
- out-of-sample performance;
- calibration where probabilistic outputs are used;
- permutation/null distribution;
- sensitivity to measurement uncertainties;
- sensitivity to removal of individual channels.

Multiple comparisons must be controlled or explicitly reported as exploratory.

## 9. Physical interpretation gate

A relational signal can advance to physical interpretation only if it survives:

1. label-shuffle control;
2. feature-shuffle control;
3. catalogue-selection checks;
4. uncertainty perturbation;
5. leave-one-channel-out testing;
6. comparison with conventional physical baselines;
7. independent or temporally separated validation where available.

## 10. Candidate classification states

`BH0_UNRESOLVED`

`BH1_BLACK_HOLE_COMPATIBLE`

`BH2_ALTERNATIVE_COMPACT_OBJECT_COMPATIBLE`

`BH3_RELATIONAL_SIGNAL_REPLICATED`

`BH4_INDEPENDENTLY_SUPPORTED`

`BH4` cannot be assigned from the relational model alone.

## 11. Falsification rules

The relational hypothesis is rejected for the tested dataset if its performance is indistinguishable from the appropriate null control or if any apparent advantage disappears under predefined robustness tests.

A conventional model winning over the relational model is a valid negative result.

## 12. External physical anchor

NASA's Physics of the Cosmos program identifies black holes and neutron stars as extreme environments for testing gravity and matter, and emphasizes strong-field and multi-messenger observations as important discriminants. citeturn0search0turn0search4

Existing observational work also demonstrates that some compact objects can remain ambiguous between neutron-star and black-hole interpretations, making controlled discrimination a legitimate test target rather than assuming the label. citeturn0search1turn0search7

## 13. Execution status

No data run has been performed by this protocol.

`PROPOSED ≠ EXECUTED`
