# PROOF_L_SHARP_KK_001 — Reopening soft constraint 11: the condition (H) on a declared class, via the CC_001 envelope

Phase 199, prover (pen and paper; NUMÉRICO only on existing files).
ARGUED / OPEN / NO-GO / NUMÉRICO.

## 0. Corpus / index check and reason for reopening
- Read: AUDIT_CONSTRAINTS_001 §3 row 11 and §4 item 4 ("prove (H) itself ... a flow proof that proves it is legal"; escape via
  CC_001); H_001 §1–§5 (dilated frame, Lemma H.2, (H-ODE), Thm H.5, falsifier table); AUDIT_L_SHARP_2; CC_001 (Thm CC.4,
  (H_ν), explicit η); Z_001 Thm C; BB_001 (BB.1, Schur depression W(δ) = 0.2325 W*); FF_001/AUDIT_16 (corrected FF.2);
  TEST_MOBIUS_SAWTOOTH_001 (Mori V Table 1, κ₄ = λ_min/(1−λ₄), μ = 11–20); ROUTES-TRIED-INDEX README (phase-199 block,
  R186_038 α.3, SIGN-REAUDIT I16, R186-S2seeds Fold/Grönwall NO-GO).
- Not a retry. The recorded NO-GO (H_001 §4.3, α.3) is: (H) is a virial of the minimiser at relative precision 1/c. New here:
  (1) (H) is evaluated on a family where both sides are explicit (prolate tails), using the now-PROVED envelope CC.4, which did not
  exist when H_001 was written; (2) for the minimiser, (H) is factored as (prolate rate) + (rate of an O(1) ratio), and the
  ratio's requirement is stated in integrated form and confronted with the only multi-μ data (Mori V). The class of the method
  changes from "bound ρ_N at precision 1/c" to "bound an O(1) ratio from below polynomially".

## 1. The integrated form of (H) is what Grönwall uses (PROVED, elementary)
From (H-ODE), ∂_cQ = −ρ_N Q + (ρ_L − ρ_N + A/c)κμ^{−A}L. Writing R(c) := N(c)/L(c) along any C¹ (or piecewise C¹) family:
  d/dc log R = ρ_L − ρ_N,   and   Q ≥ 0 ⟺ R ≥ κμ^{−A}.
Hence pointwise (H) on [c₀,c] is sufficient but **only the integrated statement**
  (H_int)  log R(c) − log R(c₀) ≥ −A log(c/c₀)   (all c ≥ c₀)
is needed: (H_int) and Q(c₀) ≥ 0 ⇒ Q(c) ≥ 0. Conversely (H_int) with the right constant is implied by Q ≥ 0 with margin.
So for a *fixed family* (H_int) is a value statement; on the *minimiser* it is L′♯ written as a ratio (no gain, H.5(ii)).
This is the precise sense in which "proving (H)" can be legal: pointwise derivative control is never required.

