# P76.031 - Safe-axis-only closure

## Product bound

Let `F` be an even real entire function of order at most one, with `F(0)=1`
and only real zeros.  Pairing the nonzero zeros gives its canonical product

```text
F(z)=prod_j (1-z^2/rho_j^2).                    (SA-1)
```

There is no nonconstant exponential factor: order at most one and evenness
leave only a constant, fixed by `F(0)=1`.  Hence for `|z|<=R`,

```text
|F(z)|
 <=prod_j (1+R^2/rho_j^2)
 =F(iR).                                        (SA-2)
```

The same argument applies to the bilateral finite characteristic
`Psi_{L,N}` of P76.030.  Its uncancelled sine zeros are real and their paired
canonical product converges.

## Safe-axis-only theorem

Let `N(L)/L -> infinity`.  Assume that for every compact interval
`J subset (1/2,infinity)`,

```text
Psi_{L,N(L)}(-i sigma)
 -> [Xi(1/2+sigma)/Xi(1/2)]^2                  (SA-SAFE)
```

uniformly for `sigma in J`.  Then Omega7 holds.

## Proof

Fix a disk `|z|<=R` and choose `sigma>max(R,1/2)`.  Evenness and `(SA-2)`
give

```text
|Psi_{L,N}(z)|<=Psi_{L,N}(i sigma)
               =Psi_{L,N}(-i sigma).
```

`SA-SAFE` bounds the right side.  Thus the family is locally bounded on the
whole plane, hence normal.  Every subsequential limit agrees with normalized
`Xi^2` on the safe imaginary ray.  The identity theorem identifies it on
the plane, and uniqueness gives convergence of the full family.  Since all
finite zeros are real, Hurwitz forbids an off-real zero of `Xi^2`.  Therefore
all nontrivial zeta zeros are critical and Omega7 follows.

## Exact remaining arithmetic theorem

The analytic normality hypothesis has disappeared.  The only remaining
statement is the Euler-safe determinant limit

```text
SA-SAFE:
[Phi_{+,L,N(L)}(-i sigma) Phi_{+,L,N(L)}(i sigma)]
 -> [Xi(1/2+sigma)/Xi(1/2)]^2,
sigma>1/2.                                      (SA-3)
```

Each factor is an explicit normalized bordered determinant ratio from
P76.013.  The target lies in `Re(s)>1`, where the Euler product converges
absolutely.  No normal-family estimate, eigenvector phase, zero list or
inverse Fourier convergence remains to be supplied.
