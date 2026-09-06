# COSMOS-NS-01 — Protocol v0.1

## Status

`PROPOSED`

This document defines the preregistered computational protocol before the first catalogue-wide run. Thresholds are deliberately separated from conclusions.

## 1. Research question

Can astronomical objects with measured mass and radius be identified whose inferred compactness or mass–radius position is incompatible with conventional planetary structure strongly enough to justify testing compact-object explanations?

The protocol does not assume the existence of neutron-core objects.

## 2. Primary observables

For each object, retain:

- object identifier
- mass `M` and positive/negative uncertainty
- radius `R` and positive/negative uncertainty
- measurement provenance
- measurement method
- number of independent measurements where available
- density supplied by the source, if available
- host/system identifier where relevant

Derived quantities:

`rho = 3M / (4*pi*R^3)`

`C = G*M / (R*c^2)`

where `rho` is mean density and `C` is dimensionless compactness.

## 3. Unit normalization

All calculations use SI internally:

- mass: kg
- radius: m
- density: kg/m^3
- compactness: dimensionless

Catalogue-native units must be preserved in the raw provenance layer.

## 4. Quality gates

An object enters the primary sample only if:

1. mass is measured rather than an upper/lower limit;
2. radius is measured rather than an upper/lower limit;
3. uncertainties are available or the source explicitly documents a justified uncertainty treatment;
4. the provenance of both quantities is retained;
5. no known catalogue flag invalidates the measurement for the intended calculation.

Objects failing a gate are not discarded permanently. They enter a secondary/excluded-with-reason category with the reason recorded.

## 5. Uncertainty propagation

For independent symmetric uncertainties, first-order propagation may be used for screening:

`(sigma_rho/rho)^2 = (sigma_M/M)^2 + 9*(sigma_R/R)^2`

`(sigma_C/C)^2 = (sigma_M/M)^2 + (sigma_R/R)^2`

Asymmetric uncertainties must remain asymmetric in the source layer. Monte Carlo propagation is preferred for candidate ranking when the posterior shape is materially non-Gaussian.

## 6. Candidate screening

Screening is performed in stages:

### Stage A — measurement sanity

Check units, signs, missing values, duplicated solutions, limits and provenance.

### Stage B — derived-property consistency

Recalculate density and compactness from M and R. Compare with catalogue-derived values where available.

### Stage C — conventional-model comparison

Compare the object against relevant ordinary mass–radius/structure expectations for its class. A statistical outlier is not automatically a physical anomaly.

### Stage D — alternative explanations

For high-interest outliers test, as applicable:

- measurement/systematic error;
- composition and ordinary structure;
- white-dwarf models;
- neutron-star models;
- black-hole constraints;
- binary/dynamical effects;
- classification error;
- other physically motivated models.

### Stage E — independent evidence

Prioritize candidates with independent measurements or observables that constrain the same physical interpretation.

## 7. Candidate status

`C0_NORMAL` — consistent with the tested conventional model.

`C1_OUTLIER` — statistical/model outlier requiring review.

`C2_UNEXPLAINED` — remains unexplained after documented conventional/systematic checks.

`C3_COMPACT_COMPATIBLE` — compact-object models provide a materially better explanation.

`C4_NEUTRON_COMPATIBLE` — neutron-star/neutron-matter model is specifically compatible with the observations and competing models are constrained.

`C5_INDEPENDENTLY_SUPPORTED` — interpretation supported by independent observational evidence.

No C4/C5 status may be assigned from mass and radius alone.

## 8. Falsification rules

The compact-core hypothesis loses support if the apparent anomaly disappears after:

- correcting a measurement/systematic error;
- replacing an invalid catalogue solution;
- applying a conventional physical model that explains the observations;
- discovering that the mass/radius pair is not independently constrained;
- or demonstrating that the compact-object interpretation conflicts with stronger independent observations.

## 9. No cherry-picking

The primary search must operate on a predefined catalogue snapshot and predefined quality rules. Candidate selection thresholds must not be tuned after inspecting individual objects.

Any exploratory threshold tuning becomes a separate analysis and cannot be presented as preregistered evidence.

## 10. Reproducibility record

Every run must record:

- catalogue/table name;
- catalogue retrieval date;
- exact query;
- software version/commit;
- constants and units;
- filters;
- thresholds;
- number of input rows;
- number passing each gate;
- candidate list;
- output hash where practical.

## 11. First data source

The first planetary search should use the NASA Exoplanet Archive Planetary Systems (`ps`) or Planetary Systems Composite Parameters (`pscomppars`) tables through TAP. The archive currently documents these as the supported programmatic tables for confirmed-planet data. citeturn0search1turn0search4

The archive currently reports 6,354 confirmed planets, with 2,165 having mass measurements and 4,742 having radius measurements. The intersection must be computed from the actual catalogue query rather than inferred from these totals. citeturn0search3turn0search7

## 12. First run target

Construct the maximal quality-controlled intersection of confirmed planets with usable mass and radius, calculate `rho` and `C`, validate the calculations against catalogue values where possible, and produce a ranked anomaly table.

**No physical interpretation is claimed until the ranked candidates pass the control-model stage.**
