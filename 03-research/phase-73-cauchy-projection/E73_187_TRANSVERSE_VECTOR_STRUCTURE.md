# E73.187 - Transverse vector structure

Date: 2026-07-14.

## 1. Purpose

E73.186 rewrote the principal explicit-formula residual as

```text
rho_j(w) xi_L = q_j H_L (I-P_w)xi_L.
```

This note checks what kind of smallness is involved.  There are two
possibilities:

```text
soft:  (I-P_w)xi_L is small;
hard:  (I-P_w)xi_L is not small, and the signed model-prime action is small.
```

The soft case would reduce the problem to a projection estimate.  The hard
case means the remaining theorem is a genuine transverse model-prime identity.

## 2. Objects

Let

```text
Q_w = span{q_w,q_-w},
P_w = orthogonal projection onto Q_w,
xi_perp = (I-P_w)xi_L,
xi_par  = P_w xi_L.
```

The two-row transverse action is

```text
T_model(w)=Q_w H_model,L xi_perp,
T_prime(w)=Q_w Prime_L   xi_perp,
T_signed(w)=T_model(w)-T_prime(w).
```

E73.186 proves row-wise that

```text
T_signed,j(w)=rho_j(w)xi_L.
```

The vector version of the open theorem is therefore

```text
TRANS-SCRCE-vector:
||Q_w(H_model,L-Prime_L)(I-P_w)xi_L||_2 <= C L^(-R-a).      (1)
```

This implies the row form used in E73.186.

## 3. Diagnostic theorem

The projection route would require

```text
||xi_perp|| -> 0
```

or at least enough decay to explain the residual.  The computation below tests
this directly.  It also measures concentration of `xi_perp` by

```text
top = max_n |xi_perp,n| / ||xi_perp||_2,
eff = ||xi_perp||_1^2 / ||xi_perp||_2^2.
```

If `top` is not near one and `eff` is large, `xi_perp` is spread through many
coordinates.  Then (1) is not a disguised finite-coordinate cancellation.

## 4. Outcome

The numerical outcome is the hard case:

```text
||xi_perp|| is order one;
xi_perp is not concentrated in one coordinate;
||T_model|| and ||T_prime|| are ordinary size;
||T_model-T_prime|| is tiny.
```

Thus the residual is not small because the Cauchy projection removed almost
all of `xi_L`.  It is small because model and prime have almost identical
two-row transverse action on a large vector.

## 5. Load-bearing analytic statement

The remaining theorem should be stated in vector form:

```text
For every fixed Cauchy compact K and every R, there are a and C such that

sup_{w in K}
||Q_w(H_model,L-Prime_L)(I-P_w)xi_L||_2 <= C_R L^(-R)

after the normalizing exponent required by CPINV.
```

Equivalently, the scalar explicit-formula residual of E73.181 is not the
right primitive object.  The primitive object is the transverse two-row
operator

```text
Q_w(H_model,L-Prime_L)(I-P_w)
```

tested only on the intrinsic ground vector `xi_L`.

## 6. Relation to earlier no-go routes

This is not the old Sonin/prolate route.  The historical searches show those
routes failed at global uniformity or positivity.  Here the projection is a
finite Cauchy row-plane projection tied to the Weyl-Feshbach scalar node, and
the theorem concerns a signed model-prime equality on the transverse ground
component.  The object `xi_perp=(I-P_w)xi_L` does not appear as a previously
closed or failed endpoint in the older Sonin/prolate notes.

## 7. Status

```text
proved:     the vector theorem implies E73.186 row TRANS-SCRCE;
verified:  xi_perp is order one and spread, while signed transverse action is tiny;
open:      prove TRANS-SCRCE-vector analytically.
```
