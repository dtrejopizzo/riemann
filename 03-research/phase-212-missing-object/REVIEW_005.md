# Review of round 5 (generative: write an object from the specification A1–A6)

Memos reviewed: `ROUND_005_G1.md` … `ROUND_005_G5.md`. All five conclude "I did not manage to write an object that
satisfies A1–A6". No candidate. Global sign OPEN. No result of this round carries a sign.

## Verdicts

| Seed | Memo | Verdict | Checked | Reservation |
|---|---|---|---|---|
| G1 object of degree ≥ 3 with Hessian −a_T | 005_G1 | ACCEPTED | Lemma 2–3: with p(e + sF) = p(e)∏(1 + sλ_i), Σλ_i = 0 and Σλ_i² proportional to a_T(F) on P_T, whence \|e_k(λ)\| ≤ (Σλ_i²)^{k/2}; for d = 3 the discriminant gives a_T³ ≥ 54 p(F)² | The reduction of the four certificate classes to (G) was read, not redone in full. "Probably false at near-minimizers" is ARGUED. The citation of G2_B8_R5 has no interval arithmetic |
| G2 closure under product over the signature | 005_G2 | ACCEPTED | Lemma 1 (homomorphism: product of factors ↦ sum of forms); Lemma 2 (a semigroup closed under product contains x_∞ ⊛ x_2^{⊛n}, whose form 𝔪_T − nΠ_{T,2} has unbounded negative index on P_T for T > ½ log 2) | Lemmas 3–5 read, not redone. "c = 2 fails exactly" is not checked; only large c |
| G3 the form as a variance | 005_G3 | ACCEPTED WITH RESERVATION | Lemma 1 (variance format ⟺ (G)); Lemma 3 (the laws of ζ^c are probabilities for all c > 0) | Lemma 2 (Π_T with definite subspaces of arbitrary dimension of both signs on P_T) was reviewed only for plausibility |
| G4 induction that lengthens the window | 005_G4 | ACCEPTED | Lemma 1 (c_F(±2T) = 0: at the crossing λ_A does not depend on the incoming weight); Lemma 2 (admissible interval with interior when λ_A(T) > 0); Lemma 3 (every weight satisfies a(n) = (a∗1)(n) − Σ_{d\|n, d<n}a(d)) | The premise of the seed was false (Lemma 3). The analysis of the Riccati forcing is ARGUED |
| G5 free invention | 005_G5 | ACCEPTED | L1 (−∇² log det(X_0 + ΣxA)[u,u] = tr((X_0⁻¹A_u)²): Gram form); L3 (for homogeneous p, by Euler's identity ∇²p(x_0)x_0 = (d−1)∇p(x_0), "at most one positive eigenvalue" ⟺ ∇² log p ⪯ 0 on the orthogonal complement of the gradient) | L2 is PROVED in finite dimension; its point (e) is relative to G2_B8_R1 |

## Results recorded (all without sign)

R5-a (PROVED, `ROUND_005_G5.md` L1, L3; `ROUND_005_G3.md` Lemma 1). Log-concavity at a base point
(determinant, partition function, variance) and Lorentz signature of the Hessian of a homogeneous
polynomial at a point: equivalent to a Gram realization (G) or to the statement on the sector. They add no
mechanism. Does not exclude a property valid on a whole cone with its own certificate.

R5-b (PROVED, `ROUND_005_G1.md` Lemma 3). If p is hyperbolic of degree d ≥ 3 with respect to e with Hessian −a_T
on P_T, then \|D^k p(e)[F^k]\| ≤ C a_T(F)^{k/2}: either the terms of degree ≥ 3 vanish on P_T
(class of R160_C7_R1 Prop. 6.2), or hyperbolicity is the target with margin (for d = 3,
a_T³ ≥ 54 p(F)²). Answers R160_C7_R1 §6.3(2) in the four certificate classes examined.

R5-c (PROVED, `ROUND_005_G2.md` Lemmas 1–2). Multiplying Euler factors is adding forms. No semigroup
closed under product containing the archimedean factor and that of the prime 2 admits a closure theorem
"n₋ ≤ κ on P_T" for T > ½ log 2. With the balance condition (each local factor once per
archimedean factor, equivalent to the oddness of the logarithmic derivative under s ↦ 1 − s) and coefficients
in {0, 1} no closure operation remains: the claim is the statement. The intermediate stages with
twisted functional equation are in phase 122 (P122_018).

R5-d (PROVED, `ROUND_005_G4.md` Lemmas 1–3). At the instant the window reaches log n, λ_A does not depend
on the incoming weight; in every window with λ_A(T) > 0 the set of admissible weights at n is an interval
with interior. Every weight is determined by its divisor sum and the previous weights; what is specific to
Λ is that this sum is log n. Antecedents: R162_802 §§4–5, R162_2701, phase 197 BARRIER_W_001.

R5-e (PROVED, `ROUND_005_G3.md` Lemma 3; Lemma 2 with the indicated reservation). The valuation laws of ζ^c are
probabilities for all c > 0; no variance identity breaks at c = 2. The comb is not an
explained variance. Antecedents: phase 209 CONSTRUCTOR_005 §10, ANTICORRELATION_003; 106_114 Thm. 2;
211 POWER_GLOBAL_ROUTE_REVIEW.

## What the round leaves unexcluded, and without a written object

The five memos point, in different words, to the same gap:
1. A local splitting a_T = q_∞ + Σ_p q_p with q_v ⪰ 0, where q_p is neither translation-invariant nor of
   Lévy type and has its own formula (G1, G5). With free splitting its existence is equivalent to the target.
2. A stage predicate for induction over primes, with its own formula (G2).
3. A relation non-linear in the weight between composing shifts (convolution) and composing lengths
   (window) (G4).
4. Real-rootedness certificates outside the four classes examined; an F-dependent base point (G1).
