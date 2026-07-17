# E73.209 - Entry-radius target for the Krawczyk matrix interval

Date: 2026-07-14.

## 1. Purpose

E73.208 gives an admissible operator-norm radius `epsH` for the bordered
Krawczyk certificate.  This note converts that into a concrete per-entry target
for the closed finite-frequency matrix engine.

## 2. From entry radii to operator radius

Let `[H]` be an interval Hermitian matrix centered at `H_0`, and suppose every
entry satisfies:

```text
|H_mn-H_0,mn| <= r_entry.
```

Then the error matrix `E=H-H_0` satisfies:

```text
||E||_op <= ||E||_F <= d r_entry,
```

where `d=2N+1` is the matrix dimension.  Therefore the Krawczyk budget
`||E||_op <= epsH` is guaranteed by:

```text
r_entry <= epsH/d.                                  (1)
```

This is crude but sufficient as a first certificate target.

## 3. Closed entry components

Each entry has the form:

```text
H_mn=A_L^digamma[Q_mn]-P_L[Q_mn].
```

The interval radius per entry is the sum of:

```text
R_entry <= R_elem + R_WR_head + R_digamma_tail + R_exp_tail + R_prime.
```

All terms except `R_digamma_tail` are elementary finite sums of exponentials
and rational operations.  The digamma tail uses:

```text
D_1(R,omega)=1/2[psi(R+1/2)-psi(R+1/4-iomega/2)],
D_2(R,omega)=1/4 psi_1(R+1/4-iomega/2).
```

Thus the only non-elementary enclosure needed for the matrix interval is the
same `psi/psi_1` enclosure already isolated in E73.198--E73.199.

## 4. Numeric target from E73.208

For the tested windows:

```text
lambda  dim  epsHmax       target r_entry=epsHmax/d
8       13   L^-54.46      L^-56.26
10      17   L^-50.07      L^-51.93
12      21   L^-47.04      L^-48.94
```

Since the high-precision centers use 100 decimal digits, these targets are
well above the arithmetic precision floor.  A rigorous ball implementation
should therefore be feasible.

## 5. Status

```text
proved: per-entry radius target implies Krawczyk matrix budget;
open: outward-rounded implementation of the closed entry enclosures.
```
