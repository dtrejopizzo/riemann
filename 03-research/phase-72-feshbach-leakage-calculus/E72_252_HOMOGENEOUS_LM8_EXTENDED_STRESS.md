# E72.252 - Homogeneous LM8 extended stress

## Purpose

E72.248 showed that the homogeneous LM8 envelope removes constant drift and passes for
`lambda>=16` in the original tested range. This note stress-tests the same fixed homogeneous
coefficients beyond that range.

No refit is performed.

## Diagnostic

Script:

```text
E72_252_homogeneous_lm8_extended_stress.py
```

Output:

```text
E72.252 homogeneous LM8 extended stress
Uses fixed E72.248 P degree 10 homogeneous coefficients; no refit.
lam L dim exactBSE homEnv slack pass op0 op1
 16 5.545177  40 7.937823e-01 8.686477e-01 +7.225226e-02 YES 3.995e-01 4.374e-01
 24 6.356108  56 7.403769e-01 8.407793e-01 +1.001207e-01 YES 3.490e-01 5.085e-01
 32 6.931472  72 4.921427e-01 6.210974e-01 +3.198026e-01 YES 3.001e-01 2.737e-01
 36 7.167038  80 6.476415e-01 8.015013e-01 +1.393987e-01 YES 3.065e-01 5.083e-01
 40 7.377759  88 5.057326e-01 6.668728e-01 +2.740272e-01 YES 2.728e-01 3.739e-01
 48 7.742402 104 5.427474e-01 7.120783e-01 +2.288217e-01 YES 2.663e-01 4.471e-01
 56 8.050703 120 5.616939e-01 7.319211e-01 +2.089789e-01 YES 2.536e-01 4.922e-01
worst_hom=8.686477e-01 at lambda=16
```

## Reading

The homogeneous LM8 envelope passes through `dim=120` with no visible dimensional drift.

The worst tested value is:

```text
lambda=16, homEnv=0.868648 < 0.9409.
```

Thus the homogeneous replacement fixes the specific obstruction found in E72.247.

## Status

Positive stress evidence. Still needed for proof:

```text
1. rationalize the coefficients;
2. certify R_j(u)>=1 on [-1,0] and R_j(u)>=(1-a_j)^2 on [0,1] by exact interval/SOS;
3. prove the corresponding Green-cycle trace bound uniformly.
```
