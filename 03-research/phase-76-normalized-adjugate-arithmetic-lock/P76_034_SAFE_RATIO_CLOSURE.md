# P76.034 - Safe-ratio closure

## Safe normalization

Fix `sigma_0>1/2` and define from the bilateral characteristic

```text
Theta_{L,N}(z)
 =Psi_{L,N}(z)/Psi_{L,N}(-i sigma_0).           (SR-1)
```

This changes no zeros.  Unlike normalization at `z=0`, both the reference
point and every comparison point `z=-i sigma`, `sigma>1/2`, correspond to
`Re(s)>1`, where the Euler product is absolutely convergent.

The unknown critical normalization cancels exactly.  In Schur variables,

```text
Theta_{L,N}(-i sigma)
= [sinh(sigma L/2)^2 |T_+(i sigma)|^2]
  /[sinh(sigma_0 L/2)^2 |T_+(i sigma_0)|^2].    (SR-2)
```

No eigenvector scale, value of `Xi(1/2)`, or fitted constant occurs.

## Closure theorem

Assume `N(L)/L -> infinity` and, locally uniformly for
`sigma in (1/2,infinity)`,

```text
Theta_{L,N(L)}(-i sigma)
 -> [Xi(1/2+sigma)/Xi(1/2+sigma_0)]^2.          (SR-SAFE)
```

Then Omega7 holds.

## Proof

Write the normalized canonical product of P76.031 as

```text
Psi(z)=prod_j(1-z^2/rho_j^2).
```

For a disk `|z|<=R`, choose `sigma>max(R,sigma_0)`.  Then

```text
|Theta(z)|
 <= Psi(iR)/Psi(i sigma_0)
 <= Psi(i sigma)/Psi(i sigma_0)
 =Theta(-i sigma).                              (SR-3)
```

`SR-SAFE` bounds the right side, hence the family is normal.  Every sublimit
agrees on the safe imaginary ray with

```text
[Xi(1/2+iz)/Xi(1/2+sigma_0)]^2.
```

The identity theorem gives that limit globally.  Hurwitz and finite
real-rootedness exclude every off-real zero of `Xi`; hence Omega7.

## Final arithmetic endpoint

`SR-SAFE` is strictly cleaner than `SA-SAFE`:

```text
old: identify an amplitude normalized at the critical center;
new: identify a ratio of two finite Schur moduli entirely in Re(s)>1.
```

The remaining proof must insert the finite Gamma-prime formula into `(SR-2)`
and show that its logarithm converges to

```text
2 log Xi(1/2+sigma)-2 log Xi(1/2+sigma_0),
```

using absolute prime-power convergence and a uniform finite-section error.
This is the current non-circular arithmetic identity.
