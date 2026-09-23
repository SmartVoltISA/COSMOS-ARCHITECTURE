# COSMOS-GALAXY-01 — Hierarchical coupling in the Local Group

**Status:** TESTABLE → EXTERNAL-CONTROLLED
**Date:** 2026-09-23
**Purpose:** test whether adding dynamically coupled galaxies changes the future state of a larger galaxy system.

## Question

Does the future MW–M31 trajectory remain effectively a two-body problem when the next massive Local Group members are included?

## Null hypothesis

The additional galaxies M33 and the LMC have negligible effect on the MW–M31 future orbit compared with observational uncertainty.

## Test structure

Compare:

1. MW + M31
2. MW + M31 + M33
3. MW + M31 + LMC
4. MW + M31 + M33 + LMC

The published control uses Monte Carlo sampling of observational uncertainties and numerical integration over 10 Gyr. The fiducial masses are approximately:

- MW: 1.0 ± 0.2 × 10^12 M_sun
- M31: 1.3 ± 0.4 × 10^12 M_sun
- M33: 3.0 ± 1.0 × 10^11 M_sun
- LMC: 1.5 ± 0.5 × 10^11 M_sun

## External control result

Sawala et al. (Nature Astronomy, 2025) report:

| Configuration | MW–M31 merger within 10 Gyr |
|---|---:|
| MW + M31 | slightly below 50% |
| MW + M31 + M33 | about 2/3 |
| MW + M31 + LMC | slightly above 1/3 |
| MW + M31 + M33 + LMC | slightly above 50% |

They used 50,000 Monte Carlo samples for the fiducial four-body model and 2,500 for variants, with statistical errors below 1%. They also checked the semi-analytic calculation against N-body simulations; the published N-body comparison gives a consistent merger outcome for the fiducial central initial conditions.

The important dynamical result is not the merger probability itself. M33 and LMC alter the motion of their host galaxies, changing relative velocity and orbital geometry. M33 mainly changes the in-plane motion; the LMC also contributes momentum perpendicular to the initial MW–M31 orbital plane.

## Independent 2026 control

Wu et al. (2026) repeated the problem with updated Gaia proper motions and the same general semi-analytic framework. Their fiducial model gives a substantially higher merger probability (~90%), with a median merger time of about 6.5 Gyr. Their sensitivity analysis still spans roughly 64.7%–100% over the 2-sigma proper-motion region.

This disagreement is itself a result: the long-term outcome is highly sensitive to present-day astrometric inputs and model assumptions.

## COSMOS interpretation

The external controls support the following limited statement:

> Adding dynamically coupled subsystems changes the state and future trajectory of the larger system. The effect is measurable and can be large.

This does **not** establish a new physical law. Gravity, distributed dark-matter halos, dynamical friction and ordinary orbital dynamics already provide a known explanation.

The result does support a testable systems-level question:

**Does the effect of adding a subsystem scale predictably with its mass, position, velocity and coupling geometry?**

## Required next run

A true COSMOS reproduction must execute the authors' public code rather than reproduce only their published percentages.

Source code:
https://github.com/TillSawala/MW-M31

Required local run:

1. obtain the exact published notebook and dependencies;
2. freeze package versions;
3. run the two-, three- and four-body configurations;
4. preserve raw outputs;
5. repeat the central N-body comparison;
6. calculate sensitivity to mass and proper-motion perturbations;
7. compare our outputs with the published figures and merger fractions;
8. record any numerical or implementation differences.

## Falsifier for the broader coupling claim

If controlled addition of M33/LMC produces no measurable change in the MW–M31 state beyond numerical noise and observational uncertainty, the hierarchical-coupling claim fails for this system.

## Current evidence state

**EXTERNAL-CONTROLLED / LOCAL REPRODUCTION PENDING**

The published evidence demonstrates the effect, but COSMOS has not yet independently executed the authors' notebook in our environment.
