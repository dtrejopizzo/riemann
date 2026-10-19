# PROOF_L_SHARP_EE_001 — Strategy EE: variational characterization in the exterior; the rough correction as one object

Phase 199, prover (pen and paper; NUMÉRICO only on existing EXTERIOR_DATUM_001 data, no new runs).
Sources: AUDIT_L_SHARP_13/14 (constraints 1–26, esp. 3 and 25), EXTERIOR_DATUM_001 (Lemma E.1, Prop C′.1, Cor C′.2) + AUDIT_12,
A_001 (Thm 1.1, Prop 2.1), U_001 (U.2), F_001 (Prop F.0), Z_001 + CC_001 (Theorem C), Y_001 (Theorem B′), BB_001, ROUGH_COMPLEMENT_001,
AA_001 + GRAM_INERTIA_001, data `EXTERIOR_DATUM_001_data/analysis.json`.

**Outcome in one line.** (i) The Euler–Lagrange system of the ratio problem is written (PROVED on every finite Galerkin space;
attainment in the full class CONDITIONAL); κ(μ) is the bottom of a Λ-free compressed pencil. (ii) The proposed coercivity of 𝒦 on the
complement of the prolate tails **via Theorem B′ is NO-GO as posed**: by Lemma E.1 the complement content of admissible data (Δr_out)
consists of exact dilates of the edge line carried by ρ_pro, i.e. it is *resonant by construction*, outside B′'s hypothesis; moreover
Δr_out is not a free variable but a fixed linear image of the edge datum. (iii) On p's own split the 2×2 bracket holds numerically,
C²/(AB) = 0.324 < 1 (NUMÉRICO), but no uniform (a, b, c) exists to prove: the off-diagonal is an exact coherence (Cauchy–Schwarz is
sharp on it) and b has no uniform floor on the cancellation direction found by GRAM_INERTIA. (iv) The 2×2 scheme collapses to the
graph form 𝔔[(I+L_μ)·] on the edge datum = the q-grouped form of AA_001 (OPEN). No sign of row D. L′♯ OPEN. Row D OPEN.

## 0. Corpus / index check, and why this is not a retry
Index README l.434 (BB_001 phase 198: Euler–Lagrange identities of Π(T) at the minimizer), l.476 (Z_001), l.477 (ROUGH: conjecture (RC),
2×2 bracket θ′ = 0.156 < √(ab) on the split g* = p + δ; "Cauchy–Schwarz in W is circular"), l.478 (EXTERIOR), AA_001, GRAM_INERTIA_001,
PROOF_L_SHARP_BB_001 (Feshbach/perturbation about the prolate span: NO-GO). **Difference:** (a) BB_001 (198) and BB_001 (199) work in the
window/Galerkin variables g; EE writes the extremal problem in the exterior variable ρ ∈ PW_μ|_(1,∞) with F_001's μ-free form 𝔔.
(b) ROUGH's bracket is on g* = p + δ (bulk rough vector δ); EE's is on p = ρ_pro + Δr (prolate tail vs Möbius-lattice complement)
and is measured in the exterior mass norm, not in W (so not the circular CS of ROUGH). (c) EE does not perturb in the comb (BB_001
NO-GO) and does not split into smooth pieces (constraint 25): the split is at leakage scale (edge lines at u = λ/m).
The result of (ii)–(iv) is that EE *reduces* to AA_001's open object; it is recorded so that the 2×2/coercive-complement route is not
re-run.

## 1. (i) Euler–Lagrange equation of the ratio problem
Setting (F_001 Prop F.0, PROVED there): 𝔔 is one quadratic form on L²(1,∞), independent of μ; the admissible class is
V_μ := PW_μ|_(1,∞) ∩ {Tate/moment constraints} (a closed linear subspace: the constraints g(0) = ĝ(0) = g(μ) = 0 are linear);
the radical R := 𝒢̄₁ ⊂ V_μ (A_001 Prop 2.1: gauge = radical, 𝔔 vanishes on R and 𝔔(ρ, R) = 0); dist²(ρ, R) = ‖(I − P_R)ρ‖².
Comb collapse (E_001 Thm E.2, F_001 §1): after the Zeta-sum the form has no Λ; write 𝔔[ρ] = ⟨ρ, 𝒦ρ⟩ with 𝒦 the self-adjoint
(unbounded, form-defined) operator whose kernel is the archimedean part (Θ_∞ multiplier = Lévy + Γ_ℝ on the lags log(m/n) of the
dilate expansion Ψ̌_ρ = Σ_n ρ(n e^y)e^{y/2}), the rank-2 pole term A·B, and the log-weights −(log m + log n) on dilates
(this is exactly `Xbil` in EXTERIOR_DATUM_001_analysis.py).

