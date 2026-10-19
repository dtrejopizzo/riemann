# TEST_BRIDGE_001 — MORI15 kill-tests of BRIDGE_001 planks P1, P3a, P3b and P2 (NUMÉRICO)

Phase 199, numerical analyst. ,
no zero datum is used,
**Everything quantitative here is NUMÉRICO** on Mori VIII's published μ = 15 even-sector matrices (A + J, 832 even Legendre
modes, midpoints at 200 digits) and on the MORI15_EXTREMAL_001 bottom vector g* (120 digits); no new certification.

**Outcome in one line.** P3b (edge) is **alive**: with the canonical Schur p_λ the edge channel is benign (θ_emp = 0.996–1;
edge self-term 0.04 % of W globally). P1 is **localized in value to ≈ 80 %**: R_J = 1.26 for J = 2…20 (in [½,2] from J = 1),
but no J ≤ 50 gets within 20 % (Ritz minimum on 50 rungs = 1.20 W*); the last ≈ 20 % is carried by a rough complement of norm²
≈ 5·10⁻⁷¹. P3a and P2 **meet their kill criteria** on the extremal data: C*/S* = 0.19 (criterion [½, 2]) and
|Σ_{m≠n}X_mn|/S* = 0.55 (criterion 0.5; prediction 0.10), the deficit being the resonant (1,2), (1,3) archimedean
cross-dilate terms (−0.48 and −0.30 of X₁₁); non-resonant pairs are ≈ 0. No sign claimed. L′♯ OPEN; row D OPEN.

## 0. Corpus / index check, and why this is not a retry
- Read: BRIDGE_001 (§3.2 P1 test, §4.2 P2 test, §5.1 P3a test, §5.2 P3b test), MORI15_EXTREMAL_001 (+ data, scripts),
  U_001 Thm U.2.1 (Π = min-leak gauge), A_001 Thm 1.1 / Rem 1.1(iv) (edge split), E_001 Cor E.3, S_001 S.6, PRECHECK_T1_001
  (prolate-continuation pipeline; its μ = 10, 20, 30 runs were not duplicated), Y_001 entry (Thm B′, ARGUED (1,n) bound),
  AUDIT_L_SHARP_8. Index README l.467–474.
- Why new: these are exactly the falsification tests prescribed in BRIDGE_001 §3.2(i), §4.2, §5.1, §5.2, run for the first
  time; PRECHECK evaluated smooth prolate continuations, not the even-sector (Galerkin) extremal and its edge/bulk split.

## 1. Pipeline and conventions (scripts `TEST_BRIDGE_001_*.py`, data `TEST_BRIDGE_001_data/`)
- `rungs`: Legendre coefficients (Mori basis φ_j = √((2j+1)/2L)P_j(x/L), even j < 1664) of Eψ_k, k = 0,4,…,200,
  f = λ^{−½}ψ_k(u/λ), (Ef)(x) = e^{x/2}Σ_{n e^x ≤ λ} f(n e^x) (inverse of the Möbius map, MECH Prop 3.1); prolates at
  c = 30π from the normalised Legendre tridiagonal (300 modes, arb 420 bits); piecewise Gauss–Legendre on the 14 cells
  [log(λ/(n+1)), log(λ/n)], cells subdivided at equal arccos steps (P₁₆₆₂ resolution). Convergence: two node sets (QF 1, 1.5)
  agree to 10⁻¹⁰⁵ (k ≤ 100), 7·10⁻⁹² (k = 200). Rungs e_j = ψ_{4j} − (ψ_{4j}(0)/ψ₀(0))ψ₀ (f(0) = 0 imposed with 125-digit ψ(0)).
  The even-Legendre projection keeps the even part of Ee_j (the sector of g*).
- `galerkin`: G = sym(A+J) at 400 bits. Check: g*ᵀGg* = 4.763466135565557249946609·10⁻⁷⁰ = Rayleigh value (25 digits).
  Edge functional ε(g) = g(T)/√λ = f(λ); f*(λ) = −7.21938619188580·10⁻³⁵.
