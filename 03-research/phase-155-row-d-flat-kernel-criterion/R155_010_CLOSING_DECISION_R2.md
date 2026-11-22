# R155_010 — Closing decision, round 2 + reverse-engineering track

Inputs: `R155_004` (memo R2) / `R155_007` (audit R2); `R155_005` (reverse track) / `R155_006` (audit);
`R155_008` (103-window regime scan) / `R155_009` (audit). rules applied: labels only by audited
record; DIAGNOSTIC for anything derived from the zero table (circularity no-go `phase-4/00-PROOF-LOG:168`,
ES-2); no sign for ζ beyond `T ≤ log 2`; no statement about zeros.

## 1. Labels of record

| statement | label | source / repair |
|---|---|---|
| **Theorem N**: no lattice certificate of step `2T/M`, `M ≤ 8`, proves `λ^P(½log3) > 0`, β-uniformly, for any range, atom count or tail lemma (interval enclosure `Ceil(8) ≤ −5.70·10⁻³`, independent quadrature inside the enclosure) | **PROVED (machine-verified)** | R155_007 (a). Scope repaired: "step ≥ 2T/8" → "step 2T/M, M ≤ 8" (R-1). Tolerance, not the sharp constant 45169.4, for the β-box (R-2). |
| **Theorem B**: any certificate of value `c ≥ 0` has `‖β‖₂ ≤ (V⋆−c)/r₀`; `r₀ = O(T⁴)` structurally (`g₀−¼g₁ = 1−u⁴/384+…`) | **PROVED** | R155_007 (c) |
| **Theorem SC** (the ten-prime question): any non-negative sub-comb of mass `A < −C₀ = 5.3721834` gives `λ ≤ C₀ + A + φ((3π/2T)²) < 0` for all `T ≥ T₀(A)`, `T₀` explicit; positivity is a collective property of the full initial segment `{n < e^{2T}}` | **PROVED** (= Cor 2.6 for a sub-comb, `main.tex:384,406`) | R155_007 (d). Slips: `T₀(0.5637) = 1.313456`; the "first ten primes" window has contact set = the 16 prime powers `< 31`. |
| **Lemma R1 / Theorem R / Cor R2 / Cor R3**: periodisation of a `(P)`-feasible μ is a test kernel; `Ceil(M,T;β) → λ^P`; the test-kernel family is not lossy in the limit (M→∞ half of MAJOR-4 closed; fixed-M lossiness OPEN) | **PROVED** | R155_007 (e). R-8: measured Ceil is unrestricted `sup_β`, not `Ceil_B`. Rate `p = 1.2505`: DIAGNOSTIC, not asserted, and per R-3 cannot discriminate exponents. |
| `Ceil(M, 0.58)` capped at `≈ 2.0·10⁻⁴` (two figures stable under τ₀-refinement); E1 not refuted but capped; the recorded −3.20·10⁻³ is optimiser, not resolution | **DIAGNOSTIC** | R155_007 (b), R-3 |
| `Ceil(24, 0.68) < 0`, `Ceil(24, log2) < 0` | **DIAGNOSTIC, sign robust, digits spurious** (`−2.28e−7` → `−7.51e−6` on refinement) | R-3. Enclosure would be a theorem; margin ~1e−5, easier than estimated. |
| "the M-sweep must start at `M ≥ 64`"; "Ceil at β=(2,0) ≈ 1e−9 at every two-prime window" | **WITHDRAWN** | R-4, R-5 (contradicted by the memo's own logs) |
| **Theorem Z numerically verified** on both sides, eight regimes, `2.6e−7…2.8e−6` (GL 800); first check of (7.2) in the corpus (`phase-118 W5` is the primal identity) | **DIAGNOSTIC (verification)** | R155_006 1, 10; R155_009 |
| **Smoothness / far-zero lemma**: `w ∈ W_T ∩ C^k_c` across the edge ⇒ `ŵ = O(|t|^{−k−2})` ⇒ far-zero residual `≍ Γ^{−k−1} log Γ` (`k ≥ 0`); an off-line zero above Γ contributes at most `e^{U/2}` times an on-line one; extends Thm Z(ii) from `C_c^∞` to `C_c^k` | **PROVED (to be written for Paper 46)** | R155_006 2 |
| **Bernstein grid lemma**: `min_ℝ f ≥ min_grid f − ½U²‖f‖_∞δ²` for `f` band-limited to `[−U,U]`; turns Paper 46 §5's grid warning into a theorem | **PROVED (to be written)** | R155_006 4 |
| **Lemma R**: even `w ∈ L¹`, continuous, `w ≡ 1` on `[−2T,2T]`, `ŵ ≥ 0` ⇒ `w ≡ 1`. Consequence (a): `f_w ≥ 0` is never termwise in the zeros. Consequence (b) "no finite zero universe admits a flat-top certificate": only for compactly supported `w` | **PROVED**; (b) **restricted** | R155_009 |
| (E) `A_T` jumps by `v_n` at `½log n`, `τ_env^{mf} = 2πe^{A_T}` multiplied by `e^{v_n}`; (D) `τ_env^{mf}/2πe^{2T} = e^{A_T−2T}`; (M) `λ^W` non-increasing (restates Cor mono) | **PROVED (elementary)** | R155_009. Repairs: `N_T` convention `log n < 2T` makes `A_T` left-continuous (one-sided limits); `τ_env^{mf}` is Prop env's multiplier-free part only. |
| (C) `f_w(τ)` continuous in `T` across prime entries for a fixed shape family and fixed domain | **PROVED (as stated)**; "λ^W continuous" and "R155_005's step function was a moving-domain artefact" **NOT established** (domain frozen at τ≤60 on both sides; at the one moving-domain entry the value jumps 3.2×) | R155_009 |
| Universal profile (sup deviation `0.13`, not `0.0785`), `∫w = 3.13±0.07`, rate `0.17±0.01`, `~24` contacts; in-regime extrapolation keeps the (negative) sign 6/6, extrapolated weights 1.2–1.6× worse than LP; cancellation budget at `½log3`: 10 zeros `4.0e−4`, 100 `6.0e−6`, 1000 `1.2e−7` | **DIAGNOSTIC** | R155_009 |
| Reverse-engineered `w_T` positive value `+1.39e−6` at `½log3` | **WRONG** (grid: `f = −1.72` at `τ = 16.745`; the prime-side "refutation" `−8.69e−5` was GL quadrature order) | R155_006 3 |
| "no law in T" (R155_005); exponential-column negative control as archived; weight-side Theorem O as a *lower* bound | **WRONG / WITHDRAWN** | R155_006 6, 8; next-step (ii) mis-classified (upper bound, compactness fails as Thm O) |

Row-D label unchanged. Endpoint of record unchanged: `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`.

## 2. Answer of record to the the question (reverse engineering from the known truth)

1. The certificate at window `T` is a function of the zeros (Theorem Z). In a universe of finitely many
 zeros the optimal dual certificate is the zero measure itself (Suzuki), positivity is `Σ|ĥ(γ_j)|² ≥ 0`
 and is automatic; the toy universe determines no prime comb and informs nothing (R155_008 §7bis).
2. What must appear "sí o sí" is positive-definiteness of the prime side (Bochner) — Weil's criterion,
 rows A/B/C. Building D from the prime side without the zeros is Problem B = RH.
3. The zero-side LP does learn a universal profile, and it extrapolates regime to regime; what it
 extrapolates is negative at all 103 windows. Cause identified (R155_009): the lattice `h = 0.25` is
 effective order `M ≈ 4.4`, inside the class Theorem N proves impossible. **Rule for every future
 track: start above the TK ceiling.**
4. Positivity is collective (Theorem SC), never termwise (Lemma R): no finite sub-comb of primes and
 no finite set of zeros carries it.

## 3. Repairs ordered (records)

- `R155_004`: R-1 at lines 18, 81, 501 and `README.md:17`; R-2 tolerance; R-3/R-4/R-5 (delete the M=64
 claims and reading 3; mark §3 two-figure only); R-8; SC slips; R-9 remove the surviving "21 %" at
 `R155_001:29`, `README.md:11`; R-10 note.
- `R155_005`: C¹ vs C² of the test weight (3 places); delete §0.5/§6.2 quasi-positive readings;
 correct item 3 diagnosis; note L is basis-dependent; mark control as `s ≥ 1.5` class.
- `R155_008`: universal-profile statistics (0.1332 / mean 0.060; L=5 0.1378; capped 82/103; `‖w‖_∞=1`
 98/103; Γ 800→20000 4.7e−9 at T=0.62 only); delete "real analytic off {½log n}"; restrict
 consequence (b); withdraw "the domain is the whole of it" and §5.3's Prop-env threshold (with
 `‖ν_w‖_TV ≈ 48.7` it is `~2.4e22`); add the missing conditioning test; `A_T` one-sided limits.

