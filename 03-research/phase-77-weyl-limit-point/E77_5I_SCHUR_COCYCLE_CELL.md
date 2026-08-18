# E77.5i - Schur Cocylic Cell Anatomy

## Objective

E77.5h reduced `THETA-REG` to the signed three-term Schur cocycle

```text
Delta theta = A + B + C,
```

where

```text
A = (Delta tau) v_N c_N,
B = tau_M (Delta v) c_N,
C = tau_M v_M (Delta c),

v_N = Sigma_N^{-1}kappa_N,
c_N = 1/t0_N,
M = N+2.
```

E77.5i asks whether this cocycle can be reduced further to a two-term
cancellation, or whether all three terms must remain coupled.

## Probe

Artifacts:

```text
E77_5i_schur_cocycle_cell_probe.py
E77_5i_schur_cocycle_cell_results.json
E77_5i_smoke_results.json
```

Main command:

```bash
python3 E77_5i_schur_cocycle_cell_probe.py --lambda 6 --max-modes 22 --dps 100 --output E77_5i_schur_cocycle_cell_results.json
```

The probe computes:

```text
A+B, A+C, B+C,
max(|A|,|B|,|C|)/|Delta theta|,
min(|A+B|,|A+C|,|B+C|)/|Delta theta|.
```

No absolute estimate is used as a proof step.  The absolute values are only
diagnostics after the signed finite objects have been assembled.

## Certification Table

Max/min over `sigma in {0.55,0.6,0.75,1,1.5,2,3}`.

| build | step | max abs Delta theta | max part / Delta | best pair / Delta | best pair |
|---|---:|---:|---:|---:|---|
| zeta | 8 -> 10 | 0.068445728 | 977.064 | 66.7856 | AB |
| zeta | 10 -> 12 | 0.053619596 | 162973.1 | 942.114 | BC |
| zeta | 12 -> 14 | 0.023515542 | 3535.00 | 49.0931 | AB |
| zeta | 14 -> 16 | 0.022835206 | 1983.45 | 606.326 | AB |
| zeta | 16 -> 18 | 0.017264103 | 16409.6 | 6240.74 | BC |
| zeta | 18 -> 20 | 0.015438585 | 6014.89 | 1127.95 | AB |
| zeta | 20 -> 22 | 0.0067492443 | 14606.4 | 2204.43 | BC |
| planted | 8 -> 10 | 2.8023251 | 1.342 | 0.265 | AB |
| planted | 10 -> 12 | 1.8421061 | 13.108 | 5.019 | BC |
| planted | 12 -> 14 | 3.6679515 | 2.884 | 0.849 | AC |
| planted | 14 -> 16 | 7.2624973 | 0.858 | 0.142 | AC |
| planted | 16 -> 18 | 1.8386094 | 0.509 | 0.491 | BC |
| planted | 18 -> 20 | 1.9241482 | 0.442 | 0.558 | AC |
| planted | 20 -> 22 | 1.9757430 | 0.894 | 0.106 | BC |

For zeta, even the best pair remains at least

```text
49.09 * |Delta theta|
```

and can be as large as

```text
6240.74 * |Delta theta|.
```

For the planted build, best-pair ratios are often below `1`; the off-line
plant does not exhibit the same ternary cancellation anatomy.

## Autopsy

The two-term reduction fails.  The zeta cancellation is not carried by
`A+B`, `A+C`, or `B+C` alone.  It requires the full signed sum

```text
A+B+C.
```

This is a stricter obstruction than E77.5h: not only are separate factor
estimates impossible, pairwise cell reductions are also too coarse.  Any
proof that discards one of the three terms before cancellation is now
invalid for the observed zeta mechanism.

The planted falsifier gives the complementary control: it may have smaller
individual cancellation ratios, but it keeps `Delta theta` at O(1).  Thus
the zeta signature is not "large pair cancellation" in isolation; it is
large ternary cancellation producing a Cauchy `theta_N`.

## Reduced Target

`SCHUR-COCYCLE` is reduced to:

```text
TERNARY-CELL-CANCEL:
  derive A+B+C as one finite cell/Loewner object and prove its signed
  leading term is summably small on sigma-compacts.
```

The next proof must not split into:

```text
factor bounds,
pair bounds,
absolute term bounds.
```

It must derive a single coupled identity for `A+B+C`, probably by comparing
the two consecutive Schur complements before inversion and only then
applying the selected Cauchy row.

## Status

```text
proved:    exact pair-anatomy probe for the Schur cocycle;
refuted:   any two-term/pair cancellation closure;
observed:  zeta requires genuinely ternary cancellation;
observed:  planted fails the Cauchy Delta-theta behavior and does not
           reproduce the ternary anatomy;
reduced:   SCHUR-COCYCLE -> TERNARY-CELL-CANCEL;
next:      E77.5j should derive the full A+B+C cocycle from consecutive
           Schur complements as a single finite Loewner/cell residual.
```
