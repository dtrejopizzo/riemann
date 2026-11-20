# Triage D-1: row D ideas recorded and never carried through (list 1, items 1–41)

Filter: F1 (Lemma T, with the controls c = 2, deletion of a prime power and Beurling-type weight), F2 (archimedean and weight of the same object at the same step), F3 (formats affine in the weight; Gram/Schur; pieces per prime; change of reference operator), F4 (doubly exponential margin: no bound with slack), F5 (REF without an independent side). «MI l.N» = line of `05-meta-and-planning/ROUTES-MASTER-INDEX.md`. Where a source names the classical statement, [H] is written. Source paths are given relative to `03-research/` or `01-context/`. This is a classification: nothing is built or computed.

For each item the passage of the primary source was opened. The exact list is in §4. The index was used only to look for later closures.

## §1 Table

| no. | idea | source (passage read) | class | reason |
|---|---|---|---|---|
| 1 | (♦): ‖G^{1/2}(W^prime_λ − p_λ)^− G^{1/2}‖ ≤ 1; comparison «Σ prime trace − pole mass < 1» | phase-64/POLE-DEFECT-estimate.md l.18–211 | REF | l.98: «(♦) is ε₀≥0 = [H]». The trace version of §6 is withdrawn by the memo itself as «too strong and the wrong tool» (l.158–163): it loses exactly the marginal case. The sharp form (♦′)/(♦″) (l.179–203) is again ⟺ goal. Dependence on the weight: p_λ ≥ 0 is the pole barrier, of fixed mass π_res, and independent of the weight; W^prime_λ is linear in Λ (l.25, 42). The archimedean does not enter (♦) (l.94), and in §6 it is evaluated separately with PNT (l.141). Hence it does not satisfy F2: the archimedean and the weight do not come out of the same step. The trace comparison is affine in the weight (F3). The «next computation» (pointwise sign of W^prime − p_λ, l.210) decides only whether the BS kernel is positivity-improving, not the sign of the form. |
| 2 | Discrepancy of {log n} with weights Λ(n)/√n | phase-64/FACE-C-spectral-shift-monotonicity.md l.115–130 | CLOSED (class result, ARGUED) | It is an «a priori» equidistribution bound, that is, a size bound (F4). The class «bounds using only \|Λ(n)\| (large sieve, mean-value)» is closed by the METHOD OBSTRUCTION THEOREM with DH control (phase-60/0-triangulation-of-the-wall-from-three.md l.16, RIGOROUS in the memo). Moreover, the bridge arg D_P = πξ_K is invalidated by the erratum of phase 106. |
| 3 | Interlacing decided by the sign of the pole + finite HB | phase-64/FACE-C-rigidity-attack.md l.129–170 | BLIND | The proposal decides the interlacing «by the sign of the pole alone» (l.141–142), and each finite truncation is HB. The sign of the pole and the finite HB property are identical with c = 2, with deletion of a prime power and with the Beurling weight, so the relation used holds in the three controls (F1). Before that step one must take the limit of the renormalization, which is REF (Thm hbstab). |
| 4 | Isometry of the J-reflection of the primitive canonical kernel | phase-64/FACE-C-simple-crossings-audit.md l.180–201 | REF | The memo says verbatim «[H] = the s↔1−s reflection acts isometrically on the primitive canonical kernel» (l.187–188) and calls it a «new, clean equivalent». |
| 5 | (CONF) Landau–Widom: Wiener–Hopf compression → Dirichlet box | phase-60/cierre-1-CONF-landau-widom.md l.12–28 | OTHER OBJECT | It is the convergence of the renormalized low spectrum to (k+1)², «RH-neutral … closable by established machinery». It does not contain the sign: the memo separates «existence of the limit = neutral» from the sign of ε₀. |
| 6 | Bound on the Fourier tail of the full symbol | phase-60/weil-remainder-attack.tex l.227–272 | BLIND | Prop noncirc poses it as a bound on a smooth tail, i.e. a size estimate (F4). It names no sign operation. |
| 7 | Functional of δV insensitive to individual zeros | phase-60/attack-deltaV-analysis.md l.35–45 | CLOSED (ARGUED) | A functional insensitive to individual zeros only uses density. It falls into the class closed by the METHOD OBSTRUCTION THEOREM (0-triangulation l.16). The memo judges it unlikely. |
| 8 | ε₀(λ) ≥ c/λ² from prime data only (density, PNT) | phase-60/spectral-gap-analysis.tex l.150–183 | CLOSED (ARGUED) | The question is «does density suffice?», and the METHOD OBSTRUCTION THEOREM answers for that class: the DH control has comparable magnitudes and ε₀ < 0. |
| 9 | Window design: resolution(φ) ≫ 1/log λ | phase-60/0-triangulation-of-the-wall-from-three.md l.23–35 | CLOSED | «Computation in progress … recorded to continue» without result. Closed later by «structural marginality» (REDUCCION §9.2; MI l.27202). The same memo proves the method obstruction. |
| 10 | Sharp Hardy c = 2 / positivity of the finite form from PNT | phase-60/A_intento_demostracion.md l.13–27 | CLOSED (ARGUED) | «c = 2 = [H]» (l.23) is REF. The [GAP] of step 4 is «positivity of the finite form from PNT, without position of zeros» (l.24), which is the density class closed by the method obstruction. |
| 11 | Hessian arch↔arith; curved direction = global rescaling | phase-60/CONSOLIDACION_L_y_eslabones.md §4 l.38–58 | LOCAL/NUMERICAL, decides nothing | Result [N] in mpmath: the only curved direction is Λ → Λ(1+δ), precisely the direction of the control c. It is second-order information around the real weight. It gives no sign for all T (F4), and the archimedean remains a fixed skeleton (F2). |
| 12 | Identification of V(x) / rate h(λ) | phase-60/IV1-operator-identification.md l.26–89 | CLOSED | The identifications of Â_∞ were REFUTED and Airy/Bessel FALSIFIED (MI l.11534). The rest («IV.1 and IV.1★ close together modulo a residual») is the convergence of item 5. |
| 13 | Persistence of PF positivity under renormalization | phase-60/rh-proof.tex l.35–81 | REF | «[H] reduced to a single positivity-under-renormalization lemma» (l.35–45): the lemma is the goal. It falls under the topology NO-GO T1–T2 (MI l.27655). |
| 14 | Lemma 2.3.F (Doob–Feshbach–Mosco) | phase-61/R9_three_new_fronts_RESULTS.md l.81–95 | REF | «Status of 2.3.F unchanged … remains REDUCED to» 2.3.F-Loc, confirmed as a spectral scale invariant e^{−cL}. «PSC with uniform source = Lemma 2.3.F/L1 wall» (MI l.26192). (respuesta4.md does not contain the string «2.3.F».) |
| 15 | (★) CD(0,∞) per prime + tensorization | phase-64/CONSTRUCTION-spectral-surface.md l.104–180 | BLIND | It asks for signed curvature per prime (l.174–177). CD(0,∞) is invariant under scaling of the kernel, so (★) holds equally with c = 2 and with deletion of a prime power (F1/F3). The memo also notes that Γ₂ is marginal (l.157). |
| 16 | R > 0 for every configuration | phase-64/E107_RESULTS.md l.19–48 | OTHER OBJECT | Margin of the colligation with planted point sets. «R is configuration-dependent»; proving it for all configurations «is [H]». It is not a_T on P_T. |
| 17 | Rank-one renormalization continuous in strong resolvent | phase-65/D8.5b-i-SELF-ADJOINT-COMPLETION.md l.21, 141–159 | REF | Inside the strip, convergence «is exactly what is in question» (l.74). It is the NO-GO T1–T2: the index must come from the sign and not from the topology. |
| 18 | M3: positive rank-one divergence ⇒ no negative square | phase-65/M2-pole-relative-completion.md l.9–102 | BLIND | The datum that M3 must exploit is the «definite-signed rank-one defect» of the pole (l.9). That sign is the same with c = 2, with deletion and with Beurling (F1), and the memo names no arithmetic step that fails in a control. |
| 19 | sup_P ‖P_prim K_P P_prim‖ < ∞ | phase-66/MAXIMAL-CLOSURE-omega7.md l.97–156 | REF | The bound gives Kreĭn–Langer index zero, that is the goal (l.138). It is the upper bound of Thm onefence. |
| 20 | State of the semigroup producing log b − log a | phase-67/E67_8_RESULTS.md l.28–66 | OTHER OBJECT | Off-diagonal coherence of the QSC model, not a_T. A state is moreover linear (F3). |
| 21 | Off-diagonal torsion; tilting | phase-67/E67_13_RESULTS.md l.43–44 | CLOSED | Audit E67.13: «contamination AND fabrication … structural» (MI l.26319). |
| 22 | RCOER C_actual ≥ θ_H C_model; MCOER2 | phase-72/E72_134 l.17–70; E72_148 l.81; E72_267 l.91–95 | BLIND | It is a comparison with slack θ_H relative to a model (F4). Changing the reference operator does not change the sign (F3). MCOER2 is «purely archimedean … no primes» (F2). |
| 23 | Attack R_x(s) directly | phase-72/E72_15_ACD_RESONANCE_BARRIER.md l.34–50 | REF | Thm 72.15: ACD ⟺ annihilation of the off-line resonances. R_x(s) is the response of the accumulated kernel, on the zero side. |
| 24 | Null-vector identity in maximal resonance blocks | phase-72/E72_17_MAXIMAL_RESONANCE_BLOCK.md l.148 | REF | It asks to annihilate the «off-line resonance Gram» blocks: it is the goal on the zero side. Symmetries are already discarded in the same memo. |
| 25 | Uniform HOC3 (LOW1, LOW2, TAIL) | phase-72/E72_242_HYBRID_HOC3_CERTIFICATE.md l.5–27 | LOCAL/NUMERICAL, decides nothing | Certificates of the tail of the Feshbach model of phase 72 (λ = 32 delicate). It is not a_T on P_T, and the uniform version is a bound with slack (F4). |
| 26 | GAP/DCB stack; DCB at the source | phase-72/E72_296_DIRECTIONAL_COMMUTATOR_REPLACEMENT.md l.29–141 | REF | DCB splits into DCB-model + DCB-arith. Each step is an exact reformulation and the residue is the annihilation of off-line packets (MI l.26063). |
| 27 | ELR2/ELR3, XNEG, pole-pair HOC3 | phase-72/E72_270 l.1–21; E72_211 | BLIND | They are energy envelopes and measured signs («Negative supports XNEG»), i.e. size bounds (F4). |
| 28 | DSF-O2 | phase-72/E72_288_DSF_STRENGTH_AUDIT.md l.60 | REF | «should be treated as an [H]-strength arithmetic theorem». |
| 29 | GAP-151.A/B/C | phase-48/151-adversarial-audit-of-docs-145-and-148.md l.61–173 | OTHER OBJECT | Framework gaps of the semilocal form of two pure primes and completeness of the proofs of documents 145/148. It is not the full form a_T. |
| 30 | Upper bound ⟨Γ,H⟩² > ⟨H,H⟩⟨Γ,Γ⟩ outside effectivity/Bochner/relaxation/Satake | phase-15/M3-genuine-attempts-on-the-core.md l.45–58 | REF | «The upper bound (the Hodge index) is genuinely a different, one-sided statement»: it is the Hodge index, that is the goal. The reopening only excludes sources. |
| 31 | Seven lemmas of the Bottleneck Ledger | RH2024/task1/bottleneck_ledger*.md; RH2024/task11/bottleneck_ledger_v3.md | OTHER OBJECT | Numerical regularities of Q_σ and zero-side lemmas. It is not a_T. |
| 32 | Weil form localized at off-line ordinates | RH2021/task37/weil_positivity_results.txt l.7; OVERVIEW.md l.16 | OTHER OBJECT | «MISSING LEMMA» on detection of violations via test functions. It is not a sign mechanism. |
| 33 | Perturbation by displacement, \|λ\| ∝ β² | RH2022/task10/OVERVIEW.md l.17–20 | OTHER OBJECT | Sensitivity to displaced zeros (calibration). |
| 34 | Hardy-prime cancellation | phase-70/E70_6_PARTIAL_SUMMATION_BARRIER.md l.128–176 | REF | «⟺ Hardy-prime cancellation estimate», declared of full strength. |
| 35 | (C) Mellin coboundary / (D) bordered Euler current | .phase-102-discard/phase-102-omega7-closure/102_A1_SIGNED_COMPENSATION_CANDIDATES.md l.50–110 | CLOSED (D) / OTHER OBJECT (C) | Both aim at the Li inequality C_n + ¾λ_n^arch ≥ 0, not at a_T on P_T. (D) appears DEAD in the grid (row G4B-phase-102/119; ANNEX_INDEX_04 l.283, l.658). (C) is a scheme with unspecified remainder R_{n,T} ≥ 0 and was not resumed anywhere else in the corpus. |
| 36 | Pontryagin index exactly two of the source colligation | phase-114/114_d_99_MATRIX_PICONE_TOTAL_POSITIVITY_AUDIT.md l.236–245 | REF | Negative index two, with both directions exhausted by the Tate residues. By Haynsworth it is equivalent to the restricted positivity, that is the same condition (6.3) of D.53. The memo itself demands proving it «from the source colligation» without indicating with which operation. |
| 37 | Uniform n₊(A_T) = 1 | phase-114/114_d_47_TWO_JET_PONTRYAGIN_SCHUR_GATE.md l.160–180 | REF | The three uniform estimates (index, signature (1,1), absence of zero mode) are the Haynsworth gate of the goal. The structural NO-GOs of D.56 (PROVED) exclude the natural sources. |
| 38 | Two-mode oscillation (6.7): n₋(A_{T,P}) ≤ 2 and n₋(𝒢_{T,P}) = n₋(A_{T,P}) | phase-114/114_d_53_THRESHOLD_FLOW_FAILURE_AND_TWO_MODE_OSCILLATION_GATE.md §6 l.166–245 | REF (with LOCAL falsifier in §3) | The equality of indices is, by (6.5), the restricted positivity itself. The previous version of this triage gave it as CLOSED via D.135; the reading of D.135 §6 does not support this, because D.135 treats the positive index of the contact and not n₋(A_T). The half «n₋ ≤ 2 for every partition» is falsifiable at fixed T (§3). |
| 39 | Goal (9.1)/(4.3): ⟨u_o,(H_o − E)^{-1}u_o⟩ < 1 | phase-114/114_d_50_PARITY_BIRMAN_SCHWINGER_AND_DISPLACEMENT_AUDIT.md l.133–150, 263–267; 114_d_51_EXPLICIT_EVEN_LEVEL_AND_ODD_GREEN_GATE.md | REF | «μ_e < μ_o ⟺ m_o(μ_e) < 1»: reduces the goal to channel ordering plus even level ≥ 0, and neither part has an independent proof. The counterexample of D.50 (PROVED) shows that rank-one interlacing can invert the order. |
| 40 | λ_max(K_T) ≤ 1 ∀T | phase-114/114_d_135_CENTERED_BIRMAN_SCHWINGER_SPECTRUM.md §6 l.245–260 | REF | D.134 (0.4): ‖W_T R_T^{-1/2}‖ ≤ 1 ⟺ form ≥ 0. The proposed reopenings («relative screw-kernel factorization or a directed shorted-capacity estimate») are not stated, and the memo says: «No such uniform bound is asserted». |
| 41 | Non-perturbative Schur capacity with joint Gamma + contacts cancellation | phase-114/114_d_133_THRESHOLD_HADAMARD_CAPACITY_AUDIT.md l.47, 432–445 | REF | The capacity per cell is «assuming row D» (D.133 Tate–Chebyshev (5.1)/(5.2)). The non-perturbative version names no sign operation, and a capacity is a bound (F4). |

