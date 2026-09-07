# COSMOS-BH-01 — Real Compact-Object Benchmark v0.1

Status: TESTED / BENCHMARK

This is a small, source-grounded benchmark assembled from public LIGO/NASA summaries. It is not a population catalogue and is not sufficient for a final statistical claim.

## Objects

| Event | Configuration | m1 [Msun] | m2 [Msun] | Primary classification for benchmark | Evidence channel |
|---|---|---:|---:|---|---|
| GW150914 | BBH | 36 | 29 | BH+BH | GW |
| GW190425 | BNS-compatible | 2.52 | 1.68 | NS+NS compatible | GW |
| GW200105 | NSBH | 8.9 | 1.9 | BH+NS | GW |
| GW200115 | NSBH | 5.7 | 1.5 | BH+NS | GW |
| GW190814 | ambiguous | 23 | 2.6 | BH + ambiguous compact object | GW |
| GW230529 | ambiguous/mass-gap | 3.6 | 1.4 | NS + ambiguous compact object | GW |

## Derived quantities

q = m2/m1

GW150914: q=0.806, M=65 Msun
GW190425: q=0.667, M=4.20 Msun
GW200105: q=0.213, M=10.8 Msun
GW200115: q=0.263, M=7.2 Msun
GW190814: q=0.113, M=25.6 Msun
GW230529: q=0.389, M=5.0 Msun

## Provenance

GW150914: LIGO source summary and publication record.
GW190425: LIGO source summary.
GW200105/GW200115: LIGO source summary and publication record.
GW190814: LIGO source summary.
GW230529: LIGO source summary and publication record.

## Important boundary

The labels above are observational/model classifications used only for evaluation. They are not supplied to the relational representation during feature construction.

The sample is deliberately small. It demonstrates that real compact-object cases contain both clean BH/NS systems and genuinely ambiguous mass-gap systems. It does NOT establish that relational features identify black holes.