- `exterior`: for a Legendre vector h: Möbius inverse f₁ on [1/λ, λ], minimal-leak gauge in the MORI15 family (M = 28 even
  Legendre on |u| < 1/λ, f(0) = ∫f = 0) = Π within the family (U.2.1), ρ_h(ω) = r_h(λω) by direct quadrature (arb). Runs:
  ω ≤ 4 (300 nodes/cell), ≤ 24 (500), ≤ 48 (900), step 0.002 (33 points per Langer period). Check: ρ_{g*} reproduces the MORI15
  grid to 12 digits; leak of g* = 8.44·10⁻⁷⁰ (MORI15 upper value). S = λ∫_1^∞𝔴₁₅|Πρ|²dω (one-sided, BRIDGE convention), tail
  beyond ω_max bracketed by the Parseval budget (exact leak − computed mass) with weight between log 2μ and 𝔴(200).
- `analysis` (double, data ×10³⁵): dilate split of E.3: φ_n(s) = e^{s/2}ρ(n e^s), 𝔔 = Σ_{m,n}X_mn,
  X_mn = 𝒜(φ_m,φ_n) − (log m + log n)⟨φ_m,φ_n⟩ + A_mB_n + A_nB_m, 𝒜 = (1/2π)∫Θ_∞Re(F_mF̄_n) by FFT
  (Θ_∞ = Re ψ(¼+iτ/2) − log π), W_ext = λ𝔔. **Closure check (I1):** Σ_{m,n}X_mn·λ / W_Galerkin(v) = 1.02–1.10 at ω_max = 48
  (1.11–1.18 at 24; 1.3–1.6 at 4), so the exterior route reproduces the Galerkin value to 2–10 %.
- Precision: all cancellations at the 10⁻⁷⁰ level done in arb at 400–420 bits (radii ≤ 10⁻⁸⁰ on every W reported);
  ≥ 60 digits retained throughout the cancelling stages; the double stage handles only O(1) scaled quantities.

## 2. Task 2 — P1 localization: R_J = W(g_J)/W(g*)
g_J = L²(I)-projection of g* on V_J = span{P_N Ee_j : j ≤ J}; exact identity W(g_J) = W*(1 − 2‖δ‖²) + W(δ), δ = g* − g_J.

| J | R_J | Ritz min on V_J / W* | ‖g* − g_J‖² | W(δ)/W* | f_J(λ)/f*(λ) |
|---|---|---|---|---|---|
| 1 | 1.28632 | 1.28632 | 6.4·10⁻¹⁰ | 0.286 | 1.187 |
| 2 | 1.26946 | 1.26006 | 4.2·10⁻¹⁸ | 0.269 | 0.931 |
| 3 | 1.27444 | 1.25981 | 3.7·10⁻²⁴ | 0.274 | 1.016 |
| 5 | 1.27105 | 1.25224 | 5.9·10⁻³⁶ | 0.271 | 0.824 |
| 10 | 1.26057 | 1.23158 | 5.5·10⁻⁶⁰ | 0.261 | 0.917 |
| 11 | 1.26190 | 1.23137 | 5.1·10⁻⁶⁵ | 0.262 | 0.847 |
| 15 | 1.26375 | 1.22951 | 5.81·10⁻⁷¹ | 0.264 | 0.890 |
| 20 | 1.26466 | 1.22918 | 5.68·10⁻⁷¹ | 0.265 | 0.846 |
| 50 | 1.23249 | 1.20105 | 4.62·10⁻⁷¹ | 0.232 | 0.821 |

Truncation variant (MORI15 coefficients a_{4j}, J ≤ 14) agrees to 6 digits (e.g. 1.2863223, 1.2615621 at J = 1, 12).
**Reading.** R_J enters [½, 2] at J = 1 (BRIDGE kill criterion not met: **P1 not killed**). But R_J → ≈ 1.26 and stays there;
the fraction of the bottom value reproduced, W*/W(g_J), is 0.78 (J = 1), 0.79 (J = 2–20), 0.81 (J = 50): **0.5 is reached at
J = 1, 0.9 and 0.99 are never reached for J ≤ 50**, and even the W-optimal vector of the 50-rung span (well beyond the plunge
4J = 200 > 4μ) stays at 1.20 W*. The residual δ has norm² ≈ 5·10⁻⁷¹ (the Legendre floor of MORI15 §2) and Rayleigh quotient
W(δ)/‖δ‖² ≈ 2.2: it is a generic rough vector, and its coupling 2W(g_J, δ) = −2W(δ) lowers the value by ≈ 21 %.
So W is localized in the low self-dual block **to ≈ 80 %**, with a 20 % downward correction carried by the rough complement.
Also: the edge value f_J(λ) does not converge to f*(λ) (oscillates 0.82–1.19): the edge datum of g* is partly carried by the
same complement. Whether that complement is a Galerkin artifact or a property of the infinite-dimensional bottom is OPEN.

