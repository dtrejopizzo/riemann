# Maximal closure attempt for omega7

**Purpose.** This note records the strongest proof package that survives audit after
`CANDIDATE-PROOF-omega7.md`. It closes every statement that can be closed from standard
Hermite-Biehler / Krein-Langer / Schur-complement facts, and isolates the exact remaining field.

## 1. Closed lemma: HB is closed under local-uniform structural convergence

Let `E_n` be entire Hermite-Biehler functions and suppose

1. `E_n -> E` locally uniformly on `C`,
2. `E` is not identically zero,
3. the limit is nondegenerate, i.e. `E# / E` is not a unimodular constant in `C+`.

Then `E` is Hermite-Biehler.

**Proof.** Since each `E_n` is HB, it has no zeros in `C+`, and
`Theta_n := E_n# / E_n` is Schur in `C+`. By Hurwitz, `E` has no zeros in `C+`.
For each fixed `z in C+`,

`|E_n#(z)| <= |E_n(z)|`.

Passing to the locally uniform limit gives

`|E#(z)| <= |E(z)|`.

Therefore `Theta := E# / E` is analytic and Schur in `C+`. If equality occurs at one
interior point, the maximum modulus principle forces `Theta` to be a unimodular constant,
contrary to nondegeneracy. Hence `|E#(z)| < |E(z)|` for all `z in C+`, so `E` is HB. `□`

**Consequence.** The terminal line `(star)` would be proved immediately if the canonical
finite structure functions `E_P` converged to the genuine endpoint structure function `E_xi`
locally uniformly as entire functions, with no degenerate constant-Schur collapse.

**Audit warning.** Scalar determinant convergence is not this hypothesis. `D_P -> Xi` is
index-blind and does not identify the Krein-Langer kernel or the structural function.

## 2. Closed lemma: positive pole shorting preserves index zero

Let

`K_P = [[a_P, b_P*], [b_P, C_P]]`

be a finite Gram matrix with `K_P >= 0` and `a_P > 0`, where the first coordinate is the
positive pole line. Define the Schur-shorted primitive matrix

`K_P^o = C_P - b_P a_P^{-1} b_P*`.

Then `K_P^o >= 0`. If `K_P^o -> K^o` entrywise on every finite configuration, then
`K^o >= 0`, hence the limiting primitive kernel has Krein-Langer index zero.

**Proof.** Haynsworth inertia additivity gives the congruence

`K_P ~ diag(a_P, K_P^o)`.

Since `K_P >= 0` and `a_P > 0`, the Schur complement `K_P^o` is positive. Entrywise
finite-Gram limits of positive matrices are positive, because the cone of positive
semidefinite matrices is closed. Taking the supremum over finite configurations gives
index zero for the limit kernel. `□`

**Consequence.** If the endpoint kernel obtained after pole shorting is the genuine
Krein-Langer kernel of `Xi`, then RH follows.

So the exact sufficient theorem is:

> `K_P^o -> K_Xi` in finite-Gram topology after positive pole shorting.

This closes `(star)`. It is stronger and more precise than scalar determinant convergence.

## 3. Closed lemma: leading trace rank-one does not imply primitive boundedness

Suppose `a_P -> infinity`, `b_P -> infinity`, and `b_P = o(a_P)`. On
`C e_0 oplus V`, set

`K_P = a_P |e_0><e_0| + b_P Q_V`,

where `Q_V` is any positive projection of rank `r`.

Then

`Tr K_P = a_P + r b_P ~ a_P`,

so the leading trace divergence is rank-one along `e_0`. But

`||P_prim K_P P_prim|| = b_P -> infinity`.

Thus leading trace rank-one does not imply rank-one escape in operator norm; arbitrarily many
subleading primitive escape directions may be invisible to the trace asymptotic.

**Consequence.** The statement

`Tr K_P ~ (1/2)(log P)^2 carried by H`

is not enough to prove either primitive compactness or `kappa <= 1`. What is needed is the
stronger estimate

`sup_P ||P_prim K_P P_prim|| < infinity`

or an equivalent finite-Gram convergence theorem for the shorted primitive kernels.

## 4. Closed subcritical rank-one isolation

On a strict source core where every primitive source profile has decay exponent
`a_phi > 1/2`, the non-pole prime cells are absolutely summable:

`sum_{p,k} (log p) p^{-k/2} |hat(phi)(k log p)|^2
 <= C_phi sum_{p,k} (log p) p^{-k(1/2+2a_phi)} < infinity`.

The pole/degree cell contributes the positive rank-one term

`a_P |H><H|`, with `a_P ~ (1/2)(log P)^2`.

Hence on this strict core the only divergent direction is the pole line.

**Boundary obstruction.** Omega7 lives at the critical endpoint. Passing from the strict core
to the critical primitive completion requires a uniform bound independent of the source
decay margin. That uniform endpoint bound is exactly the rank-one escape theorem:

`sup_P ||P_prim K_P P_prim|| < infinity`.

So the rank-one isolation is closed on the subcritical core, but not at the critical endpoint.

## 5. Strongest valid closure theorem

The following theorem is the maximal honest proof statement.

**Theorem.** Assume:

1. finite von Mangoldt canonical systems give positive kernels `K_P >= 0`;
2. the pole line is positive rank-one and is Schur-shorted as above;
3. the shorted primitive kernels `K_P^o` converge in finite-Gram topology;
4. the finite-Gram limit is the genuine Krein-Langer kernel attached to `Xi`.

Then `kappa(Xi)=0`, hence RH.

**Proof.** By (1)-(2), each `K_P^o` is positive. By (3), the limit kernel is positive.
By (4), this positive limit is not an impostor endpoint but the actual `Xi` kernel.
Therefore the Krein-Langer negative index of `Xi` is zero. By the standard
Krein-Langer/Nevanlinna dictionary, the negative index equals the number of off-line zero
pairs. Hence there are no off-line zeros. `□`

## 6. What remains open

The remaining field is not "HB closedness" and not "rank-one perturbations change index by
at most one". Those are closed in the right topology.

The remaining field is the endpoint identification/convergence:

`K_P^o -> K_Xi`

at the critical primitive boundary, with enough control to rule out non-uniform emergence of
off-line principal parts.

Equivalently:

`sup_P ||P_prim K_P P_prim|| < infinity`.

Equivalently:

no primitive leakage beyond the positive pole line.

This is the exact omega7/RH-strength input.

## 7. Corrected status

What is proved here:

- HB passes to the limit under local-uniform structural convergence.
- Positive pole shorting preserves index zero under finite-Gram kernel convergence.
- Leading trace rank-one is insufficient for primitive boundedness.
- Rank-one isolation is valid on strict subcritical source cores.
- The full endpoint theorem follows from primitive shorted-kernel convergence to the genuine `Xi` kernel.

What is not proved:

- scalar determinant convergence implies structural/kernal convergence;
- leading trace rank-one implies operator-norm rank-one escape;
- `kappa(Xi) <= 1`;
- omega7/RH.

