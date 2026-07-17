# E72.257 - Strict homogeneous LM8 stress

## Purpose

E72.256 gives the strict interval-certified homogeneous LM8 majorant. This note checks its numerical
cost over the extended stress range.

## Diagnostic

Script:

```text
E72_257_strict_homogeneous_lm8_stress.py
```

Output:

```text
E72.257 strict homogeneous LM8 stress
Uses strict R-certified buffer 1.5e-03; no refit.
lam L dim exactBSE strictHom slack pass
 16 5.545177  40 7.937823e-01 8.709150e-01 +6.998496e-02 YES
 24 6.356108  56 7.403769e-01 8.427540e-01 +9.814604e-02 YES
 32 6.931472  72 4.921427e-01 6.224934e-01 +3.184066e-01 YES
 36 7.167038  80 6.476415e-01 8.031647e-01 +1.377353e-01 YES
 40 7.377759  88 5.057326e-01 6.681808e-01 +2.727192e-01 YES
 48 7.742402 104 5.427474e-01 7.134591e-01 +2.274409e-01 YES
 56 8.050703 120 5.616939e-01 7.332795e-01 +2.076205e-01 YES
worst_strict_hom=8.709150e-01 at lambda=16
```

## Reading

The strict buffer costs little. The worst extended value remains:

```text
0.870915 < 0.9409.
```

Thus the corrected homogeneous LM8 certificate is both interval-certified and stress-stable through
`dim=120`.
