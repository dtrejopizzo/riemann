# Round 5, seed G3 — a measure built from the form whose closure gives the sign

Notation from `../phase-211-sign-sandbox/STATEMENT_001.md`: a_T(F) = Arch_T(F) − Π_T(F), with
Arch_T(F) = (1/2π)∫ m|F̂|² and Π_T(F) = Σ_{log n<2T} v_n Re c_F(log n), v_n = 2Λ(n)/√n; P_T = {A = B = 0}.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

Verdict in advance: **I did not manage to write an object satisfying A1–A6.** Each piece of the seed has
an antecedent read as primary source (§1). The three lemmas of §3 answer questions (i)–(iv) and the control
c = 2 and delimit the class. None carries a sign.

## 1. Cross-check (before building)

Antecedents read as primary sources, one for each component of the seed:

| Component of G3 | Antecedent | What is there |
|---|---|---|
| Law of independent geometric valuations, E_s X_d = d^{−s}; positivity by arithmetic construction at s = 2α ∈ (0,1) | `phase-209-nonlocal-kernel/CONSTRUCTOR_005.md` §§2–5, §10 | P_s on finite valuations (it is a probability for all s > 0). Exact completion −R_α = (−Z_α)E_s\|A − μ_1A\|² + ∫y^{α−1}τ\|E_yA − μ_1A\|². The sign source is a single real number, −2π^{−α}Γ(α)ζ(2α) > 0. §10: positivity **survives the deletion of any finite set of primes**. There is no map to the form (GOAL_D_STATUS: OPEN; LINK_009–016 attempt it and fail) |
| Minus sign between primes inside a covariance | `phase-209-nonlocal-kernel/ANTICORRELATION_003.md` §§2–4; `POSITIVE_ASSOCIATION_002.md` §§3, 5 | Under the discrete Gaussian on ℤ∖{0} (theta: Poisson and the lattice ℤ), Cov(X_d, X_e) < 0 for d, e coprime, and Var log\|N\| < Σ_p (log p)² Var Y_p. It is exactly "log n = Σ v_p log p with negative cross terms". With the origin included the sign is the opposite; removing only the origin already reverses it. No link with the form |
| The comb as a product of means and the remainder as a covariance | `phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md`, "Grouped divisor covariance" and "The divisor remainder is indefinite even on primitive even tests" | Lift A_F = Σ μ(d)F(t − log d)X_d, B_F = Σ log m F(t + log m)X_m under E_{1/2}. The means give U_μF and U_logF, and their pairing is the comb (μ∗log = Λ). The covariance gives R(F) = Σ n^{−1/2}C_{1/2}(n)Re c_F(log n). **PROVED: R is indefinite on P_T** (explicit tests F_± with R(F_+) = (7/4)κ‖g‖², R(F_−) = −(1/4)κ‖g‖²) |
| Law of total variance with divisor selector P(N = n \| b) = Λ(n)/log b (Λ as "expectation of the prime factor") | `phase-106-global-modular-star-audit/106_114_THETA_MARTINGALE_TOTAL_VARIANCE_GATE.md` §§2–6; R161_030 (via `R161_099_SYNTHESIS.md` and `ANNEX_161_FILES_2.md`; RULES_AVOID K2) | 106_114 writes the polar theta law, the total variance (8) and the divisor martingales (12)–(14). Theorem 2, NO-GO PROVED: no complete positive martingale tower, with all Gamma, central and divisor channels, is exact on the radicals; it is contradicted by the capacity of the prime-power lines. R161_030 gives the oriented variance identity, generic in the weights |
| Zeta law with marks (Palm): log n = Σ_{d\|n}Λ(d) as a sum of marks | `phase-104-unconditional-a1-closure/104_50_SECOND_ORDER_UNIT_PALM_COVARIANCE_GATE.md` §1 | E_s[Z_fZ_g] = Cov_s(D_f, D_g) + M_s(f)M_s(g), i.e. variance plus product of means. On centring, the towers of distinct primes cancel by independence |
| Lévy–Khintchine of the series with the Γ_ℝ part; symmetry s ↦ 1 − s of the law | `phase-194-invention/INV_A_001_ARITHMETIC_LEVY_STRUCTURE.md` §§0–5; `INV_F_001` F2 (via `ANNEX_COTEJO_LORENTZ_2.md` §4) | ID law with Lévy measure e^{−σu}u^{−1}[ΣΛ(n)δ_{log n} + du/(1 − e^{−2u})] for σ > 1. Reflection transports it to σ < 0 (Prop. 4.1); the strip is left without positivity. Θ⁺ is FALSE. The ∂log wall reaches every conic premise |
| Averaging with a probability over the family of weights | `phase-159-row-d-two-front-construction/G2_B8_R1.md` §2, Theorems B and S | Jensen for the concave function V_T: averages only give upper bounds, and the Haar mean of the Satake torus is < 0 for T ≥ 0.60 |
| Lorentzian class, object of degree ≥ 3 | `phase-160-row-d-infinite-T/R160_C7_R1.md` §§5–6 | §6.3(2) OPEN. The source of that section uses an external equivalence of the target; not developed here |

