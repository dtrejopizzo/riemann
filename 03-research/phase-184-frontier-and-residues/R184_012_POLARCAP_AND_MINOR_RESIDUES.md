# R184_012 — prop:polarcap in T and minor residues of master grid item 59

Pure mathematics, no numerics. No paper or grid was edited.

## State

| item (grid §6, item 59) | verdict | label |
|---|---|---|
| prop:polarcap in T (2E) | **already analyzed** (R160_M4_R1, R162_703); the grid is out of date. Lemma 1 (Loewner monotonicity of 𝔊^{AB}_T) and Lemma 2 (left continuity of 𝔤̃_par) are added here. Does not move D. | PROVED (Lemmas 1–2); E1 for any ∀T sign statement |
| I11 absorbing channel (4H) | no statement ("unobturated angles" of doc 96; no proposition written) | no statement |
| I14 Čech of D_0 (8H) | object not constructed (technical core (a) of 123 §6 never defined; the self-pairing does not exist by 122) | no statement |
| Cayley index of 69 (7D) | named, not constructed (phase-69 README l.36: invariance w_{1−ρ}=1/w_ρ) | no statement |
| R161_073–074 residual upper certificate (3D) | identity (1) M=M_0+E*S⁻¹E and bound (2) are PROVED in R161_074; what remains is to run (3) with a certified α: it is a numerical certificate, not a mechanism | E1 (certificate, not mechanism); outside the pure-math rule except on request |

## 1. Literal statements

**prop:polarcap** (P47 `main.tex:3753`). Under WP_T and the rank condition of thm:parityschur(b) in
sectors with primitive background 0, with S^Sch_T = diag(𝔞_T(h_ev), 𝔞_T(h_odd)) and J = diag(2,−2):
𝔊_T = S^Sch_T + J; for E_T(β,α) := inf{W_T(F): F ∈ 𝒟_T real, Φ_F(0)=β, Φ_F(1)=α} one has
E_T(β,α) = (α,β) 𝔊^{AB}_T (α,β)ᵀ with 𝔊^{AB}_T = ¼[[g_ev+g_odd, g_ev−g_odd],[g_ev−g_odd, g_ev+g_odd]], infimum attained;
λ^W ≥ 0 ⟺ E_T ≥ 0 in ℝ².
Grid residue (l.138): "polar capacity 𝔊_T as a function of T (S^Sch≈−J), never analyzed in T; D3 follow-up of M4 never run".

**I11** (R160_S1 §5, l.464): "96 Thm 2.12: the Euler subspace is Q-positive; its density is ⟺ RH. Angles 1
(absorbing channel twisting Θ) and 3 (symplectic curvature) were left 'not obturated'."

**I14** (R160_S1 §5, l.474): "D_0=−{2} with K−D_0=D_0, χ(D_0)=0 … exists and is explicit (121 cross A); the
self-pairing does not (122). Technical core (a) of 123 §6 (Čech complex of C_p×C_p with tolerance) was never executed."

**Cayley of 69** (phase-69 README l.36): "gauge-invariant quantity behind it (the Cayley/Moebius invariance
w_{1−ρ}=1/w_ρ, …)" — a named quantity with no definition.

**R161_073/074**: S=H+R*R, M=RS⁻¹R*; with approximants U, E=R*−SU, M_0=RU+U*R*−U*SU: M=M_0+E*S⁻¹E,
M_0 ≤ M ≤ M_0+α⁻¹E*E; sufficient certificate for contact exclusion: I−M_0−α⁻¹E*E > 0.

## 2. Corpus check and wall test

* prop:polarcap in T: **R160_M4_R1** already analyzed it through T: L1 (𝔤̃_par nonincreasing, PROVED), A(iii)
  (𝔊_∞ = 0, S^Sch_∞ = −J exactly: this explains rem:polarcapdiag), A(ii) exterior capacity, B(i)–(ii) doubly
  exponential laws, O-1 = E2. **R162_703** (route D3) ran the "D3 follow-up": exact conditions
  PROVED, certificate at ½log5, and structural NO-GO (Type II contact not excludable by minimality of T_*).
  The grid itself records in 1E: "polarcap 156 → 703 (closed)". The entry in 2E and item 59 is an obsolete
  duplicate. Wall: any **sign** statement of 𝔊_T for all T is λ^W_T ≥ 0 ∀T ⟺ RH (Theorem Z /
  thm:parityschur(c)): E1. The only decidable thing without E1 is structure in T (monotonicity/continuity).
* I11, I14, Cayley: objects not constructed, no definable statement → discarded (rule STEP 2).
* R161_073–074: the mathematical part is proved; what remains is numerical and only excludes one contact per
  window (certificate, not mechanism; same wall as R162_303/703: it does not reach ∀T).

## 3. What was chosen: structure of the polar capacity in T

Notation from P47 §parityschur and R160_M4 L1: 𝔤̃_par(T) := inf{W_T(F) : F ∈ 𝒟^par_T, ℓ_par(F)=1} ∈ [−∞,∞),
and Ẽ_T(β,α) := inf{W_T(F): F ∈ 𝒟_T real, B(F)=β, A(F)=α} (without the WP/rank hypothesis).

**Lemma 1 (Loewner monotonicity). PROVED.** For T<T′ and every (β,α), Ẽ_{T′}(β,α) ≤ Ẽ_T(β,α). In particular,
where the hypotheses of prop:polarcap hold at T and T′, 𝔊^{AB}_{T′} ⪯ 𝔊^{AB}_T and 𝔊_{T′} ⪯ 𝔊_T.

