# E73.249 - Cauchy-Binet volume gate for maximal-minor nondegeneracy

## 1. Purpose

E73.248 selected the pivot set by maximal quotient minor:

```text
J_* in argmax_{|J|=4} |det D_Q[:,J]|.
```

This note removes most of the burden from the individual minor.  By
Cauchy-Binet, maximal-minor nondegeneracy follows from a Gram-volume lower
bound for the whole quotient packet.

## 2. Cauchy-Binet identity

Let `D_Q` have rank `r=4`.  Then:

```text
Vol_Q^2 := det(D_Q D_Q^*)
        = sum_{|J|=r} |det D_Q[:,J]|^2.
```

Therefore:

```text
max_{|J|=r} |det D_Q[:,J]|
  >= Vol_Q / sqrt(binomial(n,r)).
```

Hence `MAXMIN-NONDEG` is implied by:

```text
GRAM-NONDEG:
Vol_Q >= L^{-B_0}
```

together with a polynomial-width estimate:

```text
binomial(n,r)^{1/2} <= L^{B_1}.
```

The conclusion is:

```text
MAXMIN-NONDEG:
|det D_Q[:,J_*]| >= L^{-(B_0+B_1)}.
```

## 3. Why this matters

The pivot denominator is no longer a separate combinatorial search.  It is a
volume of the quotient packet:

```text
Vol_Q = ||delta_1 wedge delta_2 wedge delta_3 wedge delta_4||.
```

So the nondegeneracy proof should target the exterior product of the four
quotient defects directly.

This mirrors earlier wedge/Gram tools in Phase 72 and E73.171, but the object is
different: it is the DD-local quotient defect packet, not a rowspace membership
or bad-subspace projection certificate.

## 4. Remaining theorem pair

The current route is:

```text
GRAM-NONDEG
  => MAXMIN-NONDEG

MAXMIN-PIV-DIV
  => CURV-QUOT-DIV.
```

Thus the finite endpoint is now:

```text
1. prove Vol_Q >= L^{-B};
2. prove z_{J_*}=xi_{J_*}+D_Q[:,J_*]^{-1}D_Q[:,R_*]xi_{R_*}=O_M(L^-M).
```

The first is a quotient-volume estimate.  The second is the actual spectral
Mellin divisibility.

## 5. Status

```text
proved: Cauchy-Binet reduction from Gram volume to maximal-minor lower bound;
observed: max minor lies only L^{1.2--1.65} below Vol_Q in tested windows;
open: prove GRAM-NONDEG and MAXMIN-PIV-DIV analytically.
```
