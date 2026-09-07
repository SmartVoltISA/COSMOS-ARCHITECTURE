# COSMOS — REPOSITORY INTEGRATION MAP v0.1

**Status:** ACTIVE / AUDIT-BASED

## Purpose

COSMOS-ARCHITECTURE is the scientific research layer for systematic study of the Universe. Existing Ω and SPACE repositories are **not** merged blindly. They remain authoritative sources in their own domains and are connected to COSMOS through explicit provenance.

## Core rule

`SOURCE → AUDIT → CLASSIFY → LINK / ADAPT / IMPORT → VERIFY → RECORD`

No source material becomes a COSMOS result merely because it exists in another repository.

## Initial integration map

| Repository | Role | COSMOS relationship | Action |
|---|---|---|---|
| `SmartVoltISA/COSMOS-ARCHITECTURE` | Scientific domain/laboratory | Primary research environment | **KEEP / CENTRAL** |
| `SmartVoltISA/Omega-lab-.--.-` | Experimental Ω laboratory | Methodology, experiment discipline, reusable relational methods, prior experiments | **LINK + SELECTIVE ADAPT** |
| `SmartVoltISA/OMEGA-Science` | Open scientific Ω corpus | Cross-domain methodology and structured scientific knowledge model | **LINK + ADAPT** |
| `SmartVoltISA/OMEGA-RECOVERY` | Recovery/history layer | Provenance, restoration and historical-state discipline where relevant | **AUDIT / LINK** |
| `SmartVoltISA/SPACE-` | Main SPACE architecture | AI/system architecture; not itself cosmic evidence | **KEEP SEPARATE + LINK** |
| `SmartVoltISA/SPACE-INTEGRITY` | Integrity architecture | Verification/integrity patterns useful to research infrastructure | **LINK / SELECTIVE ADAPT** |
| `SmartVoltISA/SPACE-READ` | Public read layer | Read/publication boundary concepts | **LINK / SELECTIVE ADAPT** |
| `SmartVoltISA/SPACE-PROTOCOL` | Protocol layer | Protocol discipline and interface conventions | **LINK** |
| `SmartVoltISA/Space---Recovery-` | SPACE recovery | Recovery concepts; separate from scientific evidence | **LINK / AUDIT** |
| Other `SPACE-*` repositories | Specialized AI/system components | Engineering context, not scientific evidence by default | **KEEP SEPARATE** |

## Why Ω is relevant

The Ω-Lab core rule explicitly preserves the full research history, including rejected hypotheses, failed methods, parameters and provenance. It also separates observation from interpretation and hypothesis. fileciteturn32file0

The Ω-Lab foundation link further defines the research chain as:

`STATE → TRANSITION → PROVENANCE → VERIFICATION → HISTORY → FEEDBACK → RECOVERY`

and explicitly keeps `HYPOTHESIS ≠ PROPOSED ≠ EXECUTED ≠ RESULT ≠ INTERPRETATION ≠ CANONICAL`. fileciteturn33file0

These are directly compatible with COSMOS research discipline, but they are **methodological inheritance, not evidence for any physical hypothesis**.

## Why OMEGA-Science is relevant

OMEGA-Science defines a cross-domain scientific cycle:

`наука → модель → отношения → Ω-инструмент → эксперимент → сравнение → результат`

and a structured knowledge representation:

`объект → отношение → состояние → эксперимент → результат → связь с другими знаниями`.

It also explicitly requires comparison against existing science rather than replacing established models by default. fileciteturn34file0

This makes OMEGA-Science a natural methodological parent/reference for COSMOS, while COSMOS remains responsible for the astronomical domain and its own evidence.

## What is NOT being merged

1. SPACE system architecture is not treated as a physical theory of the Universe.
2. Ω axioms are not treated as empirical evidence for cosmic objects.
3. Engineering components are not copied into COSMOS merely because they are reusable.
4. Historical experiments are not rewritten to fit the COSMOS program.
5. A linked source is not automatically a verified COSMOS result.

## Integration levels

### L0 — Reference
A repository is cited as background or provenance.

### L1 — Methodological link
A method, status model, provenance rule or verification pattern is adopted with explicit attribution.

### L2 — Adapted experiment
A prior Ω experiment is reformulated for a COSMOS-specific observable and receives a new experiment ID.

### L3 — Imported evidence
Only an independently verified result with preserved source, commit/version, data and method may enter COSMOS as evidence.

## Current decision

**Do not physically merge repositories.** Build a connected research graph instead.

```text
                         COSMOS-ARCHITECTURE
                                  │
                    ┌─────────────┼─────────────┐
                    │             │             │
               OBSERVATION      MODEL       EXPERIMENT
                    │             │             │
                    │        OMEGA-Science   Ω-Lab
                    │             │             │
                    └─────────────┼─────────────┘
                                  │
                             VERIFICATION
                                  │
                               RESULT
                                  │
                               ARCHIVE

          SPACE-*  ─────────── engineering / architecture context
```

## Next audit targets

1. Enumerate Ω-Lab experiment families and identify those structurally transferable to COSMOS.
2. Inspect OMEGA-Science physics materials for existing physical models, relations and experiments.
3. Audit OMEGA-RECOVERY for provenance/recovery mechanisms that should become COSMOS infrastructure rules.
4. Audit SPACE-INTEGRITY / SPACE-READ / SPACE-PROTOCOL only for infrastructure patterns.
5. For every selected asset, record exact source path, source commit, adaptation and new COSMOS status.

## Epistemic boundary

COSMOS follows the same fundamental discipline:

**unknown ≠ true**

**proposed ≠ executed**

**interpretation ≠ observation**

**repair ≠ recovery**

**new result does not erase old history**

The integration itself must be reproducible and auditable.