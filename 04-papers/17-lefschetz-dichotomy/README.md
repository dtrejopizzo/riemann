# Paper 17 — The Lefschetz dichotomy: why the hard-Lefschetz route to the Riemann Hypothesis is obstructed by linear independence

Weil's proof for curves over finite fields combines an intersection form with a Hodge index supplied by an ample class. Transcribing that construction to Spec ℤ yields every ingredient except the ample class. The paper records an independence filter (raising operators that are functions of the Frobenius flow only restate the positivity), builds candidate Kähler data from the archimedean density Ψ, exhibits an explicit hard-Lefschetz sl₂ on the archimedean continuum outside the von Neumann algebra of the flow, and proves that under linear independence of the ordinates no sl₂ carrying a Hodge–Riemann form acts on the zero spectrum.

## Main results
- `prop:filter` (Determinacy / the filter): raising operators in W*(T) only restate the positivity. PROVED.
- `prop:psi` (Structure of Ψ): Ψ strictly increasing on r > 0, unique positive zero r₀ = 6.2898…, below the first zero. PROVED (r₀ value NUMERICAL).
- `prop:indef`: the archimedean form is indefinite on primitive vectors. NUMERICAL (explicit Gaussian test vectors).
- `prop:nogo` (No Tate-twist Lefschetz on the zeros): CONDITIONAL on LI of the ordinates.
- `prop:sl2` (Explicit continuum sl₂): commutation relations verified. PROVED.
- `prop:transport` (Transport identity): transport to the zeros is the explicit formula. PROVED.
- `prop:ps`: the continuum sl₂ is principal series and carries no Hodge–Riemann form. PROVED.
- `thm:dichotomy` (The Lefschetz dichotomy): NO-GO for this route, CONDITIONAL on LI.

## Files
- `main.tex`, `main.pdf` — source and compiled paper (computations in the appendix).

## Relation to other papers
- Sharpens the finitization-under-LI obstruction of the series; uses the localized Weil form of Paper 16.
