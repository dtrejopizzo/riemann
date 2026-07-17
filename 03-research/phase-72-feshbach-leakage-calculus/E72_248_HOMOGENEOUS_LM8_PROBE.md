# E72.248 - Homogeneous LM8 probe

## Purpose

E72.247 shows that the current fixed LM8 majorants have `P_j(0)>0`, producing dimensional drift.
This note tests the homogeneous replacement:

```text
P_j(u)=u^2R_j(u),
P_j(0)=P_j'(0)=0.
```

The constraints are:

```text
R_j(u)>=1                 on [-1,0],
R_j(u)>=(1-a_j)^2         on [0,1].
```

## Diagnostic

Script:

```text
E72_248_homogeneous_lm8_probe.py
```

Key output:

```text
-- R degree=8 / P degree=10
 lam exactBSE homEnv slack pass
  12 8.980903e-01 1.017302e+00 -7.640187e-02 NO
  16 7.937823e-01 8.686477e-01 +7.225226e-02 YES
  20 7.348533e-01 8.288609e-01 +1.120391e-01 YES
  24 7.403769e-01 8.407793e-01 +1.001207e-01 YES
  28 6.359406e-01 7.521283e-01 +1.887717e-01 YES
  32 4.921427e-01 6.210974e-01 +3.198026e-01 YES
  36 6.476415e-01 8.015013e-01 +1.393987e-01 YES
```

Lower homogeneous degrees are too loose. Degree `P=10` already passes from `lambda=16` onward but
fails at `lambda=12`.

## Reading

The homogeneous redesign removes the dimensional-drift obstruction. It costs more approximation slack,
especially in the first stable window.

The natural proof package is therefore:

```text
lambda >= 16:
  homogeneous LM8 with P degree 10;

lambda = 12:
  finite exceptional homogeneous certificate of higher degree,
  or direct F2B/interval verification.
```

This is better than the old LM8 fixed polynomial because it has no constant or linear drift.
