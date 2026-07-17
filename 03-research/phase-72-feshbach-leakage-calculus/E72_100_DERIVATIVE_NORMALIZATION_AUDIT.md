# E72.100 -- Derivative normalization audit

**Date:** 2026-07-09.
**Role:** test whether the finite-band Stieltjes defect is controlled by the derivative of the finite
Weyl root equation.

## 0. Motivation

When a quantity is evaluated at roots:

```text
M_xi(tau_j)=0,
```

the derivative:

```text
M'_xi(tau_j)
```

is the natural residue/normalization factor. A plausible next closure would be that the bordered
defect:

```text
D2_x(H,s;tau_j)
```

is small after division by `M'_xi(tau_j)`, or that it is proportional to a simple normalized pairing
such as:

```text
<xi,Z_x(tau_j)>/M'_xi(tau_j).
```

## 1. Probe

The companion script:

```text
E72_100_derivative_normalization_probe.py
```

prints:

```text
|D2|,
|M'_xi|,
|D2/M'_xi|,
|<xi,Z>/M'_xi|.
```

## 2. Result

Representative values:

```text
lambda=12:
  tau=0.825  |D2/M'_xi|=3.75e-02  |<xi,Z>/M'_xi|=1.49e-01
  tau=8.118  |D2/M'_xi|=1.08e-01  |<xi,Z>/M'_xi|=5.34e-02

lambda=20:
  tau=0.241  |D2/M'_xi|=1.55e+00  |<xi,Z>/M'_xi|=9.07e-02
  tau=3.844  |D2/M'_xi|=1.30e-01  |<xi,Z>/M'_xi|=1.60e-02

lambda=24:
  tau=6.889  |D2/M'_xi|=1.22e-03  |<xi,Z>/M'_xi|=1.27e-03
  tau=9.167  |D2/M'_xi|=2.06e-02  |<xi,Z>/M'_xi|=7.27e-03
```

The normalized values are not stable enough to reveal a simple derivative-factor theorem.

## 3. Conclusion

The finite-band Stieltjes defect is not explained by a scalar root-derivative normalization alone.
The missing identity, if it exists, must involve the full shorted matrix:

```text
C_E,
```

not only the scalar Weyl function:

```text
M_xi.
```

This reinforces the determinant endpoint of E72.97--E72.98.

## 4. Status

```text
rejected: D2 vanishing as a simple M'_xi-normalized scalar root effect;
kept:     D2 as a full bordered determinant over the shorted even complement.
```
