# R129.004 — auditor report, round 2

Target: Paper 43 after R129.003.

## Headline
Round 2 is an honest improvement.  New mathematics verified: Lemma 3.3 (valuation
splitting `φ=∏_p p^{v_p}`, `A_S^× = Γ_S × ker φ`, `C_S ≅ R^× × ∏Z_p^×`) is a TRUE
theorem; formula (8A.12) is a CORRECT computation (recomputed from P123.042), so chart
invariance of `T` under the splitting-defined maps is genuinely false.  But three of
round 2's negative claims fail:
- (8A.12) silently assumes the identity constant `c` is chart-independent (G1); the
  correct formula carries `+(c_T−c_S)F(1)`.
- **The (O-A6-1) impossibility claim is FALSE (G2).**  P123.017 §§1–4 (PROVED-IN-REPOSITORY)
  constructs the hyperbolic ruling plane with no zero, no `Λ(n)`, no explicit formula, via
  the vector-valued pairing `I_vec=(I_∂, I_Tate)`, radical `R_W = R_∂ ∩ ker M`, and the exact
  sequence `0 → D^0/R_W → D/R_W → B_T → 0`.  Every input transfers to `D_A` with
  `M=(λ_−,λ_+)`, and Paper 43 already proves them (Thm 9.1, 9.3, 9.4).  Moreover
  **Theorem 9.5 already supplies a nonzero primitive class**: it proves `λ_∓(F)=λ_∓(F')`
  and `T(F−F')≠0`, so `F−F' ∈ ker λ_± \ 𝓝`.
- The "Haar-null support" argument (9.6) is not an argument (G3): `𝓝 = {F : F̂ = 0 on
  supp T̂}`, and `c·δ_1` is carried by a point yet has full Fourier support.  The right
  formulation of (O-A6-1) is `F̂|_{supp T̂}=0 ⟹ F̂(±1/2)=0`, and the sharpest open question
  is **(T5′): is `𝓝 = 0`, i.e. is `supp T̂` all of the dual?** — a computation with the
  explicit local distributions, A.10-clean.

## Other findings
G4 the "P123.018 counterexample does not apply" paragraph is a non sequitur (extension-by-one
stays refuted; `π_{TS}` is a different, splitting-defined map, supported by P123.042 §4 and
P123.046 §4).  G5 F14 NOT fixed: the `†`-stability chain in Thm 9.4 is circular; correct
one-liner `⟨K^†,L⟩ = conj(⟨K,L^†⟩) = 0`.  G6 §14.1 restates `T=Σ_v W_v` without `+c·F(1)`.
G7 wrong cross-reference (8A.12)→(8A.13).  G8 P123.035 §5 over-cited.  G9 type friction
Def 3.1 / Rem 3.5; define `𝓝 ⊆ D_A`.  G10 (O-A8-4) is failure of one approach, not
impossibility: conductor-graded seminorms (main.md (2.2)) dominate the logarithmic
divergence `I_L=L+1` and were not tried.  G11 P123.014 §7's gate asks for a *faithful*
lift; injectivity of `F↦E_F` not shown.

## F1–F19 implementation: 15 correct, F1/F2 partial, F14/F15 wrong.

## Clause table
A.1 PARTIAL · A.2 PARTIAL · A.3 PROVED on G (no unit on `Corr_A^tr`) · A.4 PROVED on G ·
A.5 PARTIAL · **A.6 OPEN, NOT blocked** · A.7 PARTIAL · A.8 OPEN · A.9 PASSED for the
formalism · A.10 PROVED.

## Route to the label
**Spec is not inconsistent.**  A.6: (T1) `𝓝_W = 𝓝 ∩ ker λ_±` closed †-ideal [available];
(T2) exact sequence with `B_T=[[0,1],[1,0]]` [available]; (T3) primitive sector nonzero
[Thm 9.5]; (T4) "contains" vs quotient — prove a canonical splitting or adopt P123.017 §4's
reading — the real small open item; (T5) justify `𝓝_W` vs `𝓝`, or prove **(T5′) `𝓝=0`**;
(T6) (O-A6-2) boundary radical.  A.5: chart-independence of `c`; conductor-graded trace-class
topology; `E_F ≅ E_G ⟹ F=G`.  **A.8 is the binding constraint**: (O-A8-1) `Φ_det` of
P123.007 §8; (O-A8-2) geometric origin of the P123.108/110 anomaly.  No shortcut seen.
