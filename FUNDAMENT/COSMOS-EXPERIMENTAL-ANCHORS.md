# COSMOS — Experimental Anchors v1.0

## Purpose

This document fixes a set of physical systems where the COSMOS program can test the general question:

> How does changing a subsystem, its coupling, or the level of organization change the state and future dynamics of the whole system?

Core workflow:

**FACT → CHECK → MODEL → EXPERIMENT → RESULT → ARCHIVE → NEXT QUESTION**

A hypothesis is not a fact. A proposed experiment is not a performed experiment.

---

## Anchor A — Solar System / N-body hierarchy

### Question
Does adding dynamically coupled bodies change the trajectory structure of the system in a measurable and predictable way?

### Candidate tests
1. Sun–Earth two-body control → add Moon.
2. Sun–Jupiter → add Saturn.
3. Sun–Jupiter–Saturn → add Uranus/Neptune.
4. Planet → moons → barycenter motion.
5. Planetary resonances and stability.

### Measurements
- pairwise distances;
- orbital elements;
- barycenter displacement;
- angular momentum exchange;
- secular drift;
- resonance phase;
- stability time.

### Data
JPL Horizons provides positions/velocities for planets, satellites, asteroids, comets, barycenters and dynamical points including Lagrange points. citeturn0search2turn0search8

### Value
Excellent controlled laboratory because the observations and ephemerides are comparatively precise.

---

## Anchor B — Three-body / Lagrange systems

### Question
Can a third body create qualitatively new stable/unstable regions rather than merely adding another force?

### Candidate tests
- Sun–Earth–Moon;
- Sun–Jupiter–Trojan;
- Earth–Moon–spacecraft;
- L1/L2 versus L4/L5 stability.

### Measurements
- escape time;
- libration amplitude;
- phase-space volume;
- sensitivity to initial conditions;
- stability under perturbation.

Lagrange systems provide an established example where combined gravity and orbital motion create special dynamical regions; L4/L5 can support stable configurations under the appropriate mass-ratio condition. citeturn0search0turn0search12

### COSMOS interest
This is a direct test of whether **relationship + geometry** can produce a new system-level regime.

---

## Anchor C — Galaxy hierarchy / Local Group

### Status
Already opened as **COSMOS-GALAXY-01**.

### System
MW + M31
→ + M33
→ + LMC
→ + M33 + LMC.

### Question
Does adding dynamically coupled galaxies measurably alter the long-term state of the Local Group?

### Measurements
- MW/M31 trajectory;
- relative distance;
- relative velocity;
- orbital-plane orientation;
- angular momentum;
- merger probability;
- host-galaxy recoil.

### Important control
This is already standard gravitational dynamics, so a detected effect is **not new physics** by itself.

### COSMOS extension
Search for a general quantitative relationship between subsystem properties and whole-system response.

---

## Anchor D — Galaxy groups and clusters

### Question
Does increasing the number and hierarchy of coupled galaxies produce systematic changes in collective dynamics?

### Candidate levels
- binary galaxy pair;
- small group;
- Local Group;
- galaxy cluster;
- cluster merger.

### Measurements
- velocity dispersion;
- mass distribution;
- centroid/barycenter motion;
- substructure;
- tidal features;
- merger times;
- mass segregation.

Galaxy groups and clusters are observed gravitationally bound structures; clusters contain hundreds to thousands of galaxies plus hot gas and dark matter. citeturn0search3

### COSMOS interest
This extends the hierarchy test from a few-body system to many-body organization.

---

## Anchor E — Cosmic web / large-scale structure

### Question
Does local gravitational coupling produce stable higher-level structure across scales?

### Candidate structures
- filaments;
- sheets/walls;
- nodes/clusters;
- voids;
- flows toward overdensities.

NASA describes the cosmic web as a large-scale network of filaments, sheets and concentrations produced by the gravitational growth of matter. citeturn0search3turn0search7

### Measurements
- density contrast;
- connectivity;
- filament orientation;
- node degree;
- void size;
- tidal tensor;
- scale-dependent correlations.

### COSMOS interest
This is the largest-scale candidate for testing:

