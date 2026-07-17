# E72.158 -- Prime-cell PSD audit

**Date:** 2026-07-09.
**Role:** test whether the low-rank PSD certificate comes from dominant prime-power cells.

## 0. Arithmetic split

The CCM matrix has:

```text
H_actual = H_model - sum_{p^m<=x} (log p)p^(-m/2) Q_{m log p}.
```

Therefore, after projection to the even Feshbach complement:

```text
C_actual-C_model
 = - sum_{p^m<=x} (log p)p^(-m/2) B_Q^*Q_{m log p}B_Q.
```

The relative perturbation is:

```text
K_rel=C_model^(-1/2)(C_actual-C_model)C_model^(-1/2).
```

## 1. Question

E72.144 shows that a rank 2--3 positive PSD approximant certifies `PSD-DIST`.  The first structural
candidate is:

```text
positive parts of the largest prime-power cell contributions.
```

If this works, `PSD-DIST` becomes a finite prime-cell certificate rather than an abstract spectral
projection.

## 2. Diagnostic

The companion script:

```text
E72_158_prime_cell_psd_probe.py
```

constructs each relative prime-power cell, takes the positive part of the top `k` cell matrices by
Frobenius norm, and measures its PSD distance to `K_rel`.

Representative output:

```text
E72.158 prime-cell PSD probe topk=3
 lam   L cells  distOpt  distTopCells  topMassFrac  topCellN
   6  3.58    18    0.764        1.375        0.336 5,3,7
   8  4.16    27    0.800        1.364        0.247 5,7,3
  10  4.61    35    0.692        1.245        0.201 5,7,3
  12  4.97    47    0.782        1.221        0.170 5,7,3
```

The top prime-power cells do not produce a valid PSD certificate: the distance remains above `1`.
Thus the positive approximant is not local over a few dominant prime cells.

## 3. Status

```text
rejected: PSD-DIST from the positive parts of a few largest prime-power cells;
next:     test block/global arithmetic approximants.
```
