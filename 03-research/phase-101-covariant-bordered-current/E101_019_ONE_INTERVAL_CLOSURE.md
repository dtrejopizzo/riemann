# E101.019 - One-interval closure theorem

## 1. Local safe identification

Let `Theta_alpha` be normalized core bilateral finite characteristics with
only real zeros.  Let `I` be any nonempty open interval in the safe axis.
Assume

```text
ONE-INTERVAL-IDENT:
Theta_alpha(i sigma)
 ->[Xi(1/2+sigma)/Xi(1/2+sigma_0)]^2                 (1.1)
```

locally uniformly for `sigma in I`, where `sigma_0 in I` is the normalization
point.  Reflection of `Xi` makes the same formula valid with `i sigma` or
`-i sigma` in the centered variable.

### Theorem 1.1

`ONE-INTERVAL-IDENT` implies `Omega7`.

### Proof

Choose `tau in I` with `tau>sigma_0`.  Convergence in (1.1) bounds
`Theta_alpha(i tau)`.  E101.018 then bounds the Stieltjes mass at `sigma_0`,
and E101.012 makes the family locally bounded on the whole plane.

Every subnet has a locally uniform sublimit.  Equation (1.1) identifies that
limit with the normalized square of `Xi` on the open segment `iI`.  The
identity theorem identifies it globally.  Hurwitz excludes nonreal zeros of
the limit because all finite zeros are real.  Hence all zeros of `Xi` are
real in the centered coordinate, which is `Omega7`. `QED`

## 2. Covariant determinant corollary

By E101.011(1.2),

```text
LOCAL-COVARIANT-IDENT:
DEF_alpha(s;s_*)->0                                  (2.1)
```

on one nonempty open real interval `I subset (1,infinity)` is exactly
`ONE-INTERVAL-IDENT` after multiplication by the independent Euler--Gamma
ratio.  Therefore

```text
LOCAL-COVARIANT-IDENT
 =>Omega7.                                           (2.2)
```

No separate normality, Stieltjes-mass, GAP-Z, limit-point, external-mesh tail
or cofinal bound hypothesis is needed.

## 3. Converse force

Under `Omega7`, the target has only real centered zeros and the direct
identification is the expected finite-section convergence problem.  For the
forward proof program, the important logical statement is (2.2): local
covariant identification already has full RH strength.

Thus the unique force-bearing theorem of the direct route is

```text
LOCAL-COVARIANT-IDENT on one safe interval.          (3.1)
```

All compactness infrastructure can be recovered from two values of the same
identification theorem.

## 4. Status

```text
proved:
  one-interval real-rooted closure theorem;
  automatic compactness from local safe identification;
  LOCAL-COVARIANT-IDENT implies Omega7;

open:
  LOCAL-COVARIANT-IDENT itself;
  Omega7.
```
