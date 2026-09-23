# COSMOS-SOLAR-01 — Preliminary computational result

**Status:** TESTED — preliminary kinematic model  
**Run date:** 2026-09-23  
**Window:** 50 Julian years  
**Model:** circular Galactic motion + circular planetary orbits  
**Purpose:** test whether the apparent spatial spiral survives a change of reference frame.

## Inputs

NASA gives the Solar System's average Galactic orbital speed as about **720,000 km/h** and a Galactic orbital period of about **230 million years**.

Planetary semimajor-axis / orbital-period values were taken from the NASA Planetary Fact Sheet.

The model uses:

- Galactic speed: 720,000 km/h;
- Galactic period: 230 Myr;
- ecliptic/Galactic-plane angle: 60° as a geometric approximation;
- planetary radii and periods from NASA;
- 1-day sampling;
- 50-year window.

Sources:

- NASA, Solar System Facts: https://science.nasa.gov/solar-system/solar-system-facts/
- NASA, Planetary Fact Sheet: https://nssdc.gsfc.nasa.gov/planetary/factsheet/
- JPL Horizons documentation for the next, higher-fidelity phase: https://ssd.jpl.nasa.gov/horizons/manual.html

## Result

The model produces the expected large-scale translated trajectories in a Galactic/inertial frame.

However, when the Sun's position is subtracted, the planetary trajectories become bounded orbital curves again.

For the 50-year run:

| Planet | Heliocentric path (AU) | Global-frame path (AU) | Global / heliocentric |
|---|---:|---:|---:|
| Mercury | 504.52 | 2161.93 | 4.29 |
| Venus | 369.20 | 2138.03 | 5.79 |
| Earth | 314.20 | 2129.94 | 6.78 |
| Mars | 253.88 | 2122.46 | 8.36 |
| Jupiter | 137.77 | 2115.96 | 15.36 |
| Saturn | 102.18 | 2107.11 | 20.62 |
| Uranus | 71.91 | 2105.06 | 29.27 |
| Neptune | 57.91 | 2124.39 | 36.68 |

The heliocentric radius remains constant to numerical precision in this idealized model. For Earth the standard deviation is approximately 4.8e-8 AU.

## Interpretation

This is the critical result.

The visually interesting large-scale trajectory is strongly affected by the reference frame.

A simple model can generate a long, apparently spiral/helix-like track simply by adding the Solar System's bulk motion to ordinary planetary orbits.

Therefore:

> **The existence of a spiral-looking trajectory in an external/inertial frame is not evidence by itself for a new structural law.**

The result does **not** disprove any deeper dynamical relation. It establishes a necessary control:

**any claim of intrinsic spiral structure must survive removal of common translational motion and comparison across physically justified reference frames.**

## Current evidence state

**COSMOS-SOLAR-01: UNRESOLVED**

More precisely:

- visual spiral in global frame → reproduced;
- intrinsic spiral structure → not demonstrated;
- reference-frame dependence → demonstrated in the simplified model;
- new physics → no evidence.

## Next experiment

Replace the analytic circular model with real ephemerides.

JPL Horizons provides Cartesian state vectors for solar-system bodies and supports automated API access.

The next run should:

1. obtain Sun + planets state vectors from Horizons;
2. use one explicitly declared reference frame and timescale;
3. propagate the same states over the selected interval;
4. transform to:
   - Solar System barycentric frame;
   - Sun-centered frame;
   - optionally a Galactic frame;
5. calculate frame-invariant quantities;
6. measure curvature, torsion, phase relations and spatial correlations;
7. compare the measured values against null models.

Only after this control should we ask whether anything remains that cannot be explained by ordinary orbital dynamics plus coordinate transformation.
