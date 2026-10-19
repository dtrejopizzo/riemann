# Adversarial review of main.tex (10 pp.) prepared for A. Connes

Rules: no RH, no equivalences; honest labels.
Status: PARTIAL review. Items marked "verified" were checked directly against the source; three
further checks (§2–§3 vs R183/R186_004–017; §4–§6 vs R186_018–026/104/105 + DRAFT; CC citations vs
local text) were still in progress when this report was closed and are NOT included. Their results
must be appended before sending.

## 0. Overall verdict
- **No mention or suggestion of RH / equivalences** (grep: riemann, RH, hypothesis, equivalen → 0 in the body; only bibliography titles). OK.
- **No FATAL found** in what was checked: thm:nogo, thm:A, thm:B, prop:prime, cor:L1, thm:schur, D3 (thm:84(ii)) have PROVED sources. There are MAJOR issues of presentation and of unresolvable internal citations.

## 1. Labelled statements → source → status

| Claim (paper) | Source | Status | Severity / replacement text |
|---|---|---|---|
| thm:split (Sonin identity, all T, no moment condition) | R183_018 §3 "PROVED (from CITED CC (83),(152))" | OK | — |
| thm:nogo (infinite negative index on 𝒫_T, also on ker ∫F, for any inner product, k finite) | R183_018 Thm 5.1 "NO-GO PROVED"; R183_019 Thm 4.1 PROVED; R183_020 no FATAL | OK; the paper's proof follows the source (β=c_w''−c_w/4, pairs at distance log 2, O(w)) | — |
| Remark (2): n₋(𝔞_T−(1−η)Son) < ∞, of order T e^{2A'/η} | R183_023 Thm 3.1 PROVED (given Lemma ε-L∞ = continuity of ε); there N = #{λ_k(S_{Ts*}) > γ/L}, s* = min{m(s) ≥ 2A/η}, A = (1−η)κ_T+β_S+2γ | OK in substance; the constants A', A'/(A'+L) of the paper are not literally those of the source | MINOR: either "bounded, by [R183_023-type argument], by the number of eigenvalues of the time–band operator above an explicit threshold", or reproduce the exact A, γ, L |
| thm:84(ii) level dictionary 2log(1/λ)f(1), 0<λ≤1, ε_1=ε | R186_017 D3; R186_099 "Label D3: PROVED (via (i)–(iii)) for 0<λ≤1"; §1(c) Frullani ARGUED (not used) | OK (PROVED) | MINOR: the paper's proof ("passage from S(1,b) to S(1,1) adds log(1/b)f(1) plus an explicit continuous density; combine with (83) at λ=1") agrees with R186_099 (i)–(iii) |
| cor:split, extension to S={∞,2,3}: "log² singularities at S-units 2^a3^b cut off at scale 1/b" | R186_015 L2_S: "PROVED given R1 and Sp; exact form of the log^{r−1} term: ARGUED"; cut-off 1/b PROVED | OK (r=2 ⇒ log²) | MINOR: add "(the lower-order terms are not made explicit)" |
| thm:A: λ_A(τ) ≥ log(1/τ) − 1.209 − τ, τ ≤ 0.1 | DRAFT l.236 identical; R186_105 row 6 PROVED "by hand R=2: C_A ≤ 1.208+τ"; 1.209 = conservative rounding of the chain −3.108+2.1045(1−0.0975) = −1.2089 | OK | — |
| thm:B: C_B(τ) closed form, →1.6399, C_B(0.02)=1.657, (0.0619)=1.696, (0.1)=1.733; hypothesis τ ≤ 1 | R186_105 l.25: 1.6573/1.6957/1.7331, limit 1.6399; MINOR (iv) "Theorem B does not need τ ≤ 0.1"; closed form in DRAFT | OK | MINOR: "C_B(τ) in closed form": the paper does not give it; add "(given in [Paper47, §…])" or the formula |
| "coupling norm exactly π; contribution to the quadratic form π/2" | R186_105: ≥π ∀k≥2 PROVED, =π on the pair; README round 13 editorial correction C1 (π bilinear, π/2 in the form) | OK | — |
| "k ≥ 70 at ½log5 against k=25" | README round 13 "NO-GO by norms intact (k ≥ 70 vs 25)" | OK | — |
| prop:prime: ‖Π_T‖ ≤ Σ v_n cos(π/(L_n+1)); 𝒜_T/2 for T ≤ log2; 0.4901; 1.6740 on (log2, ½log5] | DRAFT "PROVED (formerly CITED)"; R186_104/105 ‖P₂‖=v₂/√2=0.693; recomputed by hand: 0.693+0.634+0.347=1.674 ✓; log2/√2=0.4901 ✓ | OK | — |
| cor:L1: c(½log3,8) ≥ 0.486 (dim 14), c(½log5,25) ≥ 0.094 (48), c(½log5,30) ≥ 0.281; k₀ ≤ T e^{𝒜_T+C_B} | R186_105 "k=25/26/30 → +0.094/+0.134/+0.281", dim 48/50/58; recomputed 0.486 ✓ | OK | — |
| thm:schur, sandwich min(c,λ_S)/(1+‖K‖)² ≤ λ_A ≤ min(c,λ_S) | DRAFT + R186_105 "Rigorous reduction (L1)+Thm 3.1 ⟹ λ_A>0 ⟺ S_{T,k} ≻ 0 (dim 48)" PROVED | OK | — |
| thm:phase (Thm C, C′), prop:AS (L0, no-HS, S_p), thm:gap (gap, TC_S, T3), thm:L2 (β_j), thm:84(i) | README: Thm C/C′ PROVED (R186_008/094); L0, gap PROVED (009/095); TC_S PROVED (010); no-HS PROVED (007/093); S_p p>2 PROVED (011); L2_S PROVED (012/097, "for d_S"); (84)_S PROVED (014/098); chain for finite S PROVED (015) | OK per README; **line-by-line check pending (§2–§3 check)** | Points to watch: thm:L2 "O_R(1) uniform" and "ε_S ∉ L^∞_loc" (README 096: "unboundedness only NUMERICAL", then 012 PROVED divergence at 2^j; confirm that the paper's proof via ‖1_{[2^{-j}λ,λ]}A_S‖_HS = ∞ is in 012/014); thm:gap(ii) "absolute convergence although Σλ_n²=∞" = T3 of 014 (PROVED) |

## 2. Numerical constants checked
| Constant | Source | Status |
|---|---|---|
| λ_max(K_I)=1.05158 (±0.0012), ⟨ξ₀|ζ⟩=0.94865, ε'(1⁺)=22.9965 | cc_2006.13771_text l.2789, 3038, 3152, 2131 | OK |
| §2 "λ₂(K_I) ≤ 0.7722" and §4 "λ₂=0.684 against 0.6865" | CC (127): λ₂=0.686494; CC Prop (iii): λ₂ ≤ 0.772216 | OK both, but **inconsistent for the reader**: MINOR: in §2 write "λ₂(K_I)=0.6865 (bounded a priori by 0.7722)" |
| 1−λ₁=2.6e-6, λ₂=−0.9927 (λ=1); 0.988/−0.507 (λ=½); 0.885/−0.107 (A_∞) | R186_018 (2.617e-6, −0.992626), R186_007 (0.988/−0.507) | OK; 0.885/−0.107 not located (pending) |
| β₁=0.510 at λ=1; slopes 0.128/0.272/0.448 at λ=½ "1 %" | R186_018 "β₁ = 0.510"; R186_012 "numerical <1 %" | OK (exact slopes not checked) |
| 1.386‖F‖², Son(½)−Son(1) margin 1.20, Son_S(h*)=0.0174, C=0.0164, 9.9e-4 (5.7 % → "94 %") | R186_017/099 (1.386; 1.1978–1.2010; 0.0174/0.0164/9.9e-4) | OK |
| table ρ*: 0.001/0.003/0.055/0.245/0.644/0.944; Son(u_T) 0.38→0.018 | R186_021 | OK (row C(u_T) and Son 2.82/2.29 not checked: pending) |
| 0.9936; 0.135/0.140; 0.989; 0.03; −0.140→+0.010; 11.05→7.60; cos(7.6 log2)=0.527; 0.145; −0.142; 0.153; T≈0.45 | R186_102, R186_021, R186_022, R186_023 (one-mode law fails beyond 0.45) | OK |
| minimum Son 0.0145 (§4) vs 0.0140 archimedean / 0.0147 semilocal (obs:s0) | R186_013 "min 0.014"; R186_021 | **MINOR: 0.0145 vs 0.0147 for the same quantity (Son_{Π_S} min at ½log3)**; unify |
| −0.083/−0.040 (2 negative directions), factor 2.5, ⟨h*,v₁⟩≈0 | R186_018 (−0.0824, −0.0397; E_S/Son=0.61 ⇒ ≈1/0.4=2.5) | OK numerically, **but R186_101 marked 2 FATAL in 018 (apparent convergence; n₋ not robust)**: MAJOR: say "two negative directions in the Galerkin basis used (M=32; their number is not stable under refinement)" |
| 1−‖A_S‖² = 5e-6 | (1−2.617e-6)² ⇒ 5.2e-6 | OK |
| C₀=−5.3722; C₀+log2+π/2=−3.108; w(2)=2.1045; 16(R²+a)³/(27π⁴R²)=0.0975 | arithmetic | OK |
| commutator −12π(30π²u⁴−19πu²+1) | R186_003 | OK |
| λ_A(½log5) ≈ 3e-12 (λ_S ≈ λ_A); 2.5e-12 bound | R186_104 (3.1–4.0e-12); Paper47 Thm log5A | OK |
| footnote: third parties, log 7, L≈1.1147 | R186_027 §4: GitHub repository jose-paul-b/weil-positivity-certificates (Arb, 2026), no arXiv | **MAJOR**: source neither cited nor citable; either cite the repository with URL and date, or delete the note |

## 3. Citations of Connes–Consani
| Citation | Local evidence | Status |
|---|---|---|
| CC §6 numbers (127), Fact 6.5, λ₂ ≤ 0.772216 | cc_2006.13771_text | VERIFIED |
| (16), (83)–(90), (152)–(154), Thm 1, Def 4.4, Thm 4.7, Prop 1.5(iv), Thm 3.6/Cor 3.8 (|I| ≤ 2·0.1404), Lemma D.1 | local text available; R186_027 confirms Thm 3.6/Cor 3.8/Rem 3.9 (0.0975 improved to 0.1404) | PENDING equation-by-equation check (citation check); R183_019 l.8 cites "Theorem 1 l.109; Lemma 6.9, 6.10, Theorem 6.11", consistent |
| CCquasi 2008.10974 Lemma 3.1, Thms 2.1/4.4, ker u₂₂ | only via R186_020 (u = ρ_∞∏ρ_p, Sonin = ker u₂₂); text not available locally | NOT VERIFIABLE locally; number with caution ("see [CCquasi, §3]") |
| CCM2023 Prop 4.1 (F_S∘η_S=η_S∘F_∞); CCM2024 moments | R186_002/006 | the number "Prop. 4.1" is not verifiable locally |
| Connes2026 2602.04022 §7.2 Thm 7.1, §7.4 | R186_027 §2 | OK; **bibitem without title**: MINOR, add title |
| Zhu Thm 1.1 / Thm 1.4, certificate T ≤ 0.8; Groskin; Kim; CvS; Suzuki ×2; Yoshida Lemma 3 | R186_027 (mandatory) | ALL PRESENT and correctly attributed; "not the first finite reduction", "same doubly exponential order as Zhu's barrier" meets R186_027 §3.2 |
| Bombieri2000, Burnol1999, CM2022 | not cited in the text | MINOR: remove or cite |
| \cite[Thm.~log5A]{Paper47}, [Thm.~margin], [Lemma~K], [Lemma~mbounds], implicit "lem:contA" | internal LaTeX labels of a non-public preprint | **MAJOR**: the recipient cannot resolve them. Replace by section/theorem numbers of the attached PDF, or state the four facts in the text (they are elementary) and cite "[Paper47, §2]" |

## 4. Tone and audience
- Personal opening: correct in content (more than ten years, amateur, CC+Moscovici route, a new insight is missing, wishes to contribute). MINOR: "as a hobby" → "as an amateur"; "I would still like you to have it" fine.
- **MAJOR (form)**: second person ("your Theorem 1", "your (87)", "your §6", "Compactness is yours", "at your level", "your Lemma D.1") in the mathematical sections; with a single author, "we" + "you" mixed with "I". Decide: (a) letter + separate paper in the third person (Connes–Consani) or (b) keep "you" only in the opening and in §6. Recommended: (a), so that the paper can circulate to Consani/Moscovici.
- Internal jargon: "first contact" (l.540) → "the orbit blocks for T∈(½log2, log2)"; "certificate" ok (Zhu's usage); "window form", "Tate moments/conditions" defined, OK; "the independent re-derivations that were made of each of them" (l.132) reads as an internal process note → "and the full arguments are available on request".
- "The term 2log(1/λ)f(1) was, for us, the difference between a consistent and an inconsistent chain" (l.350): debugging narrative; reduce to one sentence: "Without this term the semilocal Sonin trace would be negative on the near-minimizer at λ=½; with it every consistency check we made passes (…)".
- No exaggeration; "None of this produces a sign" repeated three times (abstract, intro, remark): keep two.
- On Zhu: compliant (claims no gain; cites Thm 1.1 and 1.4).

## 5. English / typos
- Abstract: "stops exactly at log2" vs "T>½log2": write "at window length log 2, i.e. T=½log2".
- l.342 proof of thm:84: "…⟨ζ_n|ϑ(f)ζ_n⟩-type bookkeeping closes" is unreadable; rewrite: "and the identity Tr ϑ(f)Q₁Q₂Q₁ − Tr ϑ(f)Π_F = E_F(f) + Σλ_n²⟨ζ_n|ϑ(f)ζ_n⟩ follows by summation" (note: the later proofreading found this identity incorrect; see PROOFREAD, row A).
- l.488: "a Weyl sequence x'^{-1/2}1_{[2τe^{-M},2τ]} in the distance to the common endpoint": x' undefined; write "a Weyl sequence d^{-1/2}1_{[2τe^{-M},2τ]}(d), d the distance to the common endpoint".
- l.251 "Compactness is yours" → "Compactness is proved in".
- l.266 "real but tiny at your level" → "at the level λ=1".
- "a Lévy energy" OK; "Hilbert--Schmidt form" OK; "the comb only sees k log p<2T" OK.
- Obs. 4.2: "a ``cosine with negative shoulders''" fine in quotes; "drifting downward" OK.
- "The honest summary is" (§6) → "In summary" (avoids "honest" suggesting the opposite elsewhere).
- For a French reader: "record three things" → "record three facts"; "It has a shape" → "It has a visible structure".
- Bib: Kim2026 and CCM2024 without title or full authors; Connes2026 without title.

## 6. Items not verifiable locally
CCquasi (Lemma 3.1, Thms 2.1/4.4), CCM2023 Prop 4.1, Simon Thm 4.5 (ℓ¹(L²) criterion), Yoshida Lemma 3 (via Suzuki 2206.03682 §4.2 per R186_027), Arb certificate repository (footnote), values 0.885/−0.107 of A_∞, row C(u_T)/Son(u_T) of the table.
