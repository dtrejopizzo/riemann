# Phase 119 — coefficient separator, corrected audit

Date: 2026-08-25. Scripts are in `scripts/`. The corresponding discussion is
in paper 42, §“What the contact block does and does not separate”.

## 1. Three independent coefficient properties

For the coefficients `Lambda_f` of `-f'/f`, paper 42 singles out:

| property | statement | status for zeta |
|---|---|---|
| **P0** | `Lambda_f(n) >= 0` | proved by the positive torsion-contact degree |
| **P1** | support on prime powers | proved by the cyclotomic contact calculation |
| **P2_norm** | `[Lambda_f(mn)]_{m,n in S} >= 0` for every finite `S` | coefficient shadow of the rank-one blocks, because `p^j` uniquely determines `(p,j)` for `Spec Z` |

These properties are not a logical hierarchy: none of the three implications
needed to call them “nested” holds in general.

## 2. Davenport–Heilbronn

With `kappa` the defining Davenport–Heilbronn parameter, direct Dirichlet
inversion gives

    Lambda_DH(3) = -kappa log 3 < 0,
    Lambda_DH(4) = -(2+kappa^2) log 2 < 0,
    Lambda_DH(6) = (1+kappa^2) log 6 != 0.

Therefore P0 fails; P1 fails because 6 is not a prime power; and P2_norm fails
already on the one-element set `S={2}`. The support is **not** all integers:
for example `Lambda_DH(5)=Lambda_DH(10)=0`.

The following NumPy results are reproducible reconnaissance, not interval
certificates and not an asymptotic theorem:

| N | \|S\| | zeta `(n+,n-,n0)` | DH `(n+,n-,n0)` | DH `lam_min` |
|---|---|---|---|---|
| 400 | 19 | (8, 0, 11) | (9, 6, 4) | -35.557 |
| 1600 | 39 | (12, 0, 27) | (16, 12, 11) | -106.844 |
| 4900 | 69 | (19, 0, 50) | (28, 19, 22) | -282.802 |

No claim that the negative index grows like `pi(sqrt N)` is justified by
these samples.

## 3. Norm pushforward versus place indexing

For a minimal real finite exponential sequence

    a_k = sum_r c_r alpha_r^k,

the infinite Hankel matrix `[a_{i+j}]_{i,j>=1}` is PSD exactly when all
`alpha_r` are real and all `c_r` are positive. The proof must use uniqueness
of the positive Hamburger representing measure together with the rational
Cauchy transform; treating complex atoms directly as a Hamburger measure is
not valid.

Consequences for the **norm-pushforward** sequence:

- For a positive-genus curve over `F_q`, the Weil-number atoms in
  `#C(F_{q^m}) = q^m+1-sum omega_i^m` have negative mass, so P2_norm fails.
- For a Dedekind zeta function the correct local formula is

      Lambda_K(p^k) = log(p) sum_{P|p, f_P|k} f_P.

  A residue degree `f>=3` introduces nonreal `f`-th roots of unity into the
  rational-prime exponential representation, so that norm-indexed Hankel
  block is not PSD.

These are indexing effects. The invariant package is labeled by a place `v`
and its iterate. Its block is

    K_v(i,j) = log N(v),

an all-one PSD matrix of rank one. For a curve `log N(v)=deg(v)log q`; for a
prime ideal `log N(P)=f_P log p`. Thus curves, zeta and Dedekind zeta all have
the same positive rank-one package per place. P2_norm is not the universal
form of Weil polarization because the pushforward `(v,j) -> N(v)^j` forgets
geometric labels.

There is a stronger insufficiency example. For `0<a<1/2`,

    F_a(s)  = zeta(s+a) zeta(s-a),
    Xi_a(s) = xi(s+a) xi(s-a)

has the symmetric completed functional equation `Xi_a(1-s)=Xi_a(s)` but has
zeros off the central line. Its Euler coefficients

    Lambda_a(n) = Lambda(n)(n^a+n^-a)

satisfy P0 and P1, and each prime Hankel block is a sum of two positive
rank-one matrices, so P2_norm also holds. Hence

    P0 + P1 + P2_norm + functional symmetry

does not imply Weil positivity. This example has local rank two, not zeta's
rank-one contact, so the complete contact provenance remains potentially
usable only when joined to a genuinely global construction.

## 4. Correct Davenport–Heilbronn triage

- The positive balanced factorization, shift-chain coercivity and scalar
  factor-four no-go consume P0 and zeta-specific prime asymptotics.
- A localized explicit formula has a DH analogue after changing Gamma and
  conductor data.
- Zero-extension nesting is formal only after rebuilding the birth list from
  the actual coefficient support; the prime-power threshold theorem does not
  transfer verbatim.
- Schur complements and Douglas factorization are abstract operator algebra.
  The physical `D_out,y_N` of paper 42 nevertheless depend on the positive
  `R-L` factorization and therefore consume P0.

The safe ceiling is: an argument using only functional symmetry and an
explicit formula cannot distinguish zeta from DH. An argument using the
specific positive rank-one contact provenance may distinguish them, but the
local contact data alone are insufficient.

## 5. Status

Questions (i)–(ii) of the phase-119 plan have a limited positive answer: the
programme has an invariant place-indexed input distinguishing zeta from DH,
and its exact rank-one clause distinguishes zeta from the shifted pair. It is
shared by curves and Dedekind zeta, so it is not a closure mechanism. Row
(d), the required global polarization and RH remain open.
