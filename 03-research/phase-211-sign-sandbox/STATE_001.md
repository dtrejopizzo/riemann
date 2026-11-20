# State of phase 211 after rounds 1–3

Sources: README.md, STATEMENT_001.md, DOSSIER_001.md, SURVEY_001.md, AUDIT_001–003.md, LITERATURE_001.md,
BRIEF_CONSTRUCTOR.md, ROUND_001_A–D.md, ROUND_002_A, B, D, E.md (there is no ROUND_002_C), ROUND_003_A.md,
ROUND_003_B.md, REVIEW_001.md (statement and dossier), REVIEW_002.md (round 1), REVIEW_003.md (round 2 and
ROUND_003_B), LEDGER.md. Round 2 and ROUND_003_B labels below are the REVIEW_003 verdicts (CONFIRMED read as PROVED,
DOWNGRADE read as the label given); ROUND_003_A has not yet been reviewed and its labels are the constructor's own,
marked "unreviewed". Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. The target is treated
as a statement about one quadratic form; no equivalence of it with any statement outside STATEMENT_001 is used.

---------------------------------------------------------------------------------------------------------------------
## 1. The target and its reduced forms

(★) λ_A(T) ≥ 0 for every T > 0, with λ_A(T) = inf{a_T(F) : F ∈ P_T, ‖F‖ = 1}, a_T = Arch − Π (STATEMENT_001 §1).
Known: PROVED (certified) for T ≤ ½log5; CITED T ≤ ½log15 (Mori, unrefereed), T ≤ 17/16 (Liu, preprint). OPEN beyond.
LITERATURE_001: no new certification or method beyond ½log15.

Internal reformulations in use (all internal moves, STATEMENT_001 §5):

| Form | Statement | Label | Where |
|---|---|---|---|
| (L2) | S_{T,k} ⪰ 0, finite Schur matrix of dimension 2k−2 | PROVED equivalence | P47 §coer; DOSSIER §1.2 |
| (S) | 𝔸_M = Arch_M − Div_M − Near_M ⪰ 0 for all M (2T_0 < log 2, ‖F_0‖ = 1) | PROVED equivalence | P47 prop:AM; STATEMENT §2 |
| (B) | B(d) = ⟨F_0, a V_d F_0⟩ positive definite on ℝ; for d > 2T_0, B(log x) = −x^{−1/2}ΣΛ(n)φ(n/x) − Σ_{j≥1}γ_j x^{−(2j+½)}, ∫φ = ∫φ/y = 0 | PROVED equivalence (P47 thm:oneprofile); the Chebyshev form is CITED from P47 lem:transl(iv), thm:band (REVIEW_001 1.3(ii)) | STATEMENT §2–3 |
| Band | (★) ⟹ \|B(d)\| ≤ B(0) for d > 2T_0: a necessary 2×2 condition without sign | PROVED (Bochner) | STATEMENT §3; REVIEW_001 |
| (L2′) | For every shift α, gauge c and η ∈ (0, η_0]: λ_A(T) ≥ 0 ⟺ S ⪰ 0 on N′ = pr_T span{shifted Nyquist modes with s^{α,c}_k ≤ 0}; complement coercive with c_* = ½(s^e_+ + s^o_+); dim N′ ≤ \|𝒩\|, and \|𝒩\| ≥ n_−(a_T on L²(I_T)) | PROVED (REVIEW_002 §3: CONFIRMED) | ROUND_001_C Thm 1 |
| (L2′) at ½log5 + ε | 𝒩 = {0, ±3, ±5, ±9, ±14, ±23}, \|𝒩\| = 11 at gauge c ≈ 1.22 | NUMERICAL (structure PROVED, membership NUMERICAL until certified; REVIEW_002 §3) | ROUND_001_C §4; ROUND_002_A §1 |
| Candidate-I split | (★) at T ⟺ Θ_T ≥ 0 ∧ 1 ∈ J_T, where Θ_T = inf{Arch(F) : F ∈ S_T, Π(F) = 0} = max_c λ_A(T; cΛ) and J_T = {c : λ_A(T; cΛ) ≥ 0} is a closed bounded interval, non-empty iff Θ_T ≥ 0 | PROVED (complex space; Toeplitz–Hausdorff, Brickman covers the real case) | ROUND_002_D Thm 1 |
| Cone form of (I.a) | Θ_T(w) ≥ 0 ⟺ the line ℝw meets the compact convex body 𝒦_T = {w : λ_A(T; w) ≥ 0} | PROVED | ROUND_002_E Lemma 2 |
| Schur-suppression | (★) ⟺ t*_M = 0 ∀M, where {t : 𝔸_M ∘ [e^{−tδ}] ⪰ 0} = [t*_M, ∞) | PROVED; restatement only, no information gained from t > 0 | ROUND_003_B Prop 5 |