## 3. Task 1 — P3b: edge/bulk split, θ_emp
**Structural remark (PROVED, linear algebra).** If p_λ is the canonical Schur complement (W-orthogonal to the core block of a
space that contains the extremal), then b(v) ≡ 0 on that core block and θ_emp = 1 identically; BRIDGE §5.2's test is
non-trivial only when p_λ is Schur relative to a smaller block. Both versions were computed:
- **Global canonical Schur** (whole 832-mode even space): p = G⁻¹ε/(εᵀG⁻¹ε), e₂ = 3.4908·10⁻⁵, b* = 0,
  f*²e₂/W* = 3.82·10⁻⁴, C* = W(v*) = 0.99962 W*, cos(p, g*) = −1 + 5.7·10⁻⁹. Identity C* + 2f b* + f²e₂ = W* exact.
- **Schur within V_J** (p_J W-orthogonal to V_J ∩ core; v* = g* − f*p_J ∉ V_J, so b* ≠ 0):

| J | e₂ | C*/W* | 2f*b*/W* | f*²e₂/W* | 1 − b*²/(e₂C*) | S*/W* (ω ≤ 48) | θ_emp = 1 − b*²/(e₂S*) |
|---|---|---|---|---|---|---|---|
| 1 | 0.08347 | 0.2281 | −0.1413 | 0.9133 | 0.9760 | 1.51 | 0.9964 |
| 3 | 0.03785 | 0.7474 | −0.1615 | 0.4142 | 0.9789 | 3.90 | 0.9960 |
| 5 | 0.02442 | 0.8699 | −0.1371 | 0.2672 | 0.9798 | — | — |
| 12 | 0.01194 | 0.9311 | −0.0617 | 0.1306 | 0.9922 | 5.01 | 0.9986 |
| global | 3.49·10⁻⁵ | 0.9996 | 0 | 0.00038 | 1 | 5.22 | 1 |

The three terms sum to W* = 4.763·10⁻⁷⁰ to 20 digits in every row. With S* bracketed by the tail budget the θ_emp values
move by < 10⁻³ (range 0.9958–0.9987 over all brackets and ω_max = 24, 48). **P3b: alive (θ_emp ≥ 0.996 ≫ 10⁻²).**
Corrections: BRIDGE §5.2's scale estimate "edge self-term ≈ 10× W" is not what happens: e₂ ≤ 0.083 and f*²e₂ ≤ 0.91 W*
(0.04 % with the global canonical choice); the −51 % "edge defect" of PRECHECK (𝒲_ext applied to the non-core f*) and AUDIT_7's
−51…−78 % are not the canonical split — in the canonical split the edge piece is **positive** (+0.04 % … +0.77 W*).

## 4. P3a on the same data: C*/S* (the plank that fails)
C*/S* with S* = λ∫𝔴|Πρ_{v*}|²: **0.19** (global; 0.187–0.192 over the tail bracket), 0.19 (J = 3), 0.18–0.19 (J = 12),
0.14–0.15 (J = 1) at ω_max = 48 (tail mass ≤ 2 %); ω_max = 24 gives 0.18–0.21. Even the lower bound S ≥ S_{[1,4]} gives
C*/S* ≤ 0.45. The core part u_J of the **low-block projection** (u_J = g_J − f_J(λ)p_J ∈ V_J, i.e. no rough complement) gives
C/S = 0.27–0.39 (J = 3, 5, 12), closure ΣX/C = 1.02–1.06. **BRIDGE's P3a kill criterion C*/S* ∉ [½, 2] is met at μ = 15.**
Contrast: PRECHECK's smooth prolate continuations give C/S ≈ 0.91–1.07. The difference is in the data, not the form: for the
same rung coefficients the min-gauge leak of the even-sector (Möbius) datum exceeds the prolate leak Σy_k²(1−λ_k)
(6.36 vs 4.07·10⁻⁷⁰ at J = 12; 4.05 vs 2.73 at J = 3). ARGUED: the extra component is the image of the parity projection
(Φ_{f_−} = ½(Ψ − Ψ∘R), AUDIT_6), i.e. the even window datum is not the prolate continuation; it lives at larger ω
(mean weight 𝔴̄ = 5.9–6.6 vs 4.0 on ω ≤ 4) and is the part that the cross-dilate terms cancel.

