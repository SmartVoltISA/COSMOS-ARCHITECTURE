# COSMOS-BH-01 — Data Schema v0.1

## Purpose

Define the minimum provenance-preserving record for each compact-object system before analysis.

## Required identity

- `object_id`
- `system_id`
- `source_id`
- `source_version_or_date`
- `measurement_method`

## Physical quantities

Each quantity must store:

- value;
- unit;
- lower uncertainty;
- upper uncertainty;
- limit flag if applicable;
- provenance.

Primary quantity groups:

- mass;
- distance;
- orbital parameters;
- astrometric parameters;
- timing parameters;
- electromagnetic observables;
- gravitational-wave observables;
- radius/radius limit;
- spin;
- tidal deformability where available.

## Relation record

```text
relation_id
source_observable
constraint_target
relation_type
measurement_dependency
uncertainty_model
transformation
provenance
```

`measurement_dependency` must distinguish known independent measurements from quantities derived from the same underlying observation.

## Label separation

The physical class label is stored outside the model-development feature table and is joined only for held-out evaluation.

## Integrity rules

- Unknown is not zero.
- Missing is not negative evidence.
- Derived values must retain the source quantities used to calculate them.
- A reused measurement must not be counted as an independent constraint.
- Historical values are preserved rather than overwritten.
