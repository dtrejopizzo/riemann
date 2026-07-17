# E73.114 Results - GATE-73 Box Integration Check

Date: 2026-07-12.

Script:

```text
E73_114_gate73_box_verifier.py
```

Purpose:

Integrate the possible-set box certificate for the `FAR3-MAIN-RAT`
component with the previously consolidated `GATE-73` budget.

Important scope:

```text
MAIN        is certified on the full box by E73.112/E73.113.
LOCK/TAIL/OUT are still evaluated at the box center in this script.
```

Thus this is not yet the full uniform box theorem for `GATE-73`.  It is
the compatibility check showing that the box-certified MAIN component fits
inside the same numerical gate without consuming the budget.

Targets used:

```text
center LOCK <= L^-5
center TAIL <= L^-5
center OUT  <= L^-9
box MAIN    <= 1
```

The tested boxes are the wide stress boxes

```text
alpha in [0.15,0.25],
tau   in [gamma_j-0.50,gamma_j+0.50],
j=1,2.
```

Output:

```text
E73.114 GATE-73 box verifier
MAIN uses possible-set box certificate; LOCK/TAIL/OUT shown at box center.
Targets: center LOCK<=L^-5, TAIL<=L^-5, OUT<=L^-9; box MAIN<=1.
 lam     L box                         lockB  tailB    outB  mainBox status
  16   5.545 [0.15,0.25]x[13.63,14.63]  -6.685  -8.245 -10.504 2.049e-01 PASS
  16   5.545 [0.15,0.25]x[20.52,21.52]  -6.732  -8.292 -11.206 2.058e-01 PASS
  20   5.991 [0.15,0.25]x[13.63,14.63]  -9.919 -12.449 -14.213 1.411e-01 PASS
  20   5.991 [0.15,0.25]x[20.52,21.52]  -9.955 -12.485 -14.314 1.348e-01 PASS
  24   6.356 [0.15,0.25]x[13.63,14.63] -10.043 -12.204 -15.634 2.366e-01 PASS
  24   6.356 [0.15,0.25]x[20.52,21.52] -10.155 -12.317 -13.630 2.542e-01 PASS
  28   6.664 [0.15,0.25]x[13.63,14.63]  -8.954 -11.482 -13.560 1.912e-01 PASS
  28   6.664 [0.15,0.25]x[20.52,21.52]  -9.031 -11.560 -14.793 2.050e-01 PASS
```

Worst observed margins:

```text
LOCK center exponent  = -6.685  <= -5
TAIL center exponent  = -8.245  <= -5
OUT  center exponent  = -10.504 <= -9
MAIN box budget       =  0.2542 <= 1
```

Conclusion:

`FAR3-MAIN-RAT` survives intervalization on the wide boxes with a factor
of about four slack.  The center budgets for `LOCK-COMP-BUD`,
`TAIL-LC-BUD`, and `OUT-FAR` remain safely below their targets on the same
boxes.

The next mathematical step is not another point computation.  It is to
intervalize `LOCK/TAIL/OUT`, or prove a monotone box domination reducing
them to the already certified `MAIN`/Hermite envelopes.

