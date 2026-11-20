# CONSTRUCTOR_007 — Module of arithmetic contractions of the kernel −R

2026-10-18. **PROVED, favourable final review in AUDIT_007:** multiplicative representation by contractions on the canonical completion of −R_α, with explicit positive defect and critical normalisation. It is not yet a representation of the form Q_T.

## 0. Corpus and written new reason

Consulted: index, grid and crossword for contractions, isometries, Frobenius, modules and semigroups of dilations. Pertinent entries: L2_016, L2_025–027, BUILD_R1_001 X1.0 (norms and angles between exterior data, NO-GO as sign), INV_D (unitary dilations and character), P1_BBSTAR and CELL_001.

An angle bound between r and D_nr is not retried nor is it claimed that a unitary dilation generates a sign. **New reason:** the Hilbert space is that of the independent kernel −R_α just identified; divisibility arithmetic and the Gaussian define two actions that intertwine exactly. The defect is not estimated by separate norms: it is computed as a positive integral with explicit multiplier `1−q_n`. The isometric law of the first factor requires keeping every observed prime. This changes the object and the hypothesis with respect to the indicated routes, without by itself proving a link to the gamma of the node.

## 1. Domain and already proved positive norm

Let s=2α∈(0,1), C_α=−Z_α>0. On the algebra of finite divisibility observables, I take **Haar-centred** representatives

`𝒜₀={A=Σ finite a_d X_d : E_1A=0}`,

allowing X_1=1 for centring. For this domain, CONSTRUCTOR_005 gives

`𝒦_α(A)=−R_α(A)=C_α E_s|A|²+Π_α(A)`,

`Π_α(A)=∫_0^∞ y^(α−1)τ(y)|E_yA|²dy`.

The centring condition makes Π converge at zero. I define 𝓗_α as the completion of 𝒜₀ for 𝒦_α. This completion is not identified with the domain of Q_T.

It can be realised without assuming closability of auxiliary operators: close in the Hilbert product the image

`A ↦ (√C_α A, y↦E_yA)`

in `L²(P_s) ⊕ L²(y^(α−1)τ(y)dy)`. The norm of that image is exactly 𝒦_α.

## 2. Divisibility action and geometric memory

For n≥1, I define

`(D_nA)(N)=1_{n|N} A(N/n)`;

on generators, `D_nX_d=X_(nd)`. Then `D_mD_n=D_(mn)`.

**Lemma 1 (PROVED).** For t>0 and finite A,

`E_t(D_nA)=n^(−t)E_tA`,

`E_t|D_nA|²=n^(−t)E_t|A|²`.

It is the geometric memory of valuations under P_t: conditioning on v_p≥v_p(n), the difference has the same independent law. In particular D_n preserves 𝒜₀ because `E_1D_nA=(E_1A)/n=0`.

In the punctured Gaussian,

`E_y(D_nA)=q_n(y)E_(n²y)A`, `q_n(y)=τ(n²y)/τ(y)`.

This comes from the change N=nM in the sum; it is exact and does not use stationary phase.

## 3. Normalised contraction and positive defect

I define `V_n=n^(s/2)D_n`. Its action on the arithmetic factor L²(P_s) is isometric by Lemma 1. On the Gaussian factor, for f(y)=E_yA, it acts as

`(G_nf)(y)=n^(s/2)q_n(y)f(n²y)`.

The change u=n²y gives

`Π_α(V_nA)=∫_0^∞ u^(α−1)τ(u)q_n(u/n²)|E_uA|²du`.

**Theorem 2 (PROVED).** V_n extends to a contraction on 𝓗_α, `V_mV_n=V_(mn)`, and on the algebraic core

`𝒦_α(A)−𝒦_α(V_nA)`

`=∫_0^∞ u^(α−1)τ(u)[1−q_n(u/n²)]|E_uA|²du ≥0`.   (1)

For n>1, punctured concavity gives q_n(z)<1/n for all z>0, so that

`𝒦_α(A)−𝒦_α(V_nA) ≥(1−1/n)Π_α(A)`.              (2)

(2) is not needed for the contraction: q_n≤1 already suffices. The strict bound offers the explicit defect.

**Proof.** Subtract the two norms; the term C_α E_s|A|² cancels by the exact isometry. The multiplicative representation is algebraic and is preserved when extending by continuity. ∎