**local difference → coupling → collective structure.**

It is also the place where we must be most careful not to confuse visual pattern with causal law.

---

## Anchor F — Compact binaries

### Question
Does the coupling of two compact objects produce a predictable progression of system state?

### Candidate systems
- binary neutron stars;
- binary black holes;
- neutron-star/black-hole binaries.

### Measurements
- orbital frequency;
- inspiral rate;
- gravitational-wave phase;
- amplitude;
- final mass/spin;
- deviation from GR waveform models.

LIGO treats compact-binary inspirals as a direct observational laboratory for evolving coupled gravitational systems. citeturn0search5turn0search11

### COSMOS interest
This moves the program from classical orbital dynamics into strong-field relativistic dynamics.

---

## Anchor G — Neutron-star internal structure

### Question
Can a compact object's internal state be linked quantitatively to its observable external dynamics?

### Candidate measurements
- mass;
- radius;
- tidal deformability;
- equation-of-state parameters;
- post-merger signal.

### COSMOS interest
This connects **internal organization → external response**.

This should be treated separately from the galaxy-scale hierarchy because the physical regime is radically different.

---

## Anchor H — Exoplanet multi-body systems

### Question
Does increasing planetary multiplicity produce identifiable dynamical organization, resonances and stability regimes?

### Candidate tests
- two-planet control;
- three-planet system;
- resonant chains;
- near-resonant systems;
- stability versus spacing/mass.

NASA notes that planetary systems contain multiple bodies whose orbital architecture can be studied observationally; our Solar System itself provides a benchmark. citeturn0search9

### COSMOS interest
Potential bridge between the Solar System and galaxy-scale hierarchy.

---

# Cross-system measurements

For every anchor, use the same abstract state representation where physically meaningful:

**State**
- position;
- velocity;
- mass/energy;
- angular momentum;
- geometry;
- internal variables.

**Difference**
\[
\Delta X(t,\tau)=X(t)-X(t-\tau)
\]

**Coupling**
- gravitational;
- tidal;
- dissipative;
- radiative;
- relativistic;
- environmental.

**Response**
\[
R = S_{coupled}-S_{control}
\]

The key comparison is always:

**CONTROL → PERTURBATION → RESPONSE**

not visual similarity.

---

# Priority order for COSMOS

1. **Solar System N-body** — precise data, easiest validation.
2. **Three-body / Lagrange systems** — cleanest test of relational dynamics.
3. **COSMOS-GALAXY-01** — already started.
4. **Galaxy groups/clusters** — hierarchy expansion.
5. **Compact binaries** — strong-field regime.
6. **Exoplanet multi-body systems** — independent planetary validation.
7. **Cosmic web** — highest-scale test, but most model-dependent.
8. **Neutron-star internal structure** — separate high-density branch.

This order is methodological, not a ranking of scientific importance.

---

# Main COSMOS question

The program should not begin by assuming that the proposed universal principle is true.

Instead test:

> When a system gains an additional dynamically coupled degree of freedom, does the change in the whole-system state follow a measurable, reproducible and scale-consistent relationship?

Possible outcomes:

- **SUPPORTED** — reproducible quantitative relationship;
- **PARTIAL** — effect exists but no universal scaling established;
- **REJECTED** — no effect beyond controls/uncertainty;
- **UNRESOLVED** — data/model precision insufficient.

No new physical law is claimed unless existing physics fails to explain the measured effect and the result survives independent controls.

---

# Next experiments

## COSMOS-SOLAR-02
Replace the simplified kinematic model with JPL Horizons state vectors and test frame dependence plus true N-body trajectories.

## COSMOS-THREEBODY-01
Build a controlled numerical experiment:
Sun–Earth → Sun–Earth–Moon,
then compare barycentric motion, orbital elements and perturbation growth.

## COSMOS-GALAXY-01
Run an independent reduced model and, when the original published notebook is executable locally, compare it against the published calculation.

## COSMOS-HIERARCHY-01
After the three branches above, compare normalized response across:
planetary → stellar → galactic systems.

The purpose is not to force one law onto every scale, but to test whether a common mathematical description survives changes of scale and physical regime.
