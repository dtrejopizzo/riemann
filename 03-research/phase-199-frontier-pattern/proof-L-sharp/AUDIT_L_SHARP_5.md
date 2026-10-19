# AUDIT_L_SHARP_5 — audit of PROOF_L_SHARP_T_001 (Fourier sectors) and TEST_CG_001 (gauge test)

Phase 199. Pen-and-paper audit; no numerics re-run (scripts read, not executed).
OPEN / NO-GO / NUMÉRICO. Sources checked: AUDIT_L_SHARP_4 §6–§8, A_001 Thm 1.1 / Prop 2.1 / Rem 2.2, P_001 (P.1), S_001,
Paper 47 thm:A (Lévy representation, K(u)), Guo Lemma 4.4 (as quoted and read in A_001).

## 1. T Lemma 1.1 (intertwining) — PROVED, constants confirmed
Poisson for even f, u = e^x: f(0) + 2Σ_{n≥1}f(nu) = u^{−1}(f̂(0) + 2Σ_{n≥1}f̂(n/u)). Multiply by u^{1/2}/2:
  Φ_f(x) + ½f(0)e^{x/2} = Φ_{f̂}(−x) + ½f̂(0)e^{−x/2},
hence Φ_{f̂}(x) = Φ_f(−x) + ½f(0)e^{−x/2} − ½f̂(0)e^{x/2}. With f(0) = 0, f̂(0) = 2ρ₀: Φ_c(y) = Φ_ρ(−y) − ρ₀e^{y/2}. ✓ (same
convention f̂(ξ) = ∫f e^{−2πixξ} as AUDIT_4 (P)). Rank-two polar correction exact. **Classical:** this is the co-Poisson /
Poisson intertwining of the summation map with the Fourier transform (Burnol's co-Poisson identity; Connes' map E). Label
PROVED, attribution CITED-classical; not new.

## 2. Sector formula (T Thm 3.1, Cor 3.2)
**Re-derivation.** With the sign convention of A_001 §1 (pole +, primes −, archimedean off-diagonal −, consistent with
Paper 47 thm:A, where the form is C₀‖F‖² + Lév(𝒞) − Σv_n𝒞(log n), i.e. the Lévy kernel enters with −Re Φ(u)K(u)):
- Lemma 1.1 on f ∈ 𝒮, f̂ = εf: Φ_f(−x) = εΦ_f(x); so Φ_f = Ψ + εRΨ, Ψ = Φ_f|_{(0,∞)}. ✓ (no support claim; Φ_f is not
  supported on a half-line, its negative half is the mirror.)
- Cross form 𝒲(Ψ,RΨ) for disjoint supports: Lévy −∫∫Ψ(x)Ψ(x′)ν(x+x′) ✓; primes: (RΨ)(x−log q) = Ψ(log q − x), the other
  translate vanishes for x > 0 ✓ ⇒ −𝒫; pole: ∫Ψe^{x/2}·∫RΨe^{−x/2} + ∫Ψe^{−x/2}·∫RΨe^{x/2} = A² + B² ✓.
  So 𝒲(Ψ,RΨ) = −𝒲_refl[Ψ], and radical ⇒ 𝒲_{(0,∞)}[Ψ] = −ε𝒲(Ψ,RΨ) = ε𝒲_refl[Ψ]. ✓
- ν(t) = e^{−t/2}/(1−e^{−2t}) = Σ_{j≥0}e^{−(2j+½)t}: geometric series, each term completely monotone, so ν is CM ✓ (it is the
  Γ_ℝ off-diagonal kernel: e^{−|u|/2}/(1−e^{−2|u|}), the standard Weil archimedean kernel; matches the "Σ_j e^{−(2j+½)|u|}"
  structure of K in Paper 47 up to the 1/u-type diagonal part, which does not enter a cross term of disjoint supports).
- Tonelli (positive kernel, |Ψ|) gives ∫∫ΨΨν(x+x′) = Σ_{j≥0}L_j², L_0 = ∫Ψe^{−x/2} = B ✓; −B² cancels the j = 0 square
  exactly ✓. Σ_jL_j² < ∞ since L_j = O(1/j) for bounded Ψ near 0.
- 𝒫 sign/normalisation: c_q = Λ(q)q^{−1/2} as in A_001 §1 ✓; 𝒫 enters 𝒲_refl with +, the self-convolution
  (Ψ∗Ψ)(log q) = ∫_0^{log q}Ψ(x)Ψ(log q−x)dx ✓. Mellin dictionary L_j = H(−2j), A = H(1) ✓ (H of the half-line piece).
**Status: Thm 3.1/Cor 3.2 PROVED as algebra, CONDITIONAL on (H1) Lemma 1.2 on 𝒮 and (H2) existence of a rich subclass of 𝒮
with the decay needed for absolute convergence.**

**Hypotheses, precisely.**
- (H1) Radical lemma WΦ_f = 0: CITED (Guo Lemma 4.4, A_001 Thm 1.1(b)) only for the compact class of A_001/Guo. Extension to
  Schwartz-decay f with f(0) = f̂(0) = 0: ARGUED (Mellin H_Φ = ζ·M_f entire with poles killed; explicit formula for
  Schwartz-class tests by approximation). Plausible; it is the classical "range of E lies in the radical" statement
  (Connes; Connes–Consani 2006.13771 work with the Sonin space precisely in this setting). Upgrade requires a line-by-line
  cut-off argument; until then CONDITIONAL.
