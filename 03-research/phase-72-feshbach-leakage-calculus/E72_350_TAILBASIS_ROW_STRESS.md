# E72.350 -- TailBasis row stress

**Purpose.** Test the first concrete addition to the CFIR interpolation row: the finite collapsed
`TailBasis` from E72.343.  This is a numerical stress of a partial `R_T`, not the full certificate.

## 1. Added finite tail row

The probe implements the closed formula

```text
TailBasis_{z,n}^M(a)=P_{z,n}^infty(a)-P_{z,n}^M(a),
```

where

```text
P_{z,n}^infty(a)
= i/(z+i d_n) [
   e^(zL)( E_L(a-z)+E_L(-a-z) )
 - ( E_L(a+i d_n)+E_L(-a+i d_n) )
 + e^(zL)( E_L(a-i d_n)+E_L(-a-i d_n) )
 - ( E_L(a+z)+E_L(-a+z) )
],
```

and

```text
P_{z,n}^M(a)=sum_{|m|<=M} a_m(z) PairCell_{m,n}(a).
```

For the diagonal cell, the removable limit used is

```text
PairCell_{n,n}(a)
= [2-e^(aL)-e^(-aL)] * [-(2/L) Phi_a'(d_n)],

Phi_a(d)=d/(a^2+d^2).
```

This avoids numerical quadrature.

## 2. Tested rows

The rows tested are:

```text
base:
  mu k_a.

self:
  (mu-K_L(a,a))k_a.

window:
  mu k_a - sum_w K_L(a,w)k_w.

tail:
  sum_w TailBasis_{a,.}^M(w).

window_tail:
  window + tail.

window_minus_tail:
  window - tail.

fitLam:
  lambda k_a - sum_w K_L(a,w)k_w + tail,
  with one scalar lambda fitted over the finite window to minimize the null defect.
```

Rows are tested against the singular finite operator

```text
E=H_actual-lambda_0 I,
```

using

```text
relNull=|row xi|/||row||.
```

## 3. Analytic lesson

At root nodes, the Cauchy root relation makes `base`, `self`, and `window` nearly invisible to `xi`.
At shifted nodes, these partial rows have large relative null defects.  The `tail` row alone has a much
smaller shifted defect, but adding or subtracting it from the incomplete `window` row does not close
the gap.

Therefore the missing part is not merely the finite Fourier tail.  The complete coupled

```text
T_W02 - T_WR - T_Prime - 2kappa_*G
```

assembly remains load-bearing in the derivation of the exact residual row, but E72.352
shows it cannot be used as an additive repair after the row has been tested.  Any row
of the form `A(C_E-mu I)` is already in the rowspace and has zero action on `xi`.

The fitted-scalar row reduces the shifted defect but does not close it, so the remaining obstruction
is not only the value of `Lambda_L`.

## 4. Status

```text
implemented: finite TailBasis without infinite tails or quadrature;
observed: TailBasis alone is close to row-ideal membership in shifted controls;
observed: window +/- TailBasis is still not enough;
corrected: additive finite operator rows leave the CFIR defect invariant;
next: derive the exact residual row R_T before rowspace testing.
```
