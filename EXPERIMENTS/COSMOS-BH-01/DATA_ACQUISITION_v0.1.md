# COSMOS-BH-01 — Data Acquisition v0.1

Status: PROPOSED

## First benchmark
The first real-data benchmark will use compact-object systems with independently documented observational constraints. It must contain at minimum:

- clearly established black-hole systems;
- clearly established neutron-star systems;
- genuinely ambiguous compact-object systems;
- provenance for every measurement;
- uncertainty and limit state;
- measurement-dependence metadata.

## Inclusion rule
A system enters only if the source provides enough information to reconstruct at least two independent constraint channels or one high-quality channel with a documented uncertainty model. Systems with only a class label and no reconstructable observables are excluded from model development.

## Candidate anchor
OGLE-2011-BLG-0462 / MOA-2011-BLG-191 (OB110462) is reserved as an ambiguity/held-out case rather than being used to define the model. Published analyses give an inferred mass range of roughly 1.6–4.4 solar masses and explicitly report difficulty distinguishing a neutron star from a low-mass black hole. This makes it useful as a stress test, not as a pre-labeled training example.

## Known black-hole anchor
OGLE-2011-BLG-0462 has also been analyzed independently with HST astrometry and reported at about 7.1 +/- 1.3 solar masses in one analysis. Because the literature contains differing model assumptions/results, provenance must remain analysis-specific; measurements are never silently merged.

## Acquisition requirements
Record:
- source title/identifier;
- URL or persistent identifier;
- retrieval date;
- publication date/version;
- object/system identifier;
- raw observable and unit;
- uncertainty or limit;
- method/instrument;
- dependence on other measurements;
- transformation into normalized SI values;
- checksum/hash of locally stored source data when applicable.

## No result claim
This file defines acquisition. It does not assert that any candidate is physically classified by COSMOS. `PROPOSED != EXECUTED`.
