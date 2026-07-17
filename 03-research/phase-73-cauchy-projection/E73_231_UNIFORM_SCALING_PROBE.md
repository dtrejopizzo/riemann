# E73.231 - Uniform scaling probe

Date: 2026-07-14.

## 1. Purpose

E73.230 closes the finite-window scalar interval wrapper.  The remaining
mathematical task is uniform production in `L` and admissible windows.

E73.231 is a diagnostic stress test beyond the certified windows.  It asks
whether the closed coefficient/weight scalar wrapper shows visible blow-up in
moderately larger windows.

## 2. Important caveat

The probe extrapolates the certified `rho_eta` exponent beyond `lambda=12`.
Therefore it is not a certificate.  It is only a scaling diagnostic for the
coefficient/weight side of the wrapper.

## 3. Result

For representative rows:

```text
lambda  centerB  RclosedB  ratio
8       -21.68   -46.32    5.6e-16
10      -18.50   -42.28    1.7e-16
12      -20.62   -40.44    1.6e-14
14      -18.38   -40.35    1.3e-16
16      -20.52   -42.80    2.7e-17
18      -16.56   -42.25    2.7e-20
```

The weight size and coefficient l1 size do not display an immediate finite
blow-up in this range.  The observed bottleneck remains the availability of a
uniform `rho_eta` certificate, i.e. the bordered Krawczyk/eigenline production
uniformly in `L`.

## 4. Status

```text
diagnostic: no coefficient/weight blow-up observed up to lambda=18;
not proof: rho_eta beyond lambda=12 is extrapolated;
next: state the uniform theorem in terms of explicit factor bounds.
```
