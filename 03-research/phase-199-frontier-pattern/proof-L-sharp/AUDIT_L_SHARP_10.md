# AUDIT_L_SHARP_10 — audit of TEST_BRIDGE_001 (MORI15 kill-tests of BRIDGE_001 planks P1, P2, P3a, P3b)

Phase 199,
Checked against BRIDGE_001 (§3.2, §4.2, §5.1, §5.2), PRECHECK_T1_001, MORI15_EXTREMAL_001,
U_001 (U.2.1), A_001 (Thm 1.1, Rem 1.1(iv)), AUDIT_L_SHARP_7/8/9, and the shipped JSON in `TEST_BRIDGE_001_data/`
(re-read, ratios recomputed in double; no new runs).

**Verdict.** Numbers reproduce from the data. The P2 and P3a kill-verdicts **survive the closure error**. The P3b "ALIVE /
edge benign" verdict is **not supported**: the global canonical split is degenerate (p ∥ g*), and in the non-degenerate
V_J splits the edge self-term carries 13–91 % of W* and θ_emp ≈ 1 is inflated by S* ≈ 5 C* (i.e. by the P3a failure).
P1's rough complement is **not attributed** (physical vs. Galerkin) and is plausibly tied to the edge datum. The closing
sentence "sign burden in the caustic layer ω ∈ (1,2)" is an interpretation of one μ, not measured in ω. Row D OPEN.

## 1. Closure error vs. the O(1) ratios (priority 1)
From `exterior_OMX48_analysis.json`: (ΣX·λ − C)/S = 0.0034 (v_1), 0.0044 (v_3), 0.0088 (v_12), **0.0195 (v_glob)**.
The 2–10 % closure is relative to C, which is itself only 0.15–0.19 S; in units of S the defect is ≤ 0.02.
- Diagonal share 0.761: error ≤ 0.02/0.76 ≈ 2.6 %. Cross Σ_{m≠n}/S = −0.550: ≤ 0.02/0.55 ≈ 3.6 %; with the ω_max 24→48 drift
  (≤ 0.02) the honest band is |Σ_{m≠n}|/S ∈ [0.51, 0.59] for v_glob, [0.50, 0.54] for v_1. **P2 kill (≥ 0.5) holds, marginally;
  at v_1 it is within error.** (1,2)/X₁₁ = −0.479: X₁₁/S = 0.61, so ≤ 0.02/0.61 ≈ 3 % in X₁₁ units, i.e. −0.48 ± 0.03.
- C*/S* = 0.19 (P3a): C is the Galerkin value (arb), S is exterior; error from tail ≤ 2 % ⇒ 0.19 ± 0.01. Far below ½: robust.
- Caveat: the closure defect is not localized (could sit in diag, cross, or the Nyquist jump correction added to X_nn in
  `analysis.py` l.64–65, which is a model term). Acceptable for O(1) verdicts; not for any statement at the 5 % level.

## 2. "b ≡ 0 with canonical Schur" and θ_emp (priority 2)
- The lemma is correct and trivial: p = G⁻¹ε/(εᵀG⁻¹ε) is G-orthogonal to ker ε, so b(v) = W(p,v) = 0 there. PROVED (linear
  algebra), and consistent with A Rem 1.1(iv) because on core W_T(v) = 𝒲_ext[Zr_v] (I1).
- **New finding (from the memo's own numbers): cos(p, g*) = −1 + 5.7·10⁻⁹.** G⁻¹ε is dominated by the bottom eigenvector,
  so the global "edge direction" *is* the extremal. The global split C* = 0.9996 W*, f*²e₂ = 3.8·10⁻⁴ W* says nothing about an
  edge channel: it is g* split along itself. "Edge 0.04 %" is an artefact of the cut. Withdraw it as evidence.
- V_J splits (non-degenerate): f*²e₂/W* = 0.913 (J=1), 0.414 (J=3), 0.267 (J=5), 0.131 (J=12); cross 2f*b*/W* = −0.14…−0.06.
  So the edge piece is **positive but leading order** for small J; "benign" is cut-dependent.
- θ_emp = 1 − b²/(e₂S) vs. the Cauchy–Schwarz quantity 1 − b²/(e₂C) = 0.976–0.992 (always ≥ 0 by positivity of W on the 2×2).
  Since S ≈ 5 C, θ_emp ≈ 0.996 is the C-number diluted by the P3a failure. Moreover v* ∉ V_J while p_J is Schur only against
  V_J ∩ core, so the BRIDGE condition "p W-orthogonal to the core block containing v" is not met: the test is a hybrid.
  **θ_emp meaningful only as "b is not large"; P3b status: OPEN (not ALIVE).** The real P3b question (BRIDGE §5.2) needs a p_λ
  Schur against a block that contains v but not g*; none of the computed cuts is that.
- Reconciliation with PRECHECK −51 %: **different objects.** PRECHECK evaluated 𝒲_ext[Zr_{f*}] = 9.6·10⁻⁷⁰ on the non-core
  f* and called W* − 𝒲_ext the "edge defect"; that is the failure of I1 off core, not a term of A's identity (no p_λ, no b,
  no e₂). TEST_BRIDGE computes A Rem 1.1(iv) with a chosen p_λ. Neither is the canonical edge for P3b: PRECHECK has no split,
  TEST_BRIDGE's global cut is degenerate. The −51 % should not be quoted as an edge share; the +0.04 % should not either.

