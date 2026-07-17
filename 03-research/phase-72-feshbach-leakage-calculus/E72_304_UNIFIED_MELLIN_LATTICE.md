# E72.304 -- Unified Mellin lattice for ARCH-FORM and PNTERR-FORM

**Purpose.** Put the archimedean residual of E72.301 and the spectral error of E72.302 on the same
finite Mellin transform `M_tau`. This turns `ARCH-FORM + MSD-FORM` into one divisor sum.

## 1. Archimedean residual as Mellin lattice

E72.301 gives

```text
ARCH_tau = 1/2 int_0^L e^(-5y/2)/(1-e^(-2y)) F_tau(y)dy.
```

For `y>0`,

```text
e^(-5y/2)/(1-e^(-2y))
= sum_{k>=0} e^(-(5/2+2k)y).
```

Since `F_tau(0)=0`, the singularity at zero is removable in the integral sense. Thus

```text
ARCH_tau
= 1/2 sum_{k>=0} int_0^L e^(-(5/2+2k)y)F_tau(y)dy
= 1/2 sum_{k>=0} M_tau(-(5/2+2k)).                  (1)
```

The same closed formula from E72.302 applies:

```text
M_tau(z)
= (1-e^(zL))
   sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [Phi_z(d_m)-Phi_z(d_n)]/[pi(n-m)],
Phi_z(d)=d/(z^2+d^2).
```

## 2. Relation with trivial zeros

The trivial zeros of zeta are

```text
rho=-2,-4,-6,...
```

After the spectral shift `z=rho-1/2`, they sit at

```text
z= -5/2, -9/2, -13/2, ...
```

which is exactly the archimedean lattice in (1):

```text
-(5/2+2k),        k>=0.
```

Therefore `ARCH_tau` is not an unrelated model residue. It is the shifted trivial-zero lattice of the
same Mellin transform `M_tau`.

## 3. Unified FORM identity

E72.301 says

```text
FORM_actual(tau)=ARCH_tau - 1/2 PNTERR_tau.
```

E72.302 writes

```text
PNTERR_tau
= sum_{rho_nontriv} M_tau(rho-1/2)
   + trivial/polar/tail terms.
```

Combining this with (1), the compact-root form can be written schematically as

```text
FORM_actual(tau)
= -1/2 sum_{rho_nontriv} M_tau(rho-1/2)
   +1/2 sum_{k>=0} M_tau(-(5/2+2k))
   -1/2(trivial/polar/tail bookkeeping).              (2)
```

With the standard explicit-formula normalization, the explicit trivial-zero contribution should pair
with the arch lattice above. The remaining bookkeeping task is to align signs and polar terms exactly.

## 4. Finite tail of the arch lattice

For `a_k=5/2+2k`,

```text
M_tau(-a_k)
= (1-e^(-a_k L))
   sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [Phi_{-a_k}(d_m)-Phi_{-a_k}(d_n)]/[pi(n-m)].
```

Since

```text
Phi_{-a}(d)=d/(a^2+d^2),
```

the divided difference is `O(a^(-2))` uniformly in fixed mesh frequency and improves as `a^(-3)` away
from the origin. Thus the arch lattice has an explicit absolutely convergent tail:

```text
sum_{k>K} M_tau(-(5/2+2k))
```

is bounded by the same finite coefficient norm times `sum_{k>K} a_k^(-2)`. This makes the arch part
finite-checkable after truncation.

## 5. Updated divisibility target

The compact-root Mellin spectral target should now be stated as the unified divisor identity:

```text
UMSD-FORM:
the shifted nontrivial-zero sum, shifted trivial-zero lattice, polar terms, and explicit tail in (2)
combine to O_H(L^4) for the finite transform M_tau.
```

This is sharper than treating `ARCH-FORM` and `MSD-FORM` as independent estimates. It is the same
finite transform evaluated on the full shifted explicit-formula divisor.

## 6. Current proof direction

The next exact bookkeeping step is:

```text
derive the fully normalized explicit-formula version of (2),
including signs, polar terms at 0/1, and height truncation,
as a finite identity for M_tau.
```

That identity is the closest current form of the scalar WRL divisibility obstruction.

E72.305 completes this bookkeeping: the shifted trivial-zero lattice cancels `ARCH_tau` exactly in
`FORM_actual`. The remaining target is the nontrivial-zero sum

```text
FORM_actual(tau)=-(1/2)sum_rho M_tau(rho-1/2).
```
