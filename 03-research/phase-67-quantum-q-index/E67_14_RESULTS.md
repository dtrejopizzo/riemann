# E67.14 -- the forcer precondition (FIRST positive result of the quantum arc)

**Date:** 2026-07-06.
**Script:** [E67_14_negligible_forcer.py](E67_14_negligible_forcer.py).

## Mechanism under test

The regularization (forcer) is the quotient by NEGLIGIBLES = directions of vanishing quantum
dimension under the canonical pivotal `g=K^2`, `g e_n = q^{2(n+y)} e_n`:
`qdim(v) = |sum_n |c_n|^2 q^{2(n+y)}|`. Negligible <=> qdim = 0.

## Results (z0=100-i, y=1, N=12; q=e^{i pi/ell}, ell=7,11,13)

1. **Diagonal baseline:** `qdim(e_n) = 1.0000` for all n. Nothing negligible -> quotient trivial.
   This is exactly why E67.13 (diagonal q-deformed norms) could not regularize.

2. **Exact off-diagonal defect avoids contamination AND fabrication:** using the exact
   `J = A_N - P_lambda` (not q-deformed norms), **zeta -> ind_- = 0** for all ell. No artifacts,
   no false positives. Architecture lesson: do NOT q-deform the FORM (that injected artifacts);
   keep the form exact and use q only as a pivotal/negligible OVERLAY.

3. **Off-line negatives are non-negligible and spread:** planted off-line zero gives `ind_- = 6`,
   with `qdim in [0.11, 0.73]` (never ~0) and participation ratio `PR = 3.3-7.2` (spread over
   3-7 levels). The off-line RH content carries genuine quantum dimension -> the quotient KEEPS it.

## Reading

Forcer criterion (artifacts negligible / RH content non-negligible) is SATISFIED:
- zeta -> ind_- = 0 (nothing to quotient);
- off-line -> non-negligible, spread negatives (survive the quotient; cannot hide).

This is NECESSARY, not sufficient. The `J` used is exact (needs zeta), so "zeta -> 0" here is still
E67.9. What is newly established:
- the correct ARCHITECTURE: exact form + q negligible-overlay (not a q-deformed form);
- the precondition SATISFIED: off-line content is non-negligible, artifacts are removable.

It is the first necessary condition of the entire quantum arc to come out POSITIVE, and it is clean.

## Remaining gap = the forcing theorem

Prove that the quantum trace of the defect is non-negative **by structure** (a q-trace / fusion /
Verlinde identity), WITHOUT computing the zeros -- i.e. that the q-weighted negative index
`sum_{lambda_i<0} qdim(v_i)` is forced to 0 for the actual defect. Now we know it must live in the
architecture of point (2)-(3): exact defect form, quantum-trace positivity, negligible quotient.

## State

```
solid  : signed index = faithful detector (q=1)                 [E67.9, E67.11]
solid  : diagonal q-form fails (contamination+fabrication)      [E67.12, E67.13]
NEW +  : exact-form + negligible-overlay avoids both, and the
         forcer precondition holds (off-line non-negligible)    [E67.14 this file]
open   : the forcing theorem -- q-trace positivity of the defect
         by structure, without computing the zeros
```