**Proposition EE.1 (PROVED on finite-dimensional V ⊂ V_μ; CONDITIONAL on attainment in V_μ).** Let Π := orthogonal projection of
L²(1,∞) onto V_μ ⊖ R, and κ(μ) := inf{𝔔[ρ]/‖Πρ‖² : ρ ∈ V_μ, Πρ ≠ 0}. Because 𝔔 is R-invariant (𝔔[ρ + r] = 𝔔[ρ]),
κ(μ) = inf spec(Π𝒦Π |_{V_μ⊖R}) (form sense). If the inf is attained at ρ*, then for all η ∈ V_μ:
 ⟨η, 𝒦ρ*⟩ = κ⟨Πη, Πρ*⟩, i.e. Π𝒦Πρ* = κΠρ* in V_μ ⊖ R, and in L²(1,∞): 𝒦ρ* = κΠρ* + ν, ν ∈ V_μ^⊥
(the Lagrange multipliers of PW_μ-membership and of the Tate constraints are the components of ν; they are what BB_001 called the
multipliers, and EXTERIOR measured 5·10⁻³⁹, 1.7·10⁻³⁸ for the Tate ones).
Proof: first variation of the quotient; R-invariance gives the projection; on a finite Galerkin space V the inf is a minimum of a
generalised eigenvalue problem (Courant–Fischer). Attainment in V_μ needs lower semicontinuity of 𝔔 and compactness of the
sublevel set modulo R — **not proved** (𝒦 is not bounded below by a positive multiple of the identity on the line: constraint 3,
symbol vanishes there). □
Reading: κ is the bottom of a **Λ-free** compressed operator; μ (the Möbius function and the size μ) enters only through V_μ, i.e.
through the data class — consistent with F.0. That is the honest content of (i); it is a reformulation, not a bound.

## 2. (ii) The split ρ = ρ_pro + Δr and the complement
Take ρ_pro := projection on the prolate tails (Langer chirps ψ_k|_(1,∞)), Δr := ρ − ρ_pro. Theorem C (Z_001, CC_001; AUDIT_14:
PROVED for c ≳ 820, NUMÉRICO at N = 15) gives 𝔔[ρ_pro] ≈ ½D(μ)·(mass) with D(15)/2 = 2.53 per unit (1 − λ_k).

**Proposition EE.2 (PROVED structure; NO-GO for the route as posed).** On admissible data f = E⁻¹g + φ₀, Lemma E.1 (PROVED,
AUDIT_13 §1) gives f₁ = Σ_{m≤μ} μ(m)h(m·)1_{[1/λ,λ/m)}; hence the exterior complement content is
 Δr_out = L_μ σ + ρ_reg,  L_μ σ(ω) := Σ_{2≤m≤μ} (μ(m)/m) σ(ω/m),
with σ the upper-edge line, which is (to leading order, EXTERIOR §3) the m = 1 line already contained in ρ_pro. Consequences:
(a) **Resonant by construction.** The line m of L_μσ at dilate n·(·) coincides with line nm at dilate 1 *identically* (same function
σ(ω/m)), with sign μ(m)μ(nm). Theorem B′ (Y_001 Thm Y.5) bounds the form from below for non-resonant chirps with error C_res c^{−½};
Δr_out violates its non-resonance hypothesis at every pair (m, nm), so "the complement is covered by B′" is false for exactly the
data that matter. **NO-GO** (within the class "B′ applied to the complement of the prolate span").
(b) **Not a free variable.** Δr_out (its singular part) is the image of the edge datum under the fixed operator L_μ. A coercivity
constant b on "the complement" is therefore an infimum over a set that the admissible class does not explore independently of ρ_pro;
conversely, on the full orthogonal complement (free data) no positive b exists: constraint 3 (symbol zero on the line) plus the
GRAM_INERTIA null direction (inertia (10,0,1) once φ₀ is included, null vector μ⊕1) give directions with 𝔔/‖·‖² → 0.
(c) The coupling considered here is then not a perturbation: the (1,2) pairing prolate@1 × Δr_out@2 is
⟨σ, 𝒦_{12} L_μσ⟩ with exact coherence, value ≈ Σ_m μ(m)μ(2m)/(2m²)·I(σ) (Prop C′.1, ARGUED), measured −0.481 W* (reverse +0.0001).