Not opened as primary sources: 104_49, 106_65, 106_104, R161_030–031 (read through the synthesis and the annex),
209 CONSTRUCTOR_002/004 and their AUDITs, G2_B8_R2–R5, `phase-193/CA_J_002`, Paper 48 and catalogues 01–06 of the
index (read through the annexes of this folder).

**Conclusion of the cross-check.** The seed, as formulated, is a repetition. It has three parts and each one
is in the corpus with its obstacle:
(a) the comb as a "squared mean" and the remainder as a covariance: 211 GLOBAL, with the remainder indefinite on P_T;
(b) total variance with the selector Λ(n)/log b: 106_114, with a NO-GO for every positive martingale tower;
(c) the arithmetic law at σ = ½ positive by construction: 209 CONSTRUCTOR_005, which survives the deletion of primes.
The coupling with the Gamma law, with the functional equation as a symmetry of the joint law, is in INV_A_001.
There the symmetry transports positivity from σ > 1 to σ < 0 and not to the line.
What the cross-check did not find, without this proving novelty: a statement that the comb cannot be an
"explained variance" on P_T (Lemma 2), and the control c = 2 done within the class of laws (Lemma 3).

## 2. Object (not written: what was attempted and why it is not an object)

The requested form was attempted: arithmetic (Ω, ℙ_T) and F ↦ X_F linear with a_T(F) = Var(X_F) + ρ(F) on P_T.
The three natural realizations are those of the cross-check:

- Random translations. If X_F = U_Y F with Y ⊥ F, then Var(U_YF) = ‖F‖² − ‖μ∗F‖² = (1/2π)∫(1 − |μ̂|²)|F̂|².
  This is a Fourier multiplier and falls in R3-a. When μ is the law of log N under ζ^c, it is blind to c (Lemma 3).
- The lift by valuations of 211: the remainder R is indefinite (PROVED in the source).
- The total variance with divisor selector of 106_114: NO-GO by its Theorem 2.

I do not have a fourth realization with its own formula. Lemma 1 shows that the variance format by
itself contributes nothing: without a written (Ω, ℙ, X) there is no object.

## 3. Identity, mechanism and answers to (i)–(iv)

**Lemma 1 (the variance format is (G); PROVED).** Let ℓ be a linear form on L²(I_T) that vanishes on
P_T. The following statements are equivalent:
(a) there exist (Ω, ℙ) and a linear map X with E X_F = ℓ(F) and a_T(F) = Var X_F + ρ(F) on P_T, ρ ≥ 0;
(b) there exist ℋ and V with a_T = ‖VF‖² + ρ on P_T, i.e. (G).
Moreover, if the identity holds on all of L²(I_T), then E|X_F|² − |ℓ(F)|² = a_T^{ext}(F) + ρ(F) defines an
extension with n₋ ≤ 1. That is the polar accounting of P46 thm:parityschur, which the inertia count R4-f does not
separate from c = 1.
*Proof.* (a)⇒(b): on P_T one has ℓ = 0, hence Var X_F = E|X_F|² = ‖X_F‖²_{L²(ℙ)}. (b)⇒(a): take the
centred Gaussian process with covariance ⟨VF, VG⟩ and add ℓ(F) to it as a constant. As for n₋ ≤ 1:
E|X|² ≥ 0, and subtracting |ℓ|² subtracts at most one direction. ∎
Reading: "zero mean exactly on P_T" adds no mechanism. The variance restricted to P_T is a squared
norm, and the novelty would have to lie entirely in (Ω, ℙ, X).

