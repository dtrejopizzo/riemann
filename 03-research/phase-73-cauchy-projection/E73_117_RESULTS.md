# E73.117 Results - Exact Local Box Verifier

Date: 2026-07-12.

Script:

```text
E73_117_exact_local_box_verifier.py
```

Purpose:

Remove the sampled `tau` suprema from E73.116.  The local factors
`NLC(tau)` and `Gloc(tau)` are not genuinely smooth functions of `tau`;
they depend on `tau` only through `local_window(tau,nwin)`, the set of the
nearest critical ordinates.  Therefore they are constant on the finite
nearest-zero cells cut out by the midpoints

```text
(gamma_j+gamma_{j+1})/2.
```

E73.117 evaluates each cell intersecting the box.  This gives an exact
finite supremum for the local-window part of `LOCK` and `TAIL`.

`OUT` uses the corrected E73.115 rule:

```text
OUT^+(B,L)
 =
 max_{S compatible FAR top-three}
 sum_{k notin S} O_k^+(B,L).
```

## Wide boxes

Output:

```text
E73.117 exact-local box verifier
NLC/Gloc suprema are exact over tau boxes by nearest-zero cell enumeration.
OUT uses interval-order compatible FAR triples.
Wide boxes
 lam     L box                         lockB  tailB    outB mainBox nTri status
  16   5.545 [0.15,0.25]x[13.63,14.63]  -4.519  -6.401 -10.313 2.049e-01    1 FAIL
  20   5.991 [0.15,0.25]x[13.63,14.63]  -7.958 -10.290  -6.737 1.411e-01    2 FAIL
  24   6.356 [0.15,0.25]x[13.63,14.63]  -8.699 -10.725 -13.590 2.366e-01    1 PASS
  28   6.664 [0.15,0.25]x[13.63,14.63]  -8.378 -10.108 -13.337 1.912e-01    1 PASS
  16   5.545 [0.15,0.25]x[20.52,21.52]  -4.537  -6.419 -10.915 2.058e-01    1 FAIL
  20   5.991 [0.15,0.25]x[20.52,21.52]  -7.971 -10.303  -6.903 1.348e-01    2 FAIL
  24   6.356 [0.15,0.25]x[20.52,21.52]  -8.782 -10.807 -13.356 2.542e-01    1 PASS
  28   6.664 [0.15,0.25]x[20.52,21.52]  -8.402 -10.132 -13.083 2.050e-01    1 PASS
```

Interpretation:

```text
lambda >= 24: wide boxes pass all components.
lambda = 20: wide boxes fail only because OUT has two compatible FAR triples.
lambda = 16: wide boxes fail only by LOCK.
```

## Lambda 20 finite subdivision

The `lambda=20` ambiguity is removed by finite subdivision:

```text
Lambda 20 finite subdivision
 lam     L box                         lockB  tailB    outB mainBox nTri status
  20   5.991 [0.15,0.20]x[13.63,13.88]  -8.151 -10.651 -14.191 1.000e-01    1 PASS
  20   5.991 [0.15,0.20]x[13.88,14.13]  -8.144 -10.644 -14.180 1.011e-01    1 PASS
  20   5.991 [0.15,0.20]x[14.13,14.38]  -8.138 -10.638 -14.186 1.022e-01    1 PASS
  20   5.991 [0.15,0.20]x[14.38,14.63]  -8.132 -10.632 -14.211 1.032e-01    1 PASS
  20   5.991 [0.20,0.25]x[13.63,13.88]  -8.012 -10.316 -14.025 1.350e-01    1 PASS
  20   5.991 [0.20,0.25]x[13.88,14.13]  -8.005 -10.309 -14.025 1.365e-01    1 PASS
  20   5.991 [0.20,0.25]x[14.13,14.38]  -7.999 -10.303 -14.031 1.379e-01    1 PASS
  20   5.991 [0.20,0.25]x[14.38,14.63]  -7.994 -10.298 -14.045 1.392e-01    1 PASS
  20   5.991 [0.15,0.25]x[20.52,20.77]  -7.982 -10.314 -14.132 1.329e-01    1 PASS
  20   5.991 [0.15,0.25]x[20.77,21.02]  -7.989 -10.321 -14.122 1.312e-01    1 PASS
  20   5.991 [0.15,0.25]x[21.02,21.27]  -7.996 -10.328 -14.111 1.294e-01    1 PASS
  20   5.991 [0.15,0.25]x[21.27,21.52]  -8.004 -10.336 -14.100 1.275e-01    1 PASS
```

Thus the `lambda=20` wide-box failure is purely a finite FAR-triple
transition.  The transition is removed by a finite box cover.

## Lambda 16 low-scale audit

Subdividing `lambda=16` does not fix the remaining failure:

```text
apart 2 tpart 2 boxes 8  failures 8  worst_lock -4.575  worst_out -10.321
apart 2 tpart 4 boxes 16 failures 16 worst_lock -4.578  worst_out -10.325
apart 4 tpart 2 boxes 16 failures 16 worst_lock -4.580  worst_out -10.321
apart 4 tpart 4 boxes 32 failures 32 worst_lock -4.582  worst_out -10.325
```

The obstruction is not FAR selection or box width.  It is the low-scale
`LOCK` constant in the sufficient theorem.  Therefore `lambda=16` should be
treated as a finite base case with a sharper `LOCK` estimate, not by more
box subdivision.

## Frontier after E73.117

The box route now has a clean split:

```text
lambda >= 24: wide-box GATE-73 passes in this verifier.
lambda = 20: finite subdivided cover passes.
lambda = 16: finite low-scale LOCK base case remains.
```

The next useful step is a sharper finite `LOCK` base certificate for
`lambda=16`, replacing the crude global factor

```text
4(1+exp(alpha L))/alpha
```

by the exact local Hermite/Cauchy expression on the certified FAR triple.