## 5. Task 3 — P2: cross-dilate (1,n) terms vs (1,1) on ρ_{v*} (ω_max = 48, n ≤ 47)

| vector | X₁₁/S | Σ_n X_nn/S | Σ_{m≠n}X_mn/S | (1,2)/X₁₁ | (1,3)/X₁₁ | (1,4) | (1,5) | non-resonant/X₁₁ | X₁₂/√(X₁₁X₂₂) | X₁₃/√(X₁₁X₃₃) |
|---|---|---|---|---|---|---|---|---|---|---|
| v_glob | 0.612 | 0.761 | **−0.550** | −0.479 | −0.295 | +0.062 | −0.148 | +0.0002 | −0.557 | −0.576 |
| v_12 | 0.594 | 0.747 | −0.552 | −0.500 | −0.303 | +0.067 | −0.149 | −0.002 | −0.570 | −0.576 |
| v_3 | 0.592 | 0.738 | −0.542 | −0.483 | −0.290 | +0.050 | −0.151 | +0.007 | −0.545 | −0.562 |
| v_1 | 0.531 | 0.673 | −0.519 | −0.675 | −0.342 | +0.152 | −0.176 | +0.095 | −0.714 | −0.620 |

((1,n) entries count both (1,n) and (n,1).) Parts of X₁₂ (v_glob): archimedean −0.293 X₁₁, log term +0.058, pole −10⁻⁵ — the
cross terms are **archimedean (nonlocal Lévy kernel)**, with a large plain overlap ⟨φ₁,φ₂⟩ = −0.084 X₁₁ (≈ −0.4 ‖φ₁‖²·𝔴̄⁻¹):
dilates 1 and 2 of the even-sector datum are strongly anti-correlated, not oscillation-decoupled. Low-block core vectors:
Σ_{m≠n}/S = −0.42…−0.45. Stability: ω_max = 24 → 48 changes these ratios by ≤ 0.02.
**Verdict.** |Σ_{m≠n}X|/S = 0.52–0.55 ≥ 0.5: **BRIDGE's P2 kill criterion is met** (marginally but stably); the predicted
size ≈ 0.10 (c^{−½}) is off by ×5. The non-resonant pairs are ≈ 0, consistent with Theorem B / B′ on their classes; the
deficit is entirely in the resonant (1,n) pairs, n = 2, 3, 5. Y_001's ARGUED bound 1/√(nH_n) (0.577 for n = 2, 0.426 for
n = 3) is saturated at n = 2 and **exceeded at n = 3 (0.56–0.62)** — these data sit at the ω → 1 caustic/edge layer that
Y_001 excludes by hypothesis, so this is no contradiction with Y's theorem, but it locates the failure there.

## 6. Labels, verdicts, residuals
- **NUMÉRICO:** all tables (μ = 15 only; Galerkin data; Π within the M = 28 gauge family; tails beyond ω = 48 bracketed;
  dilate closure 2–10 %).
- **PROVED (elementary):** b ≡ 0 for the canonical Schur p_λ on a block containing the vector (so the canonical θ test is
  trivially 1); W(g_J) = W*(1 − 2‖δ‖²) + W(δ) for the L²-projection of an eigenvector.
- **ARGUED:** parity-projection origin of the extra exterior component (§4).
- **Plank verdicts at μ = 15:** P3b ALIVE (θ_emp ≥ 0.996; edge benign). P1 NOT KILLED (R_J ∈ [½, 2] from J = 1), localized in
  value to ≈ 80 %, not to 90 %. **P3a: kill criterion met (C*/S* = 0.19).** **P2: kill criterion met (0.55 vs 0.5),
  carried by resonant (1,2), (1,3).** The sign burden of the chain therefore sits in P3a/P2 on the caustic layer ω ∈ (1, 2)
  of the even window datum, not in the edge channel. Not a NO-GO of the route (single μ, Galerkin data); μ-trend OPEN.
- OPEN: whether the rough complement (§2) and the parity component (§4) persist for the infinite form; same tests at μ = 7,
  10, 20 (Mori V/VIII data not restored); deflated λ_min of BRIDGE §3.2(ii) (not run).
- **Do not retry:** BRIDGE §5.2 θ-test with the global canonical Schur p_λ (b ≡ 0 identically); reading PRECHECK's −51 % as
  the edge share of the canonical split; using smooth prolate continuations as evidence for P3a on the even-sector extremal.
- No sign claimed. L′♯ OPEN; (★★) OPEN; row D OPEN.
