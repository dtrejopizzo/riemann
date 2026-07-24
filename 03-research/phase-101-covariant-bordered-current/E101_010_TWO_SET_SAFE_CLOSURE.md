# E101.010 - Two-set safe closure theorem

## 1. Finite real-rooted family

Let `F_alpha` be even real entire functions of order at most one, normalized
at a fixed safe point `i sigma_0`, with only real zeros.  Write

```text
Theta_alpha(z)=F_alpha(z)/F_alpha(i sigma_0).         (1.1)
```

The paired canonical product gives, for `|z|<=R` and `tau>R`,

```text
|Theta_alpha(z)|<=Theta_alpha(i tau).                 (1.2)
```

Every value on the right is positive.

## 2. Two independent safe sets

Assume the following two statements.

```text
IDENT-I:
  on one nonempty open interval I subset (1/2,infinity),
  Theta_alpha(i sigma)->Theta_infinity(i sigma)
  locally uniformly in sigma;                        (2.1)

BOUND-U:
  there is an unbounded set U subset (1/2,infinity)
  such that for every tau in U,
  sup_alpha Theta_alpha(i tau)<infinity.              (2.2)
```

The supremum may be replaced by an eventual supremum along the directed
family, because finitely many initial functions do not affect normality.

### Theorem 2.1

Under (2.1)--(2.2), the family `Theta_alpha` is normal on the plane.  Every
sublimit equals the analytic continuation of `Theta_infinity`, and every zero
of that continuation is real.

### Proof

Fix `R`.  Choose `tau in U` with `tau>R`.  Equations (1.2) and (2.2) bound
`Theta_alpha` uniformly on `|z|<=R`.  Since `R` is arbitrary, Montel gives
normality on the plane.

Every convergent subnet agrees with `Theta_infinity` on the interval `iI` by
(2.1).  The identity theorem makes all sublimits identical.  Hence the whole
family converges locally uniformly.  Hurwitz then forbids a nonreal zero of
the limit because every `F_alpha` has only real zeros. `QED`

## 3. Tail-ray corollary

If safe identification is proved on one entire tail

```text
sigma>sigma_1>1/2,                                  (3.1)
```

then both hypotheses hold with `I=(sigma_1,sigma_1+1)` and
`U=(sigma_1,infinity)`.  Thus safe identification on any far-right tail is
already sufficient for real-rootedness of the limiting completed function.

## 4. Application to the bordered family

Take `F_alpha` to be the normalized bilateral bordered characteristic and

```text
Theta_infinity(z)
 =[Xi(1/2+iz)/Xi(1/2+sigma_0)]^2.                    (4.1)
```

Then `IDENT-I+BOUND-U` implies `SR-SAFE`, hence `Omega7`.

The two hypotheses have different logical roles:

```text
IDENT-I  identifies the arithmetic analytic function;
BOUND-U  supplies only compactness of the real-rooted family.       (4.2)
```

Therefore a compactness theorem may remain build-neutral without carrying
the arithmetic discriminant.  The RH-strength content can be confined to
identification on one safe interval.

## 5. Status

```text
proved:
  two-set safe closure theorem;
  far-right-tail corollary;
  exact separation of identification from normality infrastructure.
```