## 4. Paper 46 changes ordered

1. §8 (`main.tex:1269–1272`): replace the parenthesis by **Theorem N** with Theorem B and its
 Lemma (≈1 page), scope `M ≤ 8`, tolerance stated; fix "step ≥ 2T/8" at `main.tex:1270`.
2. §8: **Theorem SC** (sub-comb negativity) after Cor mono's use, with the ten-prime example and the
 collective-property reading.
3. §7: **Lemma R** (+ consequence (a)) beside Cor 7.4; **smoothness/far-zero lemma** extending
 Thm Z(ii) to `C_c^k`; note that Theorem Z has been checked numerically on both sides
 (DIAGNOSTIC, eight regimes).
4. §5: **Bernstein grid lemma** as a lemma, with Theorem C's grid re-read through it.
5. §8.2: one paragraph on the regime dichotomy (E)+(D): `τ_env^{mf}` multiplied by `e^{v_n}` at each
 entry, index `e^{A_T−2T}`; one sentence for (M).
6. §8: Theorem R / Cor R3 (test-kernel family not lossy in the limit) as the resolution of the
 "whether the ceilings converge" question at `main.tex:1276–1277`; rate OPEN.
7. §9 tables: labels above. Nothing from R155_004 §3 beyond one significant figure; no M=64 claims;
 nothing from the zero table beyond DIAGNOSTIC.

## 5. Next round (round 3)

- Enclosures of `Ceil(24, 0.68) < 0` and `Ceil(24, log2) < 0` (same script; first proved negatives at a
 two-prime window if they close).
- The λ^P version of Theorem 3.3 (still owed from R155_003 repair (1)).
- Problem A proper: a class-dependent **lower** bound. Everything in rounds 1–2 and the reverse track is
 upper-bound-side.
