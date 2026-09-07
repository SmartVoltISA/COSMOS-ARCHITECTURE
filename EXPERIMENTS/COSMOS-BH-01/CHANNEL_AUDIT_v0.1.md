# COSMOS-BH-01 — Channel Audit v0.1

**Status:** TESTABLE / PREPARATION  
**Date:** 2026-09-07

## Purpose

Identify which compact-object benchmark systems contain genuinely independent observational constraints suitable for the multi-channel relational test.

The key rule is:

> Multiple measurements are not automatically multiple channels. Measurements derived from the same underlying observation must retain their dependency relation.

This audit prevents the relational model from manufacturing "independence" by splitting one observation into several derived quantities.

## Independence classes

- **I0 — same observation:** alternative summaries/derived quantities of one underlying dataset.
- **I1 — partially dependent:** different instruments or reductions with substantial shared underlying signal/systematics.
- **I2 — substantially independent:** distinct physical observables or observing modalities constrain the system through different measurement pathways.
- **I3 — independent multi-messenger / multi-physics:** constraints arise from physically distinct channels and can test materially different aspects of the interpretation.

Only I2/I3 relations should count toward the primary multi-channel benchmark. I1 may be retained for sensitivity analysis; I0 must not increase channel count.

## Current benchmark audit

| System | Available channel(s) | Independence | Role | Current limitation |
|---|---|---:|---|---|
| GW150914 | gravitational-wave inspiral/merger/ringdown | I0 | conventional BH positive control | Current benchmark is effectively single-channel |
| GW190425 | gravitational-wave signal | I0 | NS-compatible control | Single-channel; does not test multi-channel relation structure |
| GW200105 | gravitational-wave signal | I0 | NS-BH control | No independent EM channel in current benchmark |
| GW200115 | gravitational-wave signal | I0 | NS-BH control | No independent EM channel in current benchmark |
| GW190814 | gravitational-wave signal | I0 | ambiguity stress test | Secondary mass is ambiguous; GW-only classification insufficient |
| GW230529 | gravitational-wave signal | I0 | mass-gap ambiguity stress test | Primary nature not uniquely determined by GW data alone |
| Gaia BH1 | Gaia astrometry + spectroscopic radial velocities | I2/I3 | primary multi-channel benchmark | Dependency model must preserve joint orbital inference |
| OGLE-2011-BLG-0462 / MOA-2011-BLG-191 | HST astrometric microlensing + ground-based microlensing photometry | I2 with dependency audit required | isolated compact-object ambiguity / BH control | Photometry and astrometry are fit jointly; not fully independent |
| HST isolated-BH analysis of OGLE-2011-BLG-0462 | HST astrometry + photometric microlensing information | I2 with dependency audit required | high-value compact-object case | Different analyses give different allowed mass ranges; analysis dependence must be preserved |
| GW170817 | gravitational waves + electromagnetic counterpart | I3 | multi-messenger control | Remnant interpretation remains model-dependent; not a simple BH ground truth |

## Evidence notes

### Gaia BH1

Gaia BH1 is a strong candidate for the first primary multi-channel benchmark because the discovery used astrometric orbital motion and follow-up radial velocities. The joint solution constrains a dark companion of roughly ten solar masses; the spectroscopic mass function independently provides a strong lower bound that rules out an ordinary luminous companion. The source paper explicitly compares astrometry-only, RV-only, and joint constraints.

This makes Gaia BH1 particularly useful for testing whether the relational representation adds information beyond conventional orbital dynamics rather than merely reproducing a black-hole label.

### OGLE-2011-BLG-0462 / MOA-2011-BLG-191

HST astrometric microlensing plus ground-based photometric microlensing provides two measurement modalities. However, both are observations of the same lensing event and are fitted through a common physical model. Therefore the graph must encode their dependence instead of treating them as two independent votes.

The published analyses also disagree in the allowed mass range: one analysis estimates about seven solar masses, while another permits approximately 1.6–4.4 solar masses. This disagreement is valuable as an uncertainty/model-dependence control, not as evidence that either interpretation is automatically correct.

### GW170817

GW170817 is a genuine multi-messenger system because gravitational-wave data were accompanied by electromagnetic observations. It is therefore useful for testing the architecture's cross-channel consistency logic. It should not be used as a simplistic BH ground-truth label because the nature of the merger remnant is model-dependent.

## Inclusion rule for the next benchmark

A system enters the **primary multi-channel test set** only if:

1. at least two observational constraints are classified I2 or I3;
2. the underlying datasets and observing modalities are explicitly recorded;
3. shared-model dependencies are represented rather than duplicated;
4. class labels are excluded from feature construction;
5. all F1–F6 relational features are frozen before held-out labels are evaluated;
6. conventional physical baselines are computed from the same allowed information;
7. missing channels remain missing and are not silently imputed.

## Consequence

The first real GW-only benchmark remains valid as a **negative methodological result**: it cannot establish the strongest relational hypothesis because its observations do not provide enough independent relational structure.

The next decisive step is therefore not "run a bigger classifier". It is to construct a provenance-preserving multi-channel benchmark beginning with Gaia BH1 and carefully audited microlensing cases, with GW170817 retained as a multi-messenger control.

## Provenance

External scientific references used for this audit include ESA's Gaia BH1 discovery summary, the Gaia BH1 discovery paper, NASA's Hubble isolated compact-object analysis, and the NASA Technical Reports Server record for OB110462.

**Important:** this document is an audit/preparation artifact. It contains no new astrophysical result and does not assign a new black-hole ontology.
