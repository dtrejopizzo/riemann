# E72.287 -- Dirichlet-symbol floor for APCB

**Purpose.** Give a sufficient symbolic form of APCB.

E72.285 writes

```text
Delta_arith = -sum_{n<=e^L} Lambda(n)n^(-1/2) Q_{log n}.
```

Using the one-sided overlap `Q_y=U_y+U_y^*`, define on `L^2(R)` the translation operator

```text
T_L = sum_{n<=e^L} Lambda(n)n^(-1/2) T_{log n}.
```

Its Fourier multiplier is the finite Dirichlet symbol

```text
P_L(omega)=sum_{n<=e^L} Lambda(n)n^(-1/2) exp(i omega log n).
```

The finite interval operator in APCB is a compression of `T_L+T_L^*` to the finite Fourier window and
then to the even sector.  Hence

```text
lambda_max(Delta_arith)_+
<= -2 inf_omega Re P_L(omega).                              (DSF)
```

Therefore APCB follows from the explicit symbol-floor estimate

```text
-2 inf_{omega in R} Re P_L(omega) = O(L^2).                 (DSF-O2)
```

This is stronger than APCB, but it is a scalar finite Dirichlet-polynomial inequality.

## Probe

Run:

```text
python3 E72_287_dirichlet_symbol_floor_probe.py
```

Output:

```text
E72.287 Dirichlet-symbol floor probe
P_L(omega)=sum Lambda(n)n^-1/2 exp(i omega log n), n<=e^L.
APCB follows from -2 min_omega Re P_L(omega)=O(L^2).
lam L posDelta/L2 symbolFloor/L2 argMin minRe
 16 5.545177 1.617975e-01 1.260732e+00 7.040000e-01 -1.938312e+01
 20 5.991465 1.530683e-01 1.418617e+00 6.440000e-01 -2.546251e+01
 24 6.356108 1.428683e-01 1.553751e+00 6.040000e-01 -3.138584e+01
 28 6.664409 1.406409e-01 1.697788e+00 5.720000e-01 -3.770306e+01
 32 6.931472 1.327397e-01 1.836460e+00 5.480000e-01 -4.411663e+01
```

## Reading

The symbol floor dominates the finite positive part, as expected for a compression bound.  It is much
looser than the actual APCB constant, but still on the desired `L^2` scale in the tested windows.

This gives a scalar route to APCB:

```text
prove DSF-O2 for P_L(omega)
=> APCB
=> upper complement
=> compact-root commutator.
```

The new arithmetic problem is no longer an operator norm: it is the lower envelope of a finite
Dirichlet polynomial on the critical half-weight.
