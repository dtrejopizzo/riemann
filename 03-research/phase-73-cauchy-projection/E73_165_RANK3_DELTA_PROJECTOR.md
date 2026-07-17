# E73.165 - Rank-3 delta projector

Date: 2026-07-12.

## 1. Purpose

E73.164 defines the canonical cauchy0 defect:

```text
delta_A(gamma)
= [s_A-B_L(A,K)y_A]_{cauchy0_gamma}.
```

This note asks whether the map

```text
Pi_A(gamma) -> delta_A(gamma)
```

has structure.  If the map is essentially arbitrary, then E73.164 is only
bookkeeping.  If the map is a finite projector, then the endpoint is reduced
to a smaller explicit obstruction.

## 2. Transfer operator

Fix the diagnostic critical window:

```text
K_L={i gamma_1,...,i gamma_5}.
```

Let `e_j` denote the source whose only canonical cauchy0 coefficient is one
at `gamma_j`.  For each `e_j`, perform the E73.163 elimination:

```text
y_j = argmin_y ||e_j^principal-B_L(A,K)^principal y||,
delta_j = [e_j-B_L(A,K)y_j]_{cauchy0}.
```

Define the transfer matrix

```text
T_L e_j := delta_j.
```

Then for a general source coefficient vector `Pi_A`,

```text
delta_A = T_L Pi_A.
```

This is finite, canonical, and independent of the eigenvector pairing.

## 3. Numerical result

The singular values of `T_L` are:

```text
1, 1, 1, about 1e-5, about 1e-9.
```

Moreover:

```text
||T_L^2-T_L||/||T_L||    = 1e-5 to 1e-3,
||T_L-T_L^*||/||T_L||    = 1e-7 to 1e-5,
||T_L||_F               = 1.73 ~= sqrt(3),
||T_L-I||_F/||I||_F     = 0.632 ~= sqrt(2/5),
||T_L||_F/sqrt(5)       = 0.775 ~= sqrt(3/5).
```

Thus the canonical transfer is numerically an orthogonal projector of rank
three on the five-dimensional critical cauchy0 coefficient space.

## 4. Meaning

The coefficient elimination does not make the defect small, but it removes
two cauchy0 directions exactly up to numerical precision.  The surviving
obstruction is:

```text
delta_A = P_{bad,L} Pi_A,
```

where `P_{bad,L}` is a rank-three orthogonal projector determined by the
finite rational action of `(H_L-mu_L I)`.

This is better than E73.164: the remaining theorem is no longer all of
`Pi_A`; it is the component of `Pi_A` in the rank-three quotient:

```text
CANON-PROJ-CRIT-DIV:
e^(alpha L)
|sum_gamma (P_{bad,L}Pi_A)(gamma)
  (1-e^(i gamma L))sum_n xi_L(n)/(-gamma-d_n)|
<= L^B.
```

## 5. Proof of reduction

For any source coefficient vector `Pi_A`, the canonical source is:

```text
S_A(d)=sum_gamma Pi_A(gamma)DD_L(-gamma,d).
```

By definition of `T_L`, after eliminating all generated rational and endpoint
slots:

```text
S_A = (H_L-mu_L I)Y_A
    + sum_gamma (T_L Pi_A)(gamma)DD_L(-gamma,d)
    + endpoint residual.
```

Pairing with the eigenvector kills the image term:

```text
<xi_L,(H_L-mu_L I)Y_A>=0.
```

Therefore the scalar obstruction is:

```text
<xi_L,S_A>
= sum_gamma (T_L Pi_A)(gamma)<xi_L,DD_L(-gamma,d)>
  + endpoint scalar.
```

The Phase 72 endpoint scalars are already assigned to the tail/residual
classes.  Hence the new finite gate is exactly `CANON-PROJ-CRIT-DIV`.

## 6. What remains

The next theorem should not try to prove `delta_A` small in norm.  It is not
small enough.  It should prove one of:

```text
1. P_{bad,L}Pi_A is small for natural-height off-line clusters; or
2. the critical cancelled Cauchy vector is small on Range(P_{bad,L}); or
3. a mixed identity between P_{bad,L}Pi_A and the cancelled Cauchy vector.
```

This is a genuine sharpening of the final finite identity:

```text
CRIT-DIV on 5 critical atoms
```

has become

```text
CRIT-DIV on a canonical 3-dimensional quotient.
```

## 7. Status

```text
proved numerically: T_L is an almost orthogonal rank-three projector;
proved algebraically: if T_L is defined by the coefficient elimination,
                    CANON-PROJ-CRIT-DIV implies NAT-SRC;
open: symbolic derivation of T_L as an exact projector and proof of the
      scalar bound on its range.
```

