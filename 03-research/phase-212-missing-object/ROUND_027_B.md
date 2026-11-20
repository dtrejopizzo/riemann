# ROUND_027_B — Adversarial cross-check of antecedents: damped weight v_n·cos(ω log n) and closure via closed K_T

Object cross-checked: a^{(ω)}_T = Arch − Σ v_n cos(ω log n) c_F(log n) on P_T, ω = kπ/(4T); facts (i)–(iii)
of the round's statement. Nothing was computed. No paper nor the index was edited.

Opened at the primary source: master index (Part V 212-25, 212-26-A/B, 212-cotejo-114, 212-cotejo-margen; rows of
W-lin, cor:void, thm:finmod, BARRIER_Y_001, Cesàro, Fejér); R160_M2_R1 (§§2–7 complete where relevant);
P47 main.tex thm:Z (l.1240–1290), lem:degen (l.3294–3310), prop a_θ (l.4805–4860); OBJECT_SPEC O2, O4;
RULES_AVOID B5, W1; ROUND_005_G3 Lemma 2; DOSSIER_001 (211) l.50–99; R186_051 §0; BARRIER_Y_001 §§0–2;
phase-62 README. Not opened: memos of phases 153–156 beyond what P47 cites; R160_D4_R2 (no
matches); phases 60–61; 183–185; Lemma T / W-mom only via their index rows.

## 1. Antecedents, one by one

**A1. Closure (ii) = Theorem 5.3(a) and Proposition 6.1 of R160_M2_R1 (phase 160, M2).** §5: (𝒱_T) with the
restrictions π^{T′}_T is a projective system of convex compacts, π^{T′}_T(𝒱_{T′}) ⊂ 𝒱_T (PROVED).
Prop 6.1: if there is a selection v*_T ∈ 𝒱_T with v*_{T,n} → 2a*_n/√n coordinatewise, then
λ^A_T(a*) ≥ 0 ∀T; the proof is exactly "𝒱_T closed + π^{T′}_T(v*_{T′}) → v_T(a*)". With a* = Λ the
hypothesis (iii) of that proposition is trivial and only (i)+(ii) remain: existence of the selection. The memo
concludes: "relocates the sign … without weakening it". Same in index 212-25 (ROUND_025_A/B): inverse limit of
the compacts K_T = 𝒱_T, Tychonoff. **It applies in full: (ii) is REPETITION.** The only difference is that
here the selection is explicit (w^{(ω_T)}), not taken from an optimizer.

**A2. Formula (iii) = P47 lem:degen + R160_M2_R1 Lemma 3.1 (Danskin–Kato) and Cor 3.3.** lem:degen (PROVED):
μ_T(w) ≤ λ_A − Σ (w_n − v_n) c_{F⋆}(log n), μ_T concave. With w = w^{(ω)}:
μ_T(w^{(ω)}) ≤ λ_A + Σ v_n(1 − cos(ω log n)) c_{F⋆}(log n) = λ_A + (ω²/2)Q(F⋆) + O(ω⁴).
Lemma 3.1 gives the exact directional derivative V′(v; d) = −max_{F∈M_T(v)} ⟨d, κ_T(F)⟩ (PROVED, with a
second-order formula with spectral gap g). Answer to (c): P47 does not give dλ/dT, but **the derivative with respect to the
weight exists and is proved** (R160 Lemma 3.1; P47 lem:degen as a one-sided bound); Q is the case
d = −(v_n(log n)²/2)ω². Note: the index (l.30802) records for phase 153 a "rate formula dλ/dT
PROVED" and Hellmann–Feynman in a parameter b (l.19087); not cross-checked against the round's claim.
**REPETITION** (as a formula); the numerical observation Q(F⋆) > 0 is new data.

**A3. Optimal weight ≈ damped v: index 212-26-A (ROUND_026_A).** With w ≥ 0 the optimum of max_w λ_min(a^w_T)
is stable and "looks like damped v" (w_n/v_n ≈ 0.87 … 0.22 at n = 2 … 11, T = 1.6), margin ≈ 0.08e^{−1.4T},
simple exponential. The current finding is an explicit version of that observation: same order of margin,
same simple decay. **PARTIALLY IN CORPUS** (prior numerical observation, without explicit family or ω²).

**A4. Modulation on the dual side: P47 thm:Z (i).** f_w(τ) contains −Σ v_n w(log n) cos(τ log n): it is the
explicit formula evaluated at the modulated test w(u)cos(τu). The algebraic mechanism of (i) (cos(ω log n)c_F =
Re c_{Fe^{iωt}}, shift of the spectral parameter, "family ζ(s+iω)") is the same; there it is used in a
linear certificate (flat-top, w = 1 on the window) and read on the zero side [H], which does not
count here. "One-sided smoothing" is that reading; it is not a damped weight in the primal form. **Fact (i) is in the
corpus; its use as a primal weight is not.** DOSSIER_001 (211) l.50–54 and R186_051: C_T(ω) ∝ Σ v_n cos(ω log n) as a
linear functional (coherence/symbol at frequency ω), not as a multiplier of the weight. ROUND_005_G3 Lemma 2:
tests F_ω = g cos(ωt) at ω → ∞ to show indefiniteness of Π_T; another regime (large ω), does not apply.

**A5. a_θ (P47 l.4805–4860).** Lowers a single weight (n = 2) and proves λ_A(T; a_θ) > 0 ∀θ ∈ [0,1] at T = ½log3
while λ^W fails; observation "classes closed under lowering weights". Antecedent of "lowering the comb helps",
in a fixed window and one atom. It does not cover the family or the closure.

