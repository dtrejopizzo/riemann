# Round 15, memo C — Convex functional with Hessian a_T (O14) and nonlinear odd pairing in A_M (O-odd)

Notation of the common brief: a_T(F) = Arch(F) − Σ_n v_n c_F(log n) on P_T, v_n = 2Λ(n)/√n. Controls: cΛ with c = 2,
deletion of one prime power, Beurling-type weight. I write a^{(c)} for the form with weight cΛ.

## 0. Cross-check (read in primary sources)

- `RULES_AVOID.md` M1, M4, M5, N1–N5, W4, X2; `REVIEW_005.md` R5-a…R5-e; `ROUND_013_C.md` §4.2 (Lemma K) and §5;
  `ANNEX_COTEJO_LORENTZ_2.md` (list of items not found, item 6: «Prékopa–Leindler or Brascamp–Lieb applied to the
  form. There are only mentions in lists»); `ROUND_009_G3.md` §0 (search «Prékopa» with no use).
- Phase 197 `BARRIER_W_001` §§0–4: Theorems W1 (n₋(T) monotone, every crossing downward), W2 (straight path
  a_s = (1−s)a_0 + sΛ: at most one crossing, «no kernel before s = 1» ⟺ μ_T(Λ) ≥ 0), W3 (codimension). Its §0
  already records: AUDIT_193 #101 (integer invariant/spectral flow, «constancy = positivity»), P35-3 and P49-2 (Maslov),
  ES-18 (finite Pontryagin index, DEAD), A14a-5 (Sylvester inertia blind), Theorem P / thm:index.
- Phase 186: `R186_034` (wall W-det: D_B(s;T) = det(1 − s·Pos^{−1/2}Neg·Pos^{−1/2}) entire, λ_A > 0 ⟺ β_max < 1;
  Thm 3.1: every determinant whose sign decides λ_A factors as λ_A·R and its leading term with
  multiplicative error O(1) never decides); `R186_045` §3.2 (moment criterion m_k = tr B^k: «it is W-det as a power
  series»); grid entry 28.

A search without matches does not prove novelty; the matches below do prove repetition.

## 1. Idea (1): log-concavity, Hessian of log(Γ × Euler)

**What the corpus closed.** M1 (`R160_C7_R1` §§5–6, Prop. 6.2): Lorentzian quadratic class, Alexandrov–Fenchel and its
combinatorial version reduce on the form to the statement. N1/R5-a: log-concavity at a base point (determinant,
partition function, variance) and Lorentz signature of a Hessian at a point are equivalent to (G) or to the statement.
N2/R5-b: hyperbolic degree ≥ 3 with Hessian −a_T is degree two or the goal with margin. Lemma K: convexity of a
measure or of positive weights gives Hessian ⪰ 0 for every weight. **«Hessian of a log-concave functional at a base point
determined by the integers» lies within R5-a** (the base point does not appear as a hypothesis of R5-a: the equivalence
is proved at an arbitrary point). Repetition, except for subsection 1.2.

**1.1 Lemma A (PROVED). The path s ↦ s + εF does not distinguish c.** Let Φ_c(F) = Φ_∞(F) + c·Φ_pr(F) with Φ_pr any
functional built linearly from log ζ = Σ_n (Λ(n)/log n) n^{−s} (second variation along
any path s(ε), including s + εF with F a function or operator). Then D²Φ_c(F_0) = D²Φ_∞(F_0) + c·D²Φ_pr(F_0)
is affine in c at every base point F_0 independent of c.
*Proof.* log(ζ^c) = c log ζ and the second variation is linear in the functional. ∎
Consequences. (a) If moreover each factor −log(1 − p^{−s}) is a log-Laplace transform of a positive law
(it is: geometric law of the valuation), D²Φ_pr ⪰ 0 for all c > 0 (Lemma K); the form a_T has the prime part with
opposite sign, so −a_T = D²(log Euler) − D²(log Γ) is a difference of two convex Hessians and convexity
contributes no sign. (b) Positivity of a form affine in c is an interval in c (W1 of round 13): the path s + εF
does not separate c = 1 from c = 2 by structure, only by size. It coincides with R5-e and W2 of phase 197.
Moreover, the second variation of n^{−(s+εH)} gives (log n)² H² n^{−s}, a diagonal term, not the autocorrelation
c_F(log n): to produce c_F(log n) the functional must already be the form (tautology).

