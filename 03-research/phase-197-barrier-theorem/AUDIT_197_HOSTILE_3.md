# AUDIT_197_HOSTILE_3 — audit of BARRIER_X_001 (track X)

 Checked against P46 main.tex
(l.3093 v_n=2a(n)/√n; lem:degen l.3249; def:PD l.622; definite-parity kernel l.4367; thm:log5A l.4627), BARRIER_001 Thm 3,
AUDIT_197_HOSTILE(_2), INV_I_001, L54/L55-A, VERIFY_CLAMPED_AND_EDGE_LAW (U3).

## (a) X0 — exact Bohr defect: CONFIRMED (PROVED + NUMÉRICO)
|Im R|² = (2|R|² − R² − R̄²)/4, M R² = 1 (constant term), M|R|² = ∏_p Σ_k r_{p,k}² p^{-k} (Parseval + Kronecker) ⇒ Δ = ½(∏−1). ✓
NUMÉRICO (2·10⁶ random t ∈ [0,10⁷]): R = 1−2^{-s}: 0.24985 vs ¼; R = (1−2^{-s})(1+3^{-2s}): 0.33305 vs 1/3. ✓
Normalisation w_T(n)=2c_{F⋆}(log n)/√n and the lem:degen inequality as stated match P46 (lem:degen is in v; v=2a/√n). ✓

## (b) X1 — lattice dichotomy: CONFIRMED with one precision
(a) pinning for ε<1/(2N): ✓ (d(p^k)≠0 needs some r_{p,j}≠0, j≤k, cost ≥ 1/(2p^j) > 1/(2N)).
(b) top layer ±1 with equal defect: ✓ (d(p^k)=k log p·r at the lowest changed level; r=−1 gives b=0 ≥ 0). Precision: moves with
several changed levels of the same p (p^k, p^{k+1} both in 𝒬, possible for small p) are also admitted; antipodality is claimed
only for the single-level generators — correct as stated ("contains an antipodal pair").

## (c) X2 — Kronecker parity: argument CORRECT; scope OVERCLAIMED (major)
The invariance is right: u ↦ −u on the torus is Haar-preserving, acts compatibly on s and 1−s, commutes with t-shifts, so it
covers joint distributions over finitely many lines, sup/closure of value set, max/min, L^p, entropy, equioscillation counts,
and even lagged correlations (t, t+h) — any functional of the stationary process t ↦ (R(σ_i+it),R(1−σ_i−it)). D1 and D2-type
defects are covered. NOT covered: fixed-t / real-axis evaluations (ρ_a(σ) at t=0: u=1 ↦ −1), anything coupling to ζ itself.
**Defect found:** Cor. X2′ applies to σ-closed classes, and the memo lists 𝓘 as one. 𝓘 is NOT σ-closed: R_p = 1+2x
(L_p=(1+2x)/(1−x) ∈ 1+xℤ≥0[[x]]) maps to 1−2x, b_p = −1 < 0. The positivity b ≥ 0 already breaks σ on 𝓘 (generically, not only
at the {0,1} vertex). What survives: on the single-level top-layer generators r=±1 (X1(b)) σ-closure holds, so the antipodal
conclusion is valid **near Λ in the ε<1/(2√N) regime**, and on real Euler families E_N without positivity. Fix: restate
𝒦_X^dist as "ratio defects on σ-closed classes; 𝓘 only in the X1(b) regime". The NO-GO label stands with that scope.

## (d) X3 — {0,1}-vertex: (a) PARTLY FALSE; (b)–(d) collapse to BARRIER_001 Thm 3 (no escape)
- **X3(a) counterexample** ("every coordinate change ≤ 0"): p=2, 2^k ≥ √N, 2^{k+1} < N, R_2 = 1 − x^k + x^{k+1}. Then b_{2^k}=0,
  b_{2^m}=1 (m≠k) ∈ {0,1}; d(2^k) = −k log 2, d(2^{k+1}) = +(k+1) log 2 > 0; Δ = ½(2^{-k}+2^{-k-1}) ≤ ε admissible.
  The set is finite but NOT coordinatewise one-sided; the claim "on 𝒬 the rows reduce to δa(q) ≤ 0" is false where p^k,p^{k+1} ∈ 𝒬.
  It does lie in C_div (first-order δb_{2^{k+1}} = 1 − 1 = 0). Finiteness and (d) survive.
- "Tangent cone" of a finite set at Λ is {0}; what is meant is cone(S−Λ). Language fix only.
- **Distinction "sup of linear forms of the comb, not a def:PD certificate"**: real as objects (a premise cone ≠ a dual triple),
  but it does NOT escape Thm 3(ii)/(iii). The method's conclusion over a finite S is Ψ ≡ min_Q λ_A(T;Λ_Q) (uniform), so it is
  branch (iii)-type with |π_N S|>1: soundness needs WP_T on each Λ_Q, each a statement of the same kind as WP_T(Λ) (by
  lem:degen only an upper bound links them; no lower bound transfers). Collapse = REF-D⁺, as the memo says. Confirmed.
- X3(c) falsifier exclusion: ✓ for a_P/0 only when 2 is deleted (cost ¼); deleting large primes is cheap and is precisely the
  cone generator — so O_6 is "excluded" only in the weak sense. Beurling/Ξ_Q/Epstein outside 𝓘: ARGUED (keep).

## (e) X4 — parity sign at top lags: PROVED (lemma), use CONDITIONAL
The proof is correct; a definite-parity minimizer always exists (J commutes; eigenspace J-invariant, P46 l.328/l.4367), so the
only hypothesis is "no zero of F⋆ in (T−δ,T)". U3 (ARGUED; Hopf lower bound a_±≠0 NOT available, only |h*| ≲ (log1/δ)^{−1/2})
neither supplies nor refutes it. Quantitatively c_{F⋆}(u) = O(δ'·sup_{edge}|F⋆|²) for u=2T−δ', so the odd-sector falsifier
2|c|k log p/√q > λ_A is unattainable unless λ_A ≈ 0 — X4 cannot by itself produce a falsifier or a sign. ✓ labels.

## Residues
(i) even levels p^{2j}<N: well-posed (σ fixes them); but every class containing ±1 single-level moves at even levels reproduces
X1 antipodality there by X0 (r² dependence) — one-sidedness again needs order, i.e. back to X3. Low.
(ii) sign of c_{F⋆}(log q) on 𝒬 / parity sector: well-posed, not in the index, Farkas condition of X3(b) is a finite explicit
check; but it decides only the REF-D⁺ family, not positivity. Medium; **most promising** (cheap, falsifiable, gives structure on F⋆).
(iii) non-distributional FE defects (real axis, |ξ|² weights): near-retry of INV_P/INV_Q; needs a written new reason. Low.

## Verdict
X0, X1, X4 confirmed; X2 argument correct, scope corrected (𝓘 not σ-closed); X3(a) one-sidedness FALSE (finite, not
orthant-one-sided); X3(b,d) collapse to REF-D⁺ (no escape from Thm 3). No sign. Row D: OPEN.
