# Check table: draft section "Inertia, remainders and barrier theorems"

Editor: checked against Paper 47's own definitions (eq:symbol, eq:form, eq:W, def:PD, def:W/eq:nuw, P_T,
Gamma_T (prop:nodes), Pi_T (subsec:arch), S_c (thm:P), V_T (prop:finite), lem:roughEF, lem:monoT, cor:margin2,
lem:parity / thm:parityschur(o)). main.tex NOT edited. Draft: DRAFT_SECTION_INERTIA_BARRIERS.tex
(compiles standalone with the main.tex preamble, 4 pages; only cross-refs to main.tex are undefined).

Metric legend: L2 = L²(I_T) in the variable F (Paper 47's metric); xi = CC metric h=(1/2-∂)ξ, ‖ξ‖² (H^{-1} type in h);
X = Son+‖·‖².

| # | statement | source id | Paper-47 objects used | metric | normalization verified (Y/N, how) | label | enters |
|---|---|---|---|---|---|---|---|
| 1 | Sonin split 𝔞_T = Son + 𝔯_T, 𝔯_T = −⟨C_ε·,·⟩ + Π_T, all T, no moment condition | R183_018 §3, rev. R183_020 | 𝔞_T (eq:form), Γ_T, Π_T, v_n, N_T; new: Son, ε (CC, CITED) | L2 | Y: CC h_+ = m of eq:symbol (no polar term ⇒ W_∞ = Γ_T, not A_∞); (1/2π)∫cos(τ log n)|F̂|² = Re c_F(log n); semilocal prime sum 2 log p p^{-k/2}, k log p<2T = Σ_{n∈N_T} v_n; sign of CC (83) checked in R183_020 | PROVED (from CC (83),(152) CITED) | Y (thm:inertia-split) |
| 2 | spec Π_T = {0, ±log2/√2}, ∞ multiplicity, ‖Π_T‖ = A_T/2 for ½log2<T<½log3 | R183_023 §2.1, R183_018 Prop 4.1 | Π_T, A_T | L2 | Y: fibre matrix −v_2·[[0,½],[½,0]], v_2 = √2 log 2 = A_T; consistent with ‖Π_T‖ ≤ A_T (subsec:arch) | PROVED | Y (thm:inertia-B2) |
| 3 | n₋(−C_k + Π_T | P_T ∩ ker∫) = ∞ for every bounded even k, T>½log2; hence n₋(𝔞_T − Son)=∞ | R183_018 Thm 5.1; R183_019 Thm 4.1; R183_020 | P_T, Π_T, v_2 | L2 (the ξ-metric version of R183_019 not used) | Y: Π_T(x) = −v_2‖β‖²Σ|c_j|²; β primitive by parts against e^{±t/2} (A=B=0 of P_T) | PROVED; generalized to any bounded k (proof only uses ‖k‖_∞); ε bounded = continuity CITED CC (84) | Y (thm:inertia-nogo) |
| 4 | relative bound 0, finite index n₋(ηΓ_T − C_k + Π_T) ≤ ((A'+L)/A')(2Ts_*/π), η>0 | R183_023 Thm 3.1, Cor 3.0', Cor 3.2 | Γ_T, Π_T, A_T, C_0, m increasing (thm:S), S_c and Λ_k (thm:P) | L2 | Y: rewritten in Paper-47 notation with ‖Π_T‖ ≤ A_T replacing β_S, C_0 = m(0); proof written in full (shorter than source; constant c of coercivity dropped, count only) | PROVED | Y (thm:inertia-finite) |
| 5 | quartet contribution q_z = 4Re A_z(F_e)² − 4Re A_z(F_o)², signature (2,2) on real P_T, all T>0 | R184_004 Lemma 1; R184_091 | eq:W zero sum, Φ_F, P_T^ev/odd (prop:nodes parity paragraph) | L2 (real) | Y: Φ_F as in eq:W; Φ_F(½−z) = Φ_{F(−·)}(½+z); independence argument rewritten (growth β<½ + analyticity) | PROVED (∀T>0 per R184_091) | Y (thm:inertia-quartet) |
| 6 | W^{Z'}_T − W_T rank ≤ 6m (m quartets added, m line pairs removed); |Δn₋| ≤ 6m | R184_004 Thm 4(a),(c) | W_T as zero sum | L2 (real) | Y: removed pair = 2|Φ_F(½+iγ⁰)|² (lem:roughEF) rank 2 | PROVED (Schur-complement part needs invertible blocks, MINOR R184_091) | Y (thm:inertia-rank), zero-side part only |
| 7 | Cor 5 inertia NO-GO for the class 𝒜 | R184_004 Cor 5; R184_091 caveat | decomposition Γ_T − C_ε + Π_T, inertia | L2 | Y for the pieces; the model M_m is NOT a Paper-47 object (not in def:PD weight class: extra a.c. density) | PROVED for the literal class; N^M = 2m uses R162_2602 Thm 6 CITED; strengthened conclusion "𝒜 valid ⟹ κ(ζ)=∞" | needs change: entered only as prose in "What these theorems exclude", with the R184_091 scope restriction (no quantitative property of the compact term) |
| 8 | detection law T*(a,γ) under Max–Iso; λ_min(A_T|P_T) ≤ −c e^{2aT} + C L(γ) ⇒ L^A = −∞ under Max–Iso | R184_006 Thm 1, R184_092 MAJOR-1 fix | λ_min(A_T|P_T) (eq:form on P_T), P_T via one Tate condition for even F, lem:roughEF, lem:monoT, cor:margin2 | L2 | Y: W_T on P_T = 𝔞_T; test F ∈ H¹ handled by lem:roughEF (removes the C²→C_c^∞ gap, MINOR-3); ‖F‖ bounded in T. Constants: q ≤ −0.254 M0² e^{2aT} (R184_092), C_ψ = 67K/M0² | PROVED-modulo-bookkeeping (proof text must be rewritten per R184_092); Trudgian 2014 constants CITED from memory, unverified; new bib entry | needs change: in draft with EDITOR FLAG; not to main.tex until §2 of R184_006 is rewritten and Trudgian verified |
| 9 | source/form dichotomy (R184_015 Thm 2, Cor 3) | R184_015 | λ_min(A_T|P_T); Son (CC) | L2 | Y for the lower half Q: W_T ≥ −e^{o(T)} on P_T is λ_min(A_T|P_T) ≥ −e^{o(T)} | Thm 2(i) PROVED but about M_m (non-Paper-47); "Q ⟺ RH" uses detection for ALL configurations = R162_2501 Prop 1 CITED with config-dependent constants — CONFLICTS with cor:margin2 "We do not know whether L^A = −∞ when RH fails" unless restricted to Max–Iso; no adversarial review of R184_015 in the inputs | needs change: only the Max–Iso consequence (via #8) stated, as prose |
| 10 | 𝒱_T compact (Theorem W(c)) | R184_007 Thm W(c); R184_092 | V_T (prop:finite), c_F, P_T | L2 | Y: Paper 42 w_p S_{±} ⇔ Paper 47 v_n c_F (v = 2w); generalized from 2 shifts to all of N_T (cross terms exactly 0, R184_092) | PROVED | optional addendum to prop:finite (commented block at end of draft); W(a),(b) NOT entered (= prop:finite(ii)) |
| 11 | parity symmetry, sector count (Thm A.1, Cor A.2) | R184_003; R184_091 | P_T^ev/odd | ξ and L2 | Y | PROVED, but restatement of lem:parity and thm:parityschur(o); Cor A.2(i) (ker∫ count) is two-line interlacing; "T₂ = odd crossing" downgraded to CONDITIONAL (R184_091) | N (restatement) |

## Held back (not in the draft) and why

| item | source | reason |
|---|---|---|
| CC one-direction bound R ≥ −b|v⟩⟨v| + c(I−|v⟩⟨v|), T ≤ ½log2 | R183_018 §5.1 | METRIC: holds in the ξ-metric (R183_026 §2–3), false in L2 and in X (C_ε is HS in L2); also CITED numerics of CC §6 |
| Cor 3.2 (δ = value on e^⊥; alignment ⟺ gap in ker ℓ) | R183_019 | METRIC (ξ) and a model operator R_0 of R183_017, not a Paper-47 object |
| CC index #{λ(K_I)>1} in ξ-metric; ≈4T−2 | R183_026 §3–4 | METRIC (ξ); count NUMERICAL not certified; asymptotics CONDITIONAL (Landau–Widom) |
| ε not of positive type | R183_026 §1–2 | object not in Paper 47; low band (ε̂ ≥ −m/2π) PROVED but high-frequency sign CONDITIONAL on H_dec |
| semilocal identity Son_S − Son_∞ = prime term + ∫c_h ε'_p + ∫|φ|² r_p; scaling law (Λ) | R183_025/029, R183_033 | uses CC semilocal projections Π_{S(1,b)} not defined in Paper 47; no sign; lower bound on r_p OPEN; (M)/(E′_loc) OPEN |
| n₋ → ∞ as η↓0; η₁(T) ≥ c₀/log(C/(2T−log2)); rate exp(Θ(1/η)) | R183_023 Thm 4.1, §4.2–4.3 | rests on Lemma 4.0 (|m̌(u)| ≤ C/|u|) asserted without written proof; rate CONDITIONAL |
| Prop 5.1/5.2 (Schur reduction, L-Son ⟺ coercive positivity) | R183_023 §5 | restatement of Paper 47 finite-arena/Schur mechanism |
| gap in complete form to ½log5 in ξ-metric | R183_033 §1.4 | restatement of thm:log5A/W in another metric |
| (L-Son) uniform η false; gap requirement | R183_028 §2, R183_033 §1.5 | CONDITIONAL (RH) |
| R184_003 numerics (λ₁, λ₂ tables), (M_w), Prop B.2 | R184_003 | NUMERICAL / CONDITIONAL / OPEN |
| R184_007 needle tables, interiority margins 7e-6 | R184_007 | NUMERICAL (non-converged, outer envelopes); interiority of ζ's weights itself is Paper 42 |
| A1 is E1 | R184_016, R184_094 | objects (selector, Γ_S(F), Reg⁺) not in Paper 47; four MAJOR downgrades ("⟺" → sandwich; Thm 5(ii) partly retired) |
| R184_004 Prop 2(iii)(iv) (N = 2m for large T; sup N<∞ ⟹ m<∞) | R184_004 | CITED (R162_2602 Thm 6; Yoshida statement unverified) |
| R184_015 §4 (‖Δ_T‖ ≍ e^{(2Θ−1)T}) | R184_015 | ARGUED |

## Normalization conflicts found

1. **R184_015 "Q ⟺ RH" vs Paper 47 cor:margin2(iii)** ("We do not know whether L^A = −∞ when RH fails").
   Q ⟹ RH for an arbitrary off-line configuration would answer that question; the corpus support is
   R162_2501 Prop 1 (CITED, constants configuration-dependent, no adversarial review in this input set).
   Draft states only the Max–Iso version (thm:inertia-detect gives L^A = −∞ under Max–Iso).
2. **Π_T notation (main.tex l.2316)**: written −Σ v_n c_F(log n) without Re; correct for real F only.
   Not a normalization error (v_n matches), but should read Re c_F for the L²(I_T) complex space.
3. **Metric**: R183_018 §6 / R183_024 asked for c>0 "in the norm X"; corrected by R183_026 to the ξ-metric.
   Everything entered here is L2; nothing in the ξ-metric entered.
4. Fourier sign conventions differ (R183: e^{−ist}; Paper 47: e^{iτt}); immaterial (only |F̂|² and even symbols).
5. Exact-prime-term check: R183's E_S = 𝔞_T (truncated form, no polar term), NOT W_T; R184_015's
   "E_{S(T)} = W_T on P_T" is consistent because W_T = 𝔞_T on P_T. No conflict.

---

# Part II: draft section "The semilocal Sonin decomposition at the first prime" (sec:semilocal)

Editor: same rule (checked against eq:symbol, eq:form, Γ_T and Π_T of subsec:arch, P_T, def:W/eq:nuw,
L²(I_T) metric, v_n = 2Λ(n)/√n). main.tex NOT edited. Appended to DRAFT_SECTION_INERTIA_BARRIERS.tex;
standalone compile with the main.tex preamble: OK, 8 pages total (part II ≈ 4.5 pages); only cross-refs to
main.tex and the citations are undefined (new bib keys CCquasi2020 = arXiv:2008.10974, CCM2023 = arXiv:2310.18423,
CCM2024 = arXiv:2403.01247, Simon = Trace Ideals; plus Trudgian2014 from part I).
def:W / eq:nuw are NOT used by this section (no flat-top weight enters); recorded so nobody looks for them.

Metric legend: H = u-model L²(ℝ₊,du) (≅ L²(ℝ,dt) via W); L2 = L²(I_T) (Paper 47); xi = CC ξ-metric (not used).

| # | statement | source id | Paper-47 objects used | metric | normalization verified (Y/N, how) | label | enters |
|---|---|---|---|---|---|---|---|
| II.0 | dictionary D1–D5 | R186_098 MAJOR-1 (requested), CC (61) | Γ_T, c_F, C_ε of thm:inertia-split | H ↔ L2 | Y: √2 (L²(ℝ)^ev → L²(ℝ₊,du)); CC Fourier e^{−2πixy} on even ↦ kernel 2cos 2πux; ϑ_CC(ρ)ξ(v)=ρ^{−1/2}ξ(v/ρ) vs memos' ∫h(a)a^{1/2}D_a = ϑ_CC(h̃): all three functionals symmetric under f ↦ f̃ ⇒ immaterial; f_F(e^x) = c_F(x) | definition | Y (subsec:sl-dict) |
| II.1 | Def F_S = E F_∞ E⁻¹; Mellin multiplier (1−2^{−s})/(1−2^{−(1−s)}) = ρ_2; Sonin = ran Q₁∩ran Q₂ | CCM 2310.18423 Prop 4.1; CC 2008.10974 Lemma 3.1 + main thm; R186_007 §1 (m1 of R186_094) | — | H | Y: multiplier orientation corrected per R186_094 m1; du (not d*u) per R186_093 §2 | CITED | Y (def:FS) |
| II.2 | F_∞ = I m_∞(D), F_S = I M(D), φ' = −Σ v_{2^k}cos(kt log2), multi-prime φ_S' | R186_008 Thm C, R186_010 §1, R186_096 §1 | v_n (eq:symbol) | H | Y: 2q^k log 2 = v_{2^k}; φ odd, φ(0)=0; φ_S' untruncated (truncation by supp c_F ⊂ [−2T,2T]) | CITED (CC 2008.10974) + verification | Y (lem:sl-phase) |
| II.3 | F_S unitary s.a. involution, F_Sϑ(ρ)F_S = ϑ(ρ⁻¹), real; A_S compact, ‖A_S‖<1, ±1 ∉ σ_p; A_S not HS; A_S ∈ S_p ∀p>2 | R186_009 L0/095; R186_007 §2–3/094 m8; R186_093 §5; R186_011 Sp/096 | — | H | Y (kernel 2cos, grouped sum Σ(2c_k−c_{k−1}); truncation artefact c_K removed, R186_093) | compactness CITED (CC 2008.10974 Thm 2.1/4.4) + own proof; non-HS and S_p PROVED (ours); S={∞,2} only | Y (prop:sl-AS) |
| II.4 | Tr ϑ(h)(P̂^S − P̂_∞) = Σ_{p∈S}Σ_k log p·p^{−k/2}(h(p^k)+h(p^{−k})), all λ, y ↦ h(e^y) Schwartz | R186_008 Thm C′, R186_094 m3–m5 | v_n | H | Y: = ½Σ v_{p^k}(h(p^k)+h(p^{−k})); sign + for P̂, − for 1−P̂; numerically checked R186_094 | PROVED (Simon Thm 4.5 CITED); multi-prime extension written (non-lattice h_j, Σ(1+|h_j|)|u_j|<∞); not new in substance | Y (lem:sl-linear), with attribution sentence; "unlike Connes, no o(1)" NOT entered |
| II.5 | Operator gap: cos²θ_n = λ_n², spec ⊂ {0}∪{λ_n²}∪{1}, Π_S Riesz projection, ‖(Q₁Q₂Q₁)^n − Π_S‖ = λ₁^{2n} | R186_009 H, G, D; R186_095 | — | H | Y | PROVED (ours) | Y (thm:sl-gap); link to R183_031 gap NOT entered (R186_095 M3) |
| II.6 | TC_S, TC′, T1–T3 (ϑ(f)Π_S ∈ S₁; Pϑ(f)PA_S² ∈ S₁) | R186_010/096; R186_014 T1–T3/098 | — | H | Y: CC Prop 1.5(iv) replaced by m_∞ ∈ 𝒪_M (Stirling), R186_096 | PROVED (CC Lemma D.1, Dixmier–Malliavin, Simon 4.5 CITED) | Y (lem:sl-TC) |
| II.7 | L2_S: E_S(f) = ∫f(ρ⁻¹)d_S, d_S = Σβ_j log⁺ + O_R(1), β_j = 2^{j/2}(1−2^{−j})λ²/(2 log2), b = λ²/(2log2); d_S ∈ L^p_loc ∀p<∞, ∉ L^∞_loc; divergence at 2^j | R186_012/097; R186_011 R, Q, NH, Div2/096; R186_014 T4/098 | — | H | Y: weights λ/√(1−λ²) of CC (84) (not λ²/(1−λ²) except after R-reconciliation); d_S(ρ) := d_S(ρ⁻¹) for ρ<1 (R186_098 MINOR-1) | PROVED for d_S, S={∞,2}; two MINOR gaps to write (sup_u‖G₀(u,·)‖; lacunary constant); numerics of β_j NOT entered | Y (thm:sl-L2) with EDITOR FLAG |
| II.8 | (84)_S relative form Δ | R186_014 §5–6/098 | — | H | Y: comb₂ sign: Q₂ = 1 − P̂ ⇒ −comb₂; matches Weil −ΣΛ(n)n^{−1/2}(f(n)+f(1/n)) | PROVED, every λ, no CV_S | Y (thm:sl-84(i)) |
| II.9 | (84)_S absolute form | R186_014 §7/098 MAJOR-1 | W_∞ = Γ_T (thm:inertia-split proof) | H | **conflict N1**: CC Thm 4.7 is for S(1,1) ⇒ λ = 1, not λ = ½ | PROVED at λ = 1 given CC Thm 4.7 (CITED); λ ≠ 1 CONDITIONAL | Y (thm:sl-84(ii)) with EDITOR FLAG |
| II.10 | Γ_T + Π_T^{(2)} = Son_{Π_S} − C_{ε_S}, C_{ε_S} HS on L²(I_T) ∀T; = 𝔞_T for T < ½log3; δ-finite index | R186_014 §7, R186_012 §4, R183_018 (thm:inertia-split) | Γ_T, Π_T, N_T, v_n, P_T, C_ε | L2 | Y: comb₂(f_F) = −Π_T^{(2)}(F) via v_{2^k} = 2log2·2^{−k/2}, c_F(−x) = conj c_F(x); ‖C‖²_HS ≤ 2T‖ε_S(e^{|·|})‖²_{L²(−2T,2T)}; log⁺ in ρ ≍ log⁺ in x | PROVED at λ=1 given CC 4.7; −C_{κ_S} part HS unconditional ∀λ; **n₋(−C_{ε_S}) < ∞ NOT proved** (conflict N3) | Y (cor:sl-split), δ-version only |
| II.11 | Remark: no sign; index returns at 3 for T > ½log3; enlarge S per contact; no uniform control; gap requirement; λ ≠ 1 | R186_012 §5 (S3 ARGUED), R186_095 M3, thm:inertia-nogo | Π_T^{(≠2)}, thm:inertia-nogo | L2 | Y: nogo pairs weakly null ⇒ compact part o(‖x‖²) | infinite index at T>½log3: PROVED by the proof of thm:inertia-nogo (editor, two lines); {∞,2,3}: ARGUED; S(T): OPEN | Y (rem:sl-not) |
| II.12 | attribution | R186_020 | — | — | — | — | Y (rem:sl-new) |

## Held back (part II)

| item | source | reason |
|---|---|---|
| spectrum of A_S (0.988, −0.507, …), Galerkin tables | R186_007 §5, R186_011 §3 | NUMERICAL (program rule: numerics only if strictly necessary) |
| counting law |λ_n| ≍ λn^{−1/2} | R186_008 §5 | ARGUED |
| Theorem B (R = Σ 2^{−k/2} P T (1−P) F P) | R186_008 §2 | rewriting; one-prime coincidence (fails for n = 6) |
| (Δ) for the density of Π_S via C′ | R186_008 | R186_094 M1: C′ is the linear part only |
| reduction TC_S ⟸ H_g(μ)=o(μ) | R186_009 §4 | insufficient (R186_095 M1); superseded by R186_010 |
| CV_S absolute | R186_011 | NO-GO PROVED via NH; only used implicitly (Theorem sl-84 does not need it) |
| β_j numerics, profile of ε_S, "no atom at 2" | R186_011/012 | NUMERICAL |
| moments/Jacobi integrality for S={p,∞} | R186_002 §2.4 | rederivation of CCM 2403.01247; cited, not entered |
| NO-GOs of the prolate candidates −𝔰²+λ²N_S and metaplectic | R186_003/006/093 | ours and PROVED but outside this section's chain; candidate for a separate remark |

## Normalization conflicts found (part II)

- **N1 (level λ).** R186_098 and R186_014 say "(84)_S absolute given CC Thm 4.7 at λ = ½". The CC text
  (phase-137 cc_2006.13771_text.txt l.1766) states Thm 4.7 for Sonin's space S(1,1): cut-offs |q| ≤ 1, |p| ≤ 1,
  i.e. λ = 1 in the u-model under D1. S(λ,λ) is not a dilate of S(1,1) for λ ≠ 1 (dilation maps S(1,1) to
  S(a,1/a)). Draft: absolute form at λ = 1 (CITED); λ ≠ 1 CONDITIONAL. The numerics of phase 186 (λ = ½) are
  not used. All proofs of the section are λ-uniform, so nothing else changes.
- **N2 (ϑ convention).** Memos: ϑ(h) = ∫h(a)a^{1/2}D_a d*a = ϑ_CC(h̃). Immaterial: W_∞, comb₂ and
  ∫f(ρ⁻¹)ε(ρ)d*ρ with ε(ρ⁻¹)=ε(ρ) are inversion-invariant. Also R186_008 kernel k(x)=h(e^{−x}) not h(e^x) (R186_094 m3).
- **N3 (finite index).** R186_012 row "In" / §4 and R186_014 §7: "−C_{ε_S}|P_T compact ⇒ n₋ < ∞". False as an
  inference (a compact self-adjoint operator can have infinitely many negative eigenvalues). Draft states only
  n₋(𝔞_T − Son_{Π_S} + δ) < ∞ ∀δ>0. Note n₋(𝔞_T|P_T) < ∞ is trivial anyway (thm:inertia-finite with η=1).
- **N4 (E_S ≠ 𝔞_T).** Phase-186 "E_S" for S = {∞,2} is Γ_T + Π_T^{(2)}; it equals 𝔞_T only for T < ½log3.
  The memos' "E_S = Son_S − HS for every T" is correct for E_S, not for 𝔞_T; the draft keeps them apart.
- **N5 (comb factor).** comb₂ in log2·2^{−k/2} vs v_{2^k} = 2log2·2^{−k/2}: factor 2 is the cosine
  (f(2^k)+f(2^{−k}) ↔ 2Re c_F); consistent with eq:symbol and R186_098.
- **N6 (multiplier orientation).** R186_007 §1 wrote E*E⁻¹ ↔ (1−2^{−(1−s)})/(1−2^{−s}); correct is the inverse
  (R186_094 m1); draft uses the corrected form. Unimodularity unaffected.
- Name: the HS remainder is (E′_loc)/L1′ in the R183 vocabulary, not the microlocal (M) of R183_029 (R186_097 MAJOR-2); the draft avoids "(M)".

---

# Part III: draft section "Archimedean coercivity on Tate-orthogonal blocks and the finite reduction" (sec:coer)

Editor: same rule (every statement checked against eq:symbol, eq:form (form domain 𝒟_T), eq:W, P_T, thm:A/eq:Aform,
lem:K/eq:m, thm:S(iii), lem:mbounds(i)(ii)(iii), def:PD, rem:Kprim, prop:weak, subsec:arch (𝒜_∞, Π_T), the paragraph
before lem:contA (H_T, compact resolvent, λ_A attained), lem:contA, cor:mono, thm:margin, thm:log5A). main.tex NOT edited.
File: DRAFT_SECTION_COERCIVITY_REDUCTION.tex (separate file, own guarded preamble; compiles standalone with
pdflatex: 8 pages, no errors, no overfull boxes; undefined: cross-refs to main.tex and the new bib key HLP =
Hardy–Littlewood–Pólya, Inequalities, Thm. 316 = Hilbert's integral inequality).
Sources: R186_024 §1.2–1.4, R186_025 (Lemmas 1.1–1.4, 2.1, Thms A, B, Cor. (L1), §3.2), R186_100 (Thm 3.1 form-domain
version), R186_104 and R186_105 (adversarial: what enters and with which label). Constants re-computed by the editor
(mpmath, scratchpad `consts.py`): C_A(R=2) = 1.2087+τ; C_B closed form = 1.6573/1.6957/1.7331 at τ = 0.02/0.0619/0.1,
limit 1.63994; Cor. values +0.094/+0.134/+0.281 (½log5, k=25/26/30), +0.040 (0.69, k=12), +0.070 (½log5, k=85, crude 𝒜_T).

Metric: L2 = L²(I_T) everywhere (no ξ-metric, no u-model). def:W/eq:nuw are NOT used (no dual certificate enters).

| # | statement (draft label) | source id | Paper-47 objects used | normalization / definition check (Y/N, how) | label | enters |
|---|---|---|---|---|---|---|
| III.0 | Notation: 𝔞_T = Γ + Π_T, Γ = (1/2π)∫m|F̂|² = C₀‖F‖² + 𝔈(c_F); λ_A(τ) := λ_min(A_τ|𝒫_τ) attained, continuous; 𝒩_τ = ∅ for 2τ ≤ log 2 | thm:A, subsec:arch, lem:contA | eq:form, eq:Aform, 𝒜_∞ of subsec:arch, H_T paragraph | Y: thm:A gives (1/2π)∫m|F̂|² = C₀‖F‖²+𝔈(c_F) exactly (proof of thm:A, Tonelli); Γ = 𝒜_∞ − 2AB, equal on 𝒫_T; contact set 𝒩_τ = {log n < 2τ} empty iff 2τ ≤ log 2 (eq:symbol); attainment: "H_T has compact resolvent … λ_A attained" (main.tex l.4296–4300, unconditional); lem:contA is stated for all T ∈ (0,∞), so it covers semilength τ ≤ 0.1 | definitions | Y |
| III.1 | Def 𝒱_k, E_k; Lemma decomp: 𝒱_k ⊂ 𝒫_T, 𝒱_k^⊥ = span{e_j^±} (dim 2k), dim E_k = 2k−2, 𝒫_T = 𝒱_k ⊕ E_k, E_k ⊂ 𝒟_T, 𝒟_T∩𝒫_T = (𝒱_k∩𝒟_T) ⊕ E_k | R186_024 §1.2; R186_104 row 1; R186_100 (5) | P_T (A, B of eq:form), form domain of eq:form | Y: A, B are the paper's Tate moments; independence of A, B on span{e_1^±} by the 2×2 determinant (new, written); E_k ⊂ 𝒟_T by ê = O(1/|s|) (R186_100 MAJOR-1) | PROVED | Y (lem:coer-decomp) |
| III.2 | Lemma K₁ := K − 2e^{−u/2} = 2e^{−5u/2}/(1−e^{−2u}); 0 < K₁ ≤ 1/u; K₁ = 1/u − 3/2 + O(u); cross term Γ(F+G) = Γ(F)+Γ(G) − ∫∫F(x)G(y)K(y−x) for disjoint supports; K → K₁ under one Tate condition | R186_024 §1.4; R186_104 row 2; R186_025 §3.1 | lem:K (three expressions of K), eq:Aform | Y: derived from eq:Aform with 𝒩 = ∅ (cross part of c_{F+G} for u>0 is ∫G(t)F(t−u)dt only); K₁ ≤ 1/u proved by convexity (new proof; R186_024 asserted "sup uK₁ = 1"); expansion from lem:K's sinh/cosh form. **Conflict C1 (factor 2)**: the cross term carries factor 1 for the unordered pair, i.e. the bilinear form Γ(F,G) = −½∫∫FGK; R186_104 row 2 writes "−2∫∫" and the scripts compute Q_tot = 2⟨F_B,K₁F_B'⟩ | PROVED | Y (lem:coer-K1) |
| III.3 | Lemma sector: inf of 𝔞_T over functions supported in a block of length 2τ ≤ log 2 with the block's two Tate conditions = λ_A(τ), independent of T and position; Σ_j Γ(F_j) ≥ λ_A(τ)‖F‖² on 𝒱_k | R186_024 §1.3; R186_104 row 1 | eq:Aform (translation invariance of c_F), 𝒩_τ, lem:contA paragraph | Y: c_{F(·+a)} = c_F; ∫F(·+a)e^{±t/2} = e^{∓a/2}∫Fe^{±t/2}; Π_T(F) = 0 since c_F(log n) = 0 for log n ≥ 2τ and log 2 ≥ 2τ. **C3**: the quantity is λ_A (𝒫_τ), NOT λ^prim_τ of def:PD (R186_105 §1); the draft writes λ_A(τ) throughout | PROVED | Y (lem:coer-sector) |
| III.4 | Lemma K ≥ 1/u on (0, 2] | R186_025 Lemma 1.1; R186_105 row 2 | lem:K (K = 1/(2sinh)+1/(2cosh)) | Y; proof uses the adversarial's sharper version (−tanh(u/4)/2 ≥ −u/8); range extended from (0,1.5] to (0,2] (u cosh(u/2) ≤ 4 holds to u = 2.30) | PROVED | Y (lem:coer-K) |
| III.5 | Lemma tail: ∫_{2τ}^∞K ≥ log(2/τ) + π/2 − τ | R186_025 Lemma 1.2; R186_105 row 3 | thm:S(iii) with T = τ | Y: thm:S(iii) = log coth(τ/2) + π − 2arctan e^τ; coth x ≥ 1/x; derivative −1/cosh τ ≥ −1; checked numerically (6.15600 ≥ 6.15597 at τ=0.02) | PROVED | Y (lem:coer-tail) |
| III.6 | Lemma w(s) = log(2|s|)+γ−Ci(2|s|) increasing, w(s) ≥ w(R)min(1,s²/R²) for R ≤ π | R186_025 Lemma 1.3; R186_105 row 4 | — | Y (elementary) | PROVED | Y (lem:coer-w) |
| III.7 | Lemma double Poincaré: supp h ⊂ [−1,1], h, h″ ∈ L² ⇒ ‖h″‖² ≥ π²‖h′‖² ≥ (π⁴/4)‖h‖² | R186_025 Lemma 1.4; R186_105 row 5 (MINOR: justification) | — | Y. **MINOR applied**: the sentence "∫h′=0 ⇒ second Dirichlet eigenvalue" is replaced by an explicit Dirichlet-basis argument (constraint Σ_{n odd}c_n/n = 0; Cauchy–Schwarz with S = Σ_{n≥3 odd}1/(n²(n²−4)) = ¼(4/3 − π²/8) = 0.0249, 3S < 1); this is the parity argument of R186_105 in Fourier form (constraint touches only odd n = even eigenfunctions) | PROVED | Y (lem:coer-poinc) |
| III.8 | Theorem A: λ_A(τ) ≥ C₀ + log(2/τ) + π/2 − τ + w(R)[1 − 16(R²+a)³/(27π⁴R²)], R ∈ (0,π], a = τ²/4; with R = 2: ≥ log(1/τ) − 1.209 − τ (τ ≤ 0.1), ≥ log(1/τ) − 1.31 | R186_025 Thm A; R186_105 row 6 and §6 (hand version R=2 as the PROVED one) | eq:Aform, thm:S(iii), lem:K, P_τ (Tate ⇒ Ĝ(∓iτ/2) = 0), Paley–Wiener (CITED, standard) | Y: form on 𝒫_τ is exactly eq:Aform with 𝒩_τ = ∅; scaling c_F(u) = c_G(u/τ); Plancherel as in the proof of thm:A; Ĝ(s) = ∫Ge^{isy} (paper's convention eq. l.97) so Ĝ(∓iτ/2) = ∫Ge^{±τy/2}; M_R maximum at x = (2R²−a)/3 re-derived. Hypothesis written as τ ≤ 1, 2τ ≤ log 2 (Lemma K on (0,2]); numbers for τ ≤ 0.1. Numerical inputs: w(2) = 2.1045 (Ci(4) = −0.1410, tabulated); sup over R (R = 2.165, C_A = 1.181+τ) stated as numerical in the remark | PROVED (w(2) tabulated) | Y (thm:coer-A) |
| III.9 | Remark A(2): true value λ_A(τ) = log(1/τ) − 0.510; A(3): complement of lem:contA at τ → 0, consistent with cor:mono upper bound C₀ + φ((3π/2τ)²) = log(1/τ) + O(1); A(4): extension to Kp | R186_025 §1 table; R186_104 5c; R186_105 §1 (Kp observation ARGUED) | lem:contA, cor:mono, rem:Kprim, prop:weak | Y: cor:mono gives λ_A(τ) ≤ C₀ + 𝒜_τ + φ((3π/2τ)²) with 𝒜_τ = 0; φ(x) ~ ½log x (thm:S(i), lem:mbounds(ii)) so upper bound log(1/τ)+O(1): coefficient 1 is sharp. Kp: rem:Kprim covers real F only; complex F ∈ Kp (prop:weak, Boas–Kac) not covered | (2) NUMÉRICO; (3) PROVED; (4) ARGUED, explicitly "not asserted" | Y (rem:coer-A) |
| III.10 | Lemma low-pass leakage: F ∈ 𝒱_k ⇒ ‖P_RF‖² ≤ δ(Rτ)‖F‖², δ(θ) = cosh²τ(θ²+τ²/4)²/6 | R186_025 Lemma 2.1; R186_105 row 7 | 𝒱_k (per-block Tate = orthogonality to e^{±x/2}1_B) | Y: uses only the geometry of 𝒱_k; cosh τ kept (cosh(τ/2) would suffice, R186_105) to keep the source's constants; no restriction on τ | PROVED | Y (lem:coer-lowpass) |
| III.11 | Theorem B: Γ(F) ≥ (log(1/τ) − C_B(τ))‖F‖² on 𝒱_k ∩ 𝒟_T, with C_B(τ) in CLOSED FORM: C_B = log(1/τ) − C₀δ(τ) − (2κ/3)[Φ_τ(θ*) − Φ_τ(τ)], Φ_τ elementary primitive of (θ³+aθ)ℓ(θ/τ), θ* = (√(6/κ) − a)^{1/2}; limit 1.6399; values 1.6573/1.6957/1.7331 | R186_025 Thm B; R186_105 row 8 (MINOR: closed form, uniform "≤1.74" NUMÉRICO) | eq:form with 𝒩 = ∅ (Γ = ∫m dμ), lem:mbounds(i) (m increasing on [0,∞)), eq:m (m(0) = C₀), lem:mbounds(ii) (lower bound ℓ(ρ) = log(ρ/2π) − 1/ρ − 1/(2ρ²), increasing) | Y: thm:A's form is exactly (1/2π)∫m|F̂|² (no "Tate term" in the form; Tate enters only through 𝒱_k). lem:mbounds(i) says exactly "m increasing on [0,∞)"; (ii) exactly the bound used, "increasing in τ" as stated there; m real-analytic (ψ analytic) gives the layer-cake with m′ ≥ 0 — not stated in the paper but immediate from eq:symbol. **MINOR applied**: closed form obtained by splitting m ≥ C₀ on [0,τ] (ρ ≤ 1, ℓ(1) = −3.34 > C₀) and m ≥ ℓ on [τ,θ*] (the exact max(C₀,ℓ) is transcendental in the crossover); loss < 5·10⁻⁵ on (0,0.1] (editor's check vs. quadrature with max). Hypothesis τ ≤ 1 (θ* real), no τ ≤ 0.1 needed | PROVED (closed form); the three values = evaluations; "≤ 1.74 uniform" NUMÉRICO (remark) | Y (thm:coer-B, rem:coer-B) |
| III.12 | Prop prime-form norm: |Π_T| ≤ 𝒜_T; |Re c_F(ℓ)| ≤ cos(π/(L+1))‖F‖², L = ⌈2T/ℓ⌉; ‖Π_T‖ ≤ 𝒜_T/2 for T ≤ log 2; ≤ v₂/√2 + (v₃+v₄)/2 = 1.6740 for log 2 < T ≤ ½log5 | R186_104 3a/3b (orbit of log 2 of length 3, path P₃ norm √2); R186_105 §2 (re-verified); R183_023 §2.1 fibre decomposition | Π_T (subsec:arch), v_n = 2Λ(n)/√n, 𝒩_T, lem:mbounds(iii) (crude 𝒜_T) | Y: Re c_F(ℓ) = ½⟨(S_ℓ+S_ℓ*)F,F⟩ with S_ℓ the compressed shift (eq:form: "Σ w_n(S_{log n}+S_{−log n}), w_n = Λ(n)/√n" — consistent, v_n = 2w_n); 𝒩_T = {2,3,4} for log 2 < T ≤ ½log5 (log 5 = 2T excluded, strict inequality in eq:symbol); L(T,log 2) = 3 since log5/log2 = 2.32; L(T,log3) = L(T,log4) = 2 since 2T ≤ log 5 < 2log 3; v₂/√2 = log 2. **Conflict C2**: R186_024 §3(c) claimed 𝒜_T/2 "PROVED by Cauchy–Schwarz" for all T; false for T > log 2 (R186_104 3b); the draft states the corrected bound and proves it (so "1.674 CITED" of R186_025 becomes PROVED here) | PROVED | Y (prop:coer-prime) |
| III.13 | Cor. (L1): c(T,k) ≥ log(k/T) − C_B(T/k) − ‖Π_T‖; table (½log3,8: 0.486; log2,12: 0.035; 0.69,14: 0.202; ½log5,25/26/30: 0.094/0.134/0.281; ½log5,85 with 𝒜_T: 0.070); ∀T ∃k₀(T): c(T,k) > 0 ∀k ≥ k₀ | R186_025 Cor. (L1); R186_105 row 9 | 𝔞_T = Γ + Π_T on 𝒟_T | Y: c(T,k) is inf over 𝒱_k ∩ 𝒟_T (form domain, R186_100 MAJOR-1); "for all k ≥ k₀" uses only the proved limit C_B → 1.6399; table values re-computed by the editor (agree with R186_105 to 3 digits) | PROVED (table = arithmetic) | Y (cor:coer-L1) |
| III.14 | Remark size of k₀(T): k₀ ≤ T e^{𝒜_T + C_B}, doubly exponential in T; dim E ≤ 60 on the declared range; Galerkin c larger by ≈ 1.0 | R186_025 §4, R186_105 row 9; R186_024 §2.2 | 𝒜_T | Y; "C_B within 0.1 of its limit for τ ≤ 0.1" NUMÉRICO (the limit PROVED) | PROVED / NUMÉRICO as marked | Y (rem:coer-size) |
| III.15 | Theorem reduction (Schur, form domain): with c(T,k) > 0: Lax–Milgram K: E_k → 𝒱_k∩𝒟_T; 𝔞_T(v+e) = 𝔞_T(v+Ke) + 𝔰(e); 𝔰(e) = 𝔞_T(e) − sup_u[2Re𝔞_T(e,u) − 𝔞_T(u)]; min(c,λ_S)/(1+‖K‖)² ≤ λ_A ≤ min(c,λ_S); λ_A > 0 ⟺ S_{T,k} ≻ 0; λ_A ≥ 0 ⟺ S ⪰ 0 | R186_019 Thm 3.1 as corrected by R186_100 MAJOR-1 (form domain) and MINOR-2 (sandwich, no "angle constant"); R186_024 §1.2 (any partition); R186_105 §5.1 | eq:form (form domain, λ_A as inf on 𝒫_T∩𝒟_T), lem:mbounds (𝔞_T + M ≥ 0 with M = 𝒜_T − C₀; equivalence of 𝔞_T + (M+1)‖·‖² with the H^{log} norm via lem:mbounds(ii) and m ≥ C₀), lem:coer-decomp(iv) | Y: completeness of (𝒱_k∩𝒟_T, 𝔞_T) written from the paper's form domain (no appeal to "bounded form"); E_k ⊂ 𝒟_T proved; the sandwich is R186_100 MINOR-2 with the inequality (x+κy)²+y² ≤ (1+κ)²(x²+y²) made explicit; λ_A ≤ c added (e = 0). | PROVED (algebra + Lax–Milgram); CONDITIONAL only on c(T,k) > 0, which cor:coer-L1 gives for k ≥ k₀(T) | Y (thm:coer-schur) |
| III.16 | Remark honest: localization only; λ_S ≤ (1+‖K‖)²λ_A inherits thm:margin; entries of S not closed form (correction is a sup over 𝒱, Galerkin gives upper bounds of S); interval certification realistic for T ≤ 0.6 only; fixed-k (orbit blocks, dim E = 4) not stable (c → 0.013 at 0.69) | R186_104 row 6, R186_105 §5.2; R186_024 §2.1; R186_100 §4 | thm:margin (λ_A ≤ 𝓑(T,k) → 0), thm:log5A (certified 2.5·10⁻¹²) | Y: thm:margin bounds λ_A, and λ_S ≤ (1+‖K‖)²λ_A whenever λ_S ≤ c; Galerkin direction stated correctly (sup ⇒ lower bounds of the correction ⇒ upper bounds of S); "99 % mass in E_k", "λ_S ≈ λ_A ≈ 3·10⁻¹²", "T ≤ 0.6" all marked NUMÉRICO | prose; NUMÉRICO marked | Y (rem:coer-honest) |
| III.17 | Remark NO-GO (norm route): bilinear coupling with kernel K₁ on adjacent Tate-orthogonal blocks has norm exactly π (≤ π: K₁ ≤ 1/u + Hilbert's inequality CITED HLP Thm 316; ≥ π: Weyl sequence x′^{−1/2}1_{[2τe^{−M},2τ]}, log-variable integral πM − O(1), Tate projection O(1)); quadratic coupling form 𝔮 has sup |𝔮|/‖F‖² = π/2 on the pair, ≥ π/2 on 𝒱_k; essential-spectrum obstruction (Carleman symbol π/cosh πσ, CITED); split route needs k ≥ 70 at ½log5 with Thm A vs k = 25 from Thm B; true coupling cost at minimizers 0.17–0.18, relative θ ≈ 0.22 NUMÉRICO | R186_025 §3.1–3.3; R186_104 5b; R186_105 rows 1, 1b, 11 | lem:coer-K1 (kernel and factor), lem:coer-sector, thm:coer-A, prop:coer-prime (path bound cos(π/(k+1)) for the adjacent part) | **Conflict C1 (constant)**: with the paper's normalization (eq:Aform ⇒ cross term −∫∫F_BF_B′K, factor 1 per unordered pair, bilinear Γ(F_B,F_B′) = −½∫∫) the memos' "‖𝒦₁‖ = π" is the norm of the K₁-kernel bilinear form (factor 1), and the quadratic coupling contributes π/2, not π; `r025_coupling_norm.py` computes Q_tot = 2⟨f_B,Hf_B′⟩ = twice the cross term. NO-GO conclusion unchanged (k ≥ 70 instead of the memos' ≈160, still ≫ 25, and the obstruction is spectral). "Chain ∈ [π,2π]" NOT entered (ARGUED, R186_105 1b); only "adjacent part ≤ π cos(π/(k+1))" and "non-adjacent part not estimated" | pair norm PROVED (Hilbert CITED); essential spectrum CITED (Carleman); NO-GO | Y (rem:coer-nogo) with EDITOR FLAG |
| III.18 | Remark labels | — | — | — | — | Y (rem:coer-labels) |

## Held back (part III) and why

| item | source | reason |
|---|---|---|
| (L1) split "c ≥ c_∞(T/k) − ‖𝒦₁‖ − 𝒜_T/2 positive on the grid with k = 13, margin 0.056" | R186_024 §2.3, §3 | FALSE (R186_104: 𝒜_T/2 wrong for T > log 2; ‖𝒦₁‖ ≈ 0.74 is a non-converged Galerkin artefact); superseded by thm:coer-B |
| "‖𝒦₁‖_𝒱 ≈ 0.74 independent of T and k" | R186_024 §2.3 | ARTEFACT (degree-10 Galerkin; continuum value π/2 for the quadratic form, π bilinear) |
| 4×4 uniform reduction (orbit blocks J, M, J′) | R186_019, R186_024 §1.1, §2.1 | NO-GO (c → 0.013 at T = 0.69, partition changes at log 2); only mentioned in rem:coer-honest(3) as NUMÉRICO |
| "(L2) as a finite objective with no loss", "h* is 99.9 % a piecewise Tate exponential" as structure | R186_024 §0, §3 | R186_104 row 6: approximation theory, W ≥ 0 rewritten; entered only as NUMÉRICO with that qualification |
| chain coupling norm ∈ [π, 2π] | R186_025 §3.1 | ARGUED (R186_105 1b: non-adjacent pairs not handled); not needed |
| relative bound θ_N ≈ 0.22 → θ < 1 | R186_025 §3.3 | NUMÉRICO, not proved, not needed (thm:coer-B is θ = 1 with explicit constant) |
| Carleman/Weyl-compression proof of "= π" (§3.1) | R186_025 §3.1 | CITED and redundant with the elementary Weyl sequence (§3.2); only the essential-spectrum sentence kept, CITED |
| R186_024 §1.5 (G_EE entries as digamma series) | R186_024 | no content written ("no se escribieron"); R186_026 in progress, not an input here |
| Galerkin tables (c(T,k), λ_S/λ_A, ‖K‖, ‖P_Eh*‖², mpmath checks) | R186_024 §2, R186_104 §2, R186_105 §2 | NUMÉRICO (program rule); only the three numbers needed for the remarks quoted, marked |
| refinement "C_A from 1.2 to ≈ 0.6 via certified eigenvalue of w(D) with double zero", "C_B to ≈ 1 via smooth window" | R186_025 §4 | OPEN proposals; not statements |
| extension of Thm A / Lemma 2.1 to Kp / λ^prim | R186_105 §1 | ARGUED; entered only as rem:coer-A(4) "not asserted" |
| interval-arithmetic certification plan for S_{T,k}, T ≤ 0.6 | R186_104 row 6, R186_105 §5.2 | plan, not a result; mentioned as "not attempted" |

## Normalization / definition conflicts found (part III)

- **C1 (coupling constant π vs π/2).** From eq:Aform (and equivalently from the kernel −½K(|x−y|) of m(D) off the diagonal), the cross term of Γ for two disjoint blocks is −∫∫F_B(x)F_B′(y)K(|x−y|)dxdy with factor 1 for the unordered pair, so the bilinear form is Γ(F_B,F_B′) = −½∫∫F_BF_B′K. R186_104 row 2 writes "−2∫∫F_BF_B′K", and `r025_coupling_norm.py` ("Q_tot = 2<f_B,H f_B'>", kernel K₁ with factor 1) computes twice the true cross term; R186_024/025/104/105 therefore quote "‖𝒦₁‖_{𝒱_k} = π" for a quantity whose contribution to Γ(F)/‖F‖² is π/2. The draft states: bilinear K₁-form norm = π (as in the memos), quadratic coupling sup = π/2 on the pair. The NO-GO verdict is unchanged; the memos' constants (k ≈ 160) become k ≥ 70 with Theorem A. Needs author confirmation before the grid entry is corrected.
- **C2 (prime bound 𝒜_T/2).** R186_024 §3(c) "‖P|𝒱_k‖ ≤ 𝒜_T/2 PROVED by Cauchy–Schwarz" is false for T > log 2 (R186_104 3b). Draft: prop:coer-prime with the orbit/path bound cos(π/(L+1)); = 𝒜_T/2 only for T ≤ log 2; = 1.6740 on (log 2, ½log5]. Consistent with thm:inertia-B2 of the draft section sec:inertia (exact norm 𝒜_T/2 for ½log2 < T < ½log3).
- **C3 (λ_A vs λ^prim).** c_∞(τ) of R186_024/025 is λ_min(A_τ|𝒫_τ) = λ_A(τ) (two Tate conditions on F), NOT λ^prim_τ of def:PD (two conditions on the autocorrelation, Kp of eq:Kprim, which by rem:Kprim is larger). Draft writes λ_A(τ) everywhere; Kp extension only ARGUED (rem:coer-A(4)), since rem:Kprim covers real F only while prop:weak produces Kp from arbitrary unit F via Boas–Kac.
- **C4 (thm:A form).** thm:A/eq:Aform defines 𝔞_T = C₀‖F‖² + 𝔈(c_F) − Σv_n c_F(log n) with 𝔈 using Re Φ; there is no "Tate term" in the form (the Tate conditions define 𝒫_T, main.tex l.112–113). Theorem B uses the full (1/2π)∫m|F̂|² and the Tate conditions only through 𝒱_k: consistent. The "cancellation of 2e^{−u/2}" of R186_024 §1.4 is a property of the cross term only (lem:coer-K1), not of the form.
- **C5 (lem:mbounds).** (i) states exactly "m increasing on [0,∞)" and (ii) exactly the lower bound ℓ(τ), "increasing in τ": both as used in thm:coer-B. m(0) = C₀ is eq:m at τ = 0. The layer-cake formula needs m absolutely continuous, which the paper does not state but which is immediate (m real-analytic by eq:symbol); written into the proof.
- **C6 (lem:contA coverage).** lem:contA is stated and proved for all T ∈ (0,∞) (its proof works on [T/2, 2T] for each T), so it covers λ_A at semilength τ ≤ 0.1; attainment is the unconditional sentence before lem:contA (compact resolvent). The sector lemma uses both; nothing is stretched.
- **C7 (Lemma 1.4 justification, MINOR of R186_105).** Replaced by the Dirichlet-basis argument (III.7); conclusion unchanged (π², attained by sin πx).
- **C8 (C_B closed form, MINOR of R186_105).** Given (III.11); the memos' uniform "≤ 1.74 on τ ≤ 0.1" is NUMÉRICO in the remark; τ ≤ 0.1 is not a hypothesis of Theorem B (τ ≤ 1 suffices), nor of Theorem A (τ ≤ 1 and 2τ ≤ log 2).
- **C9 (Thm 3.1 of R186_019).** Entered only in the form-domain version (R186_100 MAJOR-1) with the sandwich bound (MINOR-2); the "bounded form" and "angle constant" phrasings are not used. Its hypothesis (L1) is discharged by cor:coer-L1 (so it is no longer CONDITIONAL for k ≥ k₀(T)).
- Fourier convention: the paper's F̂(τ) = ∫Fe^{iτt} (l.97) is used; the Tate zeros are at ∓iτ/2 accordingly; immaterial for all |·|² quantities.
- Π_T notation (main.tex l.2316, no Re): same flag as part I.

## Decisions needed (part III)

1. Confirm C1 (π → π/2 for the quadratic coupling) with the authors of R186_024/025/104/105 and correct the grid entry for the NO-GO constant; the draft carries an EDITOR FLAG.
2. Whether sec:coer enters Paper 47 as a section (8 pages) or whether only Theorems A, B and the reduction theorem enter (≈ 4 pages), the remarks going to the grid.
3. Whether the NUMÉRICO facts quoted in the remarks (λ_A(τ) ≈ log(1/τ) − 0.510; λ_S ≈ λ_A ≈ 3·10⁻¹²; 99 % mass in E_k; coupling cost 0.17) stay in the paper or go to the grid only (program rule: numerics only when strictly necessary).
4. New bib entry HLP (Hardy–Littlewood–Pólya, Inequalities, Thm. 316); the Carleman symbol π/cosh πσ is CITED without a source (Carleman 1923) — add a reference or drop the sentence.


---

# Part IV: draft section "The window form as a truncated Wiener–Hopf operator: inertia crossings, prolate reduction and moment bounds" (sec:wh)

Editor: same rule (every statement checked against eq:symbol, eq:form (form domain 𝒟_T), eq:W, 𝒫_T (A, B), thm:A/eq:Aform,
lem:K, lem:mbounds(i)(ii)(iii), lem:monoT, lem:contA and the paragraph before it (H_T compact resolvent, λ_A attained, J),
prop:NC (S_{T,τ₁}, normalization (1/2π)∫_{|τ|≤τ₁}|F̂|²), lem:parity (n₋), prop:band(i)–(iv), prop:negtrace (Pos_T on 𝒟_T, Neg_T on
L², τ_last, λ₀ < 1 in the proof of (v)), thm:W, lem:roughEF, thm:parityschur(o)(a1)(a4), prop:polarcap, lem:polar, thm:log5A,
thm:log5W, thm:margin). def:W/eq:nuw and def:PD are NOT used (no certificate, no λ^prim enters); recorded so nobody looks for them.
main.tex NOT edited (sections 16–18 were integrated there by another run; this draft stays a separate DRAFT for decision).
File: DRAFT_SECTION_WIENER_HOPF_STRUCTURE.tex (own guarded preamble; pdflatex: 10 pages, 0 errors, 0 overfull boxes;
undefined: cross-refs to main.tex, to the drafts sec:inertia (thm:inertia-quartet) and sec:coer (thm:coer-schur), and the bib key Zhu2026).
Sources: R186_042 (Thm 2.1, 2.2, 2.3, Prop 2.5), R186_043 (Lemma M0, Cor M0-step) + adversarial R186_115, R186_044 (Thm 1, Thm 2, Lemma Q,
Prop K; Lemma P ARGUED only), R186_045 (Lemmas T, T′), R186_047 (Lemmas 1–3, Thm L-W) + adversarial R186_116, R186_048 (Lemmas 3.1, 2.3),
R186_049 (Prop 2.1), R186_028 (Thm 1.2, Cor 1.3, Thm 1.4, Thm 2.1) + adversarials R186_106/107, R186_034 (Thm 2.1(i), bound (iv)).
Metric: L2 = L²(I_T) everywhere; forms on 𝒟_T when unbounded (Pos_T, 𝔞_T, 𝔞^{(U₀)}), on L² when bounded (Neg_T, S_E, H_T).

| # | statement (draft label) | source id | Paper-47 objects used | normalization / definition check (Y/N, how) | label | enters |
|---|---|---|---|---|---|---|
| IV.0 | Notation: R_T, f(D), Pos_T/Neg_T, S_E (= S_{T,τ₁} for E = [−τ₁,τ₁]), tr S_E = T|E|/π, U_T with SYMMETRIC components E₀ = (−a₀,a₀), E_i = J_i ∪ (−J_i), n_T, s_i, Π, J, h*, λ_A(T) | prop:negtrace, prop:NC, prop:band, paragraph before lem:contA | — | Y: ⟨R_Tf(D)R_TF,F⟩ = (1/2π)∫f|F̂|² matches eq:form; tr S_{T,τ₁} = 2Tτ₁/π (prop:NC) ⇒ T|E|/π; the memos' Shannon number N_i = T|J_i|/π = ½ tr S_{E_i}; prop:band(iv) "first interval contains 0" ⇒ E₀ symmetric | definitions | Y |
| IV.1 | Lemma c_P: Pos_T(F) ≥ c_δ(1−λ₀(δ))‖F‖²; c_P > 0; 𝔭 ≥ c_P on 𝒫_T; 𝔭^{1/2} bijection 𝒫_T∩𝒟_T → 𝒫_T | R186_034 Thm 2.1(i) | prop:band(i)(iv), lem:mbounds(ii)(iii), proof of prop:negtrace(v) (λ₀ < 1), paragraph before lem:contA | Y: σ_T > 0 beyond τ_last and → +∞; closedness of Pos on 𝒟_T from lem:mbounds exactly as the paper does for 𝔞_T | PROVED | Y (lem:wh-cP) |
| IV.2 | Def B_T = 𝔭^{−1/2}𝔫𝔭^{−1/2} on 𝒫_T (trace class); σ_β = σ₊ − σ₋/β; W_T(σ_β) = Pos − Neg/β on 𝒫_T∩𝒟_T; n₋ as in lem:parity | R186_034 Thm 2.1(ii)(iii); R186_042 Thm 2.1; R186_043 §2 | prop:negtrace(i), lem:parity | Y: pencil built on the COMPRESSION 𝔭 (Pos^{1/2} does not preserve 𝒫_T). **C-W5:** thm:W says no Wiener–Hopf INDEX exists for σ_T − λ; draft uses the name only for the shape R_Tf(D)R_T and says so | definition | Y (def:wh-B) |
| IV.3 | Thm inertia crossings: (i) identity via 𝔭^{1/2}; n₋(W_T(σ_β)|𝒫_T) = #{β_j > β}, jumps at β_j; n₋(𝔞|𝒫_T) = #{β_j > 1}; λ_A > 0 ⟺ β₁ < 1; λ_A ≥ 0 ⟺ β₁ ≤ 1. (ii) 1−β₁ = inf 𝔞/Pos = ε*/(1+ε*). (iii) λ_A/Pos(u₁) ≤ 1−β₁ ≤ λ_A/Pos(h*) ≤ λ_A/c_P. (iv) n₋(𝔞|𝒫_T) ≤ #{ν_j(𝔫) > c_P} | R186_042 Thm 2.1; R186_043 §2; R186_034 Thm 2.1(iv), 2.2, §2.3 | prop:negtrace(iv), lem:parity | Y (Sylvester in form sense). **Conflict C-W1:** R186_034 writes "λ_A ≤ (1−β_max)Pos(h*)" and the interval [λ_A/Pos(h*), λ_A/c_P]; correct: lower end with the PENCIL extremal u₁, upper end with h*; numbers unchanged (u₁ ≈ h*) | PROVED | Y (thm:wh-pencil), EDITOR FLAG |
| IV.4 | Remark: last-crossing reading; counting theorems (Landau–Widom) do not locate β₁ (CITED, unused); counts 4/10 vs 37/54; 1−β₁ = 1.7e-11 at ½log5 | R186_042 §2, R186_034 §2.3 | prop:NC, thm:log5A | Y | prose; NUMÉRICO marked | Y (rem:wh-pencil) |
| IV.5 | Prop eigenbasis of Neg: φ_k (ν_k>0) ∈ 𝒟_T; 𝔞 = Σ P_{kl}a_kā_l − Σν_k|a_k|²; variational 1−β₁ | R186_042 Thm 2.2 | prop:negtrace(i), eq:form | Y: φ_k ∈ 𝒟_T proved; ker Neg part of the basis needed (memo silent). Numerical check NUMÉRICO in prose | PROVED (basis change) | Y (prop:wh-basis) |
| IV.6 | Thm constant weights: 𝔫/𝔭 = (s₋/s₊)cot²φ(Qu), φ = angle to ran Q₋; sup = (s₋/s₊)cot²φ_min; n₋ = max dim{‖Q₋v‖² > θ‖v‖²}, θ = s₊/(s₊+s₋) | R186_042 Thm 2.3 | — (model) | **Conflict C-W2 (sign slip):** Q₋ − βQ₊ = ½[(1−β)Q + (1+β)J], memo wrote −(1+β)J, hence "tan²φ_j" should be cot² (angle to ran Q₋); memo's Cor 2.4 is the correct cot² form; proof rewritten without Halmos | PROVED (corrected) | Y (thm:wh-angles), EDITOR FLAG |
| IV.7 | Cor no gap: commutation, β_j = (s₋/s₊)λ_j/(1−λ_j), n₋ = #{λ_j > θ}; interlacing on 𝒫_T by ≤ 2 | R186_042 Cor 2.4, Lemma 3.1 | prop:NC | Y | PROVED | Y (cor:wh-nogap) |
| IV.8 | Prop not-angles: εσ₊ − σ₋ keeps U_T, σ₋, all angles; β₁/ε | R186_042 Prop 2.5 | prop:negtrace(v) in prose | Y: memo's route via negtrace(v) changes the negative set (σ1_band − c1_off is negative off-band); replaced by scaling, same conclusion; M0/M2/M3 values NUMÉRICO | PROVED | Y (prop:wh-notangles) |
| IV.9 | Lemma Kreĭn rank one: β₁ ≥ ν⟨𝔭⁻¹ψ,ψ⟩ (= for rank one); ⟨𝔭⁻¹ψ,ψ⟩ = sup|⟨u,ψ⟩|²/𝔭(u) = 1/inf_{u⊥ψ}𝔭(ψ+u); rank-one positivity ⟺ ν⟨𝔭⁻¹ψ,ψ⟩ < 1 | R186_043 Lemma M0(i)(ii); R186_115 §1.1 | — | **C-W3:** memo presents the rank-one value as "deciding the sign"; for rank > 1 it is a LOWER bound (necessary condition). "λ₂/λ₀ < 1e-3" (false) and κ not entered | PROVED | Y (lem:wh-krein), EDITOR FLAG |
| IV.10 | Cor one interval/step: β_j = (a/b₀)λ_j/(1−λ_j); positivity iff aλ₀ < b₀(1−λ₀); sandwich b₀(1−λ₀) ≤ inf_{u⊥ψ}Pos(ψ+u) ≤ (1/2π)∫_{ℝ∖E}b|ψ̂|² | R186_043 Cor M0-step, M0(iii) | prop:NC | Y (order of multipliers) | PROVED | Y (cor:wh-step) |
| IV.11 | Remark model: b₀ = 0 for σ_T; level minorants indefinite; slope law κ ∈ [0.55,1.24] fitted; sub-Shannon components, λ₀(S_{U_T}) ∈ [0.76,0.88]; plateau asymptotics CITED, unused | R186_042 §1, §3; R186_043 §3, §7; R186_115 | — | Y | prose; NUMÉRICO/ARGUED/CITED marked | Y (rem:wh-model) |
| IV.12 | Def V_T (index-0 prolates per component and parity), V_T^P = ΠV_T, W_T, H_T, A_WW, A_VW, C_T; variant V′ | R186_044 §2; R186_047 §2 | prop:band, prop:NC, J, Π | Y: S_{E_i} commutes with J only because E_i is symmetric (IV.0). **C-W4 (R186_115 MAJOR-2):** R186_043 defined V ∩ 𝒫_T, computed ΠV; draft uses ΠV | definition | Y (def:wh-V), EDITOR FLAG |
| IV.13 | Lemma: V_T, V_T^P ⊂ 𝒟_T; W_T = 𝒫_T ∩ V_T^⊥; J-invariance | R186_047 Lemma 1 | eq:form, lem:contA paragraph | Y | PROVED | Y (lem:wh-W) |
| IV.14 | Thm necessary: λ_A ≤ λ_min(H_T), n₋(H_T) ≤ n₋(𝔞|𝒫_T), sup_{V^P}Neg/Pos ≤ β₁ | R186_044 Thm 1; R186_115 §3.4 | — | Y | PROVED | Y (thm:wh-necessary) |
| IV.15 | Lemma Neg on W_T: Neg ≤ min{max_±Σs_iλ₁^{(i),±}, ‖Σs_iS̃_{E_i}‖}; variant ν₁ on W′ | R186_047 Lemma 2, 2′; R186_116 §1.2 | prop:negtrace | Y: max_± Σ_i (sharper than memo's Σ_i max_±, same proof); s_i by grid not a rigorous sup (R186_116 MINOR-3): constants only | PROVED | Y (lem:wh-neg) |
| IV.16 | Lemma Pos by layers: L_s bounded finite union; S̃_{L_s} ⪰ 0 nondecreasing; Pos ≥ Σ(s_{k+1}−s_k)(1−μ̄(s_{k+1}))⁺ | R186_047 Lemma 3; R186_116 §1.1 | prop:band(i)(iii), lem:mbounds(ii), eq:form | Y: layer-cake against μ_F. **R186_116 MINOR-1 applied:** "exact at s = 0" NOT claimed | PROVED | Y (lem:wh-pos), EDITOR FLAG |
| IV.17 | Thm L-W: 𝔞 ≥ c_W = Pos_lb − Neg_ub on W_T∩𝒟_T (and W′); class-wide | R186_047 Theorem; R186_116 | — | Y | PROVED (inequality with defined constants) | Y (thm:wh-LW) |
| IV.18 | Thm exact Schur: 𝔰_T = H_T − 𝔠_T; λ_A > 0 ⟺ 𝔰_T ≻ 0 ⟺ [A_WW ≥ c>0] ∧ [H_T ≻ 0] ∧ [ρ_T < 1]; sandwich; 1−ρ_T ≤ λ_S/λ_min(H_T) ≤ (1+‖K‖)²λ_A/λ_min(H_T) | R186_044 Thm 2; R186_115 §5; R186_116 §1.5 | thm:coer-schur (draft sec:coer, now in main.tex §16–18 per coordinator), lem:mbounds | Y: hypotheses of the form-domain Schur verified; Haynsworth + IV.9 for the pencil (𝔠_T, H_T); inheritance of 1−ρ_T written explicitly (new, two lines) | PROVED (conditional on A_WW ≥ c > 0) | Y (thm:wh-schur) |
| IV.19 | Remark numbers: c_W Galerkin 0.41/0.34/0.49 (V′ 0.55/0.40/0.53) NUMÉRICO; certified 0.136/0.201 (V), 0.594/0.548/0.318 (V′) "PROVED modulo convergent floating quadrature"; 0.004 unused; equivalence only at the three windows; 1−ρ_T, λ_min(H_T), blind window δ_A < δ < δ_V, index-1 prolates ⇒ H_T ≈ λ_A, ‖A_VW‖, ‖𝔠_T‖ (NUMÉRICO) | R186_047 §3; R186_116 §1.4–1.5; R186_044 §2,§4; R186_115 §3 | — | Y; README round 21 lacked the quantifier (R186_116 MAJOR-1 bis): draft says "only at T ∈ {½log3, log 2, ½log5}" | prose; labels marked | Y (rem:wh-LWnum) |
| IV.20 | Lemma Q: Q_z = 4|Φ_c|² − 4|Φ_s|², inertia (2,2), parity form, Φ_s = δ∫Fte^{iγt} + O(δ³) | R186_044 Lemma Q; R186_114 §1.1 | eq:W (Φ_F); thm:inertia-quartet (sec:inertia) restated | Y: three-line proof (new); Q_z defined algebraically, no modified ξ needed | PROVED | Y (lem:wh-Q) |
| IV.21 | Prop K: on finite X with 𝔞|X ≻ 0: (𝔞+Q_z)|X ≻ 0 ⟺ 4S_XH₊⁻¹S_Xᵀ ≺ I₂ | R186_044 Prop K | — | Y (IV.9, rank ≤ 2); Lemma P ARGUED: one sentence, not entered | PROVED | Y (prop:wh-K) |
| IV.22 | Lemma moments: β₁ ≤ m_k^{1/k} ↓ β₁; β₁ < 1 ⟺ ∃k m_k < 1 | R186_045 §3.2 | — | Y | PROVED | Y (lem:wh-mom) |
| IV.23 | Lemma T: B′ = B + (1−β₁)v₁⊗v₁; |m_j(B′)−m_j(B)| ≤ j(1−β₁) ≤ jλ_A/c_P; Lipschitz margin ≤ Lk(1−β₁) | R186_045 Lemma T | — | Y: uses λ_A/c_P (C-W1), not Pos(h*) | PROVED | Y (lem:wh-T) |
| IV.24 | Lemma T′: L-Lipschitz universal criterion ⇒ Φ(𝔞) ≤ Lλ_A | R186_045 Lemma T′ | lem:contA paragraph (h* attained) | Y: hypotheses made explicit; class-criteria caveat kept | PROVED | Y (lem:wh-Tprime) |
| IV.25 | Remark moments: k* = 20/10⁵/10¹⁰; m_k^{1/k} ∈ [1.06,6.7]; D_B series; class criteria not covered | R186_045 §3.3–3.4; R186_034 | — | Y | prose; NUMÉRICO | Y (rem:wh-mom) |
| IV.26 | Prop old/new: 𝔞 = 𝔞^{(U₀)} − Neg^{new}; λ_A ≥ 0 ⟺ 𝔞^{(U₀)} ≥ Neg^{new}; with 𝔞^{(U₀)} ≥ c>0: λ_A > 0 ⟺ β_new < 1 etc.; sandwich | R186_049 Prop 2.1 | prop:band, eq:form | Y: identity of multipliers + IV.3; memo's "⟺ [𝔞^{(U₀)} ⪰ 0] ∧ [β_new ≤ 1]" stated only when 𝔞^{(U₀)} ≥ c > 0 (β_new undefined otherwise) | PROVED | Y (prop:wh-oldnew) |
| IV.27 | Lemma contact threshold: Re c_F(log n) = 0 on L²(I_{T_n}); form unchanged; continuity | R186_048 Lemma 3.1 | eq:symbol (𝒩_T strict), lem:monoT (its proof), lem:contA | Y: Plancherel ĉ_F = |F̂|²; honest label: restatement of lem:monoT's proof | PROVED (restatement) | Y (lem:wh-birth) |
| IV.28 | Lemma newborn Shannon < ½: |J| < π/log n, T_n|J|/π < ½, tr S_{J∪(−J)} < 1 | R186_048 Lemma 2.3 | eq:symbol | Y | PROVED | Y (lem:wh-shannon) |
| IV.29 | Prop index by sectors: (i) count identity; (ii) T ≤ ½log5: n₋(odd) = 0, n₋(ev) ≤ 1, 𝔞 ≥ 1e-18 on ker ℓ_ev ⊋ 𝒫_T; if 𝔞(φ_ev) < 0 then n₋ = 1 even, 𝔤_ev < 2; (iii) 𝔞(φ_ev) ≤ Γ_T(φ_ev) explicit | R186_028 Thm 1.2, Cor 1.3, Thm 1.4; R186_106/107 | thm:parityschur(o)(a1), prop:polarcap, thm:log5W, lem:monoT, eq:Aform, subsec:arch | Y: (i) for 𝔞_T only (paper proves (a1) for 𝔞_T; Γ version not entered). (ii) uses the paper's thm:log5W, NOT Zhu (C-W10). **C-W6:** three decompositions (sign/components/parity) kept distinct; the even polar direction of the index is never identified with the component E₀ | PROVED; "n₋ = 1" modulo IV.30 | Y (prop:wh-index) |
| IV.30 | Remark index: Γ_T(φ_ev) < 0 for T ≥ 0.12 (NUMÉRICO 1-D); not a lever (Cor 1.3(iii)); polar resolvent spec {2/(𝔤_ev−2), 2/(𝔤_odd+2)}, the −1 explained | R186_028 Cor 1.3(i), Thm 2.1, §3; R186_106 (★) | prop:polarcap, thm:parityschur(a4), lem:polar | Y: hypotheses (invertibility, σ_par ≠ 0) stated; memo's "PROVED mód. CITED" becomes "PROVED modulo 1-D NUMÉRICO sign" | prose; NUMÉRICO marked | Y (rem:wh-index) |
| IV.31 | Remarks labels / what is not asserted | — | thm:log5A, thm:margin | — | — | Y |

## Held back (part IV) and why

| item | source | reason |
|---|---|---|
| R186_042 Lemma 2.6 (Nazarov–Jaming plateau bound for unions) | R186_042 | CITED with unverified universal constant; not on the list; lem:wh-cP gives c_P > 0 without it |
| R186_042 Lemma 3.1 asymptotic (one-interval model negative for large c) | R186_042 | CITED asymptotic; model only |
| R186_042 §3.2–3.3 tables, §4 Prop 4.1 (Gauss quadrature NO-GO) | R186_042 | NUMÉRICO / NO-GO of a question |
| R186_043 M0-slope law, Lemma M1 | R186_043; R186_115 MAJOR-1 | ARGUED/NUMÉRICO (κ fitted); M1 false for n ≥ 3 as written, superseded by exact H_T |
| R186_043 §5–6 (local margins, span condition "sees M₁") | R186_043; R186_115 MAJOR-2/3 | NUMÉRICO; only the detection threshold quoted |
| R186_044 Lemma P, δ_A formula, V/W cancellation mechanism, §3 (D − G) | R186_044 | ARGUED + NUMÉRICO; the NO-GO is covered by Lemma T′ |
| R186_045 §1 (Kreĭn flow, Lemma 1.1), §2 Theorem X | R186_045 | Galerkin-only; Theorem X CITED-NOT-VERIFIED (R186_116 MINOR-6), belongs with R186_046 |
| R186_047 Gram/HS cross-leakage bound; certified-version HS formulae | R186_047 §2.3 | computational devices; only the constants quoted with their label |
| R186_048 Lemmas 2.1, 3.2, Prop 2.2, Obs 2.4, Prop 4.3, migration tables | R186_048 | trivial / NUMÉRICO / not on the list; Prop 4.3(i) inherits (one sentence) |
| R186_049 Props 2.2, 2.3, Lemma 3.4, tables | R186_049 | hypothesis numerically false / NO-GO / CITED asymptotic / NUMÉRICO |
| R186_028 Lemma 4.2, §4.3 (A_∞ dies at ≈ 0.37), Prop 3.1 as a route | R186_028 | outside the chain; NUMÉRICO (grid candidate: "A_∞ indefinite from ≈ 0.37 NUMÉRICO, PROVED from 0.4608"); NO-GO route |
| R186_034 Thm 3.1, Thm 4.1 | R186_034 | not on the list; covered by Lemma T′ |

## Normalization / definition conflicts found (part IV)

- **C-W1 (orientation of the pencil sandwich).** R186_034 Thm 2.1(iv)/2.2 mix the two extremals. Correct: λ_A ≥ (1−β₁)Pos(h*) and
  λ_A ≤ (1−β₁)Pos(u₁), u₁ the pencil extremal; hence λ_A/Pos(u₁) ≤ 1−β₁ ≤ λ_A/Pos(h*) ≤ λ_A/c_P. Numbers unchanged (u₁ ≈ h*).
  R186_049 Prop 2.1 already has the correct orientation.
- **C-W2 (sign slip in R186_042 Thm 2.3).** Q₋ − βQ₊ = ½[(1−β)Q + (1+β)J]; pencil eigenvalues are (s₋/s₊)cot²φ_j (angles to
  ran Q₋), not tan²; the memo's Cor 2.4 is the correct cot² form, so Thm 2.3 and Cor 2.4 of the memo are mutually inconsistent.
- **C-W3 (rank-one Kreĭn value is a lower bound).** R186_115 §1.1; entered as necessary condition (lem:wh-krein(i)).
- **C-W4 (V ∩ 𝒫_T vs ΠV).** R186_115 MAJOR-2; draft uses ΠV and W_T = 𝒫_T ∩ V^⊥.
- **C-W5 ("Wiener–Hopf").** thm:W: no WH index for σ_T − λ; draft uses the name only for the shape R_Tf(D)R_T and inertia.
- **C-W6 (sign / components / parity decompositions).** prop:negtrace (Pos/Neg), R186_047/044 (Neg = ΣNeg_{T,i} ≤ Σs_iS_{E_i}),
  thm:parityschur (𝒬^{par}, h_par, 𝔤_par) kept with distinct symbols; the even polar direction of the index (≈ cosh(t/2)1_I) is a
  direction in L²(I_T), the polar component E₀ is a frequency interval: never identified. "Tate kills/projects the polar mode"
  (R186_043 §5(a), R186_044 §3.1) is NUMÉRICO about ψ₀⁺ and not entered.
- **C-W7 (symmetric components; Shannon number).** Memos: J_i ⊂ (0,∞), N_i = T|J_i|/π; paper: S_{T,τ₁} symmetric, tr = 2Tτ₁/π.
  Draft: components of U_T ⊂ ℝ, tr S_{E_i} = T|E_i|/π = 2N_i; newborn lemma as tr S_{J∪(−J)} < 1. No factor lost; the parity
  sectors of S_{E_i} exist only because E_i is symmetric.
- **C-W8 (normalization of the prolates).** ψ_i^± unit eigenvectors of S_{E_i} in a parity sector of L²(I_T) (not PSWF on ℝ);
  V_T^P = ΠV_T is not orthonormal (R186_044's H_T is "the matrix in an orthonormal basis"; the draft treats H_T as a form).
  R186_047's "certified" constants use the Galerkin (Legendre) prolates ψ^{(M)}: a different explicit complement W^{(M)}; said in rem:wh-LWnum(1).
- **C-W9 (𝒫_T with two Tate conditions).** Pencil on the compression 𝔭 = ΠPos_TΠ (two Tate conditions); models IV.6–IV.10 on
  L²(I_T) (no Tate), transferred by interlacing; R186_028 index statements on 𝒟_T (no Tate) or ker ℓ_ev (one Tate). The draft
  names the space in every statement.
- **C-W10 (which theorem certifies W_T ≥ 0 on L²).** R186_028 Thm 1.4 cites Zhu ≤ 0.8 and thm:log5W; the range [0.12, ½log5] is
  covered by the paper's own thm:log5W + lem:monoT; Zhu (cor:KEP08) not used. R186_106's "not certified for T > ½log2" was corrected by R186_107.
- **C-W11 (R186_116 MINOR-1).** "μ̄(0) exact" false (non-orthogonal ψ across components, 15 % at log 2); lem:wh-pos is a bound.
- Fourier convention F̂(τ) = ∫Fe^{iτt} (l.97): immaterial for all |·|² quantities. Π_T notation without Re (l.2316): same flag as parts I/III.

## Decisions needed (part IV)

1. Confirm C-W1 and C-W2 with the authors of R186_034/042 and correct the memos/grid entries quoting "tan²φ" or the interval
   [λ_A/Pos(h*), λ_A/c_P]; no number changes.
2. Title: keep "truncated Wiener–Hopf operator" (with the C-W5 disclaimer) or rename to "truncated convolution operator".
3. Whether sec:wh enters Paper 47 as a section (10 pages) or only thm:wh-pencil, thm:wh-angles, lem:wh-krein, thm:wh-LW,
   thm:wh-schur, lem:wh-T/T′, prop:wh-index (≈ 5 pages), the model corollaries and remarks going to the grid. (Sections 16–18
   are already in main.tex; this draft is separate and references thm:coer-schur and thm:inertia-quartet there.)
4. Whether the c_W constants "PROVED modulo floating quadrature" stay in the paper, and whether an interval-arithmetic
   certification of c_W at ½log3 and log 2 is commissioned (would make "λ_A > 0 ⟺ C_T ∧ ρ_T < 1" PROVED at those windows
   without the quadrature caveat; C_T itself stays NUMÉRICO).
5. Whether the 1-D sign Γ_T(cosh(t/2)1_I) < 0 on [0.12, ½log5] is certified by interval arithmetic (closed form in R186_026
   (1.3)–(1.5)), making "n₋(𝔞_T|𝒟_T) = 1 on [0.12, ½log5]" PROVED outright.
6. Whether "𝔞_T ≥ 1e-18 on ker ℓ_ev (one Tate condition) for T ≤ ½log5" (prop:wh-index(ii), corollary of thm:log5W +
   thm:parityschur(o)) is worth a line after thm:log5W in main.tex (strengthens thm:log5A's space from 𝒫_T to codimension one).
7. Cross-references to thm:coer-schur and thm:inertia-quartet (now in main.tex §16–18): verify the label names survived the
   integration before \input-ing this draft.