**Lemma 2 (the comb is neither an explained variance nor its opposite on P_T; PROVED).** If 2T > log 2, the
form Π_T restricted to P_T has subspaces of arbitrary dimension on which it is negative definite, and others
on which it is positive definite.
*Proof.* Take g ∈ C_c^∞(I_T) real, g ≥ 0, with support of length greater than log 2; then c_g(log 2) > 0.
Let F_ω(t) = g(t)cos(ωt). By Riemann–Lebesgue, uniformly in u:
c_{F_ω}(u) = ½c_g(u)cos(ωu) + o(1), ‖F_ω‖² → ½‖g‖², A(F_ω), B(F_ω) → 0, and
⟨F_ω, F_ω′⟩ → 0, Π_T(F_ω, F_ω′) → 0 as |ω − ω′| → ∞.
Correct F_ω towards P_T by subtracting a combination of two fixed functions dual to A and B; the correction is
O(|A| + |B|) → 0. Hence Π_T(F̃_ω) = P(ω) + o(1), with P(ω) = ½Σ_{log n<2T} v_n c_g(log n)cos(ω log n).
P is a trigonometric polynomial with distinct nonzero frequencies. It is not identically zero because the
coefficient of log 2 is positive, and its Bohr mean is 0. Hence P < −δ on a relatively
dense set, and P > δ on another. Choose ω_1, …, ω_k in the negative set and sufficiently separated. The matrix of
Π_T on {F̃_{ω_j}} is negative diagonal plus o(1), and likewise with the positive set. ∎
*Consequence (answer to (iii)).* In a_T = E Var(X|𝒢) = Var X − Var E(X|𝒢), the subtracted term is
positive semidefinite. By Lemma 2 it cannot be Π_T. Conditional covariance and "explained variance"
**do not produce the minus of the comb**. Every writing Π_T = V⁺ − V⁻ with V^± variances leaves
a_T = (Arch_T + V⁻) − V⁺: the same problem under another name (A4).
In the independence realizations, each prime contributes with a plus sign (G2_B8). The only arithmetic
minus that is written is the anticovariance between coprime primes of ANTICORRELATION_003. That minus
lives between pairs of primes (p, q), with coefficients (log p)(log q). The comb is diagonal in n = p^k, with
coefficient c_F(log n). The anticovariance has the format of the two-base channel −2 log p log q (K5,
R170_850 §5), already known to be linear in the weight.

**Lemma 3 (control c = 2 and non-integer c within the class of laws; PROVED).**
(a) For σ > 1 and all c > 0, P(N_c = n) = d_c(n)n^{−σ}/ζ(σ)^c is a probability, with
d_c(n) = Π_p binom(v_p + c − 1, v_p) ≥ 0. The valuations are independent, negative binomial
NB(c, p^{−σ}), and E N_c^{−iτ} = (ζ(σ + iτ)/ζ(σ))^c. The Gamma(σ/2) law, whose Mellin transform gives Γ_ℝ, does not
depend on c.
(b) P(p | N_c) = 1 − (1 − p^{−σ})^c, and this equals p^{−σ} if and only if c = 1. The function
x ↦ 1 − (1 − x)^c coincides with x at a point of (0,1) only if c = 1, by strict concavity (c > 1) or
convexity (c < 1).
*Proof.* (a) It is the Euler product of ζ^c, with nonnegative binomial coefficients. (b) Direct computation. ∎
*Answer to the control.* For c = 2 **no identity stops being a variance**. The joint law (N_2, G)
is a product probability, and every form Var(·) or E|·|² in it remains ≥ 0. What changes is the
linear identification of the means: E X_d = d^{−σ} holds only at c = 1 (Lemma 3(b)). Hence, in the
lift of 211, ⟨EA_F, EB_F⟩ stops being the comb 2Λ and becomes another linear functional. The sign of the
remainder is governed by nothing. The breaking is in a linear identification (D14, INV_I_001: identifies,
does not sign), not in the fixed archimedean factor. By A5 the mechanism does not break where it should. For non-integer c
the same holds, because the laws ζ^c exist for all c > 0 (infinite divisibility).