## 3. (iii) The 2×2 bracket at μ = 15 (NUMÉRICO, existing data only)
From `analysis.json` (units W*; masses ∫_1^{48}ρ² ×10⁻⁷⁰; S = λ∫𝔴ρ²):
𝔔[pro04] = A = 1.954, 𝔔[Δr] = B = 0.752, 𝔔(pro04, Δr) = C = −0.690 (check A + 2C + B = 1.327 = 𝔔[p] ✓, Galerkin W(p) = 1.2325).
Masses 0.5306, 0.3981, cross −0.0068 (near orthogonal); S: 1.819, 2.529, cross −0.0517.
| norm | a = A/‖pro‖² | b = B/‖Δr‖² | |c| | c²/(ab) | λ_min of pencil (A, Gram) |
|---|---|---|---|---|---|
| exterior mass | 3.68 | 1.89 | 1.50 | 0.324 | 1.05 |
| S (weighted) | 1.07 | 0.297 | 0.322 | 0.324 | 0.184 |
C²/(AB) = 0.324 is norm-independent (Gram nearly diagonal). So for p's own split **c² < ab with margin ≈ 3×** (NUMÉRICO). The
complement is weaker than the prolate block (b/a = 0.51 in mass, 0.28 in S) and the off-diagonal is ≈ 0.57√(ab).

**Why this is not a provable inequality (ARGUED + NO-GO for the CS step).** A proof needs uniform a_inf, b_inf, c_sup over V_μ.
(1) c_sup: the pairing is an exact coherence (EE.2(a)); Cauchy–Schwarz in the exterior norm with the dilation-2 operator norm
‖D₂^*𝒦D₁‖ is sharp only up to the Θ_∞ log-growth (unbounded on L², so a log-weighted norm is needed), and its value is the full lattice
coefficient — it does not shrink with μ (Cor C′.2: Σ_n|R_n|/X₁₁ ≍ log). (2) b_inf: EE.2(b), no uniform floor on free complement data.
(3) Restricting to the graph {(ρ_pro, L_μσ)} removes the freedom, but then the 2×2 matrix is a 1×1 form: see §4. Hence the 2×2 scheme
gives nothing beyond 𝔔[p] > 0 for the measured p (which is already known numerically).

## 4. (iv) Honest statement
- PROVED: Prop EE.1 on finite Galerkin spaces (EL system Π𝒦Πρ* = κΠρ* + multipliers; κ = bottom of a Λ-free compressed operator);
  EE.2 structure (complement singular content = L_μσ, exact dilate coherence, sign μ(m)μ(nm)).
- CONDITIONAL: EE.1 in V_μ (attainment).
- NO-GO (class declared): "coercivity of 𝒦 on the complement of the prolate span via Theorem B′/B" (complement resonant by
  construction); "uniform 2×2 bracket a, b, c with c by exterior Cauchy–Schwarz on the dilation-2 operator" (no uniform b; coherence
  makes c O(1) and non-decaying).
- NUMÉRICO: c²/(ab) = 0.324 on p's split at μ = 15; pencil bottom 1.05 (mass) / 0.184 (S).
- **Remaining inequality (OPEN)** — the graph form: for admissible edge data σ,
  𝔔[ρ_pro + L_μσ + ρ_reg] ≥ κμ^{−A}·dist²,  with L_μ = Σ_{2≤m≤μ}(μ(m)/m)D_{1/m};
  grouped by q = n/m it is AA_001's vᵀGv ≥ κS on the cancellation direction (C_{b/a} = μ(a)M̃_a(μ/a)/a), already OPEN there.
- **Λ-input:** none in 𝒦 (comb collapse); the arithmetic enters only through L_μ (Möbius coefficients of E⁻¹) and V_μ. Any proof
  must use the specific coefficients μ(m)μ(nm) on the coherent pairs, not their size (AA_001 NO-GO (iii): bounds |M̃| ≤ 1 hold for
  a_P and cΛ too).
No sign of row D is claimed. L′♯ OPEN. Row D OPEN.