*Proof.* Extend F ∈ 𝒟_T by zero to I_{T′}: by the proof of lem:monoT (P47 l.384) the norm, A(F), B(F),
the autocorrelation and 𝔞 do not change (the new contacts have log n ≥ 2T, where the autocorrelation
vanishes), so W_{T′}(F)=W_T(F) and the constraints are preserved. The feasible set grows; the infimum decreases.
Under the hypotheses, Ẽ = E is the quadratic form of 𝔊^{AB}, and a pointwise inequality of quadratic
forms in ℝ² is the Loewner inequality; 𝔊 and 𝔊^{AB} are congruent via a fixed change
(c,s)=((α+β)/2,(α−β)/2), independent of T. ∎

This refines L1(c) of M4 (which gives only the diagonals by parity): since the change is fixed, the
matrix statement is equivalent to the statement for the two diagonals; the novelty is only presentational. Consequence:
S^Sch_T = 𝔊_T − J is Loewner-nonincreasing, and with A(iii) of M4, S^Sch_T ↓ −J **from above** exactly
when 𝔊_T ⪰ 0 for all T, i.e. (E1) under RH. Thus the near-degeneracy S^Sch ≈ −J of
rem:polarcapdiag is monotone.

**Lemma 2 (left continuity). PROVED, modulo the standard fact (D) below.** T ↦ 𝔤̃_par(T) is
left-continuous on (0,∞) (as a function to [−∞,∞)).

*Proof.* By Lemma 1, lim_{T′↑T} 𝔤̃_par(T′) = inf over 𝒰 := ∪_{T′<T} 𝒟^par_{T′} ∩ {ℓ_par=1} ≥ 𝔤̃_par(T).
For the other inequality it suffices that 𝒰 be dense in {F∈𝒟^par_T: ℓ_par(F)=1} in the form norm, since W_T
is continuous in that norm (closed form bounded below, thm:A of P47; the polar term 2ε ℓ² is
continuous in L²). Given F, let F_s(t)=F(t/s), s<1: support in I_{sT}, same parity.
(D) The dilation s ↦ F_s is continuous at s=1 in the form norm: the Lévy part is ∫(1+φ(τ²))|F̂|² with φ
of logarithmic growth (Theorem S of P47), and |F̂_s|² = s²|F̂(sτ)|²; by dominated convergence
(φ(τ²/s²) ≤ φ(τ²)+C for s∈[½,1], Bernstein subadditivity) F_s→F; the contact
terms v_n·(autocorrelation)(log n), log n<2T, are continuous in L². Hence ℓ_par(F_s)→1 and F_s/ℓ_par(F_s) ∈ 𝒰
converges to F. ∎

The same holds for Ẽ_T(β,α) for each (β,α). Right continuity is **not** asserted: at T=½log n
a contact enters and P47 only has it for λ^W via Bombieri Thm 5 (l.398); for 𝔤̃_par it remains OPEN (not
investigated; does not affect sign).

## 4. Battery of falsifiers (logic)

Lemmas 1–2 use only: extension by zero, W as a fixed functional, dilation. They hold for **every**
weight a ≥ 0 (combs of cor:convfail, Λ1_{n≥5}, a_θ), for Ξ_a, Epstein and DH: they do not distinguish ζ from the
falsifiers, as should be the case for a signless statement. In the deletion model both channels cross
zero (rem:polarcapdiag, T≈0.372 and 0.44) — consistent: monotonicity does not prevent crossing, only prevents returning.
No statement in this file carries a sign, so no falsifier can refute it and none is
excluded by it.

## 5. Does it move D?

**No.** Lemmas 1–2 give that {T: 𝔊_T ⪰ 0} = (0, T_W] is a right-closed interval — already known for
λ^W (lem:monoT, lem:contA, Bombieri Thm 5). The ∀T content remains O-1 of M4 (λ^A_T ≥ 0 for T>0.8),
E2. Recommendation for the grid: move "prop:polarcap in T (2E)" from OPEN to "closed by R160_M4 L1/A/B and
R162_703; R184_012 Lemmas 1–2"; I11, I14, Cayley-69 to "no statement"; R161_073–074 to "E1 (certificate)".

## For the audit

1. Is W_{T′}|_{𝒟_T} = W_T literally, including the polar term 2Re(A B̄)? Yes: A,B are integrals against
   cosh/sinh(t/2) of F, invariant under extension by zero (lem:monoT uses this).
2. Lemma 2, (D): verify the bound φ(τ²/s²) ≤ φ(τ²)+C against the exact form of φ in Theorem S (Bernstein with
   φ(x) ~ ½log x); if it fails, Lemma 2 drops to CONDITIONAL.
3. Lemma 1 is not new in substance relative to M4 L1(c); only the matrix form and the reading
   "S^Sch ↓ −J from above ⟺ RH" (E1, not an advance) are claimed.
4. Confirm that grid 1E "polarcap 156 → 703 (closed)" and 2E l.138 contradict each other: this file
   maintains that 2E/item 59 is obsolete.
5. No sign statement; nothing about RH or the closure of D.

## Note (R184_093)

* «S^Sch_T ↓ −J exactly when 𝔊_T ⪰ 0 ∀T» → only «⟸». 𝔊_∞=0 is an identity at T=∞, not a limit. Covers 5 of 11 residues of item 59.
