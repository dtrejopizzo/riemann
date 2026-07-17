# E73.119 Results - Low-Scale LOCK Alpha-Interval Certificate

Date: 2026-07-12.

Script:

```text
E73_119_low_lock_alpha_interval.py
```

Purpose:

Turn the `lambda=16` gridded base probe of E73.118 into a finite
alpha-interval certificate.  The remaining dependence is

```text
z = alpha + i gamma,
alpha in [0.15,0.25].
```

For each compatible FAR triple and each exact local window, the local
quantity is

```text
HWIN(z;W)
 =
 sum_{w in W} |A(z,w) H_0(w)| + |B(z,w) H_0(-w)|.
```

The coefficients are

```text
A(z,w)= i ((e^{wL}-1)+e^{zL}(e^{-wL}-1))/(w-z),
B(z,w)=-i (e^{zL}(e^{wL}-1)+(e^{-wL}-1))/(w+z).
```

E73.119 uses the analytic derivatives

```text
dA/dz = i (N_A'/(w-z) + N_A/(w-z)^2),
dB/dz = -i (N_B'/(w+z) - N_B/(w+z)^2),
```

where

```text
N_A=(e^{wL}-1)+e^{zL}(e^{-wL}-1),
N_A'=L e^{zL}(e^{-wL}-1),

N_B=e^{zL}(e^{wL}-1)+(e^{-wL}-1),
N_B'=L e^{zL}(e^{wL}-1).
```

Then on each alpha subinterval,

```text
HWIN(alpha+i gamma;W)
 <= HWIN(alpha_c+i gamma;W)
    + radius * sup |d_alpha HWIN|,
```

with a small exponential inflation `exp(radius L)` on the derivative term.

Derivative sanity check:

```text
relative error against central finite difference:
5.73e-12  1.80e-11
9.37e-12  8.81e-12
3.53e-11  3.84e-11
```

Output:

```text
E73.119 low-scale LOCK alpha-interval certificate
Uses analytic coefficient derivatives and finite alpha subintervals.
 lam     L box                         lockIntB mainBox nTri status
  16   5.545 [0.15,0.25]x[13.63,14.63]    -9.921 2.049e-01    1 PASS
  16   5.545 [0.15,0.25]x[20.52,21.52]   -10.001 2.058e-01    1 PASS
```

Conclusion:

The low-scale `lambda=16` base case is no longer only a grid probe.  It is
a finite alpha-interval certificate for the exact local `LOCK` expression,
with large slack:

```text
LOCK <= L^-9.921
```

on the first box and

```text
LOCK <= L^-10.001
```

on the second.

Together with E73.117:

```text
lambda=16: exact alpha-interval LOCK base certificate;
lambda=20: finite subdivided box cover;
lambda>=24: wide-box GATE-73 certificate in tested range.
```

The remaining global task is to replace the tested range phrase by an
asymptotic theorem in `L`, or to state the finite certificate as the exact
machine-checkable gate for the current scale range.

