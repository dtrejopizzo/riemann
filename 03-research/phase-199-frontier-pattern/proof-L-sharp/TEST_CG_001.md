# TEST_CG_001 — converged structural test of conjecture (C_G) (AUDIT_L_SHARP_3 §6) at μ = 5, 8, 10

Phase 199, numerical test. Label of every number in this memo: **NUMÉRICO**.
Purpose: decide whether the split
𝔔 = −Q(G,G) + [2Q(F,G) + 2AB] (P.1) can carry a proof, i.e. whether (C_G)(a) |2Q(F,G)+2AB| ≤ θ(−Q(G,G)), θ < 1, and
(C_G)(b) −Q(G,G) ≥ κμ^{−A}dist²(ρ,𝒢̄₁) hold on PW_μ ∩ {ĝ(0) = 0} ∩ 𝒢̄₁^⊥.

**Verdict in one line.** Q(G,G) ⪯ 0 holds on every constrained Galerkin space tested, and 𝔔 ⪰ 0 there, but **(C_G)(a) is not
supported**: θ is converged in τ, X and node count to ≥ 4 digits, yet it is *not* converged in the radical span. It rises
with the radical dimension J (μ = 8: 0.17 → 0.74; μ = 10: 0.07 → 0.61) because the L²-gauge "ρ ⊥ 𝒢̄₁" is not a
Q(G,G)-gauge. Exact radical vectors make Q(G,G) **positive** (explicit vector §4). The mechanism predicts θ → 1. (C_G)(b)
cannot be tested: double precision does not resolve the near-band directions. The split (F₀,G) with the L² gauge is not a
viable proof frame. A gauge adapted to G is required (§6).

## 0. Corpus check / not a retry
- **Index read:** ROUTES-TRIED-INDEX README l.459–460 (K_001, P_001 + AUDIT_15).
- **Grid/crossword:** no Mellin-side test of (C_G) is recorded.
- **Why this is not a retry:** this memo executes the test that AUDIT_L_SHARP_3 §6 requires before (C_G) is used. Three
  things change with respect to P.4:
  - the constraints are imposed;
  - convergence is controlled in four parameters (τ cutoff, τ panel rule, X nodes, X cutoff) and in the radical span;
  - Q(F₀,F) is computed through the P.2 contour shift, not through ζ on the line.
  Audit item "do not retry: Mellin numerics of 𝔔 without a reported quadrature and a cutoff ≳ 2πμX_eff" is respected:
  quadrature is reported, and the tail is handled analytically (below).

## 1. Method
**Data.**
- PW_μ basis: g_k(t) = t²(1−(t/μ)²)⁶P_{2k}(t/μ), k < K = 20. Then ρ_k = ĝ_k|_(1,101) is C^∞ inside, ρ_k = O(X^{−7}), and g(0) = g(μ) = 0.
- Radical generators: χ_j(t) = t²(1−t²)³P_{2j}(t), j < J ≤ 20. These are μ-independent.
- Constraints: the hyperplane ĝ(0) = 0 is imposed separately on each family, giving 𝒢₁-generators.
- Constrained space: (PW part with ĝ(0) = 0) projected L²(1,∞)-orthogonally to span{radical generators with ĝ(0) = 0}.
  This is then Γ-orthonormalised (Γ = L²(1,∞) Gram) with a relative eigen-cutoff (10^{−11}/10^{−13}/10^{−14}; results quoted at 10^{−13}).
- In these coordinates ‖ρ‖² = dist²(ρ, span_J), the finite-J proxy of dist²(ρ,𝒢̄₁).

**Forms.**
- Q(F,F) on Re s = ½ with Θ_∞ = Re ψ(¼+iτ/2) − log π.
- Q(F₀_i,F_j) by P.2, shifted right: R_i(0)[log 2π·A_j + F_log,j(1)] + I_c with c = 3/2. The integrand is
  R_i(1−s)[(ζ′(s) − ζ(s)χ′/χ(s))F_j(s) − ζ(s)F_log,j(s)], written in the χ form, so it has no poles at zeros.
