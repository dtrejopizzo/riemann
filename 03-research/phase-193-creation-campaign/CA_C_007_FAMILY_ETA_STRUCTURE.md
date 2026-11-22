# CA_C_007 — The η-family: corrected numerics, zeros against Poisson, a one-scalar reduction, and ζ-specificity

Phase 193, round 9 (coordinator: make E6 the main task). Pen and paper plus NUMÉRICO runs, all positive for ζ.
Scripts in 03-research/phase-190-near-coincidence-experiment/scripts/: mu_family_gram.py, mu_combs_gram.py, family_split.py,
family_schur.py, mu_beurling.py. They use phase-190's profile.py and am.py (F₀ with b = 1, T₀ = 0.3) and are floating point, not certified.
**No sign contact with D. No negative value for ζ.** The negative values below are for *modified* combs or lattices.

## 0. Correction of the premise
The coordinator's premise ("on η > 2/3 the bottom is CRITICAL") came from CA_C_005, which used the wrong norm (retraction there). In the
norm of the test function ‖F_s‖² = sᵀGs, G_{mk} = c₀(log m/k), the family infimum ν_M(η) := min sᵀA_Ms / sᵀGs is (NUMÉRICO; insensitive to a
ridge of 1e−8 to 1e−11):

| M | full A_M | η = 0.4 | η = 0.7 | η = 0.9 |
|---|---|---|---|---|
| 200 | 1.28e−6 | 1.76e−6 | 2.16e−4 | 3.44e−2 |
| 400 | 1.38e−7 | 2.74e−7 | 3.62e−4 | 5.85e−2 |
| 800 | 1.16e−8 | 3.48e−8 | 6.08e−4 | 9.20e−2 |

The full form is critical (≍ M^{−3.3}; it agrees with the ℓ² value within a factor of 2, so EXP_002/003 stand). η = 0.4 is critical (it
contains the minimizer, SPEC_B §1.4(i)). **η ≥ 0.7 is a margin regime, increasing in M.** So on the prime-free family the bottom is *not*
critical, and alternatives (A)/(B) must be posed differently: why is the family critical at η ≈ 0.4 and not at η > 2/3?