- (H2) 𝒮 ∩ L² infinite-dimensional: CITED (Landau–Pollak; this is the de Branges–Sonin space, used by Connes–Consani).
  Schwartz-richness of 𝒮: CONDITIONAL (not proved in the memo; not refuted by any uncertainty principle known to the audit).
- **Is the formula vacuous for the target?** Not vacuous (𝒮 ≠ {0}), but **disjoint from the declared carrier**: 𝒮 ∩ C_c = {0},
  and the data of A_001 Thm 1.1 / L′♯ are compactly supported f (f(λ) = 0) whose exterior piece is the aliasing of
  out-of-band data. No 𝒮 vector is the f of any window datum. Hence Thm 3.1 is a true statement about the one-sided form
  𝒲_{(0,∞)} on unbounded-support data, with **zero direct content for W_T on the window** until a transfer theorem exists.
  This is the 𝒮-vs-PW transfer gap (constraint 16 below).

**Classical or new?** Every ingredient is classical: Poisson/co-Poisson (Burnol), radical of the Weil form on E-images
(Connes, Connes–Consani), Γ_ℝ kernel as a geometric series (Weil). The rewriting "on a Fourier eigen-sector the one-sided
Weil form equals ±(Σ_{j≥1}L_j² + 𝒫 − A²)" is an elementary corollary of Weil's explicit formula applied to the
E-image of a Fourier-self-dual Sonin-space function. The audit found no reference stating it in this form, but it must not be
presented as a new theorem of substance: label **PROVED-conditional, classical corollary (restatement)**. Note: the
sign burden is moved to 𝒫 vs A², i.e. it is not reduced.

## 3. The "falsifier prediction" on 𝒮_− ∩ {A = 0}
- Logic ✓: if 𝒲_{(0,∞)}[Ψ] ≥ 0 and ε = −1, then ΣL_j² + 𝒫 − A² ≤ 0; with A = 0, 𝒫 ≤ −Σ_{j≥1}L_j² < 0 (strict unless Ψ = 0,
  since L_j = 0 ∀j ≥ 1 forces Ψ = 0 by Müntz, Σ1/(2j) = ∞). A = 0 is one linear condition, so the class is non-empty if
  𝒮_− is (H2).
- **What it tests:** positivity of 𝒲_{(0,∞)} on unbounded-support data. That is NOT the declared carrier (W_T on a window
  of length T); a failure would not falsify row D at any fixed T without the transfer theorem. Re-label: "consequence of
  half-line positivity", not "falsifier of row D".
- **Consistency with known results.** No contradiction found. Connes–Consani 2006.13771 control the archimedean part on
  Sonin-type data; here the archimedean part is already a manifest SOS (Cor 3.2) and the prediction concerns 𝒫, which CC
  do not control. The explicit formula only reproduces Thm 3.1. The audit has NOT verified the exact statement of CC's
  positivity theorem line by line (CITED-unchecked).
- **Decidable by hand?** No. Elements of 𝒮_− are not explicit: they cannot have compact support (𝒮 ∩ C_c = {0}), and Hermite
  combinations are Fourier eigenfunctions but never vanish identically on (−1,1) in any finite combination (real-analytic).
  An infinite Hermite/prolate expansion is needed (CC construct Sonin vectors via prolate functions). 𝔔 is defined there
  only under (H1)+(H2) decay. A test is possible only numerically (prolate basis of the Sonin space, extended precision):
  **OPEN / NUMÉRICO-not-run**. Recommendation: do not build on the prediction before the transfer gap is addressed.

## 4. Prop 3.3 (sector orthogonality) — PROVED given (H1)
𝒮 = 𝒮_+ ⊕ 𝒮_− (f ↦ (f ± f̂)/2 preserves 𝒮) ✓. Radical on Φ_{f−} = Ψ_− − RΨ_−: 𝒲(Ψ_+,Ψ_−) = 𝒲(Ψ_+,RΨ_−) =: X. Radical
on Φ_{f+}: 𝒲(Ψ_−,Ψ_+) = −𝒲(Ψ_−,RΨ_+). R-invariance of 𝒲 (pole term symmetric under A ↔ B; Lévy and prime kernels even)
✓ ⇒ 𝒲(Ψ_−,RΨ_+) = X. So X = −X = 0 ✓. Caveat in memo (radical quotient respects the split only if the radical is 𝔉-stable)
correctly marked OPEN.
- Prop 2.1 of T (D formula): algebraic consequence of AUDIT_4 Theorem (S-dual) — PROVED for C_c^∞(1,∞) ✓. Its "constraint
  identity on 𝒮_±" uses F, G, 𝔅 defined for C_c^∞ data and is evaluated on 𝒮 where no C_c^∞ datum exists: CONDITIONAL, and
  doubly so (needs the PW-tail extension of AUDIT_4 AND a non-PW (Sonin) extension). Downgrade the note "PW-tail extension"
  to "extension to non-compact Sonin data".
