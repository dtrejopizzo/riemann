# R153.018 — Lead blueprint, round 6: the prime-free body W_T and the arithmetic half-space

*Lead: Fable 5.1, 2026-09-19. Repair of round 5's failure (pointwise minorants are impossible by Bochner): use the support as structure.*

## 0. Object
On the unit sphere of `P_T` (L²) define `x(F) := (x_0, x_n)_{n<e^{2T}}`, `x_0 = ⟨(G_{Γ,T} − m_0)F,F⟩`, `x_n = c_F(log n) = ∫F(t)F(t−log n)dt`.
`W_T := {x(F)}` ⊂ R^{1+#contacts}. Then `⟨A_T F,F⟩ = x_0 − 2Σ_n w_n x_n`, `w_n = Λ(n)/√n`, and
**`A_T ≥ 0 on P_T ⟺ W_T ⊂ H_w := {x_0 − 2Σ w_n x_n ≥ 0}`.** `W_T` is prime-free (Gamma, interval, positions `log n`); arithmetic enters only via `w`.

## 1. Corpus check (record hits): phase 147 `cos(π/m)` autocorrelation-minimum lemma (R147_005 §, R147_003) — use it as the projection
bounds of `W_T` on each `x_n` axis; phase 138 D.15–D.17 (detecting cones — different objects: polar block, translation; D.16.2′ crossing
height `2πe·e^{2T}` = round 4's `H⋆`, to be recorded as RESTATEMENT in R153_014's next pass); phase 136 map ES-14 (Kreĭn); R153_016 §LP
reformulation; Au-Yeung–Poon convexity of joint numerical ranges (literature, cite). Expected: `W_T` with shift coordinates is new.

## 2. Tasks
(T1) **Convexity and closedness** of `W_T` (or of its closure) for `dim P_T = ∞`: prove via Au-Yeung–Poon/Hausdorff–Toeplitz on finite
Galerkin sections plus a limiting argument, or state precisely what is proved (PROVED/RESTATEMENT).
(T2) **`W_{log 2}` in R³** (coordinates `x_0, x_2, x_3`): compute its support function `h_W(u) = max_{‖F‖=1} ⟨u, x(F)⟩` on a grid of directions
(each value is a top eigenvalue of `u_0(G−m_0) + u_2(S_2+S_2^*)/2·… ` — write the exact operator), K-refined (spectral assembly of
`scripts/audit/`). Report: the projections on the axes (compare with phase 147's `cos(π/m)` values: for `L = 2T`, `a = log 2, log 3`),
the point `x(F_min)` of the `A_T`-minimiser, and **the facet** of `W_T` touched by the supporting hyperplane of `H_{w_ζ}` (is `w_ζ` a
normal to a smooth point or to an edge?). DIAGNOSTIC-NUMERIC with precision statements.
(T3) **Krein band at N = 3**: `{w_3 : W_{log 2} ⊂ H_{(w_2, w_3)}}` — an interval `[w_3^-, w_3^+]`; where is `Λ(3)/√3 = 0.6343` inside it?
Also the band in `w_2` at `T = ½log3` (only one contact) and the joint admissible region in `(w_2,w_3)` at `log 2` (a convex set; draw it
as a table of boundary points). Relate the band width to `λ_min ≈ 1e-7` (the band edge must be at distance `≈ λ_min/(2|x_3|)` from `w_3`).
(T4) **`W_{½log5}` in R⁴** (`x_0, x_2, x_3, x_4`): the same, plus: does the facet structure change qualitatively when the fourth
coordinate appears? Is `w_ζ = (w_2, w_3, w_4 = ½·log 2/2 …)` — compute `w_4 = Λ(4)/2 = (log 2)/2` — inside `H`'s dual cone (nothing
is certified there; DIAGNOSTIC; `λ_min(A_{½log5})` sign as the corpus's open (P153.3), report the Galerkin value with caveats).
(T5) **A law for the body?** Test whether the dual cone of `W_T` is described by the Ingham/`cos(π/m)` projection inequalities plus
Gamma coercivity alone (i.e. whether `W_T` equals the box/cylinder those inequalities define), or whether there are genuinely joint
constraints between `c_F(log 2)` and `c_F(log 3)` (expected: yes — `log 3 − log 2 = log(3/2)` couples them; quantify the coupling as
the difference between the true support function and the box bound in the direction `w_ζ`). Falsifier: the same body serves `Ξ_a` with
weights `w_n(n^a+n^{-a})` and doubled Gamma coordinate — verify `Ξ_{0.45}` exits `H` at `log 2` in this picture (it must).
(T6) **Honest statement**: the uniform claim "`w_ζ ∈ dual cone of W_T` for all `T`" is Weil's criterion; what this round adds is the
separation geometry/arithmetic and the finite-`T` theorems. Say what would make the body's law prime-free and explicit, and whether the
data support it.

## 3. Rules
Labels PROVED / RESTATEMENT / DIAGNOSTIC-NUMERIC / OPEN; FATAL rule; no sign for ζ beyond `T ≤ log 2` (T4's value at `½log5` is
diagnostic only); corpus-check lines; scripts `scripts/round6/`; deliverable `R153_019_ROUND6_BODY.md` (≤ 4000 words, tables).