## 1. (A): the criticality is a zero-side phenomenon (identity PROVED; explanation ARGUED)
For s in the family, F_s = Σ s_m V_{log m}F₀ ∈ P_{T'} (P46 lem:transl(i)), and F̂_s = F̂₀·ζ_{w,M}(½ + i·). The Weil explicit formula on
P_{T'} (polar terms vanish; P46 thm:Z) gives the exact zero-side form Q_M(w) = Σ_ρ F̂₀(t_ρ)²ζ_{w,M}(ρ)ζ_{w,M}(1−ρ̄)‾ with ρ = ½ + it_ρ, and
ζ(ρ) = 0 gives ζ_{w,M}(ρ) = M^{1−ρ}𝒲(1−ρ) + r_M(ρ) (EI_002 Mellin split). A value ≍ M^{−3}·‖F‖² requires near-annihilation at every
ordinate where F̂₀(t)² is not negligible, i.e. 𝒲(½ − it_ρ) ≈ −M^{ρ−1}r_M(ρ) at ≍ many zeros. That needs a cutoff with free shape over a long
log-range. On 𝒲_η the shape is free only on [η, 1], of log-length log(1/η) (0.92 at η = 0.4; ≤ 0.41 at η > 2/3). **So criticality is
produced by the zeros, as in (A), and it disappears exactly when the cutoff loses the freedom to annihilate them.** Label: ARGUED (the
identity is PROVED; "the number of zeros annihilable grows with log(1/η)" is a heuristic consistent with the table and with EXP_005 R4).
Consequence: there is no prime-side mechanism for the critical part. What is left on η > 2/3 is a margin statement, and that is where (B)
can live.

## 2. A one-scalar reduction of the η-family, η > e^{2T₀}/3 (PROVED)
Write s = c·u + t, with u := (m^{−½}1_{m≤ηM}) and t supported on (ηM, M].
**Lemma 1 (tail is a small window).** The tail block A_t := A_M|_{(ηM,M]} is the window form on the span of translates V_{log j}F₀,
j ∈ (ηM, M]. These functions lie in P_{T_eff}, T_eff := T₀ + ½log(1/η), after centring (lem:transl(i)). If η > e^{2T₀}/3 then
2T_eff < log 3, so the only contact is n = 2, and WP_{T_eff} holds (P46: WP_T for T ≤ ½log 5, cor:beyond5/Thm C). Hence A_t ⪰ λ_A(T_eff)·G_t
with λ_A(T_eff) > 0.
**Lemma 2 (only Λ(2) and log N).** Every entry of the family form (Q(u), b := A_M u restricted to the tail, A_t) involves the comb only
through the following, so the whole object is explicit in Γ_ℝ, ℤ-lattice sums and log 2:
- Σ_{d|N}Λ(d) = log N (the product formula, CA_C_001 Lemma 1), for every N ≤ ηM and on the tail range with all divisors d ≥ 2 allowed;
- Λ(2), through the divisor defect n < N/(ηM) < e^{2T₀}/η < 3, and through the tail contacts.
*Proof.* As in P46 prop:shape-family(i), regrouping N = nm; in b, N ranges over (ηM, Me^{2T₀}) and the excluded divisors satisfy
n < N/(ηM) < e^{2T₀}/η. ∎
**Proposition 3.** On the family, positivity ⟺ the scalar Schur complement s_M := Q(u) − bᵀA_t^{−1}b ≥ 0 (A_t ≻ 0 by Lemma 1).
*Proof.* Minimize over t for fixed c. ∎
So T*₃(η > e^{2T₀}/3) is **one explicit scalar inequality per M**, in Γ_ℝ, log N and log 2.

## 3. Numerics of the reduction and the falsifier test (NUMÉRICO)
| lattice/comb | M | Q(u)/M | s_M | s_M/Q(u) | family ν_M(0.9) |
|---|---|---|---|---|---|
| ℤ, Λ | 200 / 400 / 800 | 0.0029 / 0.0029 / 0.0029 | 0.083 / 0.162 / 0.320 | 0.143 / 0.140 / 0.138 | 0.034 / 0.058 / 0.092 |
| Beurling, jitter 0.02 (exact PF in its semigroup) | 200 / 400 / 800 | −0.0004 / 0.0005 / 0.0023 | −1.25 / −1.24 / −1.73 | — | −0.45 / −0.41 / — |
| Beurling, 3 → 3.1 | 200 / 400 | | | | −0.38 / −0.36 |

ℤ: s_M ≈ 0.14·Q(u) ≈ 4·10⁻⁴·M, so the family is positive with a margin linear in M. Beurling: the bulk Q(u) and the tail (Gram-min ≈ 0.70,
the same as ℤ's 0.71) are each positive at M = 800, but the **bulk–tail coupling b** makes s_M negative.

On ℤ, with modified combs (ν_M at η = 0.7 / 0.9, M = 400):
- negative for the upward perturbations v₂×1.1 (−0.039 / +0.024), v₂×3 (−0.80 / −0.64), v₃×2 (−0.35 / −0.23), v₅×3 (−0.007 / +0.053);
- positive for the downward ones v₂×0, v₃×0, v₄×0, v₅×0 (all ≥ 0.004, up to 0.40), although the full forms of all of these are negative.

## 4. Verdict (honest labels)
- **(A) vs (B):** both hold, in different regimes. The critical bottom (η ≲ 0.4, full A_M) is zero-side (§1; identity PROVED, explanation
  ARGUED): no prime-side mechanism. The η > 2/3 family is a margin statement, reduced exactly to one scalar s_M (§2, PROVED) in Γ_ℝ, ℤ-lattice
  sums and log 2.
- **ζ-specificity (NUMÉRICO, bounded M):** s_M > 0 for ℤ, while s_M < 0 for Beurling systems that satisfy the product formula exactly in their
  semigroup. The difference sits in the bulk–tail coupling b, i.e. in the ℤ-lattice (Poisson-on-ℤ) sums, as in (B). Upward weight
  perturbations also fail; downward ones and deletions pass. So the statement is one-sided in the weights, matching the class (≤, ≤) of
  CA_C_001, which contains a_P.
- **Caveat:** for jitter, Q(u)/M drifts toward ℤ's 0.0029 as M grows (−0.0004 → 0.0023). If the linear coefficient κ of s_M is a
  density-level constant, common to all density-1 systems, then for large M the Beurling s_M also turns positive. The separation would then
  live only in the O(1) term, and the family theorem would be a density (class) statement for large M. **This is the decisive open point.**
  It needs larger M (NUMÉRICO, strictly necessary) or the hand computation of κ.
- **Hand route (OPEN, not blocked by B′ because it is a margin):** prove s_M = κM + O(1) with an explicit κ > 0, using Euler–Maclaurin /
  Poisson on ℤ for Q(u) and b (EI_002 Mellin split, CA_C_003(a) bulk vanishing) and the continuum limit of A_t (translates over a
  log-interval of length log(1/η)). Then check finitely many M. The result would be a **necessary-condition positivity theorem on the
  η-family**, explicit in Γ_ℝ, ℤ and log 2. It is not D: the family misses the critical minimizer, and the class is closed under deletions.
  Whether it is ζ-specific at large M is the caveat above.
- **Self-review:**
  1. The ridge-insensitivity and the agreement of the full-space values with EXP_002/003 support the Gram numerics. The jitter tail block is
     ill-conditioned (ℓ²-min 1e−10), so the Beurling s_M via A_t^{−1} is less reliable than the ν_M column, but both are negative.
  2. Lemma 1 uses WP_{T_eff} from P46 at T_eff = 0.353 (PROVED range).
  3. No negative value for ζ; no sign contact with D.

## 5. FE-class falsifier test (after CA_D_001/003): the family positivity is FE-generic, not ζ-specific (NUMÉRICO)
Script family_epstein.py. The archimedean symbol is that of (√|D|/2π)^sΓ(s), m_Q = 2Re ψ(½ + iτ) + 2log(√|D|/2π). The comb is
v_n = 2Λ_f(n)/√n from −f′/f with f = Z_Q/r(1) (signed weights). The family span is c·a(m)m^{−½} on m ≤ ηM plus a free tail. Gram norm.

| object | M | full form | family η = 0.9 | family η = 0.7 |
|---|---|---|---|---|
| x² + y² (= 4ζ_{ℚ(i)}: FE + Euler, O12) | 200 / 400 / 800 | 4.7e−4 / 5.8e−5 / 5.0e−6 | 0.116 / 0.194 / 0.349 | — |
| x² + 5y² (h = 2: FE, no Euler, O10) | 200 / 400 / 800 | **−4.5 / −8.8 / −12.4** | **0.282 / 0.209 / 0.433** | 0.189 / 0.060 |

The Epstein function of class number 2 is a falsifier of the full form (negative, growing), yet it is **positive on the η-family**. ζ_{ℚ(i)}
behaves like ζ: the full form is critical (≍ M^{−3.3}) and the family has a margin. Combined with §3: the family fails for systems without FE
(Beurling, weight perturbations up) and holds for every FE object tested.
**Conclusion.** Alternative (B) is correct in its first half: the margin on the η > 2/3 family comes from the functional equation (theta
inversion / Γ-factor matched to the lattice of the Dirichlet series). It is wrong in its second half: the statement is **FE-class generic, not
ζ-specific**. It survives O10 and O12, as CA_D_001's Theorem 1″ does, by a different mechanism: the amplitude here is one, so that transfer
does not apply (CA_D_003). By thm:shape(C), positivity on the η-family cannot be the sign step of row D. It is a necessary-condition fact shared
by the FE class.
On the coordinator's central-cell question (CA_D_003 split): in the correct norm there is no M^{−3} cancellation on the η > 2/3 family to
explain. The near-critical values came from the ℓ² artifact. Cancellation at critical precision occurs only on the full span / η ≲ 0.4. There
the comb, polar and ρ_M terms at bounded height must annihilate the zero contributions (§1, (A)). This is zero-side, and it fails for x² + 5y²
(whose full form is negative), which is consistent.

## 6. Final verdict of E6
- The criticality premise was an ℓ²-normalization artifact (CA_C_005 retracted). True values: η ≥ 0.7 has a margin; η ≲ 0.4 and the full span
  are critical.
- Critical regime: zero-side (A). The identity is PROVED; the mechanism (annihilation of ζ_w at ≍ many zeros, which needs a long free cutoff) is
  ARGUED. No prime-side mechanism.
- Margin regime η > e^{2T₀}/3: exact one-scalar reduction s_M (PROVED). Its positivity is FE-generic (NUMÉRICO: Epstein h = 2 and ζ_{ℚ(i)}
  positive, Beurling negative), so it is excluded as a sign step by O10 (thm:shape(C)). Not a route to D. Recorded as a tool: "η-family
  positivity: FE-class generic, Beurling-separating".
- Span versus smooth family: the Gram minima are over the span, which contains the smooth family, so positivity on the span implies positivity
  on the family.
- **Sign contact: none. No negative value for ζ.** The negative values are for x² + 5y², Beurling and perturbed combs.