## 3. P1 rough complement (priority 3)
- Data check: ‖δ‖² = 5.8·10⁻⁷¹ (J=15), 4.6·10⁻⁷¹ (J=50); W(δ)/W* = 0.264, 0.232 ⇒ Rayleigh ≈ 2.2–2.4 (O(1), i.e. ~10⁷⁰ × W*).
  The identity W(g_J) = W* + W(δ) − 2W*‖δ‖² is right (PROVED, eigen-relation). Wording "lowers the value by 21 %" is a
  sign-convention gloss: R_J − 1 = W(δ)/W*.
- Physical or artefact? Not decided by the memo, and the parity argument (§4 of the memo) is a comparison of two leak numbers
  (6.36 vs 4.07·10⁻⁷⁰) with no computation of the parity image itself — stays **ARGUED, unverified**. Alternative:
  the plateau in ‖δ‖² (J ≥ 15) plus f_J(λ)/f* oscillating 0.82–1.19 indicate δ carries the **edge/jump datum** (Ef has jumps
  at x_n when f(λ) ≠ 0; smooth rungs cannot reach their Legendre tail). Then P1's 20 % and P3b are the same object. A second
  Galerkin size (N ≠ 832) is the only discriminator; not available. OPEN.

## 4. P2/P3a numbers and "archimedean" (priority 4)
- Recomputed from `X_first4_overS`: X₁₂/√(X₁₁X₂₂) = −0.557 (glob), −0.570, −0.545, −0.714; X₁₃: −0.576, −0.576, −0.562, −0.620.
  Y_001 bound 1/√(nH_n): 0.577 (n=2) saturated at 97 % (exceeded at v_1), 0.426 (n=3) exceeded by 35–45 %. ✓.
  Note also X₁₄ correlation +0.20 (+0.48 at v_1). Non-resonant off-diagonal ≈ 0 ✓ (≤ 10⁻⁷¹ except v_1 3.6·10⁻⁷¹).
- "Archimedean": parts of X₁₂ (v_glob) = Θ_∞ piece −0.298 X₁₁, log piece +0.059 X₁₁, pole 8·10⁻⁶. The Θ_∞ piece dominates ✓,
  but the pair (1,2) exists only through dilation by the integer 2 and the log(mn) term is the arithmetic weight; "no prime
  contribution" is true of the kernel, not of the term. Say "archimedean kernel on an arithmetic dilate pair".
- Caustic-layer localization: **not measured** (no ω-resolved X₁₂). The claim "located at ω → 1" is ARGUED.

## 5. Overall reading (priority 5)
"Sign decided in the caustic layer by diagonal minus resonances" over-reads one μ, Galerkin data, a single gauge family
(M = 28), and an S that includes the unattributed parity/rough component. Fair statement: at μ = 15 on g*, the P3a/P2
normalizations of BRIDGE fail by O(1) factors with error ≤ 4 %; the deficit relative to S is carried by (1,2), (1,3), (1,5);
P3b is untested in its intended form. NUMÉRICO.

## 6. Corrections to apply to TEST_BRIDGE_001 / records
(K1) P3b: ALIVE → OPEN (global cut degenerate, cos(p,g*) = −1 + 5.7·10⁻⁹; V_J cuts hybrid, edge 13–91 % W*).
(K2) Closure: state the defect as ≤ 0.02 S; P2 band [0.51, 0.59] (v_glob), marginal at v_1.
(K3) "archimedean" → archimedean kernel on arithmetic dilate pair. (K4) caustic localization ARGUED.
(K5) Rough complement possibly the edge/jump datum; physical vs artefact OPEN.
**Do not retry:** global canonical Schur cut as an edge test (degenerate); quoting either −51 % (PRECHECK) or +0.04 %
(TEST_BRIDGE global) as the P3b edge share. Constraint 22: a P3b test needs p_λ Schur against a block containing v and
excluding the bottom eigenvector. No sign claimed. L′♯ OPEN; row D OPEN.
