# Paper 08 — A Faithful Kreĭn-Space Realization of the Weil Quadratic Form, with a No-Go Theorem for the Zero-Side Attack on Positivity

The paper realizes the Weil functional as an operator on the band-limited Paley–Wiener class
$PW_d$, $d>\tfrac12$, in three layers. (A) Under one isolated hypothesis (H), a uniform
short-interval zero-density statement, the form is closable and gives a self-adjoint operator
bounded below. (B) The form factors as $E^*JE$, where $E$ is evaluation at the zeros and $J$ is a
fundamental symmetry whose negative directions are the off-line zeros. This is a Kreĭn-space
structure, and the angular operator $K$ gives a single-axis dictionary. (C) A no-go theorem shows
that bounding $\|K\|\le1$ from the zero side is the same problem as proving Weil positivity. The
paper places the construction next to the Connes–Consani and Suzuki approaches. It locates the
sign barrier and does not claim to cross it.

## Main results

- `thm:A`, `cor:Aprime`: semibounded self-adjoint realization and faithful reformulation —
  CONDITIONAL on (H).
- `lem:A`–`lem:D`: integration by parts, quadrature error, vertical $L^2$ bound, Plancherel–Pólya
  off-line bound — PROVED (unconditional).
- `lem:E`: (H) implies coercivity — CONDITIONAL on (H).
- `thm:B`, `prop:identity`: Kreĭn identity $E^*JE$; $\|K\|<\infty$ iff the bottom is finite —
  PROVED (the domain statements CONDITIONAL on (H)).
- `lem:inj`: qualitative injectivity — PROVED.
- `thm:C`, `cor:circular`: the zero-side realization is circular as a tool for the sign — NO-GO.

## Files

- `main.tex`, `main.pdf` — source and compiled paper.

## Relation to other papers

Continues the localized form of Paper 07. Paper 11 studies the negative index of the same Kreĭn
structure.