- §4 (4-sector decomposition NO-GO): ARGUED, accepted as ARGUED (not a NO-GO theorem; relabel "not defined as posed").

## 5. TEST_CG_001
- Scripts read (forms/analysis/radical_vector); not re-executed. Internal minor inconsistencies: one-line verdict quotes
  μ = 8: 0.74, μ = 10: 0.61 (cutoff 1e−13, §2) while §3 table gives 0.733/0.573 (cutoff 1e−11); harmless, flag for edit.
- **Radical vector with Q(G,G) = +0.095‖ρ‖²:** g supported in [−1,1] ⊂ PW_μ, ĝ(0) ≈ 3e−18, 𝔔 ≈ 1e−9 (radical) and
  2Q(F,G)+2AB equal to Q(G,G) (forced: 𝔔 = −Q(G,G) + S = 0) — internally consistent. NUMÉRICO (not reproduced by audit).
  Given one radical r with Q(G,G)(r) > 0, inf_λ[−Q(G,G)](ρ + λr) = −∞ is PROVED (quadratic in λ with negative leading
  coefficient). So "−Q(G,G) is not radical-invariant and unbounded below on radical cosets" is **PROVED modulo one NUMÉRICO
  value** (could be made rigorous by interval arithmetic on 8 coefficients — cheap, recommended).
- **θ → 1 as an L²-gauge artefact:** ARGUED. Data show θ_J increasing for J ≥ 4 but at μ = 10 only 0.573 at J = 19, no
  saturation reached; the mechanism (−Q(G,G) not L²-bounded on the radical span, top eigenvalue ≈ linear in J) is
  plausible and numerically supported, but θ_∞ = 1 is an extrapolation. Label: NUMÉRICO trend + ARGUED limit.
- **"No gauge-free form of (C_G) exists":** ARGUED, not PROVED. What is proved is narrower: (C_G) cannot be stated with
  −Q(G,G) evaluated on an arbitrary radical representative (unbounded below on cosets). Other gauge-free formulations
  (sup/inf over coset representatives of a ratio, Q(G,G) restricted to the pole complement, a quotient by a positive
  radical-invariant form) are not excluded — the memo itself lists two such repairs. Relabel: "no gauge-free version of
  (C_G) in the coset-evaluation sense: PROVED mod NUMÉRICO; in general: ARGUED".
- (C_G)(a) in the L² gauge: "NO-GO candidate" accepted; not a NO-GO (no proof of unboundedness of θ). (C_G)(b): OPEN.

## 6. Verdict and consolidated statement
- T_001: Lemma 1.1 PROVED (classical); Thm 3.1/Cor 3.2/Prop 3.3 PROVED given (H1)+(H2), a classical-corollary restatement;
  the prediction is a consequence of half-line positivity on non-carrier data, OPEN, not decidable by hand. No sign.
- TEST_CG_001: conclusions accepted with the relabels of §5.
- **(★★) unchanged** = L′♯ OPEN. Constraints 1–15 stand. Added:
  - **16. Self-dual sector formula and the 𝒮-vs-PW transfer gap.** On the Sonin class 𝒮 (f = f̂·ε = 0 on (−1,1)) the
    one-sided form is ε(Σ_{j≥1}L_j² + 𝒫 − A²) (archimedean part SOS, B² absorbed); the sign burden is 𝒫 vs A². But
    𝒮 ∩ C_c = {0}: no window datum lies in 𝒮. Any use of the sector formula for (★★) must first supply a transfer
    (projection/approximation of compact-support aliasing data by 𝒮-data with controlled error in 𝒲_{(0,∞)}); without it
    the formula has no content for W_T.
  - **17. Gauge.** Q(G,G) is unbounded below on radical cosets (explicit vector); every split argument must fix a
    radical-invariant or G-adapted gauge before comparing forms.
- **Do not retry:** sector formula as a sign source without controlling 𝒫 and without a transfer theorem; testing the
  𝒮_− prediction as a falsifier of row D; (C_G) with L² gauge.

| item | memo | audit |
|---|---|---|
| T Lemma 1.1 | PROVED | PROVED (classical, co-Poisson) |
| T Thm 3.1, Cor 3.2 | PROVED given L1.2 | PROVED given (H1)+(H2); classical corollary |
| T Prop 3.3 | PROVED given L1.2 | PROVED given (H1) |
| T Prop 2.1 / constraint identity | PROVED / CONDITIONAL | PROVED (C_c^∞) / CONDITIONAL (Sonin extension, not just PW) |
| 𝒮_− prediction | untested | OPEN; not a row-D falsifier; not hand-decidable |
| TEST_CG Q(G,G)>0 on radical | NUMÉRICO | NUMÉRICO; coset unboundedness PROVED mod it |
| θ → 1 | NUMÉRICO+ARGUED | same |
| "no gauge-free (C_G)" | stated | ARGUED (narrow version PROVED mod NUMÉRICO) |
| (★★), L′♯ | OPEN | OPEN |

No sign is claimed. (★★) OPEN. Row D OPEN.
