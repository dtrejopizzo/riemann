# H1_TRACT_001 — tractability audit (phase 204r): (A) H1⁺ = n₋(𝔄_ev(T)) ≤ 1 ∀T; (B) 𝔄_odd(T) ≻ 0 ∀T

OPEN / NO-GO / NUMERICAL. Single file written by this review.

## Summary (≤250 words)

Convention (P46 prop:WT, l.4358): 𝔄 = 𝔞_T|𝒟^par_T = archimedean 𝔪_T + comb Π_T = −Σ v_n c_F(log n), WITHOUT the polar
term; W^par = 𝔄 + 2ε_par χχᵀ with ε_ev = +1, ε_odd = −1.

(A) H1⁺. D_ev ⇒ WP^ev ⇒ H1⁺ (PROVED, Cauchy). H1⁺ implies nothing about the sign by itself; with H1⁻ it fixes n₋ = 1
and, by WT-R1, q_ev is non-decreasing: D_ev ⟺ sup_T q_ev(T) < −½ — a reduction to a monotone scalar, but the value of
that scalar is REF-D (Prop S). **Lemma A∞ (PROVED, full sketch §2):** n₋(𝔪_T|𝒟^ev) → ∞ and n₋(𝔪_T|𝒟^odd) → ∞ as
T → ∞. Corollary (PROVED): H1⁺ and B are FALSE for the comb v = 0 and for θΛ with θ < θ_c(T); both combs satisfy all
the Perron–Frobenius hypotheses of P60-1. Hence **NO-GO for the PF/Markov/density-without-size class** (refines NO-GO
Thm 2 of front I, phase 193): P60-1 gives simplicity of the ground state, not the sign of λ₂, and H1⁺ is the sign of
λ₂. Second eigenvalue: it falls into 𝒦_W (continuation in T) and into 𝒦_H by the same Theorem X argument (ARGUED; not
literally covered). TRAT(A) = **TRANSFER to (L2)/K34 (N_loc in codim 1)**, with no route of its own.

(B) **Correction:** B is NOT stronger than the odd half of D: W^odd = 𝔄_odd − 2χχᵀ ⇒ W^odd ≻ 0 ⇒ 𝔄_odd ≻ 0 (PROVED). B
is NECESSARY, weaker than W^odd ≻ 0, stronger than WP^odd. It fails for v = 0, small θΛ and (NUMERICAL) odd deletion at
½log3. TRAT(B) = **TRANSFER**, Λ-specific, with no route of its own. Neither is promoted to YES.

## 0. Corpus check (mandatory)

grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/` (line counts): «inertia» 15, «n₋» 21, «(L2)» 15, «S_{T,k}» 8,
«W1» 56, «Weyl» 7, «cor:convfail» 5, «thm:parityschur» 5, «P60-1» 3, «Perron» 13, «archimedean + comb» 1 (WT_HALVES),
«𝔄_odd» 4 (WT_HALVES/WEAKEN), «certified odd sector» 0, «H1⁺» 1, «second eigenvalue» 0, «λ₂» 4. Relevant entries:
- **P60-1** (03_PHASES_000-099 l.197; `03-research/phase-60-discriminant/H1_PROOF.md`): A_λ = M_θ − V, V = Σ Λ(n)T(n)
  positivity-preserving, positivity-improving semigroup ⇒ simple ground state, even, nodeless. "Gives simplicity, not
  sign." The "no-pole case" operator of P60-1 is exactly 𝔄 (both parities). See §3.
- **Front I, phase 193** (README l.272–274): the form without the pole is Markov, λ₀ < λ_A ≤ λ₂ (PROVED); NO-GO Thm 2:
  Markov/PF/maximum/parity/Tate do not decide. What follows is a refinement with an explicit falsifier for H1⁺, not a
  retry.
- **WT_HALVES_001 §3** (phase 204n): H1⁺ OPEN, "transfer to (L2)"; odd-H1 OPEN, "stronger than WP^odd"; archimedean
  count n₋(𝔪_T,ev) ≳ 4T only ARGUED (Landau–Pollak–Slepian). This review: (i) proves the divergence (Lemma A∞);
  (ii) turns the "transfer" into a PF-class NO-GO with a falsifier; (iii) corrects B's relation to W^odd.
- **BARRIER_W_001** (phase 197, W1): n₋ non-decreasing, single-sign crossings; 𝒦_W NO-GO. **AUDIT_CONSTRAINTS_001**
  (phase 199): Theorem X, 𝒦_H, restriction 11 (every first-order discriminant is a functional of h*, not of σ).
- **cor:convfail** (P46 l.4816): (i) deletion Λ1_{n≥5}: WP holds, W fails; (ii) a contact a_θ at ½log3.
- **WEAKEN_001 K11/K34**: K11 already weakened (D3); K34 = (N)/(N_loc), "equivalent to the datum."
New reason, written out, for touching P60-1/PF: PF is not retried as a sign route; it is used as a declared method
class to prove that it does NOT reach H1⁺ nor B (a new NO-GO, with a falsifier), something no entry registers for λ₂.

## 1. Exact statements and direction relative to D

Notation: 𝔄_par(T) operator of the closed form 𝔞_T|𝒟^par_T (P46 prop:WT); q_par = ⟨𝔄⁻¹χ_par, χ_par⟩;
W^par = 𝔄_par + 2ε_par χ_parχ_parᵀ (ε_ev = +1, ε_odd = −1; direct reading of the proof of prop:WT: 𝔤 = 1/q + 2ε).

**(A) H1⁺:** n₋(𝔄_ev(T)) ≤ 1 for all T > 0.
- D ⇒ H1⁺: PROVED by two routes: (a) W^ev ⪰ 0 and 𝔄_ev = W^ev − 2χχᵀ (rank one) ⇒ n₋(𝔄_ev) ≤ n₋(W^ev) + 1 = 1 (in the
  non-degenerate case; with a radical, n₋ ≤ 1 still holds, because only one square is subtracted); (b) Cauchy:
  λ₂(𝔄_ev) ≥ λ^ev_A ≥ 0.
- Strictly weaker than WP^ev at each T (it admits that the positive hyperplane may not be ker ℓ_ev). PROVED as an
  implication; the strictness as a class statement is illustrated by the models where WP fails with n₋ = 1
  (rem:polarcapdiag) — NUMERICAL.
- H1⁺ ⇒ ? By itself nothing about the sign: the case "n₋(𝔄_ev) = 1 ∧ q_ev > −½" is compatible with H1⁺ and gives W^ev
  with one negative square (prop:WT(i)). That is what happens with a_P at ½log3 (q_ev ≈ −0.408, NUMERICAL): H1⁺ holds,
  D fails.
- H1⁺ + H1⁻ (n₋ ≥ 1, T ≥ T₀; CONDITIONAL on a quadrature) ⇒ n₋(𝔄_ev) ≡ 1 on [T₀,∞) ⇒ (Lemma WT-R1, PROVED in finite
  dimension) q_ev non-decreasing on [T₀,∞) ⇒ D_ev on [T₀,∞) ⟺ q_ev(T) < −½ ∀T ⟺ L := lim_{T→∞} q_ev(T) ≤ −½ with
  non-attainment (L < −½, or L = −½ not attained). See §5 on whether this is an input.

**(B):** 𝔄_odd(T) ≻ 0 for all T > 0.
- **Correction to the objective and to WT_HALVES §3.4:** W^odd = 𝔄_odd − 2χ_oddχ_oddᵀ (ε_odd = −1). Hence 𝔄_odd =
  W^odd + positive rank one ⪰ W^odd: **W^odd ≻ 0 ⇒ 𝔄_odd ≻ 0 and W^odd ⪰ 0 ⇒ 𝔄_odd ⪰ 0** (PROVED, one line). B is
  therefore **necessary** for the odd half of D (in strict form), **weaker** than W^odd ≻ 0, and
  W^odd ≻ 0 ⟺ B ∧ q_odd < ½ (prop:WT, end). "Stronger" only holds relative to WP^odd (B ⟺ WP^odd ∧ q_odd > 0, by (1.1)
  of WT_HALVES). B and W^odd ⪰ 0 are NOT incomparable: B is the inertia half of the odd half, exactly as H1⁺ is in the
  even case.
- By monotonicity in T (WT_HALVES §3.1, PROVED): B ⟺ 𝔞 > 0 on all of 𝒟^odd of compact support (no kernel at each T).
- Data: B holds for T ≤ ½log5 (prop:wh-index(ii) via thm:log5W, PROVED in P46) and, via D0 (Mori, ½log15, CITED +
  lem:monoT) and the implication above, for T ≤ ½log15 (CONDITIONAL on non-degeneracy; the inclusion is new here only
  as a reading: D0 ⇒ W^odd ⪰ 0 ⇒ 𝔄_odd ⪰ 0).

## 2. Lemma A∞: the archimedean part alone has unbounded negative inertia (PROVED)

Convention: 𝔪_T(f) = (1/2π)∫ m(τ)|f̂(τ)|² dτ on f ∈ 𝒟^par_T, with m continuous, even, m(τ) = O(log(2+|τ|)), and
m < 0 on |τ| < s_m ≈ 6.29 (R186_022, R186_048; symbol Ω(t) = −log π + Re ψ(¼ + it/2) in P60-1 §1; Ω(0) ≈ −5.37).
Input: the sign of m on [0, 6] is CITED (quadrature of ψ on a compact band, certifiable; for a strict PROVED one only
needs m < 0 on [0, 3], which is elementary by monotonicity of Re ψ(¼ + it/2) for t ≥ 0 — ARGUED-elementary).

**Lemma A∞.** For every k there exists T_k with n₋(𝔪_T|𝒟^ev_T) ≥ k and n₋(𝔪_T|𝒟^odd_T) ≥ k for T ≥ T_k.

*Proof.* Fix φ ∈ C_c^∞(−1,1) even, ‖φ‖₂ = 1, and frequencies 0 < a_1 < … < a_k < 3 with separation δ > 0. For L > 0,
φ_L(x) = L^{−1/2}φ(x/L), f_j = φ_L(x)cos(a_j x) (even), g_j = φ_L(x)sin(a_j x) (odd), support in [−L, L] ⊂ I_T for
T ≥ L (centering the window; the extension by zero and the parity are those of lem:monoT). f̂_j = ½(φ̂_L(·−a_j) + φ̂_L(·+a_j)),
with |φ̂_L|² = L|φ̂(L·)|² → 2π δ₀ weakly and with tails O_N((1+L|τ|)^{−N}). Since m has logarithmic growth, by dominated
convergence: 𝔪(f_j, f_l) → ½ m(a_j) δ_{jl} as L → ∞ (the cross terms involve φ̂_L(τ−a_j)φ̂_L(τ−a_l) with
|a_j − a_l| ≥ δ, which tend to 0; likewise the term in −a_j vs +a_l). Same for g_j. The k×k Gram matrix converges to
diag(½m(a_j)) ≺ 0, so it is ≺ 0 for L ≥ L_k, and by min–max n₋ ≥ k in both sectors for T ≥ T_k := L_k. ∎

Quantitatively (ARGUED, Landau–Pollak–Slepian): n₋(𝔪_T|𝒟^ev) ≈ n₋(𝔪_T|𝒟^odd) ≈ 2T·s_m/π ≈ 4T. The PROVED lemma only
needs "→ ∞," and that is all that is used below.

**Corollary A∞ (PROVED).** (a) For the comb v = 0: H1⁺ and B are false (for T ≥ T_2, resp. T ≥ T_1).
(b) For v = θΛ (θ ≥ 0), at fixed T ≥ T_2, Π_T is a bounded operator on L²(I_T) (finite sum of translations, n ≤ e^{2T})
⇒ 𝔄(θ) = 𝔪_T + θΠ_T is a bounded perturbation, and n₋(𝔄_ev(θ)) ≥ 2 for θ < θ_c(T) := |λ₂(𝔪_T,ev)|/‖Π_T‖ > 0 (Weyl
in the useful direction: λ_j(A + B) ≤ λ_j(A) + ‖B‖). Likewise for B with λ₁(𝔪_T,odd).
(c) The comb must "fill" the negative archimedean spectrum: H1⁺ says that Π_T neutralizes all but one of the ≈ 4T
negative squares of 𝔪_T,ev, at every scale; B says it neutralizes all ≈ 4T of the odd ones. The Weyl bound in the
direction requested by the objective, n₋(A_∞ + C) ≤ n₋(A_∞) + n₋(C), gives ≥ 4T + n₋(Π_T): **useless** (confirms
WT_HALVES §3.3). The direction that is actually needed is rank₊-domination of the comb on the band |τ| < 6.29 over
every window — that is, a quantitative statement with size, not a qualitative class statement.

Remark on the comb on the band (ARGUED, a reading of the explicit formula without using zeros as input): for f
concentrated at frequency a, Π_T(f) ≈ −‖f‖²·Re Σ_{n ≤ e^{2T}} v_n cos(a log n)-average = −‖f‖²·Re P_T(a) with P_T the
truncated Dirichlet polynomial of the comb at ½ + ia. Neutralizing m(a) < 0 requires Re P_T(a) ≤ m(a) (large negative)
for |a| < 6.29 except in one direction. For Λ, the main term of P_T is the one that compensates the pole (and is not
in 𝔄: that is precisely why 𝔄 has the square χ); the rest is the fluctuation that (N)/(N_loc) (K34) controls. That is:
**H1⁺ = (N_loc) valid on some codimension-1 subspace of the even sector, at every scale**; B = (N_loc) on the whole odd
sector at every scale. K34 is recorded as "equivalent to the datum; no weakening of the cancellation PROVED." The move
to codimension 1 does not change the scale of the cancellation (e^{2T}), so it does not evade the reason for that record.

## 3. Does P60-1 (Perron–Frobenius) prove H1⁺? No. Class NO-GO (PROVED)

The objective suggests "H1⁺ is simplicity of the negative eigenvalue." **That is false:** P60-1 proves that λ₀(𝔄) (both
parities together) is simple, with a positive, even eigenvector. Simplicity of λ₀ is λ₁ > λ₀; H1⁺ is λ₁(𝔄_ev) ≥ 0,
which is a sign statement about the second even eigenvalue, not a multiplicity statement about the first. The only
thing PF gives about the parity structure is λ₀(𝔄_odd) > λ₀(𝔄_ev) (the global ground state is even and simple) — with
no sign.

**Proposition NO-GO-PF (PROVED, by Corollary A∞).** Let 𝒦_PF be the class of methods whose hypotheses on the comb are
qualitative and stable under v ↦ θv, θ ∈ [0,1] (v_n ≥ 0; positivity/positivity-improvement of the semigroup e^{−t𝔄};
irreducibility; Markov/Beurling–Deny; parity; maximum principle). No method in 𝒦_PF proves H1⁺ nor B.
*Proof.* The combs θΛ, θ ∈ [0, 1] (and v = 0) satisfy all those hypotheses: v_n = θΛ(n) ≥ 0, the semigroup is
positivity-improving by the irreducibility of the Lévy measure of M_θ, which does not depend on the comb (P60-1 §5);
v = 0 is the pure Markov case. By Corollary A∞(b), H1⁺ and B fail for θ < θ_c(T). ∎
This refines (and is consistent with) the NO-GO Thm 2 of front I, phase 193, which was stated for the sign of λ_A;
here it is extended to the inertia halves, with the explicit falsifier θΛ, θ → 0.

Consequence: H1⁺ is NOT comb-generic. With the barrier theorem of phase 197 (comb-generic hypotheses do not close),
H1⁺ and B fall outside the reach of any argument that does not use the size of the comb at every scale.

Is it at least a "class" statement with a density threshold, valid for every sufficiently dense comb and hence provable
without exact Λ? Evidence against:
- From above, the comb also cannot be arbitrarily large: with v = θΛ, θ ≫ 1, at fixed T, Π_T dominates and its negative
  part (Π_T is indefinite: c_F(log n) changes sign) gives n₋(𝔄) ≥ n₋(Π_T|band) which grows with θ — ARGUED (Π_T is a
  sum of symmetrized translations, whose symbol −Re P_T(a) takes both signs). So there is no monotonicity in density:
  the set {θ : H1⁺ holds at T} is at most a window around θ = 1 that depends on T. ARGUED.
- Deletions: a_P at ½log3 satisfies H1⁺ (n₋ = 1, NUMERICAL); odd deletion at ½log3 fails B (q_odd ≈ −0.056 ⇒
  n₋(𝔄_odd) = 1, NUMERICAL); cor:convfail(i) a = Λ1_{n≥5} has a negative odd vector of W_T on [0.4608, log 2] (PROVED
  in P46), but since W^odd = 𝔄_odd − 2χχᵀ, that does not decide 𝔄_odd: there is no PROVED falsifier of B among the
  deletion models, only the NUMERICAL one at ½log3 plus the PROVED ones of Corollary A∞.
Honest reading: "H1⁺ holds for the known battery" is true only on small windows (½log3); at large T there is no
n₋(𝔄_ev) data for any modified comb. The objective's claim "H1⁺ holds for a_P ⇒ comb-generic" does not hold up: a
single T says nothing about ∀T, and v = 0, small θΛ falsify it.

## 4. The second eigenvalue: 𝒦_W / 𝒦_H?

By monotonicity in T (PROVED), H1⁺ ⟺ λ₁(𝔄_ev(T)) never crosses 0 from above. Two classes:
- **𝒦_W (BARRIER_W_001, W1):** any proof by continuation in T that an eigenvalue does not cross 0 is a Morse-index/
  spectral-flow argument. W1 only gives "single-sign crossings" (n₋ non-decreasing); a crossing of λ₁ through 0 is a
  codimension-1 event that nothing in W1 forbids. H1⁺ falls literally into 𝒦_W (the BARRIER_W statement is for n₋ of a
  form with extension by zero, which is the case of 𝔄 — WT_HALVES §3.1 applies it to 𝔄). NO-GO (CITED BARRIER_W_001).
- **𝒦_H / Theorem X / restriction 11:** Theorem X is stated for the minimizer h* (the first-order discriminant is a
  functional of the extremal and blind to σ at resolution π/T). The second eigenvector u₁ is not the global minimizer,
  but it is the minimizer of 𝔞_T over {u₀}^⊥ ∩ 𝒟^ev; the Hellmann–Feynman/Hadamard formula dλ₁/dT = (boundary term of
  u₁ at ∂I_T) uses only extremality + boundary values, just as for h*. Hence the mechanism of Theorem X carries over:
  dλ₁/dT is a functional of u₁ (which in turn depends on u₀), not of the comb in frequency. **ARGUED** (not literally
  covered by the statement; covered by the same proof with an additional orthogonality constraint to u₀, which is
  linear and introduces no information about σ). Honest decision: it is treated as inside 𝒦_H; if someone wants to use
  λ₁ to evade restriction 11, they must show what information u₀ contributes that h* does not — and u₀ is the PF
  ground state (positive, even), i.e. a comb-generic object (§3): it contributes no size.
Conclusion §4: no continuation class (𝒦_W) nor first-order class (𝒦_H) gives H1⁺; all that remains is a quantitative
statement by scale (K34/(L2)).

## 5. What input would A and B give for D, if proved?

- **A + H1⁻:** n₋(𝔄_ev) ≡ 1 on [T₀, ∞), q_ev monotone (WT-R1) ⇒ D_ev on [T₀,∞) ⟺ L = lim q_ev ≤ −½ (not attained).
  This turns a ∀T positivity into the sign of a limit of a monotone scalar — a real organizational improvement (a
  single number, with no possible intermediate crossings, because the monotonicity of q and the constancy of n₋
  exclude re-entries). But: (i) by Prop S, sign(q_ev + ½) = −sign(λ^W_ev) at each T, so L ≤ −½ is the same datum
  (REF-D); (ii) the margin at ½log3 is ≈ 2e−8 (NUMERICAL), and q grows: the distance to −½ is being used up, as
  WT_HALVES §7 already noted. Input: **structural, not of sign**. Moreover H1⁺ alone has the cost of (L2)/K34 (§2–4),
  so buying the reduction costs a datum of the same class as what it reduces.
- **B + q_odd < ½:** W^odd ≻ 0. With B, n₋(𝔄_odd) ≡ 0 and WT-R1 gives q_odd non-decreasing ⇒ the odd half ⟺
  lim q_odd < ½ (margin ≈ 2.5e−4 at ½log3, NUMERICAL). Likewise: structural; the scalar is REF-D.
- Accounting note: in the even sector the piece that carries the sign is q_ev (H2), not H1⁺; in the odd one the sign
  is split between B and q_odd < ½. That the odd deletion at ½log3 fails B (not q_odd) says that in the odd case the
  inertia half CAN be the one that fails: B is as fine as the odd half of D in that model. NUMERICAL.

## 6. Verdicts

**(A) H1⁺: n₋(𝔄_ev(T)) ≤ 1 ∀T.**
- Direction: necessary (D ⇒ WP^ev ⇒ H1⁺, PROVED); not sufficient (a_P at ½log3, NUMERICAL).
- Route of its own: NO. Lemma A∞ (PROVED): the archimedean part alone has n₋ → ∞; the comb must neutralize ≈ 4T − 1
  negative squares at every scale. PROVED falsifiers: v = 0 and θΛ with θ < θ_c(T). NO-GO PROVED for 𝒦_PF (includes
  P60-1: simplicity ≠ sign of λ₂). 𝒦_W NO-GO (CITED); 𝒦_H ARGUED.
- **TRAT(A) = TRANSFER** to (N_loc)/K34 in codimension 1 = class of (L2) (λ_A > 0 ⟺ S_{T,k} ≻ 0, phase 186): weaker at
  each T, same cancellation scale. Statement label: **OPEN**.

**(B) 𝔄_odd(T) ≻ 0 ∀T.**
- Direction (corrected): necessary for W^odd ≻ 0 (PROVED: 𝔄_odd = W^odd + 2χχᵀ); weaker than the odd half of D;
  stronger than WP^odd. W^odd ≻ 0 ⟺ B ∧ q_odd < ½.
- Route of its own: NO. n₋(𝔪_T|𝒟^odd) → ∞ (Lemma A∞, PROVED): B requires the comb to neutralize the ENTIRE negative
  odd archimedean spectrum at every scale; falsifiers v = 0, small θΛ (PROVED), odd deletion at ½log3 (NUMERICAL);
  cor:convfail does not decide it (it affects W, not 𝔄). Λ-specific. Same NO-GO 𝒦_PF.
- **TRAT(B) = TRANSFER** to (N_loc)/K34 on the odd sector. Label: **OPEN** for T > ½log15; PROVED for T ≤ ½log5
  (thm:log5W via prop:wh-index(ii)); CONDITIONAL on D0 (Mori, CITED) + non-degeneracy for T in (½log5, ½log15].

Neither is promoted to YES. What is new and PROVED in this review: Lemma A∞, Corollary A∞, NO-GO-PF for the inertia
halves, and the direction correction for B. Pending work that IS closable without D: writing out Lemma A∞ with
constants (how many negative squares at each T, explicit lower bound ~ c·T) — it is a purely archimedean lemma, useful
as a tool for any route that goes through inertias (it quantifies how much the comb must do).

## 7. Entry for the index (README, phase 204)

- **H1_TRACT_001 (phase 204r, inertia halves H1⁺ and 𝔄_odd ≻ 0): TRANSFER for both; NO-GO PF PROVED.** Lemma A∞ PROVED:
  n₋(𝔪_T|𝒟^ev), n₋(𝔪_T|𝒟^odd) → ∞ (m < 0 on |τ| < 6.29, tests φ_L cos/sin) ⇒ H1⁺ and 𝔄_odd ≻ 0 FALSE for v = 0 and θΛ,
  θ < θ_c(T): not comb-generic; P60-1/Markov/PF (class stable under θ ↦ θv) does not reach them (simplicity of the
  ground state ≠ sign of λ₂). λ₂: 𝒦_W (CITED), 𝒦_H (ARGUED). Both = (N_loc)/K34 in codim 1 / odd sector, class (L2).
  **Correction:** W^odd = 𝔄_odd − 2χχᵀ ⇒ 𝔄_odd ≻ 0 is NECESSARY (weaker than W^odd ≻ 0), not stronger. Do not retry:
  PF/Weyl/continuation in T for inertias of 𝔄.
