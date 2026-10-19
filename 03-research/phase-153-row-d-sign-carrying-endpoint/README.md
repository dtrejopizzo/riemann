# Phase 153 — Row D: does the certified endpoint carry sign? — **CLOSED**

Question: phase 137's acceptance test D.12-α (a finite `(S,T)` where the Weil form is `≥ 0` for `ξ` and `< 0` for the falsifier `Ξ_a`), run on the certified endpoint `T = log 2` of Paper 42.

Result: **D.12-α PROVED** for `(S,T) = ({∞,2,3}, log 2)`, `a ∈ {0.30, 0.45}` (interval certificate, -confirmed), via the new **Theorem A** (`Ξ_a` form = cross term of two `ξ` forms). New diagnostic object `T*(a)` (detection threshold, logarithmic in `1/a`). Prime-blindness refuted; endpoint is critical (`λ_min ≲ 10⁻⁷`). No sign for `ζ` beyond `log 2`.

Round 3 (same phase): (P153.5) single-pair detection — closed negative (measures Weil-mass concentration, exclusions subsumed by Platt–Trudgian); (P153.4) needle — closed negative (even/odd crossing drifting with T; "arithmetic contact" reading WITHDRAWN). See R153_006–R153_010.

Round 4: decay law of λ_min(A_T) on [0.30, log 2] — c(T) → ≈76 at log 2; Slepian/origin-gap prediction REFUTED; minimiser clears zeros up to height ≍ 2πe^{2T+1} and leaks above (explicit formula verified 0.997); Theorem 4.1 second-order expansion of A_T^{(a)} PROVED; rate = cancellation over 5–6 orders of O(1) terms (no term-by-term bridge); D.133 endpoint term does not vanish at the minimiser. See R153_011–R153_014.

Rounds 5–6: Φ_N built at the symbol level (hand proof by uncertainty fails at both endpoints; Bochner kills soft minorants); prime-free body W_T vs arithmetic half-space: W_T is NOT the cos(π/m) box (deficit 1.28 in the w_ζ direction) — no projection-only argument reaches Weil positivity; Lemma 3.1 (exact autocorrelation extrema on an interval) PROVED; "weights at the band edge" = λ≈0 restated, WITHDRAWN. See R153_015–R153_021.

Files: R153_000 blueprint · R153_001 construction r1 (§§1.3, 2, 3 superseded) · R153_002 audit · R153_003 construction r2 + certificate · R153_004 confirmation (PROOF ACCEPTED) · **R153_005 review closing decision (labels of record)** · `scripts/`, `scripts/audit/`, `scripts/certificate/` (`cert.py`, mpmath.iv, ≥ 300 bits).
