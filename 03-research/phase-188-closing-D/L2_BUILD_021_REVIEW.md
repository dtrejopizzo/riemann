# L2_BUILD_021 §4 (Proposition 4): review

Pen and paper. Sources checked: phase-159 G2_B1_R5 §3 (Theorem D, Cor D1, Lemma R, eq. (1.2)),
G2_P5_R5 (panel row: PROVED, conditional on record item Q′ of G2_B1_R4), N_BUILD_011 Thm 1 (+ review), L2_BUILD_018 Thm A/B (+ review).

## 1. Same form? YES
G2_B1_R5 states that it works in P46 notation (main.tex l.114–146). A comb is a=(a_n)_{n≥2}, weight v_n=2a_n/√n at u=log n, and the form is
P46 eq:form with the full m (C₀ = ψ(¼) − log π). Theorem D is stated for the **primitive** form 𝔞^{(a)}_T on P_T, i.e. P46's 𝔞_T on P_T. The
statement "hence complete" applies only because the resonators lie in P_T. N_011 and 018 use 𝔞^ν_T = 𝔞_∞ − ∫Re c_F dν on P_T. Under
ν = Σ_n (2a_n/√n)δ_{log n}, this is the same form with the same archimedean term. Normalisation: Λ ↦ density 2e^{u/2}du = ρ_1, so a residue r
corresponds to Chebyshev density κ = r. There is no mismatch of form, window, archimedean term or normalisation.

## 2. Is the support hypothesis real and used? YES (it is built into the definition). This is the right resolution, with a sharper reason.
- Hypothesis: "comb" in G2_B1_R5 means an integer-indexed sequence, so support in log ℕ is built into the definition. It is not an extra clause.
- Use: Lemma R makes the comb part of 𝔞(F_b) exactly the multiplicative Toeplitz form b^⊤𝕄_a b. This works because every peak of c_{F_b},
  located at log(m/k), hits an atom exactly when k|m, with c_ψ(0)=‖ψ‖²>0. Width ε = 1/(8M) is allowed because distinct log(m/k), m,k ≤ M,
  are ≥ ~1/M apart. The archimedean gain is therefore log(1/ε) ≈ log M. The comb gain with b_m = m^{−½} is G_M ≈ r log M (Karamata). Comparing the two gives r ≤ 1.
- Why κ>1 combs escape (sharper than 021's wording): the obstruction is **resolution versus density**, not "rationals". The proof can be imitated
  on a comb with continuous density ρ_κ. There the comb part of a resonator is ∫2κe^{u/2}c_F = −κ𝔭(F) on P_T (N_001 (A)). This does not grow
  with M, so no bound on κ follows. The proof can also be imitated on the lattice comb of 018 (spacing h_j, bumps at lattice points). The admissible width is then
  ε ≲ h. The archimedean gain log(1/h) ≳ 30κe^{j+1} (H2) far exceeds the comb gain ≈ 2κ·2T at window T, so again no bound follows. On log ℕ the
  minimal gap of the difference set at window ½log M is 1/M ≈ e^{−2T}. That gap makes the archimedean gain only log M, which is commensurate with the
  density gain. **Theorem D is the statement that log ℕ is too coarse to buy density.** Replace 021's parenthetical ("autocorrelation lives on
  log of rationals") with this. 
- Verdict on Q(1): there is NO contradiction, and the resolution in §4 is CORRECT.

## 3. Proposition 4: CONFIRMED as a statement about the support. Its reading is OVERSTATED.
- PROVED part: let a ≥ 0 be supported on log ℕ and ∀T-positive. Then r ≤ 1 < 1.343 ≤ κ* by Cor D1 and N_011 Thm 1. So its Chebyshev main term ρ_r
  is not in Pos, i.e. g_r(0) = C₀ + 4r < 0. Λ has r = 1 and saturates. The label is PROVED **conditional on record item Q′** (G2_B1_R4), as
  the G2_P5_R5 panel recorded. 021 must carry that condition. Karamata is CITED. The case with no pole (r = 0) is trivial.
- Stronger true form: Cor D1 does not concern a "density mechanism". It is a necessary condition. **No** nonnegative log ℕ comb with r > 1
  is in Pos by any mechanism. Prefer this formulation.
- OVERSTATED: the clause "positive only through P_T-correlation" is not defined and not proved for atomic combs. The "density mechanism" is
  defined (N_011) only for ρ_κ, i.e. pointwise symbol positivity. Relabel the clause HEURISTIC, as was done for 018 (b)–(c). The statement that
  the symbol of ρ_1 is negative near τ = 0 is PROVED. The statement that the integer test-function structure "is destructive" means only Theorem D. Keep that meaning.
- "Consistency check" paragraph: it is correct, but it is not "my reading" anymore. It is confirmed here.

## 4. Are any of the three results wrong? NO.
- Theorem D / Cor D1: I re-derived G_M ≥ (2/H(M))∫_1^M S dx/x ≈ r log M and the bound (i) Σ_{n≤√M} ≤ log M + O(1). Both are correct. Dependencies: Lemma
  R / eq. (1.2) (panel-checked) and Q′ (record, panel-verified R4).
- N_011 Thm 1: correct (κ* ≥ |C₀|/4 from τ = 0).
- L2_018 Thm A/B: correct with the two cosmetic FIXes of its review. Its h_j are doubly exponentially small, which is consistent with §2 above.

## Verdict
§4 / Prop 4: CONFIRMED (PROVED, conditional on Q′). There is no contradiction. The support hypothesis is genuine and load-bearing, through
resolution. FIX the wording of the "rationals" reason. DOWNGRADE "positive only through P_T-correlation" to HEURISTIC. No sign contact.