- Derived forms: Q(G,G) = Q(F,F) − Q(F₀,F) − Q(F₀,F)ᵀ, 2symQ(F,G) = 2Q(F,F) − Q(F₀,F) − Q(F₀,F)ᵀ, 2AB = AB ᵀ + BAᵀ,
  𝔔 = Q(F,F) + 2AB. A = F(1) and B = F(0) are computed exactly.

**Quadrature.**
- τ: Gauss–Legendre panels of width 1 with 24 nodes, up to τ = 2000. Cutoffs T = 500/1000/2000.
- τ-tail beyond T, added analytically from F ~ a/(s−1), F_log ~ b/(s−1), R(1−s) ~ −ρ(1)/s, where a = Σρ(n) and b = Σρ(n)log n:
  - tail of Q(F,F): [aaᵀ(log(T/2π)+1) − abᵀ − baᵀ]/(πT);
  - tail of Q(F₀,F): ρ(1)[a(log(T/2π)+1) − b]ᵀ/(πT).
- X: Gauss–Legendre on [n,n+1], with ⌈0.6(T_max log(1+1/n) + 2πμ)⌉ + 30 nodes per interval.
- ζ, ζ′, χ′/χ and ψ: mpmath with dps = 30. The rest is float64.
- Scripts:
  - `TEST_CG_001_zeta_tables.py` (tables);
  - `TEST_CG_001_forms.py` (matrices);
  - `TEST_CG_001_analysis.py`, `TEST_CG_001_summary.py` (constrained spectra, θ, rank);
  - `TEST_CG_001_radical.py`, `TEST_CG_001_radical_vector.py` (radical diagnostics).

**Convergence checks (all passed).**
| check | result |
|---|---|
| T = 500 / 1000 / 2000 (with tail) | every reported eigenvalue and θ is stable to ≥ 3 digits (θ to 4); without the tail, the top eigenvalue drifts ~1%, as AUDIT_3 found |
| τ panel 24 → 36 nodes/unit (μ = 5, T = 500) | matrices agree to 1.5·10^{−13} (relative) |
| X nodes ×2 and X cutoff 101 → 141 (μ = 10) | matrices agree to 4·10^{−12} |
| P.2 check: contour (c = 3/2) + residue vs direct line integral, in the χ form and in the old F₀ = ζ(1−s)R form | agree to 4·10^{−7} – 1·10^{−6} (relative); **P.2 is now numerically verified**, closing the item AUDIT_3 left open |
| radical generators are 𝔔-null (Prop 2.1) | max\|𝔔\| on the radical span ≤ 3·10^{−5} against form scale 16 (J = 19) and ≤ 4·10^{−10} (J = 4); validates the whole pipeline |
| Gram cutoff 10^{−11} → 10^{−13} → 10^{−14} | θ changes ≤ 0.01; dimensions 15→16→17 (μ = 5), 11→13→14 (μ = 8), 10→12→13 (μ = 10) |

## 2. Results at J = 19 (largest radical span), T = 2000, cutoff 10^{−13}
Generalised spectra relative to Γ; "S" denotes 2symQ(F,G) + 2AB.
| μ | dim | spec 𝔔 | spec −Q(G,G) | spec S | θ = max\|gen.eig(S; −Q(G,G))\| | rank Q(F,G) (sv > 1% top) | ‖P⊥Q(F,G)P⊥‖/‖Q(F,G)‖, 2 / 4 pole functionals |
|---|---|---|---|---|---|---|---|
| 5 | 16 | [0.746, 3.96] | [0.825, 5.75] | [−4.28, 0.57] | **0.802** | 3 | 0.058 / 0.038 |
| 8 | 13 | [1.083, 4.25] | [1.465, 4.85] | [−3.41, 0.11] | **0.736** | 3 | 0.015 / 0.011 |
| 10 | 12 | [1.423, 4.28] | [1.900, 4.26] | [−2.34, 0.09] | **0.606** | 3 | 0.018 / 0.010 |
The four pole functionals are A, B, F₀(1) ∝ R(1), and F_log(1).