Dimensions of (L2′) after gauge/shift optimisation: 5, 9, 11, 11, 41, 125, ≈685 at T = ½log3, log2, ½log5^±, 1, 1.25, 1.5
(NUMERICAL, ROUND_001_C); the non-positive Nyquist set grows superlinearly in T (NUMERICAL; O(T) not proved). The dossier's
proposal of (L2′) as "smaller and already proved" was REFUTED as stated by REVIEW_001 §2(h) (same order as (L2) from the
proved bound); ROUND_001_C supplies the exact η ↓ 0 reduction and the numerical dimensions, not a proved smaller bound.

---------------------------------------------------------------------------------------------------------------------
## 2. PROVED pieces of the phase (review downgrades applied)

| # | Statement | Where | Verdict |
|---|---|---|---|
| P1 | m = −(χ′/χ)(½+iτ) = 2θ′; the subtracted comb is the truncation of +2Re ζ′/ζ; m\|ζ\|² = −2Re(ζ′(s)ζ(1−s)) on the line | ROUND_001_A (0.1),(0.2) | CONFIRMED |
| P2 | Lemma 1: P_{s_w} = ζ(½−iτ) + M^{½+iτ}w̃(½+iτ) + R_M, R_M = O(M^{−K}(1+\|τ\|)^K) | ROUND_001_A | CONFIRMED |
| P3 | Thm 1(a): leading coefficient 𝒜(w) = a_{T′}(F_0∗W), T′ = (L+2T_0)/2; B(F_0∗W) = −iF̂_0′(i/2) ≠ 0 for every w | ROUND_001_A | CONFIRMED, sharpened by REVIEW_002 |
| P4 | Thm 1(b): edge term 𝒳_M = O(M^{−K}) (contour; rewrite ζ(ζ′/ζ)(1−z) as χζ′(1−z) before shifting) | ROUND_001_A | CONFIRMED (two steps to write out) |
| P5 | Thm 1(c): 𝒵_N = O(N^{−5/2+ε}) | ROUND_001_A | CONFIRMED |
| — | Q_M = M𝒜 + O(M^{−3+ε}); "Thm 1 holds verbatim for any comb" | ROUND_001_A | DOWNGRADED to ARGUED (crude bound O(M^{−7/3+ε}); vanishing of 𝒳 is Λ-specific) |
| P6 | Necessary condition: (★) ⟹ 𝒜(w) ≥ 0 for every w of the family (vectors with A = 0, B ≠ 0, outside P_{T′}) | REVIEW_002 §1 | CONDITIONAL on writing the o(M) bound (the O(M^{−7/3}) bound suffices) |
| P7 | Thm 1.1 / Cor 1.2: radical lemma and half-line identity with a zero-free proof (removes the citation in thm:ext-half) | ROUND_001_B | CONFIRMED with σ₂ ∈ (−½,0) for non-smooth G |
| P8 | Prop 1.3: defect 𝒲^w = 𝒲 + 𝒫_{Λ−w} for any comb | ROUND_001_B | CONFIRMED; remark on a_P with P > N REFUTED; f_P "admissible" false as stated (survives with weakened hypothesis) |
| P9 | Prop 1.4: no common radical vector for 𝒲 and 𝒲^c, c ≠ 1 | ROUND_001_B | CONFIRMED |
| P10 | Prop 1.5: reduction of c-exterior gauge dependence | ROUND_001_B | CONFIRMED (last step ARGUED) |
| — | §1.6(i) defect indefinite; §0 item 3 defect formula | ROUND_001_B | ARGUED; REFUTED as written |
| P11 | Lemma 1.6: cell positivity for every w ≤ Λ (comb monotonicity) | ROUND_001_B | CONFIRMED (= P47 cor:ext-cfals(i) extended) |
| P12 | Lemma 2.1 (edge continuity, Ψ̌(0⁺) = 0 on the core); Prop 2.2 (edge terms archimedean-only) | ROUND_001_B | CONFIRMED (Prop 2.2 for the archimedean part only) |
| — | Prop 2.3 (φ₀ coupling is a forced scalar) | ROUND_001_B | DOWNGRADED to ARGUED (g-dependent jets give a second coupling) |
| P13 | Prop 2.4: near-minimiser concentration under (ext-L) | ROUND_001_B | CONDITIONAL (as labelled) |
| P14 | Lemmas 1–2: shifted Nyquist identity; two shifted sectors, gauge invariance c(−1)^k | ROUND_001_C | CONFIRMED (twist sign typo: e^{+iα4Tj}) |
| P15 | Thm 1 (L2′), explicit data of S, Props 1–3, Lemma 3 (entering contact = gauge + O(k²δ²)) | ROUND_001_C | CONFIRMED |
| P16 | Prop 4: the sign is not a function of the block samples alone | ROUND_001_C | CONFIRMED on L²(I_T) with REVIEW_002's strengthening dist²(F,E)+dist²(F,E′) ≥ κ‖F‖²; on P_T only (b) missing |
| P17 | Prop 1 (corrected proof): the germ of B at 0 is comb-free (comb part vanishes for \|d\| < log 2 − 2T_0) | ROUND_001_D; REVIEW_002 §4 | CONFIRMED in content, proof replaced; Prop 2 as written withdrawn |
| P18 | Lemma P (two projections: ‖Px‖² + ‖Qx‖² ≤ (1+‖PQ‖)‖x‖²) | ROUND_002_A | PROVED |
| P19 | Thm F: coercivity floor c_floor = ½∫_0^∞(2 − ν_t)dt ≥ c_* of the complement block; Cor F1 (Schur-test bound) | ROUND_002_A | PROVED, conditional on the ROUND_001_C coordinate input (cited there, not re-proved) |
| P20 | Prop S (floor-only sufficient inequality (I_c)); Prop L (best member c = λ_min(A_𝒞𝒞), required margin) | ROUND_002_A | PROVED, conditional on the ROUND_001_C Theorem 1 input; the floor-only Schur NO-GO built on it is NUMERICAL (see §3), not PROVED |
| P21 | Prop M, Cor M1–M2: s_k = m + r_T − A_T + c(−1)^k + 2Σv_n sin²(πk log n/4T); a deep sample forces n′^{q_n} ≈ n^{q_{n′}} | ROUND_002_A | PROVED; Cor M3 quantitative part ARGUED; the two numerical examples at M2 l.149–150 were wrong in value/sign and are corrected (nothing else depends on them) |
| P22 | Lemma 1.1, Prop 1.2: comb part of 𝔔^w exactly linear in W = w∗1; coherent part 2∫H₁^w\|ϱ\|² ⪰ 0, incoherent Σ W(n)ℬ_n | ROUND_002_B | PROVED (wording fix: the comb is w(q)q^{−1/2}(δ_{log q}+δ_{−log q}), not doubled) |
| P23 | Thm 2.1: coherent comb matrix on the prolate sector PSD and monotone, every N, K; 𝐓₀ ⪰ I; Thm 3.1(c) | ROUND_002_B | PROVED; Thm 2.2 and Prop 2.3 ARGUED (§4(ii) validation is poor, not "good for low orders"); §2.4 expansion ARGUED; Thm 3.1(b) DOWNGRADED to CONDITIONAL on Thm 2.2 + Prop 2.3 + §2.4 (not only on Prop 2.3 as the memo stated) |
| P24 | Thm 1 (i)–(v): joint range of (Π, Arch) convex; Π indefinite; max_c Φ_T(c) = Θ_T; J_T closed bounded interval; scaling identities; Θ_T = λ_arch(T) for the empty comb | ROUND_002_D | PROVED (complex space, Toeplitz–Hausdorff; Brickman covers the real-F alternative) |
| P25 | Cor 2 (Θ_T < 0 for the empty comb, T ≥ 0.60, with λ_arch(T) < 0 CITED from Paper 47); Cor 3 (λ_A ≥ Θ_T − \|1 − c*_T\|π_T) | ROUND_002_D | PROVED; "Π(F*) = 0 iff c* = 1" (l.189–193) DOWNGRADED to CONDITIONAL on the bottom being an isolated eigenvalue of finite multiplicity (Danskin), superseded by P27 |
| P26 | Lemma 1 (every w ≠ 0 gives indefinite Π_w); Lemma 2 (𝒦_T compact convex); Lemma 3 / Cor 4 first part (Θ_T(w′) ≥ Θ_T(w) − \|c*\|‖w − w′‖_1) | ROUND_002_E | PROVED; Cor 4's clause "λ_A(T) = Θ_T(Λ) = 0" is DOWNGRADED to CONDITIONAL on (★) itself, not PROVED |
| P27 | c*_T = 1 ⟺ 0 ∈ range of Π on the bottom eigenspace (Kato–Danskin, CITED for the isolated-eigenvalue case) | ROUND_002_E | CONDITIONAL on the isolated-eigenvalue property (not proved in the memo); the Galerkin method's "rigorous up to rounding" claim is DOWNGRADED to NUMERICAL (non-certified upper bounds; needs a certified maximisation or a primal Π-null witness; Tate constraints hold to quadrature precision, not exactly) |
| P28 | Prop 1 (Schur decomposition ⟺ 𝔸_M ⪰ 0, restatement); Lemma 2 (\|𝔸 − ℝ\|_{mk} ≤ βe^{−tδ}); Thm 3 (division prescription NO-GO); Thm 4 (Div/Near prescription NO-GO); Prop 5 (dual suppression restatement) | ROUND_003_B | PROVED, with Thm 4's "Near^{comb}_M ≠ 0 as soon as M ≥ 4" corrected to "for some M" (the memo's specific (4,1) entry is not shown non-zero, but density of lags plus continuity of a non-zero c_0 forces some M) |
| P32 | Prop 1 (a_T commutes with parity on P_T; λ_A(T) = min of sector bottoms; Φ_T = min of sector Φ's) | ROUND_003_A | PROVED (unreviewed); extends Paper 47 lem:parity from Arch to a_T |
| P33 | Prop 2 (exact tangency c*_T = 1 ⟺ 0 ∈ conv(Π on the two sector bottom spaces); explicit three-case criterion with simple sector bottoms) | ROUND_003_A | PROVED (unreviewed), granted the CITED Kato–Danskin formula for an isolated eigenvalue of finite multiplicity |
| P34 | Lemma 3 (Weyl pin: an orthonormal pair in P_T with Π indefinite forces λ_A(T) ≤ Θ_T ≤ Λ_2 and \|1 − c*_T\| ≤ (Λ_2 − λ_A)/min\|μ_±\|) | ROUND_003_A | PROVED (unreviewed) |
| P35 | Lemma 4 (rigidity: a near-kernel S of a_T bounds λ_A and Θ of every modified comb by ε minus an explicit eigenvalue of Π_δ on S) | ROUND_003_A | PROVED (unreviewed); explains the falsifier failures of λ_A and the observed failures of Θ |
| — | NUMERICAL finding: the near-tangency pair identified in ROUND_002_E is {e_ev,1, e_odd,1} (even–odd, ratio ≈ 200, Π positive definite on it, cannot produce c* = 1); the actual pinning pair is the EVEN pair {e_ev,1, e_ev,2} (tiny second even eigenvalue, Π indefinite on the span). Parity degeneracy is not the mechanism | ROUND_003_A §2.2 | NUMERICAL (unreviewed) |
| — | Bug note: the ROUND_002_E comb generator lists n ≤ 5 only, so it omits n = 7 for T > ½log7 ≈ 0.973; values at T ≤ 0.9 are unaffected; ROUND_003_A's own numerics use the exact Λ(n) for every log n < 2T | ROUND_003_A §2 | noted, not a correction to any proved statement |
| P29 | Arithmetic squares on (½log2, ½log3) exist iff λ^{∞,P}_min(T) ≥ v_2 = √2 log 2 | DOSSIER §6(e) | CONFIRMED (REVIEW_001); the value at ½log2⁺ OPEN |
| P30 | n_−(A_ev(T)) nondecreasing in T | DOSSIER §6(f) | CONFIRMED; "birth window" UNDECIDED (needs continuity of the 2nd eigenvalue) |
| P31 | (ext-L) holds at each fixed T with λ^W_T > 0; only uniformity is open | DOSSIER §6(g) | CONFIRMED, CONDITIONAL on λ^W_T > 0 |

None of P1–P35 is a sign step; every item that was tested is comb-generic or a restatement. ROUND_003_A's pure-math
items (Propositions 1–2, Lemmas 3–4) are structural statements about the pencil (Arch, Π) that hold for every weight
vector; they separate nothing about Λ by themselves.

---------------------------------------------------------------------------------------------------------------------
## 3. NO-GO results

| Object | Class (as corrected by review) | Falsifier status | Review verdict on the class naming |
|---|---|---|---|
| C1, ROUND_001_A | Smooth-cutoff family s_w = m^{−1/2}w(m/M), leading order in M: reduces to the continuous window form at T′ | ARGUED (asserted, not carried out; 𝒳 is Λ-specific) | Original name "lattice-to-continuum transfer by Poisson/AFE" too broad; renamed (REVIEW_002 §5) |
| Cell cancellation, ROUND_001_B | Statements on cones with sign-definite comb pairing (cell positivity) as the whole sign step | Carried out analytically (Lemma 1.6): survives c < 1, a_P | Correctly named; excludes it as the whole step, not as an ingredient |
| Fused reading, ROUND_001_B | Exterior form as clause-(5) object: its coupling runs through ζ(½+iτ) with a Möbius mollifier | Not applicable | Classification ARGUED, as labelled |
| Layer edges (phase 202 residue), ROUND_001_B | Residue as defined (archimedean pairings of dilated tails) is void | Trivial (comb-free) | Correct for that residue; "any decomposition" overstated (per-layer comb pairings carry v_q) |
| ROUND_001_B §Result (1) | "Objects whose Λ-dependence is the radical of 𝒲" | Partly; indefiniteness ARGUED | Too broad: NO-GO only for the two readings tested |
| C5, ROUND_001_D | Criteria using only the moments of the representing measure (germ of B at 0) | Analytic, via comb-independence of the germ; PROVED given the CITED falsifiers | Renamed from "moment determinacy (Hamburger/Stieltjes/Carleman)"; determinacy was not shown to fail |
| C3, ROUND_002_A | Floor-only Schur inequalities (I_c): any certificate replacing A_𝒞𝒞^{−1} by a scalar ≤ λ_min(A_𝒞𝒞)^{−1} | Comb-generic, soundness only; declared not applicable (class has no sign step) | NUMERICAL, not PROVED: Prop L (the class bound) is PROVED, but the failure is shown at two windows only by a truncated model; the truncation errors both favour the NO-GO direction (robust), confirmed by REVIEW_003 |
| C2, ROUND_002_B | Comb dependence of the exterior form on the bulk prolate sector: −Σ(W(n)/n)𝐆(n), 𝐆(n) ⪰ 0, comb-monotone and bounded-linear, plus incoherent O(N^{−1/2}log N) | Carried out by argument only (no numerics on the full sector form) | DOWNGRADED to ARGUED and asymptotic (N = e^{2T} → ∞ at fixed K only; says nothing about any fixed T): rests on Thm 2.2, Prop 2.3, §2.4, all ARGUED, and 𝐄 is not computed; the coherent part alone is PROVED monotone (Thm 2.1) |
| C9 (Candidate II), ROUND_003_B | Schur factorisations 𝔸_M = 𝕏 ∘ [e^{−tδ}] + ℝ with prescribed 𝕏 (division, Div/Near), and the dual suppression 𝔸_M ∘ [e^{−tδ}] | Uniform: the NO-GO uses only continuity of B and β > 0, valid for all falsifiers | SCOPE NARROWED by REVIEW_003: the class as originally stated (any 𝕏, ℝ) cannot be NO-GO, since 𝕏 = 0, ℝ = 𝔸_M succeeds exactly when 𝔸_M ⪰ 0 (Prop 1 is a restatement). What is PROVED NO-GO is the two concrete prescriptions (division, Theorem 3; Div/Near, Theorem 4) plus the restatements (Props 1, 5) and the structural constraint (Lemma 2) |
| C10 (Candidate III), ROUND_002_D | Signed Lévy measure / Euler subordination: c-blind like (I.a) | — | Recorded as DOMINATED by C8, not NO-GO |
| Candidate I as universal step, ROUND_002_E | (I.a) Θ_T ≥ 0 is not a sign step at windows with Θ_T(Λ) > 0 (survives small finite modifications, Cor 4) | NUMERICAL: at T = 0.9 every tested modification has Θ_T < 0 (margins 0.02–0.42); at T = log 2 all survive except η < 0 | Unreviewed; result labelled PIVOT, not NO-GO |

---------------------------------------------------------------------------------------------------------------------
## 4. Corrections to Paper 47 (to be applied only when the paper is closed)

Confirmed by REVIEW_001 (DOSSIER §6):
1. eq:coer-sandwich and lem:wh-schurabs(ii) (P47:5255–5278, 5684–5703): for λ_S < 0 the correct bounds are
   λ_S ≤ λ_A ≤ λ_S/(1+‖Ke_S‖²). The printed upper bound λ_A ≤ λ_S fails when Ke_S ≠ 0; the printed lower bound fails
   whenever K ≠ 0 (even if Ke_S = 0). Add the qualifier λ_S ≥ 0 at P47:5303 (rem:coer-honest(2)) and P47:10687–10688 ((L2)).
   The sign equivalences (thm:coer-schur(iii)) are unaffected.
2. Normalisation of F_0 (P47:7762–7769, 7835): impose ‖F_0‖ = 1 or write c_0(0) = ‖F_0‖² in Div_M.
3. prop:H final sentence (P47:6567–6569) and P48 thm:eveninertia(iii) (P48:207): "exactly one negative eigenvalue for
   every window" is false for small T; correct to "≤ 1 for all T" or "= 1 for T ≥ 0.12". P48 (ii) must restore the
   alternative "n_− = 0 and q > −½" and the range T ≥ 0.12.
4. §ext-constraints item 2 (P47:10654–10657): the half-line identity is not shown to hold for cΛ, a_P or Beurling systems;
   restrict to the algebraic identities. Proposed wording (ROUND_001_B §1.7): "…hold for the comb Λ only; for cΛ, a_P and
   Beurling systems the window form in exterior coordinates acquires 𝒫_{Λ−w}[Ef] − 𝒫_{Λ−w}[Ψ_f], and for cΛ no summation
   map is radical (Prop. 1.4)". The stronger "the exterior form is not comb-generic" is ARGUED. The dossier's citation of
   P47:10146 for this point is a mis-citation.
5. rem:directbound (P47:7909–7914) does not give λ^{∞,P}_min ≈ 0.49 at T ≈ 0.367; it says the bound is positive where
   λ^{∞,P}_min > 0.49. Problem (R)'s (½log2, ½log3) clause reduces to λ^{∞,P}_min(½log2⁺) ≥ v_2 (OPEN, NUMERICAL).
6. thm:nyq-schur(ii): for η below the least positive sample the block counts samples with s_T(ω_k) ≤ 0 (not < 0);
   dim N′_η ≤ d_η.
7. Label consistency: cor:shape(c)/P48:405 ("10^{−5}") vs rem:wit-sens ("~10^{−6}"): both NUMERICAL, harmonise.
8. thm:ext-half: may cite the zero-free proof of ROUND_001_B Thm 1.1 (σ₂ ∈ (−½,0)) instead of the external lemmas.
Refuted by REVIEW_001: DOSSIER §6(h)'s claim that (L2′) is already a proved smaller reduction; DOSSIER §6(j)'s claim that
no PROVED step relies on an unproved claim beyond (a) (items 2–3 are inside PROVED propositions). For DOSSIER §6(g) the
prediction must be stated for near-minimisers of W_T, T ≥ 1, g in the core.

Found in later memos:
9. Sign of the comb as a Dirichlet series (ROUND_001_A (0.2)): −Σ v_n cos(τ log n) truncates +2Re ζ′/ζ. P47:7408 already
   writes m = −2Re ζ′/ζ, which agrees; the reversal concerns the formulation used inside the phase, and no paper edit is
   implied unless a P47 passage with the opposite sign is found (to be checked at closure).
10. σ₂ range in the half-line identity (ROUND_001_B Thm 1.1; REVIEW_002 §2): for G with G̃ = O(1/|t|) the contour must
   have σ₂ ∈ (−½, 0), not (−1, 0).
11. K3 leading term (ROUND_002_B §2.4; concerns K3_GAMMA_001 and any P47 passage quoting it): the leading form on the
   prolate sector is log N·𝐓₀ with 𝐓₀ = Toeplitz[H∘sec] ⪰ I, not log 2N·‖b‖²; ‖b‖² is the layer part only (valid lower
   bound, not leading term). PROVED in the coherent form; the full expansion is ARGUED.
12. ROUND_001_C §4's reading that deep near-coincidences sit as small positive samples is false (ROUND_002_A §1); the
   8.8·10⁻⁵ sample is k = ±18 at the gauge-interval end (internal correction, not in P47).

---------------------------------------------------------------------------------------------------------------------
## 5. The tunnel

### 5.1 East end (finite / archimedean)
- Exact finite reductions: (L2), (S), and (L2′) with gauge/shift freedom and minimal blocks (11 at ½log5 + ε, 41 at T = 1;
  NUMERICAL).
- Complement control: Thm F gives an explicit floor c_floor (NUMERICAL 0.156, 0.251, 0.338 at ½log5+ε, 1, 1.25), which does
  not collapse at the smallest sample; the 2^b ≈ 3^a modes are not shallow (ROUND_002_A).
- Exact limit of the scalar method: Prop L; the obstruction is the alignment of b = P_𝒞Ax with the spectrum of A_𝒞𝒞,
  growing with T (NUMERICAL), not conditioning.
- The archimedean side as a convex body: 𝒦_T compact convex, the comb enters through a direction (ROUND_002_E Lemma 2).
- Mesh form of near-coincidence (Prop M): every deep Nyquist sample is an integer near-coincidence n′^{q_n} ≈ n^{q_{n′}}.
What it cannot do: every piece above is comb-generic (it holds for cΛ, a_P, Beurling, finite modifications).

### 5.2 West end (arithmetic)
- Λ enters exactly through: the half-line/radical identity (Λ-specific, zero-free proof, P7–P9); the vanishing of the
  edge term 𝒳_M (Λ-specific, P4); Λ∗1 = log in the cell weights.
- Every sign-definite comb pairing found is monotone in the comb (Lemma 1.6, Thm 2.1/3.1), hence blind below Λ.
- The only non-monotone comb content of the exterior form is 𝒪_w = Σ W(n)ℬ_n, of order 1 only at low Mellin frequency.
- No object with sign at scale √x for the smoothed fluctuation; mean-square/absolute bounds are excluded by P47 barriers.

### 5.3 The meeting condition
A proof must contain an object that (i) uses the exact Λ(n), (ii) couples them with the functional equation other than
through ζ(½+iτ), (iii) is non-linear in Λ, (iv) decides on near-coincidence vectors (README §2). No memo supplies it.

The one structure found that is specific to Λ (ROUND_002_D/E, NUMERICAL): at T₁ = ½log5 + 10⁻³ and T = 0.9 the bottom of
a_T on P_T is a near-degenerate pair (λ₁ = 3.1·10⁻¹², λ₂ = 6.5·10⁻¹⁰ at T₁; 4.5·10⁻¹⁵, 2.3·10⁻¹⁴ at 0.9), Π changes sign on
that 2-plane, and the scaling curve c ↦ λ_A(T; cΛ) peaks at c*_T = 1 to 7–8 digits, so Θ_T(Λ) = λ_A(T) (tangency of ℝΛ to
𝒦_T). Every tested perturbation at T = 0.9 (deletion of 2 or 3, Λ(2) ± 0.1, ± 0.5, swap v_2 ↔ v_3, Beurling shift 3 → 3.2)
loses the degeneracy and has Θ_T < 0 (stable across N = 20, 40, 80). At T = log 2 the bottom is simple and c* = 0.9983.
What would have to be proved (OPEN; ledger C11):
(a) at every T beyond the certified range, Θ_T(Λ) ≥ 0, i.e. the Lévy form C_0‖F‖² + ∫(c_F(0) − Re c_F(u))K(u)du is
    non-negative on the comb-null quadric {F ∈ P_T : Σ v_n Re c_F(log n) = 0};
(b) the calibration 1 ∈ J_T; at tangency windows this is the statement that 0 lies in the Π-range of the bottom
    eigenspace, so (a) and (b) coincide with (★) at that T (Θ_T = λ_A);
(c) a mechanism, using the exact values Λ(n), that produces the degenerate bottom pair with Π-range straddling 0.
At tangency windows the split does not lower the bar (ROUND_002_E §4.3); its value is that it changes the object to an
archimedean infimum on a cone, with the comb as a constraint rather than a weight.

ROUND_003_A sharpens (c), still without closing it (unreviewed). The apparent degeneracy is not parity: the pair
ROUND_002_E reported (one even, one odd eigenvector, ratio ≈ 200) has Π positive definite on it and cannot pin c* to 1.
The pinning pair is two EVEN eigenvectors, {e_ev,1, e_ev,2}, with a tiny gap (λ_ev,2 − λ_ev,1 ~ 10⁻⁷ to 10⁻¹¹ over
T = ½log5 to 0.9) and Π indefinite on their span from T ≈ 0.61 on (Proposition 1, Lemma 3, NUMERICAL instances). The
Weyl pin lemma (Lemma 3) turns this into a quantitative bound |1 − c*_T| ≤ (Λ_2 − λ_A)/min|μ_±|, matching the observed
tangency to the digit; the rigidity lemma (Lemma 4) explains every tested falsifier failure as a loss of this pin
(perturbations push Π_δ outside what the near-kernel tolerates). Both lemmas are structural (hold for every comb) and
supply no sign by themselves; the open, Λ-specific content is now localised to two facts about a_T at the exact comb:
(P1) a second even eigenvalue that is near-null, (P2) Π indefinite on the span of the two lowest even eigenvectors.
Simplicity of the bottom and a proof of (P1)–(P2) from the exact Λ(n) (rather than numerically) remain OPEN; no
Perron–Frobenius argument is available for a_T on P_T (Π destroys positivity preservation). The pair inequality
obtained by writing (P1)–(P2) out is circular as stated, since the plane depends on Λ.

---------------------------------------------------------------------------------------------------------------------
## 6. Open candidates, in order of tractability, with the first lemma

1. C11 / C8 — near-null pair and tangency (ROUND_002_E, sharpened by ROUND_003_A). First lemma (next concrete step of
   ROUND_003_A, unreviewed): make (P2) independent of the comb by testing whether Π is indefinite on the span of the two
   lowest eigenvectors of the archimedean form Arch alone on P_T^ev — a Λ-free plane E_T — and, if so, compute the 2×2
   Schur complement of a_T on that fixed plane. If E_T captures the pin (its Π-Gram eigenvalues within 10⁻² of the
   computed M_ev), the pair inequality of ROUND_003_A §4 becomes a non-circular 2×2 matrix inequality in the exact
   values Λ(n), n < e^{2T}, to be attacked directly at T = 1. Only then does the step after that apply: certify at
   T = 1 (interval arithmetic) the bottom pair of a_T on P_T and that Θ_1 = λ_A(1) with c*_1 = 1, then show 0 ∈ Π(E_T)
   using a property of Λ that fails for the tested falsifiers. Also OPEN from ROUND_002_D: (I.a) for a_P with P ≤ e^{2T}.
2. C3 continued — finite-rank-plus-scalar bound of A_𝒞𝒞 (ROUND_002_A next step). First lemma: A_𝒞𝒞 ⪰ R ⊕ c_floor(1 − Π) with
   Π the projection on span{P_𝒞Ae_k : k ∈ 𝒩} ∪ modes of W_{t_1}; test at ½log5 + ε whether the residual component of b is
   below the margin of S; requires first a certified version of the 11-mode block. Comb-generic by construction; it can
   at best organise the sign, not supply it.
3. Exterior form at low Mellin frequency (ROUND_002_B next step). First lemma: write ℬ_n on a basis of low-frequency
   admissible tails as a finite matrix and decide whether Σ log n·ℬ_n has a sign pattern failing for W = c log and W_{a_P};
   if comb-generic, the exterior form closes on every regime.
4. C6 — transport defect M → M+1 (Paper 39) / adjacent-window coercivity (Paper 38). NOT STARTED. First lemma: exact
   formula for 𝔸_{M+1} ⪰ 0 given 𝔸_M ≻ 0 as a scalar Schur complement in the new row B(log((M+1)/k)).
5. C4 — corona/symbol lens (Paper 26) on M ↦ 𝔸_M. NOT STARTED. First lemma: identify the limit symbol of the field and
   whether 𝔸_M − (limit) is compact with an exact formula.
6. C7 — phase-160 route N (finite-window Carathéodory–Fejér). NOT STARTED. First lemma: answer the recorded "dies at the
   limit" objection with a statement at fixed T.
7. P6 — the necessary condition 𝒜(w) ≥ 0 off P_{T′}: first lemma is the o(M) remainder bound (O(M^{−7/3+ε}) suffices).
   A necessary condition only; it does not advance (★) by itself.
Closed for this phase: C1, C2, C5, C9 (NO-GO as in §3); C10 dominated by C8.
Kreĭn extension with prime atoms is noted by LITERATURE_001 as absent from the literature; it is an internal reformulation
of the target and is not ranked here.

---------------------------------------------------------------------------------------------------------------------
## 7. Verdict

Nothing in this phase changes the state of (★). The PROVED range is unchanged: certified for T ≤ ½log5, CITED to ½log15
(Mori) and 17/16 (Liu), OPEN beyond. The phase produced exact reformulations ((L2′); the Candidate-I split Θ_T ≥ 0 ∧ 1 ∈ J_T;
the convex body 𝒦_T), an explicit coercivity floor for the complement of (L2′), a zero-free proof of the half-line
identity, a list of corrections to Paper 47, and NO-GO results now narrowed by review to: floor-only Schur inequalities
(NUMERICAL), the comb-monotone exterior sector (ARGUED, asymptotic only), and the two concrete Schur-coupling
prescriptions of ROUND_003_B (PROVED, scope narrowed from the originally claimed class) — all comb-generic or
restatements; no sign step was claimed and none survived the falsifier test. The single Λ-specific structure observed,
the tangency c*_T = 1 with a near-degenerate bottom pair on which Π changes sign, is now understood (ROUND_003_A,
unreviewed) to come from a tiny second EVEN eigenvalue with Π indefinite on the even pair, not from parity degeneracy;
this is a sharper description of the same NUMERICAL phenomenon, still unproved from the exact Λ(n), and at the windows
where it occurs the statement to prove is not weaker than (★) at that window. Round 2 and ROUND_003_B have been
reviewed (REVIEW_003) and their labels above are the reviewed verdicts; ROUND_003_A remains unreviewed.

## Addendum: round 4
ROUND_004_A: necessary conditions a_T ⪰ 0 on the Λ-independent planes E_k (k = 2, 3, 4, 6) hold at
log 2, ½log5, 0.9, 1.0, 1.2 (NUMERICAL) and are written explicitly for k = 2 (two linear and one
quadratic inequality in v_n, PROVED). Proposition B (PROVED): any such condition with positive margin
survives small changes of the weights and small rescalings cΛ, so no fixed Λ-free finite subspace can
carry the sign step; NO-GO for the class. The next object must have dimension growing with T and carry
Λ-dependent information at margin precision. State of (★): unchanged.
