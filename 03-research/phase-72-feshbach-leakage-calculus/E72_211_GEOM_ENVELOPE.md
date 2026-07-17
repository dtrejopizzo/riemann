# E72.211 - Geometric envelope for resonant cell energy

## Purpose

E72.210 reduced the resonant pair energy to

```text
Res_2(S_j)=2 sum_{n in S_j(x)} (Lambda(n)^2/n) Geom_x(log n),
```

where

```text
Geom_x(y)=||C_x^(-1/2)B_x^*U_yB_xC_x^(-1/2)||_HS^2.
```

This note probes the continuous shape and scale of `Geom_x(y)`.

## Diagnostic

Script:

```text
E72_211_geom_envelope_probe.py
```

Output:

```text
E72.211 continuous Geom envelope probe
Geom_x(y)=||C^-1/2 B* U_y B C^-1/2||_HS^2
lam L dim maxG at maxG*L maxG*L2 maxG*L3 intG intG*L2
 12  4.97  65 1.756217e-01 0.020 8.728e-01 4.338e+00 2.156e+01 7.683e-02 1.898e+00
 16  5.55  81 1.104889e-01 0.030 6.127e-01 3.397e+00 1.884e+01 5.154e-02 1.585e+00
 20  5.99  97 7.589222e-02 0.020 4.547e-01 2.724e+00 1.632e+01 3.760e-02 1.350e+00
 24  6.36 113 6.470310e-02 0.020 4.113e-01 2.614e+00 1.661e+01 2.952e-02 1.193e+00
 28  6.66 129 4.969396e-02 0.020 3.312e-01 2.207e+00 1.471e+01 2.445e-02 1.086e+00

Shape samples
lam u=0.1 u=0.25 u=0.5 u=0.75 u=0.9
 12 1.4634e-01 1.2209e-01 8.0982e-02 3.7782e-02 1.3827e-02
 16 9.8134e-02 8.2109e-02 5.4710e-02 2.6208e-02 9.9531e-03
 20 7.1127e-02 5.9985e-02 3.9775e-02 1.9108e-02 7.2664e-03
 24 5.6725e-02 4.7000e-02 3.1172e-02 1.4610e-02 5.1932e-03
```

## Reading

The geometric factor has a stable profile:

```text
Geom_x(y) decreases as y/L increases,
Geom_x(y) is O(L^-2) on prime-power support y>=log 2,
int_0^1 Geom_x(uL)du is also O(L^-2).
```

The continuous maximum over `u in [0.02,0.98]` is near the artificial lower endpoint. Prime powers do
not sample arbitrarily close to `0`; the first cell is `y=log 2`, i.e. `u=log 2/L`. On the prime-power
support tested here, the effective envelope is closer to the `u=0.1` samples, giving:

```text
Geom_x(log n) <= C_geom/L^2
```

with `C_geom` around `3.7` in the tested windows.

## Candidate envelope

A usable resonant-pair bound would follow from:

```text
Geom_x(y) <= (C/L^2) Phi(y/L),       y in [log 2,L],
```

where `Phi` is positive, decreasing, and `Phi(0.1)~=1`.

Then

```text
Res_2(S_j)
<= (2C/L^2) sum_{n in S_j(x)} (Lambda(n)^2/n) Phi(log n/L).
```

The remaining arithmetic input is no longer RH-strength. It is a prime-square weighted first moment,
controlled by elementary Chebyshev/PNT-type estimates for `sum Lambda(n)^2/n` with a smooth monotone
weight.

## Status

Reduced:

```text
resonant pair energy
  -> geometric envelope Geom_x(y)
  -> weighted sum of Lambda(n)^2/n.
```

Open:

```text
prove the O(L^-2) geometric envelope for the model Feshbach Green operator.
```

This is a non-arithmetic analytic estimate on the archimedean/model complement, not a zero-resonance
or RH-equivalent statement.
