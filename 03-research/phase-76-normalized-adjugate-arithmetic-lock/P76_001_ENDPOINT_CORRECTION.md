# P76.001 - Endpoint correction and dependency audit

## Exact normalized identity

Let `H` be real symmetric, let `mu` be a simple eigenvalue, and let `xi` be
a normalized real eigenvector.  Put `K=H-mu I`.  The spectral decomposition
gives

```text
adj(K)=k_mu xi xi^T,
k_mu=prod_{nu != mu}(nu-mu)=tr adj(K).
```

The sign of `k_mu` is irrelevant in the ratio.  For
`r_z(n)=1/(z-d_n)` and `C(z)=r_z^T xi`,

```text
A(z):=r_z^* adj(K) r_z / tr adj(K)=|C(z)|^2.
```

Since `P(z)=D(z)C(z)`, the exact scale-free identity is

```text
|P(z)|^2/|D(z)|^2=A(z).
```

Hence the all-orders statements are equivalent (replace `M` by `2M` in
one direction):

```text
P_L(gamma)=O_M(L^-M)D_L(gamma)
<=> C_L(gamma)=O_M(L^-M)
<=> A_L(gamma)=O_M(L^-M).
```

The Phase-75 endpoint

```text
r_gamma^* adj(K_L) r_gamma=O_M(L^-M)/|D_L(gamma)|^2
```

is not implied by P75.003.  It incorrectly drops `tr adj(K_L)` and inserts
an inverse `D_L` scale after that scale has already cancelled.  It is
withdrawn.  No later argument may use it.

## Resolvent form

For the positively oriented spectral parameter,

```text
Res_{lambda=mu} (lambda I-H)^(-1)=xi xi^T,
A(z)=Res_{lambda=mu} r_z^*(lambda I-H)^(-1)r_z.
```

Equivalently,

```text
Res_{lambda=mu} (H-lambda I)^(-1)=-xi xi^T.
```

This sign convention is fixed for P76.005.

## Multiplicity-safe form

If `mu` has multiplicity `m`, `adj(H-mu I)=0` when `m>1`; the adjugate
ratio is undefined.  The canonical replacement is the spectral projector

```text
Pi_mu=Res_{lambda=mu}(lambda I-H)^(-1),
A_mu(z)=r_z^* Pi_mu r_z=||Pi_mu r_z||^2.
```

For `m=1` this is exactly `A(z)`.  Thus simplicity must either be proved or
the closure statement must be formulated for `Pi_mu`.

## Logical dependencies

The construction of `H_L` in `E71_2_convergence_detector.py` and
`E71_9_relative_arch_background_probe.py` uses cell integrals, the
archimedean kernel, and prime powers up to the finite arithmetic cutoff.  It
does not use the imported `GAMMAS` table.  Phase-75 uses `GAMMAS` only as an
evaluation set for Cauchy rows and root matching.

This excludes direct insertion of the tested zeros, but it does not yet
exclude an algebraic nullspace or a precision-floor explanation.  The
P76.001 rank audit measures those alternatives.

## Acceptance target after correction

The unique live theorem is now

```text
NORMALIZED-ARITH-LOCK:
for every M, uniformly in resolved natural windows,
r_gamma^* Pi_{mu_L} r_gamma=O_M(L^-M).
```

For a simple ground state this is `A_L(gamma)=O_M(L^-M)`.  This target is
phase-free and product-free.  It is still not proved; proving it remains the
arithmetic content required for Omega7.
