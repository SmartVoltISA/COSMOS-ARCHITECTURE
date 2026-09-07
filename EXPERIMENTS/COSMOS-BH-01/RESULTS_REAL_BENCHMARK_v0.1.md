# COSMOS-BH-01 — Real Benchmark Results v0.1

Status: TESTED / UNRESOLVED

Date: 2026-09-07

## Result

The first real compact-object benchmark does NOT support a claim that the current relational feature set independently identifies black holes.

The reason is structural rather than a failed physics result: the public summary-level benchmark currently provides mostly one observational channel (gravitational waves) per event, while the proposed relational model is designed to exploit relations among independent constraints/channels.

## What the benchmark does show

1. The benchmark contains clearly separated regimes:
   - GW150914: two ~30-solar-mass black holes.
   - GW190425: masses compatible with a binary-neutron-star interpretation.
   - GW200105/GW200115: neutron-star–black-hole systems.
   - GW190814: 23-solar-mass black hole plus a 2.6-solar-mass object whose nature remains ambiguous.
   - GW230529: a ~3.6-solar-mass primary in the lower mass-gap region with non-zero NS probability; the most probable interpretation is NS+BH, but GW data alone do not determine the nature definitively.

2. Conventional mass/orbital information already separates several classes strongly. Therefore any relational method must beat this baseline rather than merely reproduce it.

3. The ambiguous objects are exactly the useful stress tests. GW190814 and GW230529 cannot be treated as ground-truth black holes simply from mass.

4. A one-channel GW-only representation is insufficient to test the strongest form of the COSMOS relational hypothesis. The experiment needs independent constraints: e.g. electromagnetic, astrometric, timing, tidal/deformability or other independently derived information where available.

## Quantitative preflight carried forward

Synthetic positive-control AUC ≈ 0.770.

200 label-permutation null runs: mean AUC ≈ 0.504.

Interpretation: the analysis pipeline can recover a deliberately injected structural signal and does not manufacture comparable discrimination after label randomization.

These numbers are control results, not astrophysical results.

## Current verdict

BH1_BLACK_HOLE_COMPATIBLE: achievable for individually established benchmark systems using conventional astrophysical evidence.

BH2_ALTERNATIVE_COMPACT_OBJECT_COMPATIBLE: demonstrated as a necessary state for GW190814/GW230529-style ambiguity.

BH3_RELATIONAL_SIGNAL_REPLICATED: NOT YET ESTABLISHED on real observational data.

BH4_INDEPENDENTLY_SUPPORTED: NOT ASSIGNED.

## Falsification/limitation

The current real benchmark does not falsify the relational hypothesis. It does falsify a weaker shortcut: "mass + one GW channel + graph terminology is enough to identify a black hole." It is not enough.

## Next decisive test

Construct a held-out multi-channel dataset in which each system has at least two genuinely independent observational constraints. Build the relation graph without class labels, freeze feature definitions, then evaluate against conventional physical baselines and all null controls.

Until that is done, COSMOS makes no new claim about black-hole ontology.