**Point-by-point answers.**
(i) X_F: the written choices are U_YF (random translation), Σ_d μ(d)F(· − log d)X_d with
Σ_m log m F(· + log m)X_m (lift of 211), and F evaluated at the log of a prime factor chosen with
probability Λ(n)/log b (106_114). F(log N) centred under the zeta law is the translation variant: its
variance is a multiplier (Lemma 2 and R3-a).
(ii) The window: in all of them, the support of F in I_T enters only because c_F(log n) = 0 for log n ≥ 2T. The law does not
see it: the valuations of a prime p < e^{2T} include all powers p^k, also those outside the
window. I did not find a mechanism that makes ℙ_T depend on T non-trivially. The only thing that brings the
T-dependence closer to the measure is the Mellin of 209, and there there is no τ.
(iii) The minus sign: Lemma 2.
(iv) σ = ½. There is no probability on ℕ with P(n) ∝ n^{−1/2}, because Σ n^{−1/2} = ∞ (PROVED). The laws with
characteristic function Λ(σ + iτ)/Λ(σ) exist for σ > 1 and, by reflection, for σ < 0 (INV_A_001 Prop. 4.1,
PROVED there). At σ = ½ only two routes remain:
- finitely many primes (209 §2);
- the Mellin of a theta with signed functional ν_y (209 CONSTRUCTOR_005 (2)).
In the second, the sign comes from a single real number and survives the deletion of primes. Pursuing the question
"is the law positive at the fixed point of the reflection?" requires an external equivalence of the target. Not
developed.

## 4. Controls (of the class, not of an object)

| Falsifier | Which hypothesis fails | Does it stop being ≥ 0? |
|---|---|---|
| c = 2 | E X_d = d^{−σ} (Lemma 3(b)) | No: variances remain variances; Gamma does not change. **The class does not break where it should** |
| non-integer c | Same; the law ζ^c exists (Lemma 3(a)) | No |
| a_P (deletion of primes) | None: the geometric law on the remaining primes is a probability (209 §10) | No: positivity is inherited |
| Davenport–Heilbronn | Signed coefficients: there is no law | Yes, but through Λ ≥ 0, a cone that cΛ preserves: a single channel is used (G1) |
| Epstein x² + 5y² | The valuations are not independent (no Euler product); the laws r_Q(n)n^{−σ} exist for σ > 1 | The variances remain ≥ 0; only the identification of means fails |

According to A5, a class that does not break at c = 2, non-integer c nor a_P is wrong as a sign source.

## 5. Own verdict

**I did not manage to write an object satisfying A1–A6.** The seed is a repetition of 211 GLOBAL (lift by
valuations), 106_114 (total variance, NO-GO), 209 CONSTRUCTOR_005 (law at s ∈ (0,1), inherited under deletion) and
INV_A_001 (Lévy with Gamma and reflection). It is not a proof of impossibility for every measure built from the
form.

## Result

No new mechanism. PROVED pieces without sign: Lemmas 1, 2 and 3.

## What was proved

- Lemma 1: the format "variance with zero mean exactly on P_T" is equivalent to (G); outside P_T it is the
  polar accounting with n₋ ≤ 1.
- Lemma 2: Π_T has subspaces of arbitrary dimension that are negative definite and positive definite on P_T
  (2T > log 2). Hence it is not an explained variance, and the law of total variance does not produce the minus of the comb.
- Lemma 3: the laws ζ^c are probabilities for all c > 0, with negative binomial valuations and fixed Gamma.
  Every variance identity in the class persists for c ≠ 1, and the only line separating c = 1,
  P(d | N) = d^{−σ}, is a linear identification.

## What failed and why

The sign of the probabilistic class is always "variance ≥ 0". That is closed under cΛ, under non-integer c and under
deletion, because the measure is positive by the coefficients ≥ 0, and these are preserved. The minus of the comb is
indefinite on P_T (Lemma 2), hence it cannot be a subtracted variance. And the only written arithmetic minus,
the anticovariance between primes of 209, is on pairs of primes and not in the diagonal channel of n.

## Concrete next step

A reopening would have to give a law ℙ_T whose positivity depends on c = 1 through something other than the
coefficients ≥ 0. The visible candidate is a law on ℤ (theta) in which deleting a prime changes the
sign of a covariance: POSITIVE_ASSOCIATION_002 §3 proves it for large y, but §5 shows that removing the
origin already does it. One would also need an X_F with a formula that carries that covariance to the diagonal channel of n.
Without that X_F written, the reopening does not pass the gate.