## 2. Part (i): the pure-prolate-tail family (CONDITIONAL on the identification (Id); otherwise PROVED)
**Setting.** k even fixed, c = 2πμ (μ = N in CC_001's notation), ψ_k(c) the prolate of time·band c, 1−λ_k(c) its leakage.
Leakage side (CITED Slepian + Lemma H.2, PROVED): L_p(c) ≤ leak_c(ψ_k) = 1 − λ_k(c), ρ_L^p := −d/dc log(1−λ_k)
= (2/c)λ_kψ_k(1)²/(1−λ_k) = 2 − (k+½)/c + O(c^{−2}).
Form side: **(Id)** N_p(c) := value of the window/exterior form on the k-th prolate tail = caustic-layer diagonal + resonances
+ (layers ω ≥ 2). Thm CC.4 (PROVED under (H_ν)) gives the diagonal exactly as (1−λ_k)·D(μ)·(1+η),
D(μ) := (2/3)log 4μ − 0.107689, |η| ≤ (21.4 log c + 1.54ϑ_k/c + 523)/(c(1−|e₁|)); the resonances are ≤ (2/π)·0.6174·μ^{−½}log(1.25μ)
per unit mass (Z.6, ARGUED); identification of N_p with this sum is Z_001 §5 (ARGUED; NUMÉRICO μ = 15, ψ₄: 4.96 vs 5.03).
Caveat (HARD): ψ_k(1) ≠ 0, so ψ_k is **not** admissible (φ(1) = 0 fails); the family is a comparator, not a competitor.

**Proposition KK.1 (ratio on the prolate family).** Under (H_ν) and (Id), with η_tot := η + resonance share:
  R_p(c) = N_p/(1−λ_k) = D(μ)(1+η_tot),
and therefore, on any [c₀,c] where |η_tot| ≤ η̄ < 1:
  log R_p(c) − log R_p(c₀) ≥ log(D(μ)/D(μ₀)) − 2·artanh-type loss ≥ (2/3)·log(log4μ/log4μ₀)·(1+o(1)) − log((1+η̄)/(1−η̄)).
So (H_int) holds on the prolate family with A = 0 up to the bounded constant log((1+η̄)/(1−η̄)), i.e. with any A > 0 for
c/c₀ ≥ ((1+η̄)/(1−η̄))^{1/A}. *Proof.* Divide CC.4 by 1 − λ_k; take logs; |log(1+η)| ≤ artanh-bound. □
**Rates (ARGUED, pointwise).** Formally ρ_N^p = ρ_L^p − (2/3)/(c·D(μ)) − η_tot′/(1+η_tot), since d/dc log 4μ = 1/c. The first
correction is negative (N_p decays *slower* than the leakage, by a factor growing like log μ): pointwise (H) has room
A/c + (2/3)/(cD). **But CC.4 bounds |η|, not η′**; pointwise (H) is NOT proved — only (H_int), which is all that is needed (§1).
**Thresholds (computed from CC.4's constants, k = 4, ϑ ≈ 9c):** |e₁| < 1 needs μ ≳ 20; |η| < 1 needs μ ≥ 131 (μ = 130: |η| ≤ 1.011;
μ = 200: 0.62; μ = 1000: 0.12). So (H_int) on the prolate family is **non-vacuous only for μ ≥ 131**; this is the
"μ₀ ≈ 130" of AUDIT_CONSTRAINTS_001 pair exclusion, now with an explicit constant.

## 3. Part (ii): the minimiser — factoring (H) through an O(1) ratio
Let g* = p + δ be the Galerkin minimiser, p its projection on the rung span V (TEST_BRIDGE / BB_001). By (BB.1, PROVED given
QGQ ≻ 0, NUMÉRICO 1.09 ≫ λ*): W* = W(p) − S(p), S = ⟨QGp,(QGQ)^{−1}QGp⟩ ≥ 0 (Schur depression). Define the ratios
  d(c) := S/W(p) (depression ratio),  τ(c) := W(p)/N_p-comparator,  ℓ(c) := L*/L_p.
Then exactly R*(c) = N*/L* = R_p(c)·τ(c)·(1−d(c))/ℓ(c), so
  ρ_N* − ρ_L* = (ρ_N^p − ρ_L^p) − d/dc log τ + d′/(1−d) + d/dc log ℓ.   (KK.2, identity)
**What is needed (exact).** By §1 and KK.1, (H_int) at the minimiser ⟸ Q(c₀) ≥ 0 and
  (KK.3)  log[τ(1−d)/ℓ](c) ≥ log[τ(1−d)/ℓ](c₀) − A log(c/c₀) − (2/3)log(log4μ/log4μ₀) + log((1+η̄)/(1−η̄)),
i.e. the O(1) ratio Φ(c) := τ(1−d)/ℓ may decay at most polynomially. In pointwise form this is
  −d/dc log Φ ≤ A/c + (2/3)/(cD) (+ η′ terms)  — the **ratio-virial** —
which is O(1)-precision in Φ (not 1/c-precision in ρ_N): strictly weaker than the original (H) requirement **as a precision
requirement**. The edge channel (FF.2 corrected, PROVED): the exterior jet is [1 + (−1)^k c_μμ^{−½}]g^{(k)}(a), a factor
1 ± μ^{−½}; its log-derivative in c is O(μ^{−3/2}/c)·(jump at squarefree changes of μ(μ)) — it contributes O(μ^{−½}) to log Φ
and is harmless for KK.3 except at the integer jumps of c_μ (bounded, O(μ^{−½})). (ARGUED.)

**But KK.3 is not new content (PROVED as a logical statement).** Since Φ = R*/R_p and R_p is explicit (KK.1), KK.3 is
equivalent to R*(c) ≥ R*(c₀)(c₀/c)^A·(bounded explicit factors), i.e. to λ_min(c) ≥ κ'(μ₀/μ)^A(1−λ_k): **L′♯ restated** with
the prolate as calibrator. In particular d(c) < 1 uniformly is *exactly* W(g*) > 0 relative to W(p) — the sign. The gain over
H_001 is quantitative (O(1) ratio, polynomial room), not a new source of sign. Falsifier (H_001 §5, CERT_FALSIFIERS PROVED):
for cΛ (c > 1) Δ passes from ≥ 0 to < 0 at a finite window, so d → 1 there; every step of §2 is comb-blind, hence any proof of
KK.3 must use the Λ-comb (Constraint 19/25 apply). KK.3 is the Λ-step, now with O(1) precision.

**Measured value of the ratio (NUMÉRICO, existing data only: Mori V Table 1 via TEST_MOBIUS_SAWTOOTH_001).** The closest
recorded proxy of Φ is κ₄(μ) = λ_min/(1 − λ₄(2πμ)) (even part). Per unit μ (Δc = 2π):
Δlog κ₄ = −0.138, +0.184, −0.082, +0.017, −0.031, +0.046, −0.071, +0.198, −0.086 (μ = 11→20); **net drift over 11→20: +0.037**;
|Δlog κ₄|/Δc ≤ 0.032, vs 1/c ∈ [0.008, 0.014]. Readings:
- Pointwise ratio-virial: FALSE locally with A ≲ 3 at each prime contact (local slope −0.022/unit c vs A/c); this is the
  sawtooth (κ drops 7–14 % at prime contacts). Pointwise (H) at the minimiser is not the right target (consistent with H.5(ii)).
- Integrated KK.3: holds on μ ∈ [11,20] with A = 0 (net drift positive) — NUMÉRICO, 10 points, even sector only.
- At μ = 15: d = 0.2325 (BB_001); range 0.19–0.29 across the recorded partitions (ROUGH/TEST_BRIDGE). No d(μ) series exists for
  μ ≠ 15: the requested μ = 10..15 comparison of d is NOT available in the corpus (OPEN, numerical).

## 4. Part (iii): the full chain, labelled
1. Dilated frame, N translation invariant, Lemma H.2 rate, (H-ODE): PROVED (H_001 §1, §3, §4.2).
2. §1 here: Grönwall needs only (H_int): PROVED.
3. Base: Δ(c) ≥ 2^{−2905} for 10π ≤ c ≤ 30π (μ ≤ 15): PROVED from Mori CITED (Prop H.1).
4. Gap 15 < μ < 131: no theorem. Covered only by certification (OPEN; Mori V Table 1 gives Galerkin values to μ = 20, NUMÉRICO,
   not certified). Required: certified Q(c) ≥ 0, or certified (H_int), on 30π ≤ c ≤ 262π.
5. Prolate comparator for μ ≥ 131: KK.1, PROVED under (H_ν) + (Id) [(Id) ARGUED via Z_001 Thm C resonances].
6. Minimiser: identity KK.2 PROVED (given QGQ ≻ 0, NUMÉRICO); residual KK.3 OPEN.
7. Conclusion: L′♯ for all μ ⟸ [3] + [4 certified] + [5] + KK.3 on μ ≥ 131 + KK.3 across the gap. CONDITIONAL on (Id), the
   gap certification, and KK.3.
**Exact residual.** (KK.3): the calibrated ratio Φ(c) = (N*/L*)/(N_p/L_p) decays at most like c^{−A}. Equivalently
(PROVED equivalence) L′♯ with prolate calibration. Measured: Φ-proxy κ₄ ∈ ~[4.0, 5.4], net log-drift +0.037 over μ = 11→20
(NUMÉRICO); d(15) = 0.2325 (NUMÉRICO).

## 5. Verdict
- PROVED: §1 (integrated form suffices); KK.1 modulo (Id) with explicit threshold μ ≥ 131; identity KK.2; KK.3 ⟺ L′♯ (calibrated).
- ARGUED: (Id); edge-channel contribution O(μ^{−½}); pointwise ρ_N^p = ρ_L^p − (2/3)/(cD) − η′/(1+η).
- NO-GO (new, record): pointwise (H) / pointwise ratio-virial at the minimiser — contradicted by the recorded sawtooth (NUMÉRICO);
  "prove (H) on the prolate family and transfer" — the prolate is inadmissible and the transfer step is KK.3 = L′♯ restated.
- Constraint 11 status: escape route evaluated; it reduces to KK.3 (the Λ-step at O(1) precision). Constraint 11 stays SOFT,
  sharpened: "a flow closes iff the calibrated ratio Φ decays at most polynomially (integrated)". No sign. Row D OPEN.