Count:
- CLOSED = {2, 7, 8, 9, 10, 12, 21, 35} = 8;
- REF = {1, 4, 13, 14, 17, 19, 23, 24, 26, 28, 30, 34, 36, 37, 38, 39, 40, 41} = 18;
- BLIND = {3, 6, 15, 18, 22, 27} = 6;
- LOCAL/NUMERICAL = {11, 25} = 2;
- OTHER OBJECT = {5, 16, 20, 29, 31, 32, 33} = 7;
- ALIVE = 0.

Total 41. Item 35 is counted as CLOSED by its part (D).

Changes with respect to the previous version (made from the index entries):
- 1 moves from BLIND to REF;
- 3 moves from REF to BLIND;
- 5 moves from REF to OTHER OBJECT;
- 8 and 10 move from REF to CLOSED;
- 11 moves from BLIND to LOCAL;
- 18 moves from REF to BLIND;
- 29 moves from BLIND to OTHER OBJECT;
- 35 is split between CLOSED (D) and OTHER OBJECT (C);
- 38 moves from CLOSED to REF.

## §2 ALIVE items

None. The least excluded are:

- Item 38: the index-bound part is falsifiable, but the equality of indices is the goal.
- Item 35 (C): scheme without specified remainder and aimed at another inequality.

## §3 LOCAL/NUMERICAL items that decide something

