# INTEGRATION_188 — Phase-188 results integrated into Paper 46

Target: `04-papers/46-row-d-sign-radial-intersection-form/main.tex`. Backup: `main_pre_phase188.tex`.
Compiled with pdflatex (3 passes): 0 errors, 0 undefined references, 0 multiply defined labels, 0 overfull boxes.
Pages 133 → 146 (+13).

## Added

### New §`sec:combs` "Combs, translates of one profile, and the polar-free form" (before §Barriers)
| paper item | source | status / fixes applied |
|---|---|---|
| Lemma `lem:polarelim` (polar elimination, 𝔢(F) = ‖G′‖²+¼‖G‖²) | N_001 (A) | PROVED. Not in the paper before; rem:Cheb had only ∫e^{u/2} = −∫e^{−u/2}. |
| Prop `prop:sharp` (m^♯ = Re ψ(5/4+iτ/2) − log π; 𝔞_T = 𝔞^♯ − 𝓕_T; λ^♯ ↓ C₀+4) | N_001 (B),(E) | PROVED. (L2) ⟺ (N_loc) is NOT added as a result: it is Prop. `prop:finite`(ii) of the paper; one sentence relates it to the polar-free form. |
| Prop `prop:Egamma-exact` (exact (E_γ) with threshold m^♯(γ)) | N_001 (C) | PROVED; replaces the ±4 slack of rem:wit-cheb. |
| Prop `prop:boundary` (m(γ) = −2Re ζ′/ζ(½+iγ), m^♯ boundary value; C₀ = −2ζ′/ζ(½)) | N_013 §1(b), L2_010 | PROVED (classical computation). |
| Remark `rem:critical` (packet limits critical at every γ and at the centre) | N_013 §1(c), §2–3 | Stated as a remark, explicitly conditional on convergence of the smoothed sums; the (E_γ,C) ⟺ (E_γ) theorem (Hardy–Riesz + ARGUED contour) is NOT stated as a theorem. |
| Def `def:comb`, Prop `prop:Cplus` (convexity, +ρ_κ, mass growth ≥ c₁T²) | N_011 §1 | PROVED. |
| Thm `thm:kappa` (ρ_κ ∈ 𝔆⁺ ⟺ κ ≥ κ_⋆ ≥ \|C₀\|/4; uniform η_κ) | N_011 Thm 1 | PROVED; γ = 0 case removed (continuity + evenness reduce to γ > 0); garbled self-review item replaced by the clean argument (review FIX). |
| Remark `rem:beurling` (continuous Beurling systems) | N_011 Cor 2 | Review FIX 2κ → 4κ applied; the bound now holds for every T without the small-T case split. |
| Lemma `lem:trap`, Thm `thm:atomic` (atomic comb in 𝔆⁺) | L2_018 Lemma 1, Thm B | PROVED. Review FIXes: atom at 0 handled explicitly (removal only helps); partial-block constant recomputed (≤ η/7 instead of η/16); bands rechecked; (H2) stated as log(1/(4h_j)) − 1 ≥ 30κe^{j+1}+η. Theorem A (one window) dropped as subsumed. Sections (b)–(c) "what ℤ-primes lack" NOT included (HEURISTIC); only the proved density comparison is stated. |
| Lemma `lem:reson`, Thm `thm:ceiling` (integer density ceiling) | phase-159 G2_B1_R5 Lemma R, Thm D; L2_021 Prop 4 | PROVED in full in the paper. The residue corollary is re-proved WITHOUT record item Q′: the paper's version assumes only a ≥ 0 and concludes liminf S(x)/log x ≤ 1 (direct from Thm D by monotonicity of S); density/residue versions follow by partial summation / Hardy–Littlewood–Karamata. So the Q′ condition of the review is no longer needed. Wording FIX ("log ℕ too coarse to buy density") used in Remark `rem:resolution`; "positive only through P_T-correlation" NOT stated (HEURISTIC). |
| Prop `prop:nearfree` (Λ positive on resonators) + Remark `rem:boxes` | phase-159 Prop P; L2_029 | PROVED; supersedes L2_029 (separated multiplicative sets are a special case). The Kronecker-sum / local Euler-factor structure of L2_029 is kept as a remark with the exact symbol ranges. |
| Lemma `lem:transl` (translates primitive; exact k=0 cancellation, O(e^{−5D/2})) | L2_023 Lemma L, Lemma C | PROVED. Review FIX: constant 4T₀e^{−5(D−2T₀)/2}/(1−e^{−2(D−2T₀)}) (memo's denominator was wrong); hypothesis D > 2T₀ suffices; translation invariance of the window-free form stated explicitly. |
| Thm `thm:band` (two-sided band \|X\| ≤ 2a₀) | L2_023 Thm T | PROVED, for a general comb ν. Novelty downgrade respected (no claim of strict novelty over the two-copy identity). |
| Thm `thm:poisson` (random combs: P ≤ exp(−cT log T) for every c) | L2_023 Thm P | PROVED with Esseen/Campbell CITED. Review FIX applied: stated for every c > 0 (not the "1/(2 log 2)" constant). |
| Thm `thm:oneprofile` (target ⟺ 𝖡 positive definite) | L2_024 Thm S, L2_025 Lemma I | PROVED. Review FIXes: \|b\| > ½; even cut-off χ in Step 3; density step via H ∈ H²₀ (dilating F does not preserve Tate). The memo's centring shift was unnecessary (c_g*c_g is already even) — removed. |
| Prop `prop:AM` (integer-lattice matrices, spectral identity, Arch − Div − Near) | L2_028 §1–2, L2_030 §1 | PROVED (with 2T₀ < log 2 for a clean Near formula). |

### New §`subsec:bar-arith` "Arithmetic structure, orders and squares" (end of §Barriers)
| paper item | source | status |
|---|---|---|
| Prop `prop:summable`, Cor `cor:wtail` (W-tail with exact small values; partial Euler products; real powers via prop:wit-sens) | N_003 Thm 1, N_005 §2 | PROVED. Noted that truncations were already prop:finsupp; the new content is the class statement (exact small values kept) and the Euler-product class. |
| Prop `prop:prog` (progression/short-interval classes closed under finite modification) + paragraph on twisted vectors | N_021 Thm 2, Prop 3 | PROVED (reduction to cor:void). |
| Prop `prop:relative` (KLMN relative order) | N_008 §1 | PROVED, now with an explicit falsifier form 𝔮′ and the transfer lemma. |
| Prop `prop:opcalc` (operator-language meta-theorem) | N_018 Thm 2 | PROVED; classificatory. |
| Thm `thm:sos` (no arithmetic square decomposition for T ≥ ½log3) | N_019 Thm 2, Prop 1 | PROVED using the paper's own cor:mono value (1.291 − v₂ = 0.311 < 0.980); the mixed-SOS = dual class statement is one sentence. (½log2, ½log3) listed as open. |
| Prop `prop:cone` (Möbius resolvent not monotone for the primitive dual-cone order) | N_007 §0–§3 | PROVED (uses the corrected 𝖬^{−1} = δ₀ − e^{−u/2}du). |
| Remark `rem:farext` (exterior certificates far from the window) | N_020 Thm 2 | See "corrections" below: only the PROVED weak-duality reduction is stated. |
| Remark `rem:fe` (FE antisymmetry D_{1−σ} = −D_σ) | L2_026 §1; L2_025 §3 (Prop H, classical) | PROVED; Prop H cited as classical (Davenport Ch. 12), no novelty claimed; the C_zeros caveat of the 024/025 review included. |
| Remark `rem:bar-arith` (what the class does not exclude) | — | — |

### Other edits
- Abstract: one sentence. Introduction: new paragraph "Combs and one profile" in §Results; one sentence in §Barriers; one sentence in §What remains open; §Organization updated.
- §Barriers intro: "four" → "five" kinds of argument.
- §Open problems: (N) gains its polar-free form; new main item (S) "The near-coincidence matrix" (the sign localized in Near_M, the near-coincidence part of [Ξ_{F₀}(log(m/k))], stated with what is known about Arch, Div and the Near-free tests); two secondary items (atomic positive combs; arithmetic squares on (½log2, ½log3)).
- Bibliography: Davenport 2000, Diamond–Zhang 2016, Kingman 1993, Korevaar 2004, Montgomery–Vaughan 2007, Petrov 1975.

## Corrections found during integration (beyond the reviews)
1. N_020 Theorem 2 (far-exterior certificates have negative value): the proposed "routine correction" is not valid. The dilated
   W-tail tests have c_G ≈ c_G(0) on [−2T, 2T], so their window-T moment pairings are ≈ 4 sinh T·‖G‖², not o(1). The theorem is
   therefore NOT integrated; Remark `rem:farext` states only the weak-duality reduction (PROVED) and says explicitly that
   negativity of the constrained value is not shown. Label for N_020 Thm 2: OPEN.
2. L2_021 Prop 4: the dependence on record item Q′ is removed by the lower-density formulation (see above).
3. L2_024 profile: no shift is needed (G₀ = c_g * c_g is even), so F̂₀ = (τ²+¼)|ĝ|⁴ > 0 holds literally.

## Deliberately left out
- Restatements of corpus/paper results: (L2) ⟺ (N_loc) (= prop:finite(ii)); truncated causal algebra identities (R162_903);
  IMS localization; Schur tower; prime-free slack sign (cor:Tarch); mesh Tate identities (N_001 (D)) — correct but not needed.
- ARGUED/HEURISTIC material: (E_γ,C) ⟺ (E_γ) as a theorem (N_013 §2–3); joint positivity exp(−cT²) on the clamped span (L2_021 §3);
  "positive only through P_T-correlation" (L2_018 (b)–(c), L2_021 §4); Ω₀/Ω_μ/Ω_Φ/Ω_EM targets; Lemma flowdet-type readings; the summary
  "primal and dual sides reduced to D in every known form" (SYNTHESIS §5 conclusion).
- Low-value or superseded items: L2_001–004, 007–009, 012–017, 019–020, 022, 027, 031; N_002, 004, 006, 009, 010, 012, 014–017,
  022; L2_018 Theorem A; L2_028 §3 (next-order balance, ARGUED archimedean asymptotic); L2_030 §3 (Ramanujan expansion, ARGUED);
  N_020 Prop 3 (free integer-log ceiling: an OPEN reformulation); L2_025 Prop H as a result (classical); segment λ_t / t* (N_011 §4, N_012).
- Numerics: none added.

## Self-review against the paper's definitions (review pass)
- Sign conventions: comb form 𝔪_T − ∫Re c_F dν matches eq:Aform; Λ's main term 2e^{u/2}du matches prop:wit-cheb; 𝓕_T agrees with
  prop:wit-cheb on real unit F ∈ P_T ∩ H¹₀.
- P_T, A, B, thm:nyq-cone (P_T = (¼−∂²)H²₀), lem:K expansion, lem:mbounds bounds, cor:Tarch, prop:arch(ii), cor:mono value, def:PD,
  lem:wit-conc hypotheses, lem:transfer: each use checked against the statement in the paper.
- Label clash found and fixed (an existing `lem:polar` in §KEP; the new lemma is `lem:polarelim`).
- No sign of λ_A at any T > ½log5 is claimed; no negative value is certified; Row D remains OPEN.

## Review (independent referee, pen and paper)
Scope: §`sec:combs`, §`subsec:bar-arith`, Open problem (S), abstract/intro. Each statement re-derived in the paper's notation (eq:m, eq:Aform, lem:K, thm:nyq-cone, lem:wit-conc, prop:finsupp, cor:mono, prop:arch).
- lem:polarelim, prop:sharp, prop:Egamma-exact, prop:boundary, rem:critical: CONFIRMED (rem:critical correctly unproved/conditional).
- def:comb, prop:Cplus, thm:kappa, rem:beurling (4κ), lem:trap, thm:atomic: CONFIRMED (constants of (H1)/(H2) bands rechecked; 27/(4π)·2^{-J-4} ≤ 1/7).
- lem:reson, thm:ceiling: CONFIRMED. **(a) Q′ removal is correct.** Q′ (G2_B1_R4) was only needed to produce the pole of Σa(n)n^{-σ}; the paper's
  version proves liminf S(x)/log x ≤ 1 for a ≥ 0 directly: Σ_k (1/k)S(M/k) ≥ ∫_1^M S(x)dx/x by monotonicity of S and S ≥ 0, and H(M) ≤ log M + 1,
  so S ≥ r′log x − C with r′ > 1 contradicts G_M ≤ log(8M)+C_χ. Density/residue forms take the asymptotic as hypothesis (partial summation;
  HLK CITED) and need no Q′. Phase-159 Theorem D is re-proved in full in the paper (lem:reson + thm:ceiling); nothing is cited from the record.
- prop:nearfree, rem:boxes: CONFIRMED (Schur row sum 2log m + 2(log(M/m)+E)).
- lem:transl, thm:band, thm:poisson, thm:oneprofile, prop:AM: CONFIRMED (cross term via eq:m with φ(0)=2c_0(D)=0; Ξ = X − K-term; Poisson log-product
  −(T log T)/(4T_0) with T_0 < 1/(4c); Step 2 strip analyticity since ±i/2 are not zeros of ĝ for |b| > ½; (Div+Near)_{mk} = ½Ξ(log m/k)).
- prop:summable, cor:wtail, prop:prog, prop:relative, prop:opcalc, thm:sos (0.311 = 1.291 − v₂ < v₂ ≤ μ₀), prop:cone, rem:fe: CONFIRMED.
- **(b) N_020 Theorem 2: integrator's objection CONFIRMED.** For G dilated to scale U/2 ≫ T, c_G(u) = ‖G‖²(1+O((T/U)²)) on |u| < 2T, so the
  window-T moment pairings are ≈ ‖G‖²∫_{-2T}^{2T}cosh(u/2)du = 4 sinh T·‖G‖² (resp. the u·sinh pairing ≈ const·‖G‖²), not O(‖G‖²T/U) as the memo
  claims. A cross-term correction δ against a spread-out G pairs at size ‖G‖_∞‖δ‖_1 ≈ U^{-1/2}, so the correction cannot have norm o(1).
  Label N_020 Thm 2: OPEN. rem:farext states only the weak-duality reduction: correct.
- **(c)** grep of all added lines: no statement relates row D to any other row or hypothesis; rem:fe/ C_zeros is a class barrier only.
- FIX applied: abstract and intro said "density at most one"; thm:ceiling proves *lower logarithmic density* (liminf S/log x) ≤ 1. Wording
  changed in abstract (l.94–95) and intro (l.233). No other change.
- Recompiled (3 passes): 0 errors, 0 undefined references, 0 overfull boxes, 146 pp.
Verdict: integration ACCEPTED with the one wording fix. No sign of λ_A beyond ½log5; D OPEN.
