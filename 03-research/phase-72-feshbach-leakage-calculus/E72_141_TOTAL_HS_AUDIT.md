# E72.141 -- Total relative Hilbert-Schmidt audit

**Date:** 2026-07-09.
**Role:** test whether the negative-HS gate can be replaced by an unsigned trace-square bound.

## 0. Question

E72.140 proves:

```text
||K_rel^-||_HS<1 => RFBD.
```

A stronger but simpler certificate would be:

```text
||K_rel||_HS<1.                                             (THS)
```

Since:

```text
||K_rel^-||_HS <= ||K_rel||_HS,
```

`(THS)` implies `(NHS)`.

The benefit is that `(THS)` is a plain trace identity:

```text
Tr(K_rel^2)<1,
```

with no spectral projection onto the negative part.

## 1. Diagnostic

The companion script:

```text
E72_141_total_hs_probe.py
```

reports total, negative, and positive Hilbert-Schmidt norms of `K_rel`.

Representative output:

```text
E72.141 total relative HS probe
 lam   L  dim  totalHS  totalHS2  negHS  posHS  trace  min  max
   6  3.58   18    1.300     1.690  0.764  1.052  0.056 -0.425  0.607
   8  4.16   24    1.315     1.730  0.800  1.044 -0.095 -0.489  0.569
  10  4.61   28    1.195     1.429  0.692  0.975 -0.026 -0.377  0.495
  12  4.97   32    1.204     1.450  0.782  0.915 -0.168 -0.574  0.463
  14  5.28   36    1.149     1.321  0.747  0.873 -0.090 -0.565  0.398
  16  5.55   40    1.115     1.244  0.724  0.848 -0.188 -0.542  0.371
  18  5.78   44    1.094     1.197  0.728  0.817 -0.389 -0.554  0.347
```

## 2. Status

```text
rejected: THS is too strong; positive harmless directions push totalHS above 1;
kept:     NHS is the correct signed certificate.
```
