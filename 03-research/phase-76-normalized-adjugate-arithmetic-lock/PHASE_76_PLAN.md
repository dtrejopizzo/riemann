# Phase 76 - Normalized Adjugate Arithmetic Lock

## Goal

Close the only live endpoint in the paper-53 chain:

```text
normalized arithmetic lock
=> CRIT-NUM-DIV
=> CCM-ROOT-LOCK
=> CAUCHY-EIG-LOC
=> HPR-DIV
=> NAT-PROJ
=> PW-Cauchy
=> scalar WRL
=> Omega7.
```

Phase 76 is autonomous: a failed mechanism triggers a theorem-grade autopsy
and immediate continuation with the next genuinely different mechanism.  A
reformulation equivalent to `TPW/scalar-WRL` does not count as progress.

## P76.001 - Correct the endpoint

Put

```text
A_L(z)
= r_z^* adj(H_L-mu_L I) r_z / tr adj(H_L-mu_L I).
```

For a simple real eigenvalue and a normalized eigenvector,

```text
A_L(z)=|C_L(z)|^2,
|P_L(z)|^2=|D_L(z)|^2 A_L(z).
```

Consequently, after reindexing the all-orders exponent,

```text
P_L(gamma)=O_M(L^-M)D_L(gamma)
<=> A_L(gamma)=O_M(L^-M).
```

The unnormalized statement recorded in P75.015-P75.016,

```text
r_gamma^* adj(H_L-mu_L I) r_gamma
= O_M(L^-M)/|D_L(gamma)|^2,
```

does not follow from the P75.003 identity and must not be used.  The valid
target is the scale-free ratio `A_L`.

Deliverables:

```text
P76_001_ENDPOINT_CORRECTION.md
P76_001_dependency_audit.py
```

## P76.002 - Numerical circularity and rank audit

Determine why the current zeta probe gives `mu_L` and `C_L(gamma)` at the
double-precision floor.  Measure, independently:

```text
rank(H_L), nullity(H_L), spectral gap, centrosymmetry defect,
eigenpair residual before and after parity symmetrization,
rank of the prime-sample contribution,
dependence on quadrature tolerance and prime cutoff.
```

Repeat in 80, 160, and 240 digit arithmetic.  A value is evidence of a true
identity only if its decay follows the analytic truncation scale rather than
the working precision or a finite-rank nullspace.

Acceptance gate:

```text
vary precision at fixed truncation;
vary truncation at fixed precision;
vary L and N independently;
remove every imported zero table from construction code.
```

The zero list is allowed only after construction, as an evaluation set.

## P76.003 - Stable observable package

Avoid direct products `D_L` and cofactor formation.  Compute `A_L` in three
independent ways:

```text
1. normalized Cauchy/eigenline pairing;
2. bordered determinant ratios in log scale;
3. reduced resolvent residue at mu_L.
```

Prove the equivalence algebraically and certify it numerically.  Extend the
formula to a multiple eigenvalue using the spectral projector/resolvent
residue, so simplicity is an explicit hypothesis rather than a silent one.

## P76.004 - Two-parameter asymptotic experiment

The relevant limit has at least two scales: support `L` and Fourier cutoff
`N`.  Build a grid of admissible paths `N=N(L)` and estimate

```text
-log A_L(gamma)/log L,
-log A_L(gamma)/L,
gap_L, derivative separation, Schur singular values.
```

Use interval or multiprecision residual bounds.  Classify the observed law as
exact zero, exponential, superpolynomial, algebraic, or precision floor.
Numerics may reject candidate statements; they may not prove Omega7.

## P76.005 - First exact mechanism: reduced-resolvent residue

Use

```text
A_L(gamma)
= Res_{lambda=mu_L}
  r_gamma^*(lambda I-H_L)^(-1)r_gamma.
```

Expand the scalar resolvent by a Schur complement relative to the Cauchy
two-plane and by exterior-power/minor identities.  Search for an exact
factorization

```text
numerator = Xi(1/2+i gamma) B_L(gamma) + R_L(gamma)
```

in which `R_L` has a formula fixed before evaluation at a zero.  Reject the
candidate immediately if `R_L` recombines to `EG_LOCK`.

## P76.006 - Second exact mechanism: deformation derivative

Introduce an arithmetic coupling parameter

```text
H_L(t)=H_arch,L-t H_prime,L
```

and derive Feynman-Hellmann/Jacobi identities for `A_L(gamma;t)`.  Test
whether the logarithmic derivative in `t`, integrated from a soluble base
point, has a signed prime expansion with an exact Xi boundary term.  The
argument is admissible only if it fails for planted and Davenport-Heilbronn
controls for a theorem-visible reason.

## P76.007 - Third exact mechanism: Mellin/contour factorization

Rewrite the Cauchy border and the finite CCM cell kernel through Laplace or
Mellin integrals.  Recombine archimedean and prime pieces before estimating.
Seek a contour identity whose only critical boundary factor is completed
zeta, while the remaining contour can be shifted repeatedly using compact
support and smoothness already present in the CCM construction.

This path is rejected if the contour shift requires a zero-free statement,
global Weil positivity, or the desired scalar WRL estimate.

## P76.008 - Cutoff-compatible all-orders remainder

If an exact factorization survives, prove

```text
R_L(gamma)=O_M(L^-M)
```

uniformly in natural resolved windows.  Track the complete dependence on
`N(L)`, cell endpoints, prime powers, and gamma.  Do not bound the
archimedean and prime sectors separately when the candidate cancellation is
signed.

## P76.009 - Auxiliary transfer theorems

Prove only the hypotheses actually needed to transport the lock:

```text
simple or controlled ground spectral projector;
polynomial Cauchy Gram bounds;
polynomial derivative separation near gamma;
polynomial lower bound for the 2x2 Schur transfer.
```

Each theorem must state its window and `N(L)` regime.  Global signed
positivity is prohibited.

## P76.010 - Falsifier matrix

Every surviving candidate must pass:

```text
zeta arithmetic data: predicted cancellation;
random ker(Q): cancellation only at imposed rows, then failure;
random symbol: failure;
planted off-line perturbation: failure near the planted height;
Davenport-Heilbronn: failure at off-line zeros;
prime-sign shuffle: failure;
archimedean-only and prime-only ablations: failure.
```

Also test neighboring nonzero ordinates.  A mechanism that cancels for all
symbols or all rows is structural and cannot prove the desired arithmetic
lock.

## P76.011 - Closure and continuation rule

Acceptance requires both:

```text
an exact finite identity independent of a zero list;
a written uniform all-orders estimate with all transfer hypotheses proved.
```

Then assemble:

```text
A_L(gamma)=O_M(L^-M)
=> CRIT-NUM-DIV
=> CCM-ROOT-LOCK
=> CAUCHY-EIG-LOC
=> HPR-DIV
=> E72.396 NAT-PROJ
=> E72.326 PW-Cauchy
=> SQB => CB => RNS => MC-NZ => NZ-MSD
=> scalar WRL
=> Omega7.
```

If a mechanism fails, record the exact failed lemma, a falsifier, and the
algebraic reason.  Continue to the next mechanism without reopening the
projection, pseudoinverse, raw divisibility, or termwise-tail routes already
closed in Phases 70-75.

## Stop condition

The research goal is complete only when the full chain to Omega7 has a
checked proof with no circular input.  A theorem-grade impossibility or
equivalence result closes a candidate route, not Omega7 and not the active
research goal.
