# E72.143 -- Diagonal PSD certificate audit

**Date:** 2026-07-09.
**Role:** test whether the SDP certificate can be made diagonal in the current model-normalized basis.

## 0. Question

E72.142 reduces `NHS` to:

```text
exists P>=0 with ||K_rel-P||_HS<1.
```

The simplest explicit choice is diagonal:

```text
P_diag = diag(max(K_rel,ii,0)).
```

This is the closest diagonal PSD matrix to `K_rel` in Frobenius norm.

If:

```text
||K_rel-P_diag||_HS<1,
```

then the SDP certificate becomes entrywise and no spectral projection is needed.

## 1. Diagnostic

The companion script:

```text
E72_143_diagonal_psd_certificate_probe.py
```

compares the optimal PSD distance with the diagonal PSD distance.

Representative output:

```text
E72.143 diagonal PSD certificate probe
 lam   L  dim  optPSDdist  diagPSDdist  diagDist2  diagMargin  offFrob
   6  3.58   18      0.764        1.243      1.546     -0.546    1.165
   8  4.16   24      0.800        1.265      1.599     -0.599    1.210
  10  4.61   28      0.692        1.145      1.311     -0.311    1.096
  12  4.97   32      0.782        1.167      1.362     -0.362    1.030
  14  5.28   36      0.747        1.116      1.245     -0.245    0.986
  16  5.55   40      0.724        1.079      1.164     -0.164    0.979
  18  5.78   44      0.728        1.080      1.167     -0.167    0.951
```

## 2. Status

```text
rejected: diagonal PSD certificate is too weak;
kept:     PSD-DIST needs off-diagonal structure in the model-normalized basis.
```