- Q(G,G) ⪯ 0 on the **whole** constrained space, for every μ and every J (not just at the bottom).
- 𝔔 ⪰ 0 everywhere.
- Q(F,G) is numerically low-rank: 3 singular values above 1%, and its range is 96–99% inside span{A, B, R(1), F_log(1)}.
  This confirms AUDIT_3 §6 at μ = 5, 8, 10.
- **Not confirmed:** "𝔔 ≈ −Q(G,G) eigenvalue by eigenvalue". In Γ-normalised coordinates, the eigenvalue ratios differ by
  25–93%. The 0.1–0.5% of AUDIT_3 was measured in raw, non-orthonormalised coordinates, where both forms share the Gram
  near-null directions.

## 3. The radical sweep: θ is not converged
θ (T = 2000, cutoff 10^{−11}; J = number of radical generators; J = 0 means ĝ(0) = 0 only):
| J | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 17 | 18 | 19 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| μ=5 | 0.978 | 0.699 | 0.307 | 0.537 | 0.615 | 0.576 | 0.612 | 0.683 | 0.737 | 0.768 | 0.779 | 0.802 |
| μ=8 | 0.406 | 0.250 | 0.172 | 0.222 | 0.321 | 0.425 | 0.517 | 0.594 | 0.657 | 0.691 | 0.707 | 0.733 |
| μ=10 | 0.157 | 0.107 | 0.074 | 0.108 | 0.175 | 0.256 | 0.338 | 0.415 | 0.484 | 0.519 | 0.543 | 0.573 |

Behaviour of the spectra in J:
- min 𝔔 *converges* (μ = 5: 0.568 → 0.748; μ = 10: 1.40 → 1.49), as it must, since the radical is 𝔔-null.
- max(−Q(G,G)) and the most negative eigenvalue of S *grow without visible saturation*: at μ = 5, 3.39 → 5.75 and −0.97 → −4.27.
- The second radical family (MR = 6, J ≤ 11) gives the same trend.

**Mechanism (ARGUED).**
1. On the radical, 𝔔 = 0, so S = −(−Q(G,G)) exactly: the split saturates there, with |S| = |Q(G,G)|.
2. −Q(G,G) restricted to the radical span is unbounded relative to L². Its top eigenvalue is 2.8 / 6.6 / 11.0 / 15.5 / 18.5
   for J = 4 / 8 / 12 / 16 / 19, roughly linear in J, because Q(G,G) is not L²-continuous (Z is not L²-bounded, AUDIT_2 caveat (i)).
3. Hence the L²-projection w_J = v − P_Jv keeps 𝔔(w_J) = 𝔔(v) and inflates −Q(G,G)(w_J). Then 𝔔/(−Q(G,G)) → 0 along such
   directions and θ_J → 1.
4. In the limit J → ∞ the L²-orthogonal representative is presumably outside the Q(G,G) form domain.

## 4. Counterexample vector: Q(G,G) > 0 on PW_μ ∩ {ĝ(0) = 0}
ρ = ĝ|_(1,∞) with g(t) = Σ_j c_jχ_j(t), χ_j = t²(1−t²)³P_{2j}(t), and
c = (−0.111058, −0.58127, −0.840944, −1, −0.795153, −0.646742, −0.29675, −0.162422) (j = 0..7). This g is supported in
[−1,1], so it lies in PW_μ for every μ ≥ 1, and ĝ(0) = 3·10^{−18}.
Values: Q(G,G)/‖ρ‖² = **+0.09485**, 2Q(F,G)+2AB equal to the same number, and 𝔔/‖ρ‖² ≈ 10^{−9} (radical); stable for T = 500/1000/2000.
With J = 19 generators the maximum is **+0.3697**.
It is a radical vector, so it is not a counterexample to (C_G), which removes the radical. It is a counterexample to
"Q(G,G) ⪯ 0 on PW_μ data", and it shows that the sign of Q(G,G) depends on the gauge. The infimum of −Q(G,G) over radical
shifts of a fixed ρ is −∞, since −Q(G,G) is indefinite on the radical. **No gauge-free form of (C_G) exists.**