At α=1/4, the normalisation is `V_n=n^(1/4)D_n`. This corresponds to a norm law n^(−1/2) before normalising; it must not be confused with an n^(−1/2) coefficient already identified in Q_T.

## 4. Adjoint on the Gaussian factor: exact computation

On `ℒ_α=L²(y^(α−1)τ(y)dy)`, the operator G_n is bounded and

`(G_n* g)(u)=n^(−s/2)g(u/n²)`,

`G_n*G_n f(u)=q_n(u/n²)f(u)`.

**Proof.** In the inner product of G_nf with g, change u=n²y; the factor τ(y)q_n(y) becomes τ(u), and the power leaves n^(−s/2). ∎

Hence `I−G_n*G_n` is exactly the positive multiplier of (1). Moreover `‖G_n‖≤1/√n` for n>1 and `G_mG_n=G_(mn)` by telescoping cancellation of the quotients of τ.

**Caution:** the adjoint of V_n on 𝓗_α is not identified with a restriction of the adjoint of the product of factors. The closed image may be only invariant, not reducing. The norm and semigroup identities do not require that identification.

## 5. Deletion of a prime: which arithmetic identity fails

In the law P_s^P of CONSTRUCTOR_005 §10, if p|P then X_p=0 almost surely. In particular `D_pA=0` as an observable of that law, while for A≠0

`p^(−s)E_s^P|A|²>0`.

Hence the normalised isometry of D_p of Lemma 1 **does not exist with that same deleted law and the same prime p**. For n coprime to P, geometric memory still holds and distinguishing those surviving actions is not required.

This identifies a joint property requiring all primes: the normalised isometric action of the arithmetic factor for **every** n≥1, intertwined with the complete Gaussian. It does not yet prove that this property forces the sign of Q_T nor that a quotient by null actions does not generate another positive module.

## 6. Exact connection with the FE already computed

The Gaussian factor uses τ and Π, whose complete inversion was proved in CONSTRUCTOR_006. At α=1/4 the change of scale y↔1/y keeps the parameter and transforms the increments of τ into differences of m between y and y/d². The actions D_n of this memo are compatible with the integer dilations appearing there.

It has not been proved that this inversion acts as a closed unitary involution on 𝓗_α conjugating V_n with a concrete adjoint operator. The formula for the Gaussian adjoint does not by itself provide such a global involution. This is an additional verifiable step, and it is not replaced by the FE of a multiplier symbol.

## 7. Link residue and scope

Now available:

- independent positive norm −R_α;
- an explicit representation of all integers by contractions;
- an isometric arithmetic factor with exponent s=1/2 in the critical case;
- positive Gaussian defects computed exactly;
- an FE of Π and a single-profile defect that fails after deletion.

What is missing is to identify a form or trace of these actions, defined and convergent on all tests F of the node, giving exactly the gamma and the comb of Q_T, and to treat its pole. No trace is taken as existing, nor is a character identity whose sign is the target itself imported.

Inequalities (1)–(2) are positive results of the constructed module; **they are not labelled as an inequality for Q_T**. They close neither D nor O1. They constitute a more specific object than an isolated covariance and leave a concrete link to build: the inversion of §6 and a form identity on the carrier of the paper.

## 8. Additional limit of specificity: monoid structure

Geometric memory and the norm laws of D_n, taken in isolation,
use only the multiplicative structure and the norm n. The inequality
q_n<1/n also holds for a real scale factor n>1. Hence part
of the computation can be formalised in other normed monoids; it is not claimed
that the contraction module alone distinguishes the arithmetic of all the
integers from Beurling systems.

The additional equalities that must be kept here are the realisation
of the observables by effective divisibility of integers, the identity with
the concrete renormalised R and the single-profile FE of CONSTRUCTOR_006.
It has not been proved that those equalities produce the form of Q_T. The
deleted-prime test in §5 locates an identity that fails in that law, but does not
constitute a complete specificity battery for the final link.


## Domain update — continuation015

CONSTRUCTOR_015_DOMAIN_AND_CONE resolves with another sequence the question
left open here: H=L²(P_s)⊕V and the operator T of 007 is not closable.
The strong vertical vector comes from likelihood tilts over large primes,
not from the divergent primorial sequence of 008. V=all Gaussian is not claimed,
nor invariance under the ambient FE; the Q link remains OPEN. AUDIT_015 favourable.