- **Item 38, bound (6.7) n₋(A_{T,P}) ≤ 2.**
  - What is computed: the number of negative eigenvalues of the matrix of cell averages of K_g (D.52 (2.1)) on the zero-mass hyperplane, for fine partitions of [−T, T].
  - Where: at a couple of values of T inside and above the zone T* ∈ [0.58, 0.60], where the archimedean already has negative directions.
  - Cost: diagonalization of 10²–10³ matrices with interval arithmetic.
  - What it decides: if n₋ > 2 at some T, the gate (6.3)/(6.7) is falsified as formulated, and with it the route 36–38. If n₋ ≤ 2, it proves nothing uniform.
  - Before launching it one must cross-check with Thm P (n₋ ≤ 5/7/8, «count 5 at log 2»; MI l.5150, l.12268): if that count is of the same operator A_T restricted to zero mass, the falsifier already exists and item 38 becomes CLOSED. [Correction, ROUND_024_C: it is not the same operator; Thm P counts the archimedean part alone and (6.7) the full kernel with the comb. The item remains a reformulation; (6.7) OPEN.]

## §4 Sources opened and not found

Opened (passage cited in the table):
- **phase-64-connes-route:** POLE-DEFECT-estimate.md, FACE-C-spectral-shift-monotonicity.md, FACE-C-rigidity-attack.md, FACE-C-simple-crossings-audit.md, CONSTRUCTION-spectral-surface.md, E107_RESULTS.md.
- **phase-60-discriminant:** cierre-1-CONF-landau-widom.md, weil-remainder-attack.tex, attack-deltaV-analysis.md, spectral-gap-analysis.tex, 0-triangulation-of-the-wall-from-three.md, A_intento_demostracion.md, CONSOLIDACION_L_y_eslabones.md, IV1-operator-identification.md, rh-proof.tex.
- **phase-61-open-problems:** R9_three_new_fronts_RESULTS.md; respuesta4.md (grep without the string «2.3.F»).
- **phase-65-signature-continuity:** D8.5b-i-SELF-ADJOINT-COMPLETION.md, M2-pole-relative-completion.md.
- **phase-66-rank-one-escape:** MAXIMAL-CLOSURE-omega7.md.
- **phase-67-quantum-q-index:** E67_8_RESULTS.md, E67_13_RESULTS.md.
- **phase-72-feshbach-leakage-calculus:** E72_134, E72_148, E72_267, E72_15, E72_17, E72_242, E72_296, E72_270, E72_288.
- **phase-48-audit-and-purity:** 151-adversarial-audit-of-docs-145-and-148.md.
- **phase-15-arithmetic-hodge-index:** M3-genuine-attempts-on-the-core.md.
- **phase-70-lee-yang-dbn:** E70_6_PARTIAL_SUMMATION_BARRIER.md.
- **.phase-102-discard/phase-102-omega7-closure:** 102_A1_SIGNED_COMPENSATION_CANDIDATES.md (plus phase-102-omega7-closure-campaign/102_A1_SIGNED_COMPENSATION_MECHANISMS.md).
- **phase-114-closing-the-four-rows:** 114_d_99, 114_d_47, 114_d_53, 114_d_50, 114_d_135, 114_d_133_THRESHOLD; 114_d_51 only by name and by its script.
- **01-context:**
  - RH2021/task37 (weil_positivity_results.txt, OVERVIEW.md);
  - RH2022/task10/OVERVIEW.md;
  - RH2024/task1 (listing: bottleneck_ledger.md, bottleneck_ledger_v2.md) and RH2024/task11/bottleneck_ledger_v3.md, both only located, not read in detail.

Not opened or only partially:
- Testrella-*.md (item 5): cierre-1-CONF was read in its place.
- 2b_*.md (item 12).
- E104_RESULTS.md (item 16): only E107.
- E67_12_RESULTS.md (item 21): only E67_13.
- E72_132, E72_286 (item 22).
- E72_240 (item 25).
- E72_293 §5 (item 26): only E72_296.
- E72_211–223 except 211 and 270–272 (item 27).
- RH2024/task14 (item 31).
- 114_d_52 and 114_d_56 (item 37).
- Body of 114_d_51 (item 39).
- Original Doc 151 of segment 02_02 (item 29): the phase-48 audit defining GAP-151 was used.

No source remained unlocated.
