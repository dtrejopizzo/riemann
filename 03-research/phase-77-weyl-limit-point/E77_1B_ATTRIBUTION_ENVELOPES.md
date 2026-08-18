# E77.1b - Attribution envelopes

**Run:** 2026-07-18.

## 1. Statement

E77.1 left the attribution question ambiguous.  This enlarged run asks
whether the planted off-line divisor creates a bounded Weyl-disk radius
(Outcome B), or whether the planted build also drifts toward limit-point
with a much slower, resonance-dominated rate (Outcome A).

The measured quantities are exactly the E77.1 quantities, now with:

```text
N=6,...,18 on lambdas 6,7,8;
beta=0.10,0.20,0.30,0.40;
strength=5.0 plus controls 2.5 and 10.0;
parity fits, moving windows, and three-section block-minimum envelopes;
N=20 feasibility check on lambda 6, beta 0.30, strength 5.0;
dps70 replication on lambda 6, beta 0.30, strength 5.0.
```

No zero locations enter except the declared planted falsifier
`gamma=14.134725141734693790`.  No ambient inverse norm is measured.

## 2. Probe and artifacts

Probe:

```text
E77_1b_attribution_probe.py
```

Outputs:

```text
E77_1b_attribution_results.json  - 39 cases, 507 rows
E77_1b_attribution_results.tsv   - header plus 507 data rows
E77_1b_n20_core.json/.tsv        - N=20 core feasibility check
E77_1b_dps70_core.json/.tsv      - dps70 core precision replication
```

Main command:

```bash
python3 E77_1b_attribution_probe.py \
  --lambdas 6,7,8 \
  --betas 0.10,0.20,0.30,0.40 \
  --strengths 5.0,2.5,10.0 \
  --max-modes 18 \
  --dps 50
```

## 3. Core strength-5 table

`c_all`, `c_tail`, `c_even`, `c_odd`, and `c_block` are log-linear slopes
for all sections, last six sections, even sections, odd sections, and
three-section block minima.

| case | S_18 | radius_18 | shell_18 | c_all | c_tail | c_even | c_odd | c_block |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| zeta L6 | 9.213e27 | 1.085e-28 | 1.268e-21 | 3.853 | 3.854 | 3.789 | 3.955 | 3.855 |
| b.10 L6 | 9.503e2 | 1.052e-3 | 2.412e-3 | 0.417 | 0.311 | 0.357 | 0.512 | 0.605 |
| b.20 L6 | 3.050e2 | 3.279e-3 | 2.328e-3 | 0.708 | 0.160 | 0.539 | 0.978 | 0.755 |
| b.30 L6 | 2.721e2 | 3.676e-3 | 2.547e-3 | 0.691 | 0.365 | 0.509 | 0.983 | 0.721 |
| b.40 L6 | 2.742e2 | 3.647e-3 | 2.853e-3 | 0.609 | 0.329 | 0.473 | 0.825 | 0.697 |
| zeta L7 | 8.539e26 | 1.171e-27 | 6.579e-22 | 3.850 | 2.576 | 3.860 | 3.835 | 3.970 |
| b.10 L7 | 1.446e2 | 6.917e-3 | 1.322e-2 | 0.281 | -0.726 | 0.194 | 0.419 | 0.213 |
| b.20 L7 | 1.304e2 | 7.669e-3 | 5.542e-3 | 0.342 | -0.090 | 0.313 | 0.388 | 0.368 |
| b.30 L7 | 2.217e2 | 4.511e-3 | 3.082e-3 | 0.473 | 0.121 | 0.466 | 0.484 | 0.567 |
| b.40 L7 | 3.275e2 | 3.054e-3 | 2.366e-3 | 0.633 | 0.231 | 0.656 | 0.595 | 0.958 |
| zeta L8 | 9.959e25 | 1.004e-26 | 1.945e-21 | 3.843 | 3.252 | 3.847 | 3.838 | 3.958 |
| b.10 L8 | 1.626e3 | 6.152e-4 | 5.086e-3 | 0.415 | -0.553 | 0.458 | 0.347 | 0.452 |
| b.20 L8 | 3.000e2 | 3.334e-3 | 5.912e-3 | 0.479 | -0.080 | 0.469 | 0.496 | 0.555 |
| b.30 L8 | 2.565e2 | 3.899e-3 | 5.561e-3 | 0.548 | 0.183 | 0.609 | 0.449 | 0.577 |
| b.40 L8 | 2.509e2 | 3.985e-3 | 5.299e-3 | 0.551 | 0.233 | 0.598 | 0.475 | 0.604 |

## 4. Controls

Strength controls preserve the same qualitative picture.

```text
lambda 6: all 12 planted controls have positive c_all and positive
          c_block; endpoint shell mass is 0.0023--0.0032.
lambda 7: all 12 planted controls have positive c_all and positive
          c_block; some c_tail are negative because late resonant drops
          occur, but parity/block envelopes remain positive.
lambda 8: all 12 planted controls have positive c_all and positive
          c_block; some c_tail are negative, again due to late drops.
```

The N=20 core feasibility run gives:

```text
zeta L6:     S_18=9.213e27, S_20=1.540e30, radius_20=6.493e-31
plant b.30: S_18=2.721e2,  S_20=9.411e2,  radius_20=1.063e-3
```

The dps70 core replication agrees with the dps50 core values at the
displayed precision.  In particular the planted N=17 spike and N=18 drop
are stable numerical features, not a working-precision floor.

## 5. Verdict

Outcome B is not supported by E77.1b.  Across lambdas 6,7,8 and all
strength controls, the planted build does not show a stable bounded
envelope.  It shows resonance spikes and drops, but the parity fits and
three-section block-minimum slopes remain positive in every measured case.

Outcome A is now the working attribution:

```text
LP qualitative contraction appears to hold for zeta and planted builds;
the zeta rate is huge, with c about 3.84--3.85;
the planted rate is slow, typically c about 0.3--0.7 in the measured range;
the arithmetic falsifier therefore should break at IDENT, or at a
quantitative LP rate statement stronger than bare limit-point.
```

This is not a proof of LP.  It is a strict reduction of the empirical
ambiguity left by E77.1: the next finite target is no longer
"does planted saturate?", but

```text
E77.LP-ENV:
prove a positive lower-envelope growth estimate for the canonical
solution energy S_N, stable under parity and finite-rank resonances.
```

The natural proof route is E77.2/E77.3: use RDP-1 to obtain a discrete
Koppelman-Pincus or explicit displacement-kernel theorem that rules out
l2 kernel directions and yields the observed block-envelope growth.

## 6. Status

```text
proved:    no theorem-level LP or IDENT statement is proved here;
observed:  zeta contracts to radius 1.09e-28, 1.17e-27, 1.00e-26
           at lambdas 6,7,8 respectively with shell mass about 1e-21;
observed:  every planted main/control case has positive c_all and
           positive three-section block-minimum slope;
observed:  planted shell mass falls to roughly 0.002--0.016 at N=18;
observed:  N=20 core plant rises to S_20=941, still with no plateau;
observed:  dps70 reproduces the dps50 core run;
refuted:   the clean P76.066 reading "planted stalls near 4e-3 radius"
           as an asymptotic attribution claim;
open:      theorem-grade LP, IDENT, and radical-tail estimates;
next:      E77.2 commutator theorem attempt, with E77.LP-ENV as the
           finite object to prove or autopsy.
```