**A6. Fejér / Cesàro.** Phases 60–62: Cesàro average in λ of the intrinsic Jacobi (another object); fails by
secular growth λ^{2β−1} of the average. Does not apply: here nothing is averaged in any spectral variable; the
weight is multiplied. Fejér rows (phase-102/103/104, L2_019, Fejér witness of Theorem K, 212-24-C item 150):
positivity transfers or support witnesses; none is a damped weight of the comb in a_T. They do not apply.

## 2. Class NO-GOs: do they cover the finding?

- **"Affine in the weight" (OBJECT_SPEC O2; RULES_AVOID J2, W1, W3).** Those clauses disqualify *identities*
  (G) whose square term is affine/quadratic in the weight, because they hold for every weight and do not see the sign. The
  finding is not an identity: it is the replacement of the target by another inequality (positivity of a^{w^{(ω)}})
  plus a topological closure. Affinity in the weight only says that K_T is convex and that (iii) is linear in the
  weight shift; **it does not disqualify it by itself**. What it does inherit from W1: the set of c with
  c·w^{(ω)} ∈ K_T is an interval with margin; nothing forces using c = 1 exactly at fixed T.
- **Change of reference operator (212-cotejo-114, D.186).** It is an exact congruence valid for every
  weight; the damped one is not a congruence but another weight. **Does not apply.**
- **W-lin / cor:shape.** Closes linear certificates in a fixed basis. Does not apply to the reduction; **applies to any
  attempt to prove a^{(ω_T)}_T ≥ 0 by a linear certificate**.
- **cor:void, thm:finmod, B5.** They do not apply to the reduction (ii), which is correct for any weight. **They apply to the
  missing proof**: if a^{(ω_T)}_T ≥ 0 ∀T were proved with hypotheses closed under finite deletion, rescaling
  cΛ or a_P, the closure (ii) would give the target for those falsifiers, which is false. Therefore the damped
  statement ∀T is subject to full O4: it must fail for cΛ (c ≠ 1), a_P, Λ1_{n≥N} at large T, with a
  margin that becomes negative on those families. That at T ≤ 2 the margin is ≍ ω²e^{−cT} says nothing here: the
  falsifiers are also positive at small T.
- **BARRIER_Y_001.** Farkas over the class {0,1} of deletions of the top layer; recommends not retrying
  first-order signs of c_{F⋆} with class moves. (iii) is a first-order sign of c_{F⋆}
  (Q(F⋆) > 0) under a move that lowers the top layer: **it applies to (iii) as a sign tool**; not to
  the reduction.
- **Lemma T, W-mom (only via the rows):** linear tail cost in ℓ¹; margin ≤ k(1−β_max) in moments of the pencil.
  No direct application seen; not verified at the primary source.
- **Theorem M / doubly exponential bound (212-cotejo-margen).** Compatible: the damped weight lies at distance
  ≍ e^{T} (in ℓ¹, Σ v_n(1−cos) with k = 1) from v, which is at doubly exponential distance from the boundary of K_T.
  The damped weight is not a perturbation of v; it is another interior point. The observable gain (∝ ω²) is the
  derivative of A2, not information about the tail that carries the sign.

## 3. Adversarial observation on the logic

The target asks for v ∈ K_T ∀T. The finding asks for w^{(ω_T)}_T ∈ K_T ∀T. This implies the target (A1) but is not
implied by it (K_T is not closed under non-uniform lowering of weights; A5 only sees it on one atom).
It is a **sufficient condition, possibly stronger in the tail**, of the same shape ("Arch − comb ≥ 0" on
P_T) with another weight. The non-tiny margin at T ≤ 2 is NUMERICAL and is exactly what R160 H1 and 212-26-A
already expected of the free-weight problem. What turns the margin into a proof ∀T: no mechanism proposed.
Cosine damping kills the weight at the window boundary (k = 1: ω·2T = π/2), i.e. it removes the
top contacts that produce the doubly exponential smallness (R160 H1, "tests that resolve the top
contacts"): it is plausible that the margin comes from that, and then the problem remains controlling the tail, which
is the same remainder.

## 4. Verdict

**PARTIALLY IN CORPUS** (reduction and formula: repetition; explicit family and numbers: new).

Repetition: (ii) closure via closed K_T and tower (R160_M2_R1 Thm 5.3(a), Prop 6.1; 212-25); (iii) derivative
with respect to the weight (P47 lem:degen; R160 Lemma 3.1, Cor 3.3); (i) modulation cos(τ log n) = modulated test (P47
thm:Z(i)); "optimal weight ≈ damped v" (212-26-A).

New relative to the corpus (with no priority claim outside it):
1. The explicit selection w^{(ω)}_n = v_n cos(ω log n), ω = kπ/(4T), as a candidate for Prop 6.1 with a* = Λ
   (in R160 the selection was abstract in 𝒪^prim_T).
2. NUMERICAL: positive margin ∝ k² with simple exponential decay up to T = 2; linear damping
   v_n(1 − log n/2T) gives negatives (not in the corpus).
3. The reading of (i) on the primal side: poles shifted to ½ ± iω plus archimedean correction
   ∫[m(τ) − ½m(τ−ω) − ½m(τ+ω)]|F̂|² (ARGUED: it is elementary; not cross-checked against P47 eq:m term by term).
   This correction is ≍ −½ω²m″ and could be the source of the ω² term; not checked.

What is missing so that it is not a relocation of the sign: a reason why a^{(ω_T)}_T ≥ 0 ∀T that fails for
cΛ (c ≠ 1), a_P and Λ1_{n≥N} (O4). Cheap test recommended before any derivation (small computation, not
done): the same damped margin for (1 ± 0.05)v and for v with deletion of one prime of the top layer at
T = 1.2–2.0; if the margin behaves the same, the finding is loss of margin (W1), not a mechanism.
