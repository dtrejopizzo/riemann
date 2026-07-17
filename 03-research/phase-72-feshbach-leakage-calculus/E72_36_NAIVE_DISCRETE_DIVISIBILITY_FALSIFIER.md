# E72.36 -- Falsifier for naive discrete Mellin divisibility

**Date:** 2026-07-08.
**Role:** test whether the divisibility from E72.33 is already present in the raw finite CCM matrices
with the most direct discrete cell convention.

## 0. Test convention

Use the existing Phase 71 finite CCM matrix:

```text
QW_x = H_x = H_x^0 - sum_{n<=x} Lambda(n)T_{x,n},
```

where `T_{x,n}` is the prime-power cell matrix whose entries are

```text
n^(-1/2) q_{ij}(log n).
```

Take:

```text
k_x      = ground vector of H_x^0,
xi_x     = ground vector of H_x,
P_x      = Weyl numerator from xi_x,
v_{x,s}  = C_x^(-1)Q_x(sI-D_x)^(-1)1_x,
```

and define the naive discrete Mellin scalar:

```text
M_x^{disc}(s;z)=sum_{n<=x, Lambda(n)!=0} n^z <v_{x,s},T_{x,n}k_x>.
```

This is not yet the final renormalized continuous kernel from E72.31. It is the cheapest diagnostic:
does raw divisibility already hold?

## 1. Result

It does not. Representative values at finite Weyl roots `r`:

```text
lambda=4, N=20:
  r=3.3606    |M(r)|=7.33e1
  r=7.2222    |M(r)|=2.57e6
  r=10.5697   |M(r)|=1.37e10
  r=14.1347   |M(r)|=1.23e14

lambda=5, N=22:
  r=1.6594    |M(r)|=1.01e0
  r=8.0256    |M(r)|=5.37e8
  r=14.1347   |M(r)|=1.34e17
  r=18.6599   |M(r)|=1.98e23

lambda=6, N=22:
  r=3.1656    |M(r)|=8.09e2
  r=5.2956    |M(r)|=9.91e5
  r=7.1938    |M(r)|=6.47e8
  r=9.2315    |M(r)|=7.00e11
```

The values grow with the expected exponential scale of `n^z`; they are not zero or numerically close to
zero.

## 2. Interpretation

The raw discrete Mellin scalar is not divisible by the finite Weyl numerator `P_x`.

Therefore the desired divisibility cannot be:

```text
take the prime-power cells exactly as they appear in QW and sum n^z.
```

If a divisibility theorem exists, it must use at least one of:

```text
1. the Abel-renormalized boundary expression
   x^zL_x(s;x)-int_1^x u^z partial_uL_x(s;u)du;
2. the model-main subtraction before Mellin transform;
3. a normalized Mellin character (u/x)^z rather than u^z;
4. the exact continuous interpolation of cells, not the raw prime-power lattice;
5. an additional bordered/Feshbach coboundary term.
```

## 3. Consequence

This falsifies the strongest and simplest hope:

```text
M_x^{disc}(s;z) is exactly divisible by P_x(z).
```

The route is not dead, but the divisibility must be a renormalized cohomological identity, not a raw
finite-cell algebraic accident.

## 4. New target

The correct object to test next is the normalized Abel resonance:

```text
R_x^{norm}(s;z)
 := L_x(s;x)
    - int_1^x (u/x)^z partial_uL_x(s;u)du,
```

or its finite-cell summation-by-parts analogue. This removes the exponential scale `x^z` and tests the
actual boundary-cancelled resonance from E72.31.

## 5. Status

```text
falsified: raw discrete Mellin divisibility;
open:      renormalized Abel/Mellin cohomological divisibility.
```
