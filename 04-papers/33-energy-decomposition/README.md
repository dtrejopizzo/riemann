# Paper 33 — An Energy Decomposition of the Riemann Hypothesis: the Off-Line Energy I, its Integral Representation, and Structural Barriers

For each quadruple of non-trivial zeros off the critical line write ρ = 1/2 + b + iγ with b ∈ (0, 1/2) and define the off-line energy I = Σ b_j². The Riemann hypothesis is the conjunction of two logically independent statements: finiteness, I < ∞, and purity, I < ∞ ⇒ I = 0. The paper studies this decomposition: it bounds the energy envelope, expresses I(T) through the area integral of log|ζ| over the right half-strip plus a constant and a boundary-flux term (I is the second transversal moment of the Riesz measure of log|ζ|), proves that a Cesàro-averaged version of this identity always has a limit, and places finiteness in a calibrated chain RH ⇒ (m < ∞) ⇒ finiteness ⇒ Lindelöf ⇒ density hypothesis. It also proves an anti-recurrence theorem for the intermediate energy state, an exact boundary-flux identity on the critical line, and a universal lower bound for mollified second moments.

## Main results

- `thm:envelope` (E(T) = Σ_{γ≤T} b² ≪ T/log T) — PROVED, unconditional (from Selberg's density theorem).
- `thm:GL` (Green–Littlewood identity for I(T)) — PROVED.
- `thm:cesaro` (the Cesàro limit always exists in [−π/8, +∞] and equals πI − π/8) and `cor:lower` (optimal lower bound) — PROVED.
- `thm:inverse`, `thm:lindelof` (mean values of log|ζ|; finiteness implies the Lindelöf hypothesis) — PROVED.
- `thm:dichotomy` (energy dichotomy) — PROVED.
- `thm:witnesses`, `prop:antirecurrence`, `thm:dissolution`, `cor:notaxiom`: in the state 0 < I < ∞ self-approximation near an off-line zero has finitely many separated witnesses; conditionally on finiteness, sequential self-approximation is equivalent to RH — PROVED / CONDITIONAL as stated.
- `thm:flux`, `cor:fluxbounds` (boundary flux equals a weighted first moment) — PROVED.
- Universal lower bound for mollified moments with mollifier length T^θ, θ < 1/2 — PROVED, unconditional.
- Finiteness and purity themselves — OPEN.

## Files

- `main.tex` — LaTeX source.
- `main.pdf` — compiled paper.

## Relation to other papers

Refines the finiteness/rigidity split of Paper 30 (L8 and LP-112).