**1.2 What changes with the base point: Prékopa (convexity by marginalization).** The only source of convexity that is
neither «positive measure» nor «positive weights» and that the Lorentz cross-check lists as unused. Let
Z(F) = ∫ e^{−V(x,F)} dx with V jointly convex in (x, F). Prékopa (CITED): log Z concave.

**Proposition B (PROVED, standard computation + Brascamp–Lieb inequality CITED).** With μ_F ∝ e^{−V(·,F)}dx,
−D² log Z(F) = E_{μ_F}[V_FF] − Cov_{μ_F}(V_F) = E_{μ_F}[V_FF − V_Fx V_xx^{−1} V_xF] + G(F),
with G(F) = E[V_Fx V_xx^{−1} V_xF] − Cov(V_F) ⪰ 0 (Brascamp–Lieb applied to each linear component of V_F).
If V is quadratic in x, G = 0 and −D² log Z is exactly the Schur complement of the joint block.
*Proof.* Differentiate log Z twice; the second equality is rearrangement; G ⪰ 0 is the Brascamp–Lieb variance
inequality for log-concave measures. ∎

**Corollary B′ (PROVED, in the declared class).** If a_T = −D² log Z(F_0) at a base point, the sign comes from
(i) the pointwise convexity of V at each x and (ii) G ≥ 0. (ii) holds for every convex V, hence is blind (Lemma T).
(i) is a family of pointwise PSD statements on blocks containing the weight. If V is quadratic in x, the
result is the Schur complement of a block, which falls into the dichotomy W2 of round 13 (Gram ⇒ blind; not Gram
⇒ equivalent to the form). If V is convex for every weight of one of the three control classes, the conclusion would hold in
that control: Lemma T. Hence the only unclosed variant is: V(x,F) **not quadratic in x**, convex only for the
true weight, with the pointwise convexity at each x verifiable by a finite statement that fails in the three
controls. OPEN; I have no such V. Note: a split in x of PSD blocks is structurally a pointwise signed split
(class O/O3, «signed parts without a rule»); the difference is the term G, which is blind. **It does not pass the gate.**

## 2. Idea (2): nonlinear odd pairing (sign, Cayley, resolvent, spectral shift, index)

**Lemma C (PROVED, finite dimension; ARGUED at the level of forms with compact resolvent).** Let A be the operator of a_T
relative to a fixed positive metric on P_T and f: ℝ → ℝ odd, strictly increasing, f(0) = 0 (sign, arctan,
Cayley part, etc.). Every quantity of the form tr g(A) with g odd nonlinear, the index of the pair of projections
(1_{(−∞,0)}(Arch), 1_{(−∞,0)}(A)) or the spectral shift function ξ(0; Arch, A) is determined by, or
determines, n₋(A) only when the spectrum of A is added: in particular ind = n₋(A) − n₋(Arch) (when the difference
of projections is Hilbert–Schmidt) and «n₋(A) = 0» reads as «ind = −n₋(Arch)».
*Proof.* For pairs of projections with P − Q in S_{2k+1}, ind = tr(P − Q)^{2k+1} (CITED, Avron–Seiler–Simon);
with P, Q negative spectral projections of two forms whose common domain is P_T, the index is the difference of
dimensions of the negative spaces. ∎
**Reading.** The index formula is exact and odd nonlinear in A, but requires the spectral projections of a_T,
i.e. diagonalizing the form (circular, J3). The integer is n₋ itself; W1 of phase 197 proves there is no other
conserved invariant: n₋ is monotone in T and every crossing is downward.

**2.1 Spectral flow in the coupling c ∈ [0,1].** This is W2 of `BARRIER_W_001` with a_0 = 0 (path a^{(c)}): concavity
of c ↦ μ_T(a^{(c)}) gives at most one crossing, and «number of zeros of D_T(c) in (0,1)» = n₋(a^{(1)}) − n₋(a^{(0)}) is
tautological. Above the archimedean threshold (Arch with negative directions on P_T) one adds n₋(Arch) =
thm:index, archimedean, which does not see the weight. **Repetition.**

