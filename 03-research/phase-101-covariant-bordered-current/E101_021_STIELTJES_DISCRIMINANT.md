# E101.021 - Stieltjes discriminant

## 1. Positive representation theorem

Consider the arithmetic function `g_Xi` of E101.020(2.4), initially on any
open interval `x>1/4`.

### Theorem 1.1

The following two statements are equivalent:

```text
1. Omega7 holds;
2. g_Xi belongs to the positive Stieltjes class on [0,infinity).
                                                                    (1.1)
```

Here the Stieltjes class permits the standard form

```text
g(x)=b+integral_[0,infinity)d mu(t)/(x+t),
b>=0,
mu>=0.                                              (1.2)
```

For `g_Xi`, the known real-axis asymptotic `g_Xi(x)->0` forces `b=0`.

Moreover, if `g_Xi` is a locally uniform limit of the finite transforms
`g_alpha` on one nonempty safe interval for a resolved bordered family, then
statement 2 and hence statement 1 hold.  The converse finite-section
convergence is not asserted; it is exactly the open identification theorem.

## 2. Proof that Omega7 gives a Stieltjes measure

Under `Omega7`, the centered zeros are real: `rho=1/2+i gamma`.  The even
canonical product gives

```text
Xi(1/2+sigma)^2/Xi(1/2)^2
 =product_(gamma>0)(1+sigma^2/gamma^2)^2.            (2.1)
```

Therefore

```text
g_Xi(x)=2 sum_(gamma>0)1/(x+gamma^2),                (2.2)
```

which is the Stieltjes transform of

```text
mu_Xi=2 sum_(gamma>0)delta_(gamma^2).                (2.3)
```

The series converges locally because `sum gamma^(-2)<infinity`.

## 3. Proof that a Stieltjes measure forces Omega7

Suppose

```text
g_Xi(x)=b+integral_[0,infinity)d mu(t)/(x+t)         (3.1)
```

on a nonempty positive interval.  The right side is analytic on the slit
plane `C minus (-infinity,0]`.  By the identity theorem it is the meromorphic
continuation of the left side wherever both are defined.

A zero `rho` of `Xi` produces a pole of its logarithmic derivative at

```text
x=(rho-1/2)^2.                                       (3.2)
```

No such pole can lie off the negative real axis because (3.1) is analytic
there.  Hence every square in (3.2) is nonpositive real.  This forces
`rho-1/2` to be purely imaginary.  Thus every nontrivial zero lies on the
critical line, which is `Omega7`. `QED`

Finally, Stirling's formula and the absolutely convergent prime series give

```text
g_Xi(x)=O(log x/sqrt(x))                              (3.3)
```

on the positive axis.  Hence the constant `b` in (3.1) is zero.

## 4. Identification of the force-bearing step

The finite core determinant construction supplies positive measures `mu_alpha`
unconditionally.  The independent arithmetic formula supplies `g_Xi`
unconditionally on `x>1/4`.  The sole missing assertion is

```text
STIELTJES-IDENT:
integral d mu_alpha(t)/(x+t)
 ->g_Xi(x)                                           (4.1)
```

on one open interval.

By E101.019 and Theorem 1.1, (4.1) has full RH strength.  It is the precise
form of the arithmetic discriminant.  Compactness, GAP-Z and spectral-gap
control are not separate premises.

## 5. Status

```text
proved:
  Omega7 equivalence with the positive Stieltjes representation of g_Xi;
  STIELTJES-IDENT implies Omega7;
  exact localization of the force-bearing theorem;

open:
  STIELTJES-IDENT, equivalently LOCAL-COVARIANT-IDENT and Omega7.
```
