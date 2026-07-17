# E72.183 -- Norm interval trace certificate

**Date:** 2026-07-09.
**Role:** replace the operator-norm interval hypotheses in Adaptive-SRP by finite trace inequalities.

## 0. Trace certificate

For a self-adjoint matrix `K` and `M>0`:

```text
Tr((K/M)^(2r)) < 1
```

implies:

```text
||K|| < M.
```

Indeed, if `lambda_max=||K||`, then:

```text
(lambda_max/M)^(2r) <= Tr((K/M)^(2r)).
```

Thus the Phase 72 interval hypotheses:

```text
||K_0||<=0.90,
||K_1||<=0.60
```

can be replaced by finite trace-power inequalities:

```text
Tr((K_0/0.90)^16)<1,
Tr((K_1/0.60)^16)<1.                         (NTC-8)
```

These are prime-power cycle identities of length `16`.

## 1. Diagnostic output

The companion script:

```text
E72_183_norm_trace_probe.py
```

reports:

```text
E72.183 norm interval trace-power probe
If Tr((K/M)^(2r)) < 1, then ||K|| < M.
 lam    L dim  op0  op1  r4_K0 r4_K1  r8_K0 r8_K1  r12_K0 r12_K1 pass8
  12  4.97  32 0.439 0.445 6.507e-03 9.275e-02 1.412e-05 8.462e-03 3.786e-08 7.783e-04 YES
  14  5.28  36 0.429 0.445 4.300e-03 9.250e-02 8.011e-06 8.466e-03 1.948e-08 7.789e-04 YES
  16  5.55  40 0.399 0.437 2.362e-03 8.007e-02 2.604e-06 6.353e-03 3.597e-09 5.063e-04 YES
  18  5.78  44 0.362 0.313 1.015e-03 5.776e-03 4.979e-07 3.032e-05 3.268e-10 1.664e-07 YES
  20  5.99  48 0.356 0.449 1.164e-03 9.779e-02 5.359e-07 9.544e-03 2.879e-10 9.323e-04 YES
  22  6.18  52 0.326 0.500 5.966e-04 2.322e-01 1.389e-07 5.386e-02 3.726e-11 1.250e-02 YES
  24  6.36  56 0.349 0.508 8.302e-04 2.662e-01 3.242e-07 7.079e-02 1.490e-10 1.883e-02 YES
  26  6.52  60 0.335 0.369 4.202e-04 2.068e-02 1.367e-07 4.239e-04 5.027e-11 8.727e-06 YES
  28  6.66  64 0.346 0.482 5.164e-04 1.732e-01 2.264e-07 2.995e-02 1.074e-10 5.183e-03 YES
```

`r=8` has large numerical margin in the tested stable windows.

## 2. Updated final finite target

With E72.182 and E72.183, the final stable arithmetic target can be stated without operator norms:

```text
NTC-8:
Tr((K_0/0.90)^16)<1,
Tr((K_1/0.60)^16)<1.

ASRP-0.05:
D_x+1 >= 0.99 sqrt(d_x)/(0.05 pi),
Tr(G_{x,D_x}^2)<0.9025.
```

All three inequalities are finite mixed von Mangoldt cycle inequalities. The first two have fixed
cycle length `16`; the last has adaptive cycle length `2D_x=O(sqrt(d_x))`.

## 3. Remaining theorem

The Phase 72 arithmetic theorem is now:

```text
For all sufficiently large x, prove NTC-8 and ASRP-0.05.
```

Together with finite-window `F2B` and the non-arithmetic gates, this implies scalar WRL resonance
annihilation.