## 5. Part (b) and (κ, A)
- Galerkin λ_min(−Q(G,G)) on the constrained space (J = 19) is 0.825 / 1.465 / 1.900 for μ = 5 / 8 / 10.
- Galerkin λ_min(𝔔) is 0.746 / 1.083 / 1.423.
- Taken literally, this gives κ ≈ 0.8 and A ≤ 0.
- **Not informative.** Both minima *increase* with μ, and the Gram cut (relative 10^{−13}, the limit of double precision for
  these bases) removes exactly the near-band, near-prolate directions where the true infimum (≍ e^{−4πμ} in leakage units,
  K_001/Mori) lives. (b) is therefore neither supported nor refuted. A test of (b) needs a prolate-adapted basis and
  extended precision in the X-quadrature, not just in the special functions.

## 6. Answers and consequences
1. **(C_G) at μ = 5, 8, 10:**
   - (a) is NOT supported. At every finite radical span θ < 1 (0.80 / 0.74 / 0.61 at J = 19). But θ grows monotonically in
     J for J ≥ 4, and the exact radical saturates the split (|S| = |Q(G,G)|). The predicted limit is θ = 1. The
     "θ < 1, stable in μ" reading is an artefact of a small radical span.
   - (b) is untestable in double precision (§5).
2. **Q(G,G) ⪯ 0 on the whole constrained space:** yes, at every J, μ and cutoff tested.
   - Q(G,G) is **positive** on explicit radical vectors (§4).
   - So the sign of Q(G,G) is a property of the gauge, not of PW data.
3. **Does −Q(G,G) alone dominate 𝔔?** Only on small radical spans. The cross term is low-rank and pole-controlled (96–99%),
   but its size grows with J at the same rate as −Q(G,G).
4. **Consequence for strategy (ARGUED).** The pole structure of S (rank ≤ 3–4, functionals A, B, R(1), F_log(1)) is robust.
   What fails is the normalisation: in the L² gauge, −Q(G,G) is not a coercive reference form. The two possible repairs are:
   - (i) choose the representative ρ + r that minimises a *G-adapted* norm. This is not −Q(G,G) itself, which is indefinite on
     the radical. The quotient would be by a positive form that is radical-invariant on the pole complement;
   - (ii) replace (C_G)(a) by a comparison with a form that vanishes on the radical, e.g. 𝔔 restricted to the complement of
     the 3–4 pole functionals.
   Either is a new construction and is OPEN.
5. **Do not retry:** (C_G) with the L²(1,∞)-orthogonal radical gauge; any "−Q(G,G) dominates" argument without a
   G-adapted gauge; reading θ from a radical span of fixed small dimension.

## 7. Labels
| item | label |
|---|---|
| P.2 contour identity, numerical check (relative 10^{−6}) | NUMÉRICO (confirms PROVED P.2) |
| 𝔔 ≡ 0 on radical generators | NUMÉRICO (confirms Prop 2.1) |
| Q(G,G) ⪯ 0 on L²-gauged constrained spaces, μ = 5, 8, 10 | NUMÉRICO |
| Q(G,G) > 0 on explicit radical vectors | NUMÉRICO (explicit, μ-independent) |
| Q(F,G) low-rank, range ≈ pole functionals | NUMÉRICO |
| θ_J increasing in J, θ → 1 | NUMÉRICO + ARGUED mechanism |
| (C_G)(a) in the L² gauge | not supported; downgrade to NO-GO candidate (needs a proof of unboundedness of −Q(G,G) on 𝒢̄₁) |
| (C_G)(b) | OPEN (untestable at this precision) |

No sign is claimed. (★★) OPEN. Row D OPEN.