**2.2 Fredholm determinant and cycle expansion.** D_T(c) = det(1 − cK_T), K_T = Arch^{−1/2}·Prime·Arch^{−1/2}
(below the threshold) is D_B of `R186_034` Thm 2.1; −log D_T(c) = Σ_k c^k m_k/k with m_k = tr K_T^k is exactly the
moment criterion of `R186_045` §3.2 (β_max < 1 ⟺ ∃k: m_k < 1), declared «W-det as a power series».
**What W-det closes, exactly:** Thm 3.1 of R186_034 — every continuous determinantal functional whose sign decides λ_A
factors as λ_A·R, and no leading term (Szegő, Kac–Akhiezer, Fisher–Hartwig, Landau–Widom) with
multiplicative error O(1) decides; the sign lives in the prolate leakage. It does not close an explicit bound uniform in T of some
m_k < 1.
**What is genuinely arithmetic in the expansion (ARGUED, not new as a criterion).** With S_u the translation by u
compressed to I, tr K^k = Σ_{n_1,…,n_k} v_{n_1}⋯v_{n_k} tr(Arch^{−1} S_{±log n_1} ⋯ Arch^{−1} S_{±log n_k}); since
Arch^{−1} is almost local at scale O(1) inside a window of width 2T, the term is appreciable only when the
partial sums Σ ±log n_i stay in I and the chain closes, i.e. n_1^{±1}⋯n_k^{±1} ≈ 1: multiplicative
near-coincidences between distinct primes, the place pointed to by the three residues. But the criterion asks for an **upper
bound** m_k < 1, not a sign; all v_n > 0, and what must be bounded is the sum of chains, which the control
c = 2 multiplies by 2^k (m_k^{(2)} = 2^k m_k): the control fails at m_k ≥ 2^{−k}, so a bound on m_k must
have relative precision 2^{−k}·(margin), which is W1 of round 13 by another route. Without an object bounding m_k: **does not pass**.

## 3. Four-point gate

| Candidate | (1) antecedent | (2) new object | (3) avoids the difficulty | (4) global identity | Verdict |
|---|---|---|---|---|---|
| Log-concavity at base point | R5-a, M1 | none | no | — | repetition |
| Path s + εF of log ζ | R5-e; Lemma A here | Lemma A (affinity in c) | no | — | NO-GO in the class |
| Prékopa/marginalization | Lemma K, W2 round 13 | Prop. B / Cor. B′ (reduction) | only if V non-quadratic and convex only for Λ | a_T = E[Schur] + G | no object |
| Index/Cayley/ξ | BARRIER_W_001 W1, ES-18, #101 | none | no (circular) | — | repetition |
| Spectral flow in c | BARRIER_W_001 W2 | none | no | — | repetition |
| det(1 − cK), cycles | R186_034 Thm 3.1, R186_045 §3.2 | reading of chains as near-coincidences | no (bound, not sign) | ∃k: m_k < 1 | repetition (W-det) |

No candidate passes. Nothing further is built.

## 4. Next explicit operation (OPEN)

Write V(x,F) with x ∈ ℝ^{𝒫} indexed by prime powers of the window, not quadratic in x, such that the mixed
block V_Fx couples the coordinate x_m with x_n only when |log(m/(kn))| is small, and such that joint convexity
at each x reduces to a finite inequality that uses an exact additive relation (n+1 coprime with n, 4 = 1+3) and
fails at c = 2, under deletion and under Beurling. First test: T = ½ log 5, contacts 2, 3, 4, with the remainder G of
Prop. B explicit. If V turns out quadratic in x, the candidate falls into W2 of round 13 and stops.

## 5. Labels

| # | Statement | Label |
|---|---|---|
| 1 | Lemma A (affinity in c of the Hessian along any path of log ζ) | PROVED |
| 2 | Prop. B (Brascamp–Lieb formula for −D² log Z) | PROVED mod. CITED |
| 3 | Cor. B′ (reduction of Prékopa to Schur + blind remainder) | PROVED in the declared class |
| 4 | Lemma C (index = difference of n₋) | PROVED (finite dim.) / ARGUED (forms) |
| 5 | Reading of tr K^k as closed chains and 2^k scaling of the control | ARGUED |
| 6 | O14 and O-odd with written object | OPEN |

For independent checking: rederive Lemma A, Prop. B (in particular G ⪰ 0 component by component) and the identification
m_k^{(c)} = c^k m_k (K_T is linear in the weight below the archimedean threshold).
