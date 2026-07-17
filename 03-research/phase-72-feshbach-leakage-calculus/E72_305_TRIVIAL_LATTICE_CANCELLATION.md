# E72.305 -- Exact cancellation of the trivial lattice

**Purpose.** Finish the explicit-formula bookkeeping left open in E72.304. The shifted trivial-zero
lattice is not an extra term to estimate: it cancels the archimedean residual exactly.

## 1. Explicit formula normalization

For `x=e^y>1`, use the standard Chebyshev formula

```text
psi(x)-x
= - sum_rho x^rho/rho
   - log(2pi)
   - (1/2)log(1-x^(-2)),
```

with the nontrivial-zero sum understood in the usual symmetric limiting sense.

Set

```text
A_tau(y)=e^(-y/2)F_tau(y).
```

From E72.299,

```text
A_tau(0)=A_tau(L)=0.
```

E72.301 writes

```text
FORM_actual(tau)=ARCH_tau - (1/2)PNTERR_tau,
PNTERR_tau=int_0^L (psi(e^y)-e^y) A_tau'(y)dy.
```

## 2. Constant term vanishes

The constant term contributes

```text
-log(2pi) int_0^L A_tau'(y)dy
= -log(2pi)(A_tau(L)-A_tau(0))
= 0.
```

Thus the pole/constant bookkeeping does not contribute to the FORM channel.

## 3. Trivial-zero term equals `2 ARCH`

Let

```text
T(y)=-(1/2)log(1-e^(-2y)).
```

Then

```text
T'(y)= -1/(e^(2y)-1).
```

Since `A_tau(0)=A_tau(L)=0` and `A_tau(y)=O(y)` at the origin, the boundary term in integration by
parts vanishes:

```text
int_0^L T(y)A_tau'(y)dy
= -int_0^L T'(y)A_tau(y)dy
= int_0^L A_tau(y)/(e^(2y)-1)dy.
```

Substituting `A_tau=e^(-y/2)F_tau`,

```text
int_0^L T(y)A_tau'(y)dy
= int_0^L e^(-5y/2)/(1-e^(-2y))F_tau(y)dy
= 2 ARCH_tau.
```

This is exactly the archimedean residual of E72.301.

## 4. Nontrivial-zero term

For each nontrivial zero `rho`,

```text
-rho^(-1) int_0^L e^(rho y)A_tau'(y)dy
= int_0^L e^((rho-1/2)y)F_tau(y)dy
= M_tau(rho-1/2),
```

again because `A_tau(0)=A_tau(L)=0`.

Thus

```text
PNTERR_tau
= sum_rho M_tau(rho-1/2) + 2ARCH_tau,
```

up to the standard symmetric limiting convention for the nontrivial zeros.

## 5. Final compact FORM identity

Substitute into

```text
FORM_actual(tau)=ARCH_tau - (1/2)PNTERR_tau.
```

The archimedean/trivial lattice cancels exactly:

```text
FORM_actual(tau)
= -1/2 sum_rho M_tau(rho-1/2).                       (1)
```

No separate trivial-zero, constant, or pole term remains in the compact FORM channel.

## 6. Closed finite transform

The transform is still the E72.302 divided-difference expression:

```text
M_tau(z)
= (1-e^(zL))
   sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [Phi_z(d_m)-Phi_z(d_n)]/[pi(n-m)],
Phi_z(d)=d/(z^2+d^2).
```

Therefore the entire compact-root arithmetic content is:

```text
NZ-MSD-FORM:
sup_{tau_j<=H} |sum_rho M_tau_j(rho-1/2)| <= C_H L^4.
```

## 7. Reading

E72.304 correctly identified the arch residual as the shifted trivial-zero lattice. E72.305 proves the
stronger fact: in the actual FORM channel, that lattice cancels exactly against the explicit
trivial-zero term in `psi(x)-x`.

The remaining Mellin spectral divisibility target is now only the nontrivial-zero divisor of the finite
transform `M_tau`.

E72.306 refines this target by factoring

```text
M_tau(z)=(1-e^(zL))N_tau(z).
```

The apparent mesh poles of `N_tau` are removable in `M_tau`; hence there is no finite mesh-residue
shortcut. The compact target is the normalized nontrivial-zero sum.
