# R131.015 — Audit of round 5

Independent of the
confirmation pass R131.014 (in progress when written).

## 1. Re-derived and found correct

| statement | check |
|---|---|
| (C1), (C2) | correct and carried; the two extra chart slips (Thm 8bis.2's `A_S`, Thm 8bis.4a fixed-chart) are real and are now flagged ✓ |
| Cor 8bis.1b′ | `F⋆F^† = V_N(n)·Δ^{(n),[h⋆h^†,N]}` ✓ (coset indicator convolution); bare `→ 0`, `♭ → −∞` geometrically; no rate headlined ✓. The construction's refutation of "one convention settles it" is right: the linear statement is about the smeared idempotent only |
| Thm 8bis.4a | `ω̂_fin(0) = Σ(\log p)2p^{−1/2}/(1−p^{−1/2}) > 0` ✓; `Π` primitivizes with no boundary terms ✓; `\hat g_T = (τ²+¼)T\hatφ(Tτ)`, bulk `≍ T`, Schwartz tail ✓; `Q_fin(g_T) > 0` at every finite chart ✓. Scope honestly confined to a fixed chart; colimit `OPEN` (Rem 8bis.4b) ✓. Since Paper 43 Thm 14.1 already makes the **full** form indefinite at a chart, this theorem's only content beyond 14.1 is that the failure is exhibited on the primitive sector with an explicit test; the paper does not overclaim it ✓ |
| Lemma 8bis.6 | partition of unity (8bis.12a); slow variation `(t−\log n)/gap_n = (x−n)(1+O(1/n))`; at most five `n`; bumps with `\|x−n\|>2` vanish since `\|\log(x/n)\| > gap_n` ✓; pointwise `1+O(e^{−L/2})` ✓; Step 2 ✓ |
| Lemma 8bis.5 | now `T_∞` with Chebyshev labelled; constant `4` correctly removed ✓ |
| Thm 8bis.7 Steps 1–3 | Riemann sums `w_1,w_2`, `λ`-weights (8bis.13d) ✓; determinant `≍ e^{L/2}` ✓; `a = O(e^{−L})` ✓; sup norm of the correction `O(e^{−L/2})` ✓ — with the two corrections below |
| §6bis.1 ledger row, §11 imports, Thm 8.2 carve-out, W19–W22, minors m1–m7, notes n1–n3 | ✓ as reported in R131.013 |
| scripts | ALL CHECKS PASS, ROUND-4, ROUND-5 CHECKS PASS (re-run); blocks (E),(F),(G) non-vacuous ✓ |

## 2. Findings (all in the quarantined §8bis.4; none touches B.1–B.9)

**LF5 (MAJOR) — the import (Wgr) is false as stated, and Step 4 of
Thm 8bis.7 rests on it.**  For the single-frequency test
`g_L = ψ(t/L)e^{iγ_0t}` (primitivized or not), the sum over zeros of
`h_L = g_L⋆g_L^†` is `Σ_ρ \hat g_L(ρ)\overline{\hat g_L(1−\bar ρ)}`. Every
zero on the line contributes `\|\hat g_L(ρ)\|² ≥ 0`. The off-line quadruple
`ρ_0, \bar ρ_0, 1−ρ_0, 1−\bar ρ_0` contributes
`2Re[\hat g_L(ρ_0)\overline{\hat g_L(1−\bar ρ_0)}]` plus a frequency-mismatched
(negligible) term, and for `ψ ≥ 0` both factors are positive reals:
`\|\hat g_L(β+iγ_0)\| ≍ Le^{(β−1/2)L}`, `\|\hat g_L(1−β+iγ_0)\| ≍ Le^{−(β−1/2)L/2}`
(dominated by the left end `t = L/2`). So the total is **positive**, of size
`≍ L²e^{(β−1/2)L/2}` — neither the sign nor the exponent `2\|β−1/2\|` of (Wgr)
holds, and no contradiction with `I_∂ ≤ 0` arises from this test. Weil's
actual proof of "positivity ⇒ RH" uses a **two-frequency** combination
`g_1 + c\,g_2` with `\hat g_1` peaked at `ρ_0` and `\hat g_2` peaked at
`1−\bar ρ_0` (a growing weight `e^{(β−1/2)t}` on `g_2`), and obtains negativity
from the **off-diagonal** term `2Re[\bar c\,B(g_1,g_2)]` of an indefinite
Hermitian form, not from exponential growth of a single term.
*Consequence:* Thm 8bis.7 is not proved from a true classical statement.
*Repair:* restate the import as Weil's theorem in its real form — "if RH fails
there is, for arbitrarily large `L`, a primitive complex `g_* ∈ C_c^∞([L/2,L])`
with `Q(g_*) := Σ_ρ \hat h_*(ρ) < 0`" — and **redo Step 4 with the actual
witness**: the Riemann-sum machinery needs the scale-invariant ratio
`‖g_*‖_∞‖g_*‖_{C^1}\,L\,e^{−L/4}\,/\,\|Q(g_*)\|` to tend to `0`. Estimate `‖g_*‖`
and `\|Q(g_*)\|` for Weil's witness (the `e^{(β−1/2)t}` weight on `g_2` makes
`‖g_2‖ ≍ e^{(β−1/2)L}` while `\|Q\|` is polynomial times `\|c\|`, so the ratio
may only close for `\|β−1/2\|` below a threshold). If it closes for all `β`,
state it; if it closes only for `\|β−1/2\| < θ`, state exactly that; if it
does not close, downgrade Thm 8bis.7 to `OPEN` with this obstruction written
out. Nothing in B.1–B.9 depends on the outcome.

**LF6 (MINOR, two items in Thm 8bis.7, Step 2–3).**  (a) The order of `b` is
misprinted: Cramer gives `b ≍ λ_+(e)λ_−(w_1)/\det ≍ e^{−3L/4}e^{L}/e^{L/2} =
e^{−L/4}`, not `Le^{−L/2}`; the sup norm `‖b\,w_2‖_∞ ≍ e^{−L/4}·e^{−L/4} =
e^{−L/2}` is unchanged, so (8bis.13f) stands. (b) Step 3 bounds
`‖ẽ⋆g_D'^†‖_{C^1}` by putting the derivative on `g_D'`, a **mesh** function,
while the accompanying note says the derivative "always falls on the smooth
factor". Either expand `I(\tilde g,\tilde g) − I(g_D',g_D') = I(ẽ,\tilde g)
+ I(\tilde g,ẽ) − I(ẽ,ẽ)` (so only `\tilde g` and `ẽ` occur) **and** prove
`‖(g_D)'‖_∞ = O(‖g‖_{C^1})`, which follows from the slow-variation argument
applied to the derivative (`Σ_kρ'(x−k) ≡ 0` on the uniform grid gives
`Σ_n ρ'((t−\log n)/gap_n)/gap_n = O(1)` pointwise, whence `(g_D)' = g·O(1) +
O(‖g'‖_∞)`), or keep the present expansion with that lemma. One paragraph.

## 3. Ruling

The mandatory repairs M1–M6 of R131.011 are correctly executed. The paper's
new round-5 mathematics (Cor 8bis.1b′, Thm 8bis.4a, Lemma 8bis.6) is correct.
The remaining defect is confined to the quarantined converse Thm 8bis.7,
whose classical import is misquoted (LF5); the theorem is optional (L3 was an
attempt), but a `CLASSICAL`-labelled theorem resting on a false import cannot
stand in a paper carrying the label. **One more small round (LF5, LF6) is
required before the label is written.